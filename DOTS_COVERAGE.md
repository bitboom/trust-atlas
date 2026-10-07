# Dots: Governance and Execution Boundaries

Official documentation observed **2026-10-07**. This profile describes that documentation snapshot, not a version-pinned implementation or completed security assessment.

## Inclusion decision

OpenAI [identifies dots](https://learn.chatgpt.com/docs/dots) as cloud agents with their own computer/browser and a gradual rollout. Dots belongs alongside the existing Muse case as a service-composition comparison. The checked sources do not establish its CPU/TEE identity, a complete TCB, attested execution or provider exclusion. Those gaps remain visible in the implementation record rather than being filled from another product.

The update adds one implementation, five concepts and six non-lineage `uses` edges (`r-112` through `r-117`). The existing credential-separation concept is reused. All six relationship claims are vendor descriptions, not independently validated properties.

## Extracted distinctions

| Observation | Source and location | Interpretation boundary |
|---|---|---|
| Computer, browser/network, app and communication controls are separate | [Admin guide](https://learn.chatgpt.com/docs/enterprise/dots-admin-guide), Available admin controls; FAQ | Enabling dots does not authorize every service or local resource |
| Local access is separately connected; offline is not revoked | [Computers and apps](https://learn.chatgpt.com/docs/dots/computers-and-apps), Connect your computer | Availability is not authorization lifecycle |
| Custom rules are instructions the agent can get wrong | [Controls](https://learn.chatgpt.com/docs/dots/controls), Set custom rules | Do not classify them as mandatory OS/hardware enforcement |
| Main-task pause, delegated-task stop and schedule cancellation differ | Controls, Stop work | No global kill-switch or rollback of completed actions is inferred |
| Automatic review chooses execution, approval or handoff | Controls, How action review works | Implementation, completeness and bypass resistance remain unreviewed |
| Private sign-in sends credentials outside the conversation | Computers and apps, Sign in to a website | This flow does not prove universal credential invisibility or provider exclusion |

## Comparison with Muse

Muse's checked launch account names specific runtime mechanisms; the dots sources here primarily describe product-level controls and boundaries. This difference in disclosure is not evidence that either system is more secure. No `systemd-nspawn`, eBPF, TrustZone, TDX or SEV link is assigned to dots without dots-specific evidence.

The Work Cloud security documentation was consulted for context. Statements scoped to Work or Codex are not silently transferred to dots. Shared capabilities are accepted only where the dots documentation itself identifies their applicability.

## Time and remaining work

The dataset advances to an **incremental** October 7 snapshot to accommodate current documentation. Existing citation values, source dates and relationship claims are unchanged. The view renders each citation's own provider/date instead of treating the new dataset date as a fresh citation observation.

`q-17` covers low-level execution/attestation and audit evidence. `q-18` covers authority, revocation, saved-data and delegated-work lifecycles. Live documentation has no immutable revision supplied here; future changes must be rechecked before updating this version's conclusions.

This is research metadata. Product ideas, development priorities and candidate projects remain outside Trust Atlas. No dots account, computer permission, connection or schedule was changed during the research.
