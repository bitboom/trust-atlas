#!/usr/bin/env python3
"""Validate the Trust Atlas data contract and graph references with Python 3."""
import datetime
import json
from pathlib import Path
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent


def validate(atlas):
    errors = []

    def check(ok, message):
        if not ok:
            errors.append(message)

    required = {
        'entities': {'id', 'type', 'name', 'year', 'branch', 'review_status', 'source_ids', 'details'},
        'sources': {'id', 'title', 'url', 'publisher', 'kind', 'published_date', 'accessed_date', 'access_status'},
        'claims': {'id', 'subject_id', 'statement', 'epistemic_status', 'evidence', 'valid_at', 'scope'},
        'relations': {'id', 'from_id', 'to_id', 'type', 'claim_id', 'lineage', 'review_status'},
        'metrics': {'id', 'entity_id', 'name', 'value', 'unit', 'provider', 'observed_at', 'source_id', 'status', 'details'},
        'research_queue': {'id', 'batch', 'topic', 'question', 'required_evidence', 'status'},
    }
    check(atlas.get('schema_version') == '0.3.0', 'Unsupported schema version')
    check(atlas.get('project') == 'Trust Atlas', 'Incorrect canonical project name')
    check(atlas.get('primary_language') == 'en', 'Canonical project language must be English')
    check(bool(atlas.get('mission')), 'Missing project mission')
    check(len(atlas.get('scope', {}).get('layers', [])) == 4, 'Expected four organizing layers')
    indexes = {}
    for collection, keys in required.items():
        rows = atlas.get(collection)
        check(isinstance(rows, list), f'{collection}: expected list')
        if not isinstance(rows, list):
            return errors
        index = {}
        for row in rows:
            check(isinstance(row, dict), f'{collection}: expected object')
            if not isinstance(row, dict):
                continue
            check(keys <= row.keys(), f'{collection}: missing fields {keys - row.keys()}')
            ident = row.get('id')
            check(isinstance(ident, str) and bool(ident), f'{collection}: invalid ID')
            check(ident not in index, f'{collection}: duplicate ID {ident}')
            index[ident] = row
        indexes[collection] = index
    if errors:
        return errors

    def date(value, context):
        try:
            parsed = datetime.date.fromisoformat(value)
            check(parsed <= datetime.date.fromisoformat(atlas['as_of']), f'{context}: after snapshot date')
        except (ValueError, TypeError, KeyError):
            check(False, f'{context}: invalid date')

    date(atlas.get('as_of'), 'as_of')
    entity_types = {'paper', 'concept', 'technology', 'implementation', 'standard', 'attack', 'hardware', 'configuration'}
    statuses = {'discovered', 'screened', 'extracted', 'verified', 'accepted', 'source_checked'}
    epistemic = {'paper_report', 'vendor_statement', 'independently_validated', 'analyst_inference', 'unknown'}
    relation_types = {'cites', 'extends', 'explicitly_inspired_by', 'studies', 'uses', 'alternative_to', 'attacks', 'mitigates', 'evolves_from', 'related_to', 'supports', 'contains', 'validated_with', 'supports_mode'}
    entity_index, source_index, claim_index = (indexes[n] for n in ('entities', 'sources', 'claims'))
    for source in source_index.values():
        parsed = urlparse(source['url'])
        check(parsed.scheme in {'https', 'http'} and bool(parsed.netloc), f"{source['id']}: invalid source URL")
        date(source['accessed_date'], source['id'])
        if source['published_date'] is not None:
            date(source['published_date'], source['id'])
    for entity in entity_index.values():
        check(entity['type'] in entity_types, f"{entity['id']}: unsupported type")
        check(entity['review_status'] in statuses, f"{entity['id']}: invalid review status")
        check(bool(entity['source_ids']), f"{entity['id']}: missing source")
        for sid in entity['source_ids']:
            check(sid in source_index, f"{entity['id']}: missing source {sid}")
        check(entity['year'] is None or type(entity['year']) is int, f"{entity['id']}: invalid year")
        if type(entity['year']) is int:
            check(1900 <= entity['year'] <= int(atlas['as_of'][:4]), f"{entity['id']}: year out of scope")
        if entity['type'] == 'paper':
            check(bool(entity['details'].get('authors')), f"{entity['id']}: missing authors")
            check(bool(entity['details'].get('venue')), f"{entity['id']}: missing venue")
        if entity['type'] == 'implementation':
            check(bool(entity['details'].get('deployment_status')), f"{entity['id']}: missing deployment status")
            date(entity['details'].get('as_of'), entity['id'])
        if entity['type'] == 'hardware':
            check(entity['details'].get('hardware_kind') in {'CPU', 'GPU', 'Platform'}, f"{entity['id']}: invalid hardware kind")
            check(bool(entity['details'].get('vendor')), f"{entity['id']}: missing hardware vendor")
            check(bool(entity['details'].get('support_scope')), f"{entity['id']}: missing support scope")
        if entity['type'] == 'configuration':
            check(entity['details'].get('configuration_kind') in {'gpu_cc_mode', 'reference_architecture'}, f"{entity['id']}: invalid configuration kind")
            check(bool(entity['details'].get('document_version')), f"{entity['id']}: missing configuration document version")
            check(bool(entity['details'].get('component_constraints')), f"{entity['id']}: missing configuration constraints")
            date(entity['details'].get('as_of'), entity['id'])
    for claim in claim_index.values():
        check(claim['subject_id'] in entity_index, f"{claim['id']}: invalid subject")
        check(claim['epistemic_status'] in epistemic, f"{claim['id']}: invalid epistemic status")
        check(bool(claim['evidence']), f"{claim['id']}: no evidence")
        check(bool(claim['scope']), f"{claim['id']}: no scope")
        date(claim['valid_at'], claim['id'])
        for evidence in claim['evidence']:
            check(evidence.get('source_id') in source_index, f"{claim['id']}: missing evidence source")
            check(bool(evidence.get('locator')) and bool(evidence.get('supports')), f"{claim['id']}: incomplete evidence")
    lineage_edges = {}
    for relation in indexes['relations'].values():
        ident, a, b = relation['id'], relation['from_id'], relation['to_id']
        check(a in entity_index and b in entity_index, f'{ident}: dangling entity')
        check(relation['type'] in relation_types, f'{ident}: unknown relation type')
        check(relation['claim_id'] in claim_index, f'{ident}: missing claim')
        check(type(relation['lineage']) is bool, f'{ident}: lineage must be boolean')
        if relation['claim_id'] in claim_index:
            check(claim_index[relation['claim_id']]['subject_id'] == a, f'{ident}: claim subject mismatch')
        if a in entity_index and b in entity_index:
            source_type, target_type = entity_index[a]['type'], entity_index[b]['type']
            if relation['type'] == 'supports':
                check(source_type in {'hardware', 'configuration'} and target_type == 'technology', f'{ident}: supports must connect hardware/configuration to a technology')
            elif relation['type'] == 'contains':
                check(source_type == target_type == 'hardware' and a != b, f'{ident}: contains requires distinct hardware nodes')
                check(entity_index[a]['details'].get('hardware_kind') == 'Platform', f'{ident}: containment source must be a platform')
            elif relation['type'] == 'validated_with':
                check(source_type == 'configuration' and target_type == 'hardware', f'{ident}: validated_with must connect configuration to hardware')
            elif relation['type'] == 'supports_mode':
                check(source_type == target_type == 'configuration', f'{ident}: supports_mode requires configuration nodes')
                check(entity_index[a]['details'].get('configuration_kind') == 'reference_architecture' and entity_index[b]['details'].get('configuration_kind') == 'gpu_cc_mode', f'{ident}: invalid reference-to-mode relationship')
        if relation['lineage']:
            check(relation['type'] in {'extends', 'explicitly_inspired_by', 'evolves_from'}, f'{ident}: unsupported lineage edge')
            lineage_edges.setdefault(a, []).append(b)
            ya, yb = entity_index.get(a, {}).get('year'), entity_index.get(b, {}).get('year')
            if ya is not None and yb is not None:
                check(ya >= yb, f'{ident}: temporal inversion')
    visiting, visited = set(), set()

    def visit(node):
        if node in visiting:
            check(False, f'Lineage cycle at {node}')
            return
        if node in visited:
            return
        visiting.add(node)
        for target in lineage_edges.get(node, []):
            visit(target)
        visiting.remove(node)
        visited.add(node)

    for node in lineage_edges:
        visit(node)
    for metric in indexes['metrics'].values():
        ident = metric['id']
        check(metric['entity_id'] in entity_index, f'{ident}: dangling entity')
        date(metric['observed_at'], ident)
        if metric['value'] is not None:
            check(metric['source_id'] in source_index and bool(metric['provider']), f'{ident}: observed value has no provenance')
            check(metric['status'] == 'observed', f'{ident}: non-null value not observed')
        else:
            check(metric['status'] != 'observed' and bool(metric['details'].get('reason')), f'{ident}: missing-value reason required')
        if metric['name'] == 'citation_count' and metric['value'] is not None:
            check(type(metric['value']) is int and metric['value'] >= 0, f'{ident}: invalid count')
        if metric['name'] == 'venue_acceptance_rate' and metric['value'] is not None:
            check(0 <= metric['value'] <= 100, f'{ident}: invalid percent')
            numerator, denominator = metric['details'].get('accepted'), metric['details'].get('submitted')
            check(isinstance(numerator, int) and isinstance(denominator, int) and denominator > 0, f'{ident}: count basis required')
    return errors


if __name__ == '__main__':
    atlas = json.loads((ROOT / 'data/atlas.json').read_text())
    errors = validate(atlas)
    report = dict(structural_validation='FAIL' if errors else 'PASS', errors=errors,
        project=atlas['project'], primary_language=atlas['primary_language'],
        as_of=atlas['as_of'], phase=atlas['phase'],
        counts={k:len(atlas[k]) for k in ['entities','sources','claims','relations','metrics','research_queue']},
        observed_citation_records=sum(m['name']=='citation_count' and m['value'] is not None for m in atlas['metrics']),
        unresolved_citation_records=sum(m['name']=='citation_count' and m['value'] is None for m in atlas['metrics']),
        pending_venue_statistics=sum(m['name']=='venue_acceptance_rate' and m['value'] is None for m in atlas['metrics']),
        full_text_reviews_completed=sum(e['type']=='paper' and e['details'].get('full_text_reviewed',False) for e in atlas['entities']),
        dataset_v1_complete=False,
        caveat='Structural validation is not scientific validation or a claim of corpus completeness.')
    (ROOT / 'data/validation-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(1 if errors else 0)
