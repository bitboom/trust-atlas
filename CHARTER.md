# Trust Atlas

**From Hardware Security to Real-World Services**

## Mission

Build an evidence-backed knowledge graph that traces how hardware-enforced security mechanisms are implemented and composed into system architectures and real-world services, documenting their technical lineage, trust assumptions, security guarantees, limitations, and supporting evidence.

## The question the project should answer

**What must be trusted for a service's security claim to hold, how is that trust enforced across its underlying hardware and software, and what evidence supports each link?**

The graph should support exploration in both directions: from a hardware mechanism to the systems and services that use it, and from a service claim back to the mechanisms, assumptions, and evidence on which it depends.

## Scope

The organizing theme is hardware-rooted system security. Confidential computing and Private AI are the initial research focus, within this broader scope.

| Layer | What the graph will cover | Example research targets |
|---|---|---|
| Hardware security mechanisms | Enforcement primitives and hardware roots of trust | Isolated keys, secure/measured boot, memory access control, memory encryption and integrity, protected CPU state, DMA/I/O isolation |
| Platform and system architectures | Ways those mechanisms are assembled into execution and isolation environments | Secure monitors, enclaves, confidential VMs, trusted runtimes, accelerator protection, platform TCBs |
| Security protocols and service composition | How a client establishes and maintains trust in a complete service | Remote attestation and verification policy, key release, protected storage, rollback protection, software transparency, privacy-preserving routing |
| Real-world services | Versioned services and their claimed or independently evaluated properties | Private cloud AI, confidential inference, stateful agents; later, other services with a documented connection to the hardware-security scope |

These layers are a navigation model, not a claim that every system implements the same stack. Remote attestation, for example, can span hardware, firmware, protocols, and client policy. Model it through the relevant entities and relationships rather than forcing it into a single box.

Research papers, standards, attacks, mitigations, audits, and deployment evidence are cross-cutting entities. They explain origins, branching decisions, adoption, and assurance at any layer.

## Initial focus

Start with TEE and confidential-computing research, then trace the mechanisms used in Apple Private Cloud Compute, Google Private AI Compute, Meta Private Processing, and Meta Muse Secure VM. Preserve the distinction between an isolated runtime and a system that claims to exclude its operator from accessing protected data. Track proposed capabilities separately from deployed ones.

Earlier system-security principles belong in the graph when they explain a mechanism or design decision. Additional service domains enter through evidence-backed connections, not simply because they have a security feature.

## Questions every substantial system profile must address

1. **Protected assets:** What code, data, keys, state, or metadata are protected?
2. **Adversary:** From whom, and with what assumed capabilities?
3. **Trusted computing base:** Which hardware, firmware, software, operators, and verification authorities remain trusted?
4. **Enforcement:** Which mechanism supports each security property?
5. **Composition:** What must the surrounding software and protocols do for that property to hold at service level?
6. **Limits:** Which threats, interfaces, lifecycle stages, and failure modes remain outside the guarantee?
7. **Evidence and time:** Which version, source, experiment, proof, audit, or deployment observation supports the claim?

An unresolved answer is a visible research gap. It is not replaced with a guessed dependency or a blanket trust score.

## Distinctions the graph must preserve

- A **capability** is a mechanism offered by a component. A **security guarantee** is a property asserted under a particular set of assumptions. An **assurance claim** describes the evidence supporting that property.
- **Technical lineage** explains where an idea or implementation came from. **System composition** explains what an implementation uses. **Trust dependencies** explain what a guarantee relies on. These are separate relationship families.
- A paper citation is not proof of technical inheritance or product adoption.
- Hardware isolation does not automatically establish the privacy or correctness of the complete service. Follow the software, protocol, configuration, and lifecycle assumptions along the path.
- Vendor statements, independent validation, and our own interpretation remain distinguishable.
- A service graph must include relevant boundaries and gaps, including flows that leave the protected environment.

## Boundaries

This is a research and architecture knowledge graph, not a certification system or a universal ranking of secure products. Citation counts and venue statistics guide literature exploration; they do not establish security.

Do not attempt to catalogue all cybersecurity topics. General web/application security, organizational controls, and unrelated privacy technologies are included only when they explain a dependency, limitation, attack, or alternative relevant to the scoped hardware-to-service path. FHE, MPC, ORAM, and differential privacy may be represented as complementary or alternative approaches where a source establishes the connection.

## Deliverables and completion

The primary deliverable is a versioned dataset with stable identifiers, typed relationships, scoped claims, source locations, and explicit unknowns. Technology trees, dependency graphs, timelines, and service comparisons are views generated from that data.

For the first accepted release, every focal service must have an evidence-backed hardware-to-service path **or an explicitly documented break where public evidence is insufficient**. Core lineage edges and security claims must be reviewed against primary sources; metric versions and dates must be traceable; mechanical validation must pass. Corpus size alone is not completion.

The user has authorized a public preview of the current research snapshot on GitHub Pages. Keep its incomplete coverage explicit. Complete and review the underlying corpus before declaring an accepted dataset-v1 release.

## Language

English is the canonical language for all project-authored documentation, data descriptions, research briefs, code comments, labels, and interfaces. Korean may be added when specifically useful or requested; it is supplementary, not a second mandatory copy of every artifact. Preserve source material and bibliographic names in their original language where accuracy requires it.
