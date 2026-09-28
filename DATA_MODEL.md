# Data Model and Evaluation Rules

## Canonical graph

A bibliography, a technology tree, and a system dependency graph are different views of the research. Papers supply contributions and evidence; technologies can be shared by multiple papers, standards, and implementations. Trust Atlas stores a typed graph and generates views from it.

The top-level project profile records the canonical name, English language policy, mission, initial focus, and organizing layers. The existing research snapshot remains dated independently of wording changes.

| Collection | Meaning | Main fields |
|---|---|---|
| `entities` | Papers, concepts, technologies, versioned implementations, standards, and attacks | `id`, `type`, `name`, `year`, `branch`, `review_status`, `source_ids`, `details` |
| `sources` | Retrievable evidence | `id`, `title`, `url`, `publisher`, `kind`, `published_date`, `accessed_date`, `access_status` |
| `claims` | Statements bounded by scope and time | `id`, `subject_id`, `statement`, `epistemic_status`, `evidence`, `valid_at`, `scope` |
| `relations` | Typed links between entities | `id`, `from_id`, `to_id`, `type`, `claim_id`, `lineage`, `review_status` |
| `metrics` | Versioned, provider-specific observations | `id`, `entity_id`, `name`, `value`, `unit`, `provider`, `observed_at`, `source_id`, `status`, `details` |
| `research_queue` | Concrete remaining investigations | `id`, `batch`, `topic`, `question`, `required_evidence`, `status` |

Schema 0.3 distinguishes `hardware` (CPU/GPU families and physical platforms) from `technology` (security capabilities), and `configuration` (CC modes or reference integrations) from `implementation` (service/design profiles). Hardware needs vendor, kind, and support scope; configurations need a document version, date, and component constraints. A capability record does not imply that every SKU or deployment enables it.

`data/inventory.json` is a derived type catalogue. Its leaves are entity records assigned once to a primary type. Its classification root and categories are not extra graph entities; graph-theoretic endpoints depend on edge selection and direction.

Use stable IDs. Collections may later be split into separate files without changing identity. JSON is the reviewed source of truth; SQLite or web payloads may be generated from it. A dedicated graph database is not required for the initial corpus.

`null` means unknown. Distinguish not collected, inaccessible, unpublished, unresolved matching, and not applicable. An empty list does not establish that a property or dependency is absent.

English-authored descriptions use neutral keys such as `summary`, `impact`, and `limitation`. Optional translations can be added explicitly in a future localization structure; do not duplicate every record by default.

## Hardware-to-service organization

Use four organizing layers: hardware security mechanisms; platform and system architectures; security protocols and composition; real-world services. These are research categories, not an assertion that every item belongs exclusively to one layer. Publication, standard, attack, and assurance entities cut across layers.

For a substantial system or service, extract protected assets, adversary capabilities, trusted components, enforcement mechanism, claimed properties, required composition/configuration assumptions, exclusions, version, and assurance evidence. These fields are an extraction target; current records must not pretend that an incomplete profile has been filled.

Keep a capability, a claimed guarantee, and assurance evidence distinct. A hardware feature alone does not establish a service-level property. Record relevant software, keys, verifier policies, operational interfaces, data flows, and lifecycle boundaries along the path. A missing step is a visible gap.

## Relationship semantics

| Type | Stored direction | Required basis |
|---|---|---|
| `cites` | Citing paper → cited work | Matching reference entry |
| `extends` | Successor → extended predecessor | Explicit description of technical extension |
| `explicitly_inspired_by` | Later work → inspiration | Explicit attribution by the authors |
| `studies` | Publication/standard → subject | Described contribution or subject matter |
| `uses` | Implementation/work → component | Explicit implementation, design, or code evidence |
| `alternative_to` | Design → comparison target | Described difference or evaluation |
| `attacks` | Attack work → scoped target | Version, attacker capability, and affected property |
| `mitigates` | Defense → attack/limitation | Covered threat and required conditions |
| `evolves_from` | New implementation version → prior version | Explicit version continuity |
| `related_to` | Entity → conceptually related entity | Clearly labeled analysis or documented association |
| `supports` | Hardware/reference configuration → technology | Source-scoped capability or alternative backend support |
| `contains` | Hardware platform → hardware component | Documented physical composition |
| `validated_with` | Configuration → hardware | Vendor support-matrix listing; not independent validation |
| `supports_mode` | Reference architecture → mode configuration | Documented mode support with stack-specific constraints |

