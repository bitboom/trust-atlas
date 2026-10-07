# Muse Runtime Composition and Trust Boundaries

Extraction checked: **2026-10-07**. Source design: **2026-09-08**. The research snapshot at this extraction was **2026-09-28**; this was additional extraction of an already included source, not a refresh of deployment or citation observations. See the README for subsequent incremental snapshots.

## Scope

The charter includes Muse and requires distinguishing runtime containment from provider exclusion. This update records the software mechanisms used in its reported service composition and the trust boundaries that remain unresolved.

The update adds **eight entities and eight `uses` relationships**, taking the published dataset from 63/98 to **71 entities / 106 relationships**. The **54 source records and 29 metric records are unchanged**. No new independent assurance evidence was added.

Evidence comes from Meta's [How We Built Safety Into Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse), already recorded as `s-muse26`. Each new claim has a source section and `checked_at` date. The claims remain `vendor_statement`; their relationships are `source_checked` and non-lineage.

## Added mechanisms

| Entity | Relationship from the launch profile | Source section |
|---|---|---|
| `t-systemd-nspawn` | `r-104` | Muse Secure VM |
| `t-linux-user-namespaces` | `r-105` | Muse Secure VM; Network egress |
| `t-linux-peer-credentials` | `r-106` | Muse Secure VM, IPC paragraph |
| `c-action-scoped-authorization` | `r-107` | Human in the Loop |
| `c-mediated-egress` | `r-108` | Network egress |
| `c-taint-aware-egress` | `r-109` | Network egress, taint/fallback paragraphs |
| `t-ebpf-policy-hooks` | `r-110` | Network egress, instrumentation paragraph |
| `c-brokered-browser` | `r-111` | Least Privilege; Browser |

All edges start at `i-muse-secure-vm-2026`. Technology records describe source-scoped use, not exhaustive specification reviews. Concept records are editorial categories and make no claim of historical priority. Their years remain unknown rather than assigning the service announcement year as an invention date.

Existing sandbox and credential-separation entities are reused. Credential exposure, permission to use authority and provider exclusion remain different properties.

## Trust boundaries

The launch entity's `details.trust_boundary_analysis` explicitly labels the user-VM-kernel interpretation as **analyst inference**, supported by the reported placement of the runtime cell and security services. The user VM's kernel is distinct from the physical host/hypervisor. This is not a formal or independently audited TCB inventory.

`details.data_flow_boundary` retains the provider's description of external inference/telemetry and the launch design's provider-access limitation. The existing renderer exposes both distinctions in the entity's `limitation` note. The update retains schema 0.3 and the existing renderer/validation implementation.

The announced Confidential VM entity, deployment status and existing relationship are unchanged. None of the new edges is inherited by it. No CPU model, TEE mode, attestation protocol or deployed confidential service is inferred from these runtime observations.

## Remaining research

`q-16` requests versioned specification/code and audit evidence for the runtime mechanisms, mediation coverage, credential authority, egress, policy updates and external data flows. The existing Confidential VM launch-status investigation remains open. Named hooks and mediation points do not prove coverage of every bypass path.

The mutable source URL still needs an immutable revision or archival identity for stronger historical reproducibility. Source-checking does not establish a complete security guarantee.

Downstream project proposals, rankings and implementation plans remain separate from the research dataset.

## Verification

Run `python3 validate.py`, `python3 inventory.py`, `python3 build_site.py` and `python3 check_site.py`. Inspect Muse Secure VM in the selected-node graph and expand relationship evidence. The eight new mechanisms and the trust-boundary note must be visible, with the announced Confidential VM kept separate.
