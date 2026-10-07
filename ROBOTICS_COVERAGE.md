# Scope Review: Embedded Mechanisms and Trusted Actuation

Scope reviewed **2026-10-07** against the hardware-rooted mission that predates the robotics extraction, and the public-source curation boundary. The robotics-specific wording added during extraction is not used to justify its own inclusion.

## Verdict

Robotics is not an independent coverage objective for Trust Atlas. Some mechanisms and a specific TEE application case fit the existing objective; a general robotics-security catalogue does not.

The initial extraction grouped 13 entities and 14 relationships under robotics. This review retains **nine entities and ten relationships**, reclassifies them by mechanism or bounded case, and separates the four-record ROS/DDS cluster from the active graph. The current dataset has **86 entities, 122 relationships and 65 source records**. Bibliometrics and the retained relationship claims are unchanged.

## Admission criteria

1. The record has a checked, publicly available source at an identifiable location.
2. It directly documents hardware-rooted enforcement, or explains a source-backed dependency, limit, attack or comparison for a specific in-scope case.
3. Its scope distinguishes mechanism capability, deployment, security guarantees and assurance evidence.
4. It adds explanatory value to the central trust-boundary question without making an application domain a new project objective.

Public availability is necessary but insufficient. Graph connectivity is a useful diagnostic, not proof of scientific relevance. A focal service's explicitly unresolved hardware path also does not license speculative links to unrelated platforms.

## Record-level decisions

| Records | Decision | Reason |
|---|---|---|
| OP-TEE and Hafnium | Keep under `open-tee` | They directly describe secure-world execution/partition mechanisms |
| Verified boot, firmware rollback protection and Jetson AGX Thor | Keep under `hardware` | They document hardware-rooted boot and platform capabilities, independently of robotics |
| Contego-TEE | Keep as one `trusted-actuation` paper case | It explicitly uses TrustZone/OP-TEE to mediate actuator requests |
| Reported RPi 3B platform, actuation invariants and fallback control | Keep as supporting context for Contego-TEE | They explain the evaluated configuration, protected operation and limits of that case; they are not a general control-theory survey |
| SROS 2 design, DDS Security 1.1, ROS identity enclave and authenticated pub/sub | Separate from the active graph | The checked sources do not connect this standalone middleware cluster to an included hardware-rooted case |
| Janus | Keep only in the public-evidence collection queue | Its subject is potentially relevant, but the manuscript and technical boundaries remain unreviewed |

## Why the retained material fits

[NVIDIA's OP-TEE documentation](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/Security/OpTee.html) directly identifies TrustZone-based secure-world execution. The related [Hafnium](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/Security/Hafnium.html), [Secure Boot](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/Security/SecureBoot.html) and [Rollback Protection](https://docs.nvidia.com/jetson/archives/r38.4/DeveloperGuide/SD/Security/RollbackProtection.html) records describe mechanisms within the existing scope. No particular robot, enabled configuration or confidential-GPU guarantee is inferred from platform support.

[Contego-TEE](https://sibin.github.io/papers/2019_IoTSnP_ContegoTee_Monowar.pdf) is a public, specific use of those security concepts. The record remains a paper-reported prototype with explicit limits. It does not claim independent reproduction, complete I/O mediation or universal physical safety. Its supporting context records identify `p-contego-tee-2019` as their scope anchor.

This is a mechanism-to-application example, not an authorization to catalogue perception models, motion planning, robot products or functional-safety methods generally.

## Why ROS/DDS is separated

The [ROS enclave design](https://design.ros2.org/articles/ros2_security_enclaves.html) describes identities and permissions associated with contexts. It does not establish a hardware TEE. The [DDS integration document](https://design.ros2.org/articles/ros2_dds_security.html) establishes middleware authentication/access-control behavior, but the current extraction provides no deployment or dependency evidence tying that cluster to the included TEE/boot cases.

All four cluster edges (`r-128` through `r-131`) stayed within its four records; there were no external edges. That observation corroborates the missing source-backed connection but is not the sole exclusion criterion. Adding a plausible ROS-to-Jetson or ROS-to-OP-TEE edge just to connect the diagram would be incorrect.

The records, original claims, three source records and `q-22` are preserved in a separate local scope-review archive. Their stable IDs are reserved for reconsideration if a specific public-source connection is established. This is a scope decision, not a finding that DDS is insecure or that the recorded source statements are false. A short terminology caution can remain in this review without making the middleware an independent active subgraph.

## Remaining public-source gaps

- `q-19`: published artifacts and evaluations clarifying the Contego-TEE case's mediation, sensor/peripheral assumptions and timing.
- `q-20`: public integration evidence for systems using the recorded embedded boot/TEE mechanisms, rather than an open-ended robot catalogue.
- `q-21`: readable Janus primary material and manifestation resolution before admitting technical relationships.

These are curation questions. They do not request new implementations, experiments or follow-on development projects.

## Verification

Validate references and source/data synchronization after separating the cluster. Confirm that all retained relationship claims, evidence strengths, source dates and citation observations are unchanged; each context anchor resolves; excluded IDs are absent from the active data and view; and the separate development-candidate reports are unchanged. Atlas checks do not establish security or safety of the researched systems.

This revision passed the validator, inventory generation, site build, export checks, JavaScript syntax check and a preservation/scope audit. The browser confirmed the embedded-mechanism headings, absence of the SROS entry and keyboard navigation to the retained Contego-TEE case. No browser errors were observed in that check.