Only supported `extends`, `explicitly_inspired_by`, and `evolves_from` links enter the lineage subgraph. Do not promote citations or conceptual associations into parent–child inheritance. Apply cycle checks to lineage, not to every relation in the graph.

A tree view may reverse stored lineage/dependency direction to show a basis before its successor or user. The view must label its convention. Vertical position or nearby layout is not evidence of inheritance.

Where a paper and a product share a mechanism, connect each to the mechanism unless direct adoption is documented. This records technical relevance without inventing industrial lineage.

The charter also calls for more explicit trust-dependency modeling. Add relations such as `depends_on`, `assumes`, or `supports_property` only with a defined domain/range, scoped claims, and validator support. The current data model does not yet claim to have those explicit relation types or complete trust-dependency paths.

## Evidence status

`source_checked` means that a document was checked for a statement. It does not mean that the system's security was independently established.

- `paper_report`: a contribution, argument, or result reported in a research/technical source; retain conditions and scope.
- `vendor_statement`: the provider's description; do not silently convert it into independent assurance.
- `independently_validated`: a property actually examined in external validation; record version, scope, and limitations.
- `analyst_inference`: our interpretation, with its supporting basis and alternative explanations.
- `unknown`: insufficient evidence.

Each evidence entry contains `source_id`, `locator`, and `supports`. A locator can be a page/section, document heading, or source path plus revision. Prefer short paraphrases and exact locations over reproducing documents. Preserve contradictory evidence when material.

Absence of a statement in the material checked does not establish absence of the capability. Search snippets and AI answers alone do not qualify as checked primary evidence.

## Threat and assurance comparison

Use consistent questions about:

- Assets: inputs, model weights, intermediate values, keys, persistent state, and metadata.
- Adversaries: other tenants, malicious applications, guest/host OS, hypervisors, operators, physical attackers, and suppliers.
- TCB: CPU/GPU, firmware, monitors, runtimes, guest software, applications, models, key services, and verifiers.
- Properties: confidentiality, integrity, code identity, freshness, rollback resistance, key binding, retention, and erasure.
- Exclusions: side channels, traffic analysis, DoS, prompt injection, output leakage, supply chain, and fault attacks.
- Assurance: attestation scope and policy, source/binary transparency, update/revocation behavior, reproducibility, and external audits.

Do not classify every use of encryption or sandboxing as confidential computing. Examine memory confidentiality, integrity, attestation, key release, and operator access separately. Do not treat a TEE as proof of model correctness or benign application behavior.

## Evaluation axes

| Axis | Observations | Interpretation |
|---|---|---|
| Venue selectivity | Venue, year, track, submissions, eligibility, acceptances, awards | Match the denominator; prestige does not prove correctness |
| Academic influence | Provider totals, annual citations, appropriate cohorts, subsequent works | Account for age, field size, and version dispersion |
| Technical influence | Verified extensions, standards influence, connections between branches | Graph centrality is corpus-dependent |
| Industrial adoption | Prototype, preview, deployment, external adoption | Component use differs from adopting a specific paper |
| Verifiability | Artifacts, reproduction, proofs, audits, known counterexamples | Public code alone is not proof of security |

There is no default aggregate security or paper-quality score. Reading priority follows relevance to the scoped path, explanatory value, evidence availability, and balanced coverage. Venue selectivity and reading difficulty are separate: an optional 1–5 reading-difficulty assessment must state prerequisites and be labeled editorial, and is left blank before sufficient review. Any external venue ranking needs its source and edition.

## Citation identity and normalization

1. Match title, authors, year, and DOI against primary metadata. Automated matches are candidates.
2. Keep conference, journal, and preprint manifestations distinct within a work family.
3. Do not sum version totals. A family-level count requires a deduplicated union of citing-work IDs.
4. Store provider, record ID/URL, observation date, and matching basis.
5. Separate lifetime citation rate from recent attention. Distinguish complete calendar years from partial years.
6. Compute cohort percentiles only with a defined, adequate comparison population. A rank within a small hand-selected seed is not a field-wide percentile.

Following the [OpenAlex field definitions](https://help.openalex.org/data/works/attributes/), preserve lifetime totals separately from annual arrays. An annual array may not cover the entire history; its sum is not automatically the lifetime count. Do not fill out-of-window years with zero.

## Versions and release status

Create distinct implementation profiles when hardware or trust boundaries materially change. Store product family, version label, relevant date, and deployment status. Future-tense announcements are not evidence of general availability.

Keep structural validation separate from content acceptance. Current `screened` and `source_checked` records are not a completed, independently verified dataset. The broader Trust Atlas mission changes the research frame; it does not retroactively fill missing evidence.
