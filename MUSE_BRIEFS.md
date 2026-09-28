# Muse Research Briefs

Status: the first bounded eight-paper batch was submitted and completed on 2026-09-28. See [the review](GRAPH_REVIEW.md). The instructions below are reusable briefs for subsequent work. **Return all new project material in English.**

## Shared research contract

Research one bounded batch for **Trust Atlas: From Hardware Security to Real-World Services**. The goal is an evidence-backed graph connecting hardware security mechanisms, platform/system architectures, security protocols, and real-world services, while recording lineage, trust assumptions, guarantees, limitations, and evidence. TEE, confidential computing, and Private AI are the initial focus. Use the research snapshot date specified for the batch; the current corpus cutoff is 2026-09-28.

Limit a batch to 10–15 publication candidates or four product-version profiles. Do not create recurring jobs, indefinite investigations, or unbounded sub-work. Use public research sources; do not use unrelated personal data or conversations.

Prefer conference proceedings, author manuscripts, standards, vendor technical documents, official source repositories, and independent audits. Open the material rather than relying on search snippets or another AI's response. State whether you read the abstract, selected sections, or the full paper. Do not guess a title, venue, DOI, citation count, or release status.

For each work, return exact bibliographic metadata, document type, identifier, original URL, problem/contribution, predecessor and successor candidates, protected assets, attacker, TCB, limitations, artifact links, source locations, review depth, and unresolved questions.

For each relation, return subject, type, object, a concise paraphrase of the supporting statement, source URL, page/section, version scope, and whether it is explicit or inferred. Separate technical inheritance, citation, component use, trust dependencies, and alternatives. A product using a mechanism is not proof that it adopted a particular paper. Identify gaps in a hardware-to-service path rather than inventing bridges.

Citation observations require provider, record URL, observation date, and exact manifestation. Do not sum publication versions. Venue statistics require year, track, accepted/submitted counts, and denominator caveats. Use null plus a reason when unavailable.

Return JSON sections named `records`, `relation_candidates`, `sources`, `rejected`, and `gaps`, plus a short English summary. Use stable candidate IDs and batch-specific filenames. Do not copy full papers into deliverables. If access fails, return the completed subset and exact remaining gap.

## M01 — Foundations and early trust models

Trace reference monitors, small TCBs, secure/measured boot, secure coprocessors/TPM, Terra, XOM/Aegis, and Flicker/TrustVisor. Distinguish the earliest evidence found from an assertion of historical first invention. Compare designs that trust a VMM with designs that exclude privileged resource managers from access. Follow references from Saltzer–Schroeder and Terra.

## M02 — Enclave, monitor, and confidential-VM branches

Find representative research and design documents for SGX/Haven, Sanctum/Sanctorum/Keystone, TrustZone/Komodo/CCA, SEV/SEV-ES/SEV-SNP, and TDX. Distinguish research prototypes from architecture specifications and products. Identify enforcement granularity, TCB, supported adversaries, and dependencies; do not assume enclave and VM designs provide identical guarantees.

## M03 — Attacks and responses

Examine controlled-channel attacks, Foreshadow, Plundervolt, LVI, SEVered, and Iago/rollback/I/O attacks. Record affected versions, prerequisites, properties broken or retained, and evidence for actual responses. Do not project a historical attack onto all current implementations.

## M04 — Accelerators and protected AI execution

Study Graviton, Slalom, CPU–GPU confidential execution, attestation, protected I/O, and inference serving. Distinguish a protected accelerator from verified/private outsourcing to an untrusted accelerator. Capture model/input/intermediate-state protection boundaries. Include FHE/MPC/ORAM only where they supply a relevant alternative or complement.

## M05 — Services and versioned trust paths

Trace the four focal service families downward into their hardware, runtime, protocols, and operational assumptions. Separate Apple's 2024 PCC design from its 2026 Google Cloud expansion; Google's and Meta's stateful updates; and Muse Secure VM from the announced Confidential VM capability. These are candidates for verification, not unconditional assumptions.

Starting sources:

- https://security.apple.com/blog/private-cloud-compute/
- https://security.apple.com/blog/expanding-pcc/
- https://blog.google/innovation-and-ai/products/google-private-ai-compute/
- https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/
- https://engineering.fb.com/2025/04/29/security/whatsapp-private-processing-ai-tools/
- https://engineering.fb.com/2026/09/23/security/private-processing-meta-ai-glasses/
- https://security.muse.ai/

Extract roots of trust, TCB, assets, operator access, key lifecycle, verifier policy, persistence, transparency access, audits, and deployment status. Separate vendor statements from what an audit actually checked. Record where a service guarantee needs assumptions beyond the underlying hardware capability.

## M06 — Contradictions and missing links

Review ten proposed relationships at a time. Find citations misrepresented as inheritance, missing dependencies, version-confused metrics, inverted dates, overgeneralized attacks, and vendor claims presented as independent validation. Classify findings as supported, insufficient evidence, or contradicted, with primary-source locations. Do not fill gaps merely to make the graph connected.
