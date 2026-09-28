# Initial Seed Review (Historical)

Snapshot: 2026-09-28. This is the historical record of the first eight-paper seed, now maintained in English under **Trust Atlas**. It is superseded for current coverage by [the graph review](GRAPH_REVIEW.md) and [the dataset](data/atlas.json).

The seed checked official documents and publication/abstract pages. It did not represent complete full-text review or independent testing of provider security claims.

## Original citation observations

OpenAlex records were matched against titles, authors, publication years, and, for Keystone, the DOI linked by the project. Conference and journal counts were not combined. These are provider-index observations, not normalized measures of research quality.

| Paper | Venue and year | OpenAlex citations | Original source |
|---|---|---:|---|
| The Protection of Information in Computer Systems | Proceedings of the IEEE · 1975 | [1897](https://openalex.org/W2095881341) | [Paper/page](https://web.mit.edu/Saltzer/www/publications/protection/) |
| Terra: A Virtual Machine-Based Platform for Trusted Computing | SOSP · 2003 | Unresolved in initial seed | [Paper/page](https://xenon.stanford.edu/~talg/papers/SOSP03/abstract.html) |
| Shielding Applications from an Untrusted Cloud with Haven | OSDI · 2014 | [362](https://openalex.org/W1852007091) | [Paper/page](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/baumann) |
| Intel SGX Explained | IACR Cryptology ePrint Archive · 2016 | [751](https://openalex.org/W2397423248) | [Paper/page](https://eprint.iacr.org/2016/086) |
| Sanctum: Minimal Hardware Extensions for Strong Software Isolation | USENIX Security · 2016 | [349](https://openalex.org/W2463516579) | [Paper/page](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/costan) |
| Foreshadow: Extracting the Keys to the Intel SGX Kingdom with Transient Out-of-Order Execution | USENIX Security · 2018 | [686](https://openalex.org/W2888798936) | [Paper/page](https://www.usenix.org/conference/usenixsecurity18/presentation/bulck) |
| Graviton: Trusted Execution Environments on GPUs | OSDI · 2018 | [130](https://openalex.org/W2899435347) | [Paper/page](https://www.usenix.org/conference/osdi18/presentation/volos) |
| Keystone: An Open Framework for Architecting Trusted Execution Environments | EuroSys · 2020 | [382](https://openalex.org/W3021475380) | [Paper/page](https://keystone-enclave.org/) |

Haven's OSDI 2014 and TOCS 2015 manifestations appeared separately; the seed used OSDI and did not sum them. Terra was initially unresolved and was left blank rather than assigned an unrelated search result. That gap has since been resolved by DOI in the current dataset. Venue acceptance rates were initially left unknown. Haven's Best Paper designation was checked on its [USENIX page](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/baumann).

## Version distinctions established in the seed

The seed separated Apple's 2024 PCC design and 2026 expansion, Google's 2025 introduction and 2026 memory update, Meta's 2025 Private Processing description and 2026 glasses architecture, and Muse Secure VM from the announced Confidential VM capability. The entries captured provider descriptions rather than independent assurance results.

Sources: [Apple 2024](https://security.apple.com/blog/private-cloud-compute/), [Apple 2026](https://security.apple.com/blog/expanding-pcc/), [Google 2025](https://blog.google/innovation-and-ai/products/google-private-ai-compute/), [Google 2026](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/), [Meta 2025](https://engineering.fb.com/2025/04/29/security/whatsapp-private-processing-ai-tools/), [Meta 2026](https://engineering.fb.com/2026/09/23/security/private-processing-meta-ai-glasses/), and [Muse](https://security.muse.ai/).

## Limits of the seed

The seed did not establish which papers were direct ancestors of a particular service, a universal security ranking, current general availability of announced capabilities, or field-normalized citation influence. Original relationship evidence, full threat models, audit scope, and rollout status required further work.

Structural validation checked internal consistency. It did not turn screened records into independently verified or accepted research. The initial methodology has since been refined into the hardware-to-service scope in [the charter](CHARTER.md).
