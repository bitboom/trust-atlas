# Hardware and Configuration Coverage

Snapshot: 2026-09-28. This update distinguishes **security technology → hardware family/platform → supported mode/reference stack → documented service**. Capability support is not proof that a particular machine is enabled, attested, or operated correctly.

## Inventory change

| Entity type | Before | After |
|---|---:|---:|
| Papers | 15 | 15 |
| Concepts | 14 | 14 |
| Security technologies | 10 | 9 |
| Hardware families/platforms | 0 | 10 |
| Modes/reference configurations | 0 | 4 |
| Service/design versions | 8 | 9 |
| Standards | 2 | 2 |
| **Total** | **49** | **63** |

Relationships increased from 60 to 98. H100 was already present as a technology record; it was normalized to hardware without changing its `t-h100` identifier. Its former 2023 date was a document milestone, so it is not retained as a hardware launch year. All prior citation observations remain unchanged.

[INVENTORY.md](INVENTORY.md) defines catalogue leaves and provides reproducible counts. The type catalogue has one root, seven categories, and 63 entity leaves: 71 navigation nodes. The root/categories are presentation metadata, not extra research entities. Four declared research layers and nine populated topic branches are separate organizing dimensions.

## Added hardware structure

| Technology | Hardware represented | Scope |
|---|---|---|
| Intel TDX | 5th Gen Xeon Scalable / Emerald Rapids; Xeon 6 P-core / Granite Rapids | CPU-family support and a documented reference-stack host; exact SKU/OEM enablement still matters |
| AMD SEV-SNP | EPYC 7003 / Milan, 9004 / Genoa, 9005 | Generation-level support; the checked NVIDIA reference table lists Milan/Genoa, not 9005 |
| NVIDIA GPU Confidential Computing | H100, H200, B200, Blackwell Ultra GPU component for B300, HGX B300 platform | GPU families and the eight-GPU platform are distinct; support is limited to documented variants and modes |

Sources: [Intel TDX hardware selection](https://cc-enabling.trustedservices.intel.com/intel-tdx-enabling-guide/03/hardware_selection/), [AMD EPYC architecture](https://docs.amd.com/api/khub/documents/UIqhAbjRhgnzgzzdVU4pUw/content), [NVIDIA supported platforms](https://docs.nvidia.com/datacenter/cloud-native/confidential-containers/latest/supported-platforms.html), and [HGX B300 composition](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/abstract.html).

## Mode-specific guarantees

The mode records are tied to NVIDIA R595 GA release notes, RN-12817-001_v02, April 2026.

- **SPT CC:** one passed-through GPU per CVM; encrypted CPU–GPU traffic uses a bounce buffer.
- **Hopper PPCIe:** listed multi-GPU HGX Hopper configurations. GPU peer traffic over NVLink/NVSwitch is unencrypted in this mode.
- **Blackwell MPT CC:** up to eight GPUs per CVM on named HGX B200/B300 variants, with encrypted NVLink peer traffic.

These distinctions come from [the release notes, Feature Summary](https://docs.nvidia.com/595trd1-trusted-computing-solutions-release-notes.pdf). They are not generalized to every product with the same family name. Exact firmware, driver, verifier, and platform combinations remain source-scoped.

The **NVIDIA Confidential Containers reference architecture** is a fourth configuration record, not a deployed commercial service. Its checked page requires all host GPUs to be configured for CC and assigned to one confidential-container VM. This reference-stack constraint is separate from the more general SPT mode description. Intel TDX and AMD SEV-SNP are alternative CPU backends, not simultaneous requirements. The two documentation versions must not be mixed into an invented support matrix.

## Hardware-to-service path

The new **Azure NCCads H100 v5** profile is linked to AMD EPYC Genoa, SEV-SNP, and the H100 family. Microsoft identifies the GPU variant as H100 NVL in the size documentation. This is a provider-documented service path; regional capacity and the user's account eligibility were not checked.

Sources: [Azure size specifications](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nccadsh100v5-series) and [Azure confidential GPU options](https://learn.microsoft.com/en-us/azure/confidential-computing/gpu-options).

No link from B300 to Apple PCC, Google Private AI Compute, Meta Private Processing, or a particular public-cloud CC SKU was inferred. The current B300 path ends at the documented hardware/mode/reference-integration evidence. Absence of a service edge is an evidence gap, not a claim that no such service exists.

## Schema and validation

Schema 0.3 adds `hardware` and `configuration` entity types and four relation types:

- `supports`: hardware/reference configuration → security technology.
- `contains`: hardware platform → physical component.
- `validated_with`: configuration → listed hardware. This means vendor-listed compatibility, not independent verification.
- `supports_mode`: reference architecture → mode configuration.

The validator checks these endpoint types and required hardware/configuration scope fields. Run `python3 validate.py` and `python3 inventory.py` after edits. Catalogue membership must cover each graph entity exactly once. This update does not complete the overall literature or assurance review.
