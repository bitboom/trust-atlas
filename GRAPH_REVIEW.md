# First Knowledge Graph Review

Historical 49-entity phase. Current hardware-expanded counts and coverage are in [INVENTORY.md](INVENTORY.md) and [HARDWARE_COVERAGE.md](HARDWARE_COVERAGE.md).

Snapshot: **2026-09-28**. The graph contains 49 entities, 60 relationships, and 47 source records: 15 papers, eight service/design-version profiles, and supporting concepts, technologies, and standards. Source records include publication pages, manuscripts, and citation API records; they are not 47 independent studies.

The project is now **Trust Atlas**, with English as its canonical language. The [charter](CHARTER.md) establishes a broader hardware-to-service research frame. The rename and translation preserve entity identities, observed metrics, evidence strength, and the original snapshot date. They do not imply completion of the broader scope.

## Interpreting the view

The technology tree is an explanatory projection of a typed graph. Vertical position is not a strict timeline, and undated concept nodes do not represent invention dates. Read the relation type and its evidence before interpreting an edge as inheritance.

The overview shows 34 selected entities. All 49 are available through the entity catalogue. Strong lines identify explicit extension; ordinary lines represent component use, study, or citation; dashed lines identify conceptual links or interpretation. The selected-node graph preserves subject-to-object relation direction.

## Checked relationships

- **Sanctum → MI6:** the [MI6 abstract and section 3.3](https://arxiv.org/abs/1812.09822) explicitly describe extension. The MICRO 2019 manifestation is kept separate from the 2018 preprint.
- **SEV → SEV-ES → SEV-SNP:** the [AMD 2020 whitepaper](https://docs.amd.com/api/khub/documents/atTablNxGjuR5pX3kM7WdQ/content) describes added protection of memory, CPU state, and integrity across generations.
- **Flicker ↔ TrustVisor:** [TrustVisor sections 3.2, 4.1, and 4.3](https://ptolemy.berkeley.edu/projects/truststc/pubs/750/mlqzdgp-oakland2010.pdf) support a design alternative addressing performance limitations, without establishing code inheritance.
- **Keystone ↔ Sanctum:** the [Keystone comparison table and related work](https://arxiv.org/abs/1907.10119) support citation and comparison. The edge is not promoted to direct inheritance.
- **Controlled-Channel → Haven:** [section V.A](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ctrlchannels-oakland-2015.pdf) scopes the attack to the described Haven prototype and assumptions.
- **Komodo → TrustZone:** the [Komodo abstract](https://www.andrew.cmu.edu/user/bparno/papers/komodo.pdf) identifies the prototype platform. This does not make every later Arm security architecture a descendant.

Service-version links retain their vendor-statement status. The existing data distinguishes Apple's PCC expansion, stateful Google/Meta designs, and Muse Secure VM versus the announced Confidential VM.

## Muse batch and source comparison

A bounded eight-paper discovery batch completed with Muse. Its private conversation and receipt are excluded from this public repository. Candidate findings were checked against the public primary sources below. No recurring job was created; subsequent briefs request English output.

Candidate relations and metadata were compared with selected primary-source sections. The MI6–Sanctum and TrustVisor–Flicker distinctions were incorporated. Some Keystone wording/section claims, code-reuse conclusions, and Muse-supplied citation totals were not treated as independently checked facts.

Muse's report of reading full papers is distinct from Codex's review depth. The recorded number of completed comprehensive full-text reviews remains zero; selected sections and abstracts have been checked.

## Metrics and gaps

- **Citations:** 14 of 15 paper manifestations have OpenAlex observations matched by metadata/DOI. Terra's earlier matching gap was resolved. Version totals were not added together.
- **Slalom:** the search matched the 2018 preprint. That count was not substituted for the 2019 conference manifestation.
- **Selectivity:** the [IEEE S&P 2010 conference report](https://www.ieee-security.org/Cipher/ConfReports/2010/CR2010-SP-tech-2010.html) states 26 research acceptances from 237 submissions and separately reports five SoK acceptances. The displayed 10.97% is the reported research-paper ratio, not an overall conference acceptance rate. Twelve other conference-paper records still lack verified statistics.
- **Influence:** the graph describes contributions, extensions, and component use without manufacturing a 0–100 quality or security score.
- **Scope:** hardware primitives, complete trust-dependency paths, assurance comparisons, and deployment updates still require further research. The charter is the target scope, not a claim of present coverage.

## Validation history

The dataset passed `python3 validate.py` checks for references, duplicate IDs, provenance, dates, and lineage cycles. The original exploration view was exercised through tree → MI6 graph → tree using keyboard input; 736px and 360px screens were inspected and 320px horizontal overflow was checked. No browser execution error was observed in that check.

The English revision passed language-completeness, graph/data synchronization, and JavaScript syntax checks. The MI6 selection and map return were exercised with keyboard input. English details were inspected at 360px and the map at 736px. Four labels were shortened after a 320px check; the final root width and scroll width both measured 288px, with no overflowing node labels. See `data/language-revision-checks.json` for this revision’s checks.

The full dataset-v1 review and GitHub Pages publication are not complete. Next research priorities are hardware roots and early attestation, explicit trust dependencies, transparency origins, and service-specific audit/deployment scope.
