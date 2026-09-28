# Research Plan

## Mission and research frame

Use the [Trust Atlas charter](CHARTER.md) as the source of truth. Research both directions: hardware mechanisms upward into systems and services, and service claims downward into dependencies, assumptions, and evidence.

Private cloud AI is the first end-to-end case study. Keep Apple's product name, Private Cloud Compute, distinct from the generic category of private cloud AI. General enterprise private-cloud infrastructure is outside the initial focus.

The initial historical frame runs from early system-protection principles through material published by **2026-09-28**. Follow earlier references when necessary. Record the earliest example observed within the search scope rather than making unsupported claims of historical priority. Later developments require a new research snapshot.

Plan for roughly 60–100 core papers and 12–20 versioned platform/service profiles for the first release. These are workload estimates, not a quota or a completeness claim. Evidence coverage and unresolved paths determine acceptance.

## Research areas

| Area | Main question | Discovery targets |
|---|---|---|
| Hardware roots and protection principles | Where does enforcement begin, and what remains trusted? | Reference monitors, least privilege, secure coprocessors, TPM, secure/measured boot, isolated keys |
| Enclaves and shielded execution | How can selected computation be protected from privileged software? | XOM, Aegis, Flicker, TrustVisor, SGX, Haven, SCONE, Graphene-SGX |
| VM-scale isolation | How are resource management and access to protected state separated? | Terra, Overshadow, CloudVisor, SEV/SEV-ES/SEV-SNP, TDX, Arm CCA |
| Open designs and assurance | What are the tradeoffs between a small TCB, flexibility, and verifiability? | Sanctum, Sanctorum, Keystone, Komodo, CURE, formal verification |
| Attacks and responses | Which assumptions fail, and which changes address them? | Controlled-channel attacks, Foreshadow, Plundervolt, LVI, SEVered, Iago, rollback and I/O attacks |
| Accelerators and AI | What happens when protected computation crosses a CPU boundary? | Graviton, Slalom, GPU protection, CPU–GPU attestation, protected I/O |
| Service composition | How do component capabilities support a service claim? | Attestation policy, key release, storage, transparency, non-targetability, private inference and stateful agents |

These are discovery candidates. Their presence in a research queue does not establish an inheritance or adoption relationship. FHE, MPC, ORAM, and differential privacy enter only through a documented alternative or complementary role.

Search security venues such as IEEE S&P, USENIX Security, ACM CCS, and NDSS; systems/architecture venues such as SOSP, OSDI, EuroSys, ASPLOS, ISCA, MICRO, and HPCA; and relevant AI venues when the work directly concerns protected or verifiable execution. Do not exclude important standards, technical reports, preprints, or industrial designs because they lack a conference venue.

## Workflow

### 1. Discover and screen

Ask Muse to find 10–15 candidates in one bounded area. Check titles, authors, publication years, venues, identifiers, and original documents. Do not merge papers by similar titles alone. Select the first 20–30 core works for detailed reading while retaining background candidates and exclusion reasons.

The initial seed batch is complete and the first graph is available. The accepted literature corpus is not complete.

### 2. Extract mechanisms and assumptions

For each core work, record the problem, prior limitations, contribution, protected assets, attacker capabilities, TCB, explicit non-goals, experimental environment, baselines, results, artifacts, and author-stated limitations.

For hardware-to-service paths, identify each enforcement mechanism and the assumptions introduced by the surrounding software, protocols, configuration, operations, and lifecycle. Preserve gaps where an implementation detail is not publicly documented.

Performance observations must retain hardware, workload, baseline, configuration, and measurement scope. Do not rank incomparable measurements together.

### 3. Trace origins, branches, and responses

Run at least two backward-reference and forward-citation expansion rounds. Check a survey's account against the original works. Include less-cited early work and attacks that challenge a popular design.

Distinguish citation, explicit extension, component use, design alternatives, attacks, and analyst interpretation. Chronological precedence alone does not establish inheritance. Do not add a plausible-looking edge solely to make a diagram connected.

### 4. Trace service claims downward

Include Apple Private Cloud Compute, Google Private AI Compute, Meta Private Processing, and Meta Muse Secure VM, separating versions and announced capabilities. Follow technical documentation, protocol descriptions, source code, public measurements, independent audits, and attack analyses.

Compare roots of trust; CPU/GPU boundaries; attestation verifiers and acceptance policies; key creation, release, storage, and destruction; plaintext locations; operator privileges; updates, debug and telemetry paths; persistence and rollback; access patterns; routing; binary/source availability; and audit scope.

Using a mechanism is not evidence that a company adopted a particular paper. A system can be connected through a shared mechanism without claiming direct historical adoption.

### 5. Collect metrics and challenge evidence

Use OpenAlex citation observations with explicit manifestation matching. Add an independent index selectively for important ambiguities, without adding provider totals together. Collect venue statistics by year, track, and denominator from documented conference records. Preserve missing values and their reasons.

Recheck every accepted inheritance edge and material security claim against a source location. Keep vendor statements separate from independent validation. Be precise about operator exclusion, side-channel coverage, transparency access, and deployment status.

### 6. Produce and review a dataset release

Deliver the data, reading map, mechanism explanations, versioned service comparisons, unresolved-path register, and methods/search record. Use `discovered → screened → extracted → verified → accepted`; preserve `source_checked` for checking that a source states something, not for establishing independent security assurance.

Core paths must have evidence at each material step or an explicit unresolved break. Review what guarantee is supported, which assumptions remain, and where the guarantee does not automatically carry over.

## Muse and Codex

Muse handles bounded discovery, reference following, primary-document locating, and candidate extraction. Codex handles source comparison, identity/version resolution, semantic normalization, data integration, and validation.

Require five output sections: `records`, `relation_candidates`, `sources`, `rejected`, and `gaps`. Each relationship candidate needs a source location and an explicit distinction between source statement and inference. All new project output should be in English.

Use a dedicated project conversation. Keep the first batches small; do not request indefinite research, unbounded sub-work, or recurring jobs. A Muse completion claim does not itself establish that the primary document was reviewed by Codex. The first bounded eight-paper batch has completed; see [the graph review](GRAPH_REVIEW.md).

## Dataset-v1 acceptance

- Core works have checked metadata, contribution, threat model, and limitations, with full-text access restrictions explicitly documented.
- Every accepted inheritance/adoption edge and material security claim has a traceable primary-source location.
- Each focal service has a reviewed hardware-to-service path, or a visible break where evidence is insufficient.
- Citation values have provider, version, date, and matching evidence, or an explicit missing-value reason. Venue statistics have year/track and denominator context.
- Focal service families and major evidenced versions are represented, with vendor statements, independent assurance, and deployment status separated.
- No essential research area is empty. Two consecutive expansion batches produce fewer than 5% new core works; this is an operational saturation heuristic, not proof of completeness.
- Material contradictions are resolved or recorded as open questions. Missing information is not converted to zero, absence, or a negative security finding.
- Structural validation passes and views can be regenerated from the dataset.

The user should be able to explain why the major branches differ and trace a service claim through the graph. Paper count alone is insufficient.

## Presentation and release

The initial technology tree was requested before the full corpus was complete. Keep it marked as a work in progress. Later views can include historical lineage, component/trust dependencies, and service-level comparisons.

Publish the approved presentation as a static GitHub Pages site generated from reviewed JSON, without runtime credentials or a required server. Choose additional graph libraries only when the data and interactions justify them. Do not publish copied paper PDFs or private Muse conversations. Repository ownership, public scope, and deployment URL remain decisions for the actual release.
