# Trust Atlas

**From Hardware Security to Real-World Services**

[Explore the live atlas](https://bitboom.github.io/trust-atlas/) · [Repository](https://github.com/bitboom/trust-atlas)

Trust Atlas is an evidence-backed knowledge graph tracing how hardware-enforced security mechanisms are implemented and composed into system architectures and real-world services. It records technical lineage, trust assumptions, security guarantees, limitations, and the evidence supporting each relationship.

The central question is: **What must be trusted for a service's security claim to hold, how is that trust enforced, and what evidence supports the chain?**

TEE, confidential computing, and Private AI are the initial research focus. The wider organizing scope is hardware-rooted system security. Read [the project charter](CHARTER.md) for the mission, boundaries, and acceptance criteria.

## Current status

Research snapshot: **2026-09-28**. The graph contains **63 entities, 98 relationships, and 54 source records**, including 15 papers, ten hardware families/platforms, four mode/reference configurations, and nine service/design-version profiles. Citation observations have been matched for 14 papers. The complete literature review, most venue statistics, and independent assurance reviews remain unfinished.

The interactive exploration view includes hardware, research, and selected-node maps. The public site is published from `docs/` on the `main` branch using GitHub Pages. See [hardware coverage](HARDWARE_COVERAGE.md) for the new Intel, AMD, NVIDIA, and Azure paths and their limits.

## Structure

- Hardware security mechanisms: roots of trust, key isolation, boot integrity, protected memory/state, and I/O isolation.
- Platform and system architectures: enclaves, confidential VMs, monitors, runtimes, and accelerator protection.
- Security protocols and composition: attestation policy, key release, protected storage, transparency, and routing.
- Real-world services: the applications of these mechanisms and their version-specific claims.
- Cross-cutting evidence: research, standards, attacks, mitigations, audits, metrics, and deployment observations.

The dataset is a typed graph. A technology tree is one way to navigate it; it is not the underlying data model. Multiple mechanisms can contribute to a service, and multiple trust assumptions may remain along a path.

## Read next

Current counts: [inventory and leaf definitions](INVENTORY.md). Latest expansion: [hardware and configurations](HARDWARE_COVERAGE.md).

1. [Project charter](CHARTER.md): mission, scope, and the questions each system profile must answer.
2. [Research plan](RESEARCH_PLAN.md): how to find, review, and expand the evidence.
3. [Data model](DATA_MODEL.md): entities, relationship semantics, claims, and metrics.
4. [First graph review](GRAPH_REVIEW.md): findings, checks, and remaining limitations.
5. [Muse research briefs](MUSE_BRIEFS.md): bounded instructions for further discovery.
6. [Initial seed review](SEED_REVIEW.md): historical record of the first eight-paper batch.
7. [Graph dataset](data/atlas.json) and [validation report](data/validation-report.json).

## Validation

Run with Python 3 and its standard library:

```sh
python3 validate.py
python3 inventory.py
python3 build_site.py
python3 check_site.py
```

This checks structure, references, provenance, dates, and lineage cycles. It does not establish the scientific validity or completeness of the corpus. Citation observations belong to a particular provider, publication version, and retrieval date.

## Language and publication

English is the canonical project language. Korean is supplementary when needed. Original source artifacts retain their source language; project summaries and labels are written in English.

After dataset review, refine the public graph and service comparisons, then publish the approved scope to GitHub Pages. Public outputs should contain reviewed metadata, original summaries, brief evidence, and source links—not copied paper collections or private research conversations.

## Website source and updates

Edit the canonical data and `site/graph.template.html`, then run the validation/build commands above. `site/view-config.json` contains compact display labels. Commit the regenerated `docs/` output to publish an update. The exported shell is checked in, so rebuilding requires only Python 3, without a desktop application or its plugins.

The site is static and has no required account or server. Public source links open in a separate tab. Private research conversations, receipts, credentials, and scratch files are excluded. Original source documents remain with their authors; publication here does not imply a license to redistribute them.
