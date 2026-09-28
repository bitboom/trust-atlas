#!/usr/bin/env python3
"""Generate an explicit type catalogue and counts without inventing graph leaves."""
from collections import Counter
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
TYPE_NAMES={'paper':'Papers','concept':'Concepts','technology':'Security technologies',
    'hardware':'Hardware families and platforms','configuration':'Modes and reference configurations',
    'implementation':'Service/design versions','standard':'Standards','attack':'Attack records'}

def inventory(atlas):
    entities=atlas['entities']; types=Counter(e['type'] for e in entities)
    catalogue=[dict(id='type-'+kind,name=TYPE_NAMES[kind],count=types[kind],
        entity_ids=[e['id'] for e in entities if e['type']==kind]) for kind in TYPE_NAMES if types[kind]]
    incoming=set(r['to_id'] for r in atlas['relations']); outgoing=set(r['from_id'] for r in atlas['relations'])
    participating=set()
    historical_parents=set()
    for r in atlas['relations']:
        if r['lineage']:
            participating.update([r['from_id'],r['to_id']]);historical_parents.add(r['to_id'])
    return dict(project=atlas['project'],as_of=atlas['as_of'],
        graph_entity_count=len(entities),graph_relationship_count=len(atlas['relations']),
        source_record_count=len(atlas['sources']),declared_scope_layer_count=len(atlas['scope']['layers']),
        scope_layers=atlas['scope']['layers'],scope_layer_note='Research scope, not an exclusive populated taxonomy.',
        topic_branch_counts=dict(sorted(Counter(e['branch'] for e in entities).items())),
        entity_type_counts=dict(types),hardware_kind_counts=dict(Counter(e['details']['hardware_kind'] for e in entities if e['type']=='hardware')),
        catalogue=dict(root='Trust Atlas',depth=3,root_count=1,category_count=len(catalogue),
            leaf_count=len(entities),total_navigation_nodes=1+len(catalogue)+len(entities),categories=catalogue,
            leaf_definition='Each entity appears once under its primary type. Catalogue leaves are records, not terminal vertices of the knowledge graph.'),
        graph_endpoint_diagnostics=dict(
            stored_direction_zero_outdegree=[e['id'] for e in entities if e['id'] not in outgoing],
            stored_direction_zero_indegree=[e['id'] for e in entities if e['id'] not in incoming],
            lineage_latest_leaves=sorted(participating-historical_parents),
            note='Endpoint counts depend on edge selection, direction, and incomplete coverage. They do not establish historical or scientific finality.'))

if __name__=='__main__':
    atlas=json.loads((ROOT/'data/atlas.json').read_text())
    report=inventory(atlas)
    ids=[ident for c in report['catalogue']['categories'] for ident in c['entity_ids']]
    assert len(ids)==len(set(ids))==len(atlas['entities'])
    (ROOT/'data/inventory.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    rows=['# Inventory','',f"Snapshot: {atlas['as_of']}",'',
        f"**{report['graph_entity_count']} entities · {report['graph_relationship_count']} relationships · {report['source_record_count']} source records**",'',
        '## Classification to leaf','',
        f"The catalogue has three levels: **Trust Atlas → {report['catalogue']['category_count']} entity-type categories → {report['catalogue']['leaf_count']} entity leaves**. Including the root and categories, that is {report['catalogue']['total_navigation_nodes']} navigation nodes. Classification nodes are presentation metadata, not additional research entities.",'',
        report['catalogue']['leaf_definition'],'',
        '| Entity type | Records / catalogue leaves |','|---|---:|']
    for c in report['catalogue']['categories']:rows.append(f"| {c['name']} | {c['count']} |")
    rows+=['','## Other organizing dimensions','',f"There are {report['declared_scope_layer_count']} declared scope layers and {len(report['topic_branch_counts'])} populated topic branches. These are separate views, not successive levels of the type catalogue.",'',
        '| Topic branch | Records |','|---|---:|']
    rows += [f'| {k} | {v} |' for k,v in report['topic_branch_counts'].items()]
    rows += ['','## Hardware detail','',', '.join(f'{count} {kind}' for kind,count in report['hardware_kind_counts'].items())+'.',
        '', 'The full typed graph has no single canonical leaf count. Directed endpoint diagnostics are included in `data/inventory.json`; they are not the same as the catalogue leaves.']
    (ROOT/'INVENTORY.md').write_text('\n'.join(rows)+'\n')
    print(json.dumps({k:report[k] for k in ['graph_entity_count','graph_relationship_count','entity_type_counts','hardware_kind_counts']},indent=2))
