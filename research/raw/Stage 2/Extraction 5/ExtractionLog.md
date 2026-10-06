---
stage: 2
created: 2026-10-07
extracted_from:
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/README.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/00_Index/Index.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/00_Index/Synthesis.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/01_Background/Concepts.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/01_Background/Regimes.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/02_Origin_Evidence/OriginEvidence.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/03_Laundering_Cases/Cases.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/04_Tracing_Technologies/Technologies.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/04_Tracing_Technologies/Concentration.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/05_Origin_Record_Design/Design.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/06_Evidence/Sources.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/06_Evidence/Findings.md
extractor: stage2-extractor-agent
gate_results:
  gate_1_source_coverage: pass
  gate_2_claim_traceability: pass
  gate_3_evidence_class_integrity: pass
  gate_4_metric_conditions: pass
  gate_5_entity_completeness: pass
  gate_6_extraction_log_completeness: pass
  gate_7_ingestibility: pass
---

# ExtractionLog — Wave 5 (Critical Minerals and Semiconductor Supply Chains)

_Extraction of 2026-10-07 from the Wave 5 Stage 1 survey (research pass dated 2026-10-06). One row per non-obvious extraction decision._

| Log ID | Step | Stage 1 source | Decision type | Description | Resolution |
| --- | --- | --- | --- | --- | --- |
| L001 | Step 1 | README.md | scope_boundary | Stage 1 mixes a survey corpus (external facts) with a design deliverable (Mineral-Origin Record v0) and article-facing outputs. | Survey facts extracted to Claims/Metrics/Entities; design deliverable extracted as `recommendation` claims + entities; article brainstorm (Artifacts) excluded from extraction (not Stage 1 research). |
| L002 | Step 1 | All notes | label_resolution | Stage 1 uses P/T/C source reliability plus claim labels (documented fact / reported signal / inference / recommendation). | Reliability mapped for the Classification column: P→Primary, T→Secondary, C→Primary (self-published; the *claim* keeps reported-signal/low-medium confidence — never promoted). Claim-type labels copied verbatim. |
| L003 | Step 2 | 06_Evidence/Sources.md | label_resolution | Stage 1 register IDs are zero-padded (S01–S75). | Preserved exactly per protocol ("If an identifier was already assigned in Stage 1, preserve it exactly"); downstream consumers must not re-key as S1–S75. |
| L004 | Step 2 | 06_Evidence/Sources.md | classification_conflict | Several register entries bundle multiple documents (e.g., S01 = BIS press release + Federal Register rule; S40 = ABC + Reuters + AFR). | Kept as one row per Stage 1 entry (Stage 1 assigned one ID per bundle); the most authoritative document in each bundle governs Classification. |
| L005 | Step 2 | 06_Evidence/Sources.md (domain-level URLs) | label_resolution | Many Stage 1 sources record domain-level URLs only ("exact article path not surfaced"); some rows have no publication date. | URL recorded as Stage 1 states it (domain or full path); unknown dates recorded as `n.d.`. Flag: re-pin exact URLs at drafting time (mirrors Stage 1 open follow-ups). |
| L006 | Step 2 | (new) | label_resolution | Stage 1 contains facts stated in notes without an external register citation (definitions, design choices, synthesis statements). | Added internal-corpus source row S76 (Internal classification), following the Fusion Energy precedent (its S51). Claims resting on synthesis cite S76. |
| L007 | Step 7 | Concepts.md, Cases.md, Technologies.md | label_resolution | Stage 1 provides no numbered subject-domain workflow table; workflow positions are described narratively (mining → refining/blending → distribution → manufacturing → import → compliance → enforcement). | Assembled W01–W07 from explicitly described stages only; every Quality-gates cell states an observable check (tag present, audit certificate exists, ECID queries back, certificate present, indictment filed). Assembly decision recorded here. |
| L008 | Step 5 | Regimes.md §1.1 | evidence_downgrade | BIS FY2025 penalty figures (~$324M) were flagged in Stage 1 as "secondary citation — verify against BIS annual report". | Recorded as `reported signal`, confidence `low` (M013/M014, C012), matching the Stage 1 flag rather than the T-class source. |
| L009 | Step 5 | Concentration.md §1 | evidence_downgrade | TSMC sub-7nm ~90% share is marked UNVERIFIED-BACKGROUND in Stage 1. | Excluded from Metrics entirely; no claim row carries it (protocol: unsupported specificity rejected). |
| L010 | Step 6 | Concentration.md §1 | condition_absent | Analyst HBM shares differ by quarter and definition (Counterpoint vs Yole vs TrendForce). | Recorded as a range (M038) with the conflict stated in Scope; both source families named in one row per Stage 1 register bundling. |
| L011 | Step 6 | Concentration.md §4 | omission | Stage 1 explicitly declines the Ford Explorer / JLR halt claims (conflated with Nexperia crisis and JLR cyberattack) and quantified Oct-2025-control impact estimates. | Not extracted as claims or metrics; recorded here so downstream users do not reinstate them. |
| L012 | Step 5 | Cases.md §5 | label_resolution | Stage 1 labels C4ADS "Covert Compute" as NGO/method-based (ESTIMATE), and the arXiv smuggling estimate as ESTIMATE (academic preprint). | Both extracted as `reported signal` at `medium`/`low` confidence respectively; ESTIMATE label preserved in Scope/conditions columns. |
| L013 | Step 3 | Concepts.md §2–§5 | boundary_absent | Stage 1 concepts (E001–E017) are analytic definitions rather than sourced entity definitions with explicit boundaries. | Boundaries written from the Stage 1 definitions themselves (each states what the concept is *not*); flagged as boundary-by-definition rather than boundary-by-source. |
| L014 | Step 5 | Findings.md, Synthesis.md | label_resolution | Stage 1 "inference" findings on regime structure (C018, C034, C056, C059, C061, C063, C064) rest on multiple sources. | Extracted as `inference` with the full source set listed; evidence class never promoted to documented fact. |
| L015 | Step 5 | Design.md | label_resolution | Design requirements (transformation ledger, claim-class ladder, OIC metric) are the wave's deliverable proposals, not facts about the world. | Extracted as `recommendation` claims (C057–C060) with S76 (internal corpus); falsifier column `—` (a recommendation is not source-falsifiable), per protocol the type label carries the distinction. |
| L016 | Step 5 | Design.md §4 | open_question | Whether the battery passport or an ESPR product act becomes the first legislated machine-checkable origin surface. | Carried forward unresolved in C060 (stated as inference with explicit falsifier); not resolved editorially. |
| L017 | Step 5 | Findings.md open follow-ups | open_question | Nine open follow-ups from Stage 1 (BIS penalty verification, TSMC tracker figure, WCO statistics, license-approval rate, truce expiry status, Perth Mint/Iran, Re\|Source fate, SIA/BCG weak-links count, Ga/Ge transshipment cases). | Carried forward unresolved; several materialize as `reported signal`/`low` confidence rows (C012/M013–M014, C029/M011); the rest live here and in Stage 1 Findings.md. |
| L018 | Step 2 | 06_Evidence/Sources.md | label_resolution | Stage 1 register mixes "T" for state-affiliated media (Global Times, Xinhua) and corporate primary records (ASML statements). | S32 (Xinhua) kept Primary as official announcement of record with confidence held at `medium`–`low` on dependent claims (M008); S08/S10 mixed bundles classified by their governing document (S10 → Primary: White House fact sheet). |
| L019 | Step 4 | Cases.md §7, Regimes.md §5 | label_resolution | Stage 1 uses informal relationship phrasing ("shifts burden to importer", "jurisdiction follows ownership"). | Mapped to standard predicates: `imposes_burden_on`, `determines_origin_of`, `controls`, `re_papers_origin_of`, `blends`, `transships`; original phrasing preserved in Examples. |
| L020 | Step 6 | Regimes.md §2 | condition_absent | Stage 1 antimony price (~$52,000/t late 2026) lacked a stable single-source anchor in the register (MarketScreener secondary). | Excluded from Metrics (weak anchor + volatile price); logged as deliberate omission rather than extracted at low confidence. |
| L021 | Gate 7 | Sources.md | label_resolution | Ingestion verification (2026-10-07, `ingest_citations.py` against `data/citations.duckdb`, full Stage 2 run: 35 documents, 291 sources, 349 claims). Sources.md warnings total 55, all explained: 54 × `source_rows_lacking_direct_urls` (domain-level URLs retained as Stage 1 records them — L005; re-pin exact paths at drafting time), 1 × `unresolved_alias` (S76 internal-corpus row carries no URL by design — L006, Fusion Energy S51 precedent). Two pre-flight defects were fixed before this final run: S42 title contained an unescaped pipe (`Re\|Source`) that split the table row, and S49's title contained a bare domain (`pharma.solutions`) that the URL scanner read as a second candidate (`duplicate_candidate`). Claims.md shows 90 `unresolved_alias` warnings because the parser resolves S-aliases per document and Claims.md holds no source table — identical to the accepted Extraction 3 pattern (its gate_7 = pass with the same shape); `claim_source` mappings are 0 corpus-wide, a parser limitation, not an extraction defect. | Gate 7: pass — every warning is explained in this entry (protocol §5 Gate 7 allowance). |
| L022 | Gate summary | All | label_resolution | Gate summary row (not a content decision): results for Gates 1–7 recorded here and in each file's frontmatter. | Gate 1: every claim/metric source ID ∈ S01–S76. Gate 2: every claim row names its Stage 1 file + section. Gate 3: no evidence class promoted (inferences and recommendations kept, downgrades logged at L008–L010). Gate 4: no `[conditions not stated in source]` rows remain — conditions were either stated in Stage 1 or the metric was omitted (L020). Gate 5: all 50 entities carry non-empty boundaries. Gate 6: this log. Gate 7: L021. |
