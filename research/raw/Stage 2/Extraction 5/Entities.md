---
stage: 2
created: 2026-10-07
extracted_from:
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/01_Background/Concepts.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/01_Background/Regimes.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/02_Origin_Evidence/OriginEvidence.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/03_Laundering_Cases/Cases.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/04_Tracing_Technologies/Technologies.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/04_Tracing_Technologies/Concentration.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/05_Origin_Record_Design/Design.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/06_Evidence/Sources.md
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

# Entities — Wave 5 (Critical Minerals and Semiconductor Supply Chains)

| Entity ID | Canonical name | Type | Boundary (what it is not) | Stage 1 source | Section | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| E001 | Provenance laundering | concept | Not sanctions evasion per se — the intermediary steps are lawful; it is the re-papering of origin absent a record that transformations append to | 01_Background/Concepts.md | §2 | high |
| E002 | Certificate of origin | concept | Not a physical witness — issued on declarer's statements and documentary review | 02_Origin_Evidence/OriginEvidence.md | §1 | high |
| E003 | Substantial transformation | concept | Not content-based origin — a last-meaningful-change test, not a value-share test | 01_Background/Concepts.md | §3 | high |
| E004 | De minimis content threshold | concept | Not a production-lineage test — attaches jurisdiction by value share of controlled content | 01_Background/Concepts.md | §3 | high |
| E005 | Foreign Direct Product (FDP) rule | concept | Not a location or content test — attaches jurisdiction by production lineage from US-origin technology/software | 01_Background/Concepts.md | §3 | high |
| E006 | Affiliates (50% ownership) rule | concept | Not entity listing — jurisdiction follows corporate ownership share, not designation | 01_Background/Concepts.md | §3 | high |
| E007 | Chain of custody | concept | Not a chain of transactions — an append-only record where breaks are visible | 01_Background/Concepts.md | §4 | high |
| E008 | Chain of transactions | concept | Not chain of custody — each hand-off re-issues fresh paperwork unconstrained by the prior record | 01_Background/Concepts.md | §4 | high |
| E009 | Attestation | concept | Not a physical witness — a party's assertion recorded on paper or in an audit | 02_Origin_Evidence/OriginEvidence.md | §5 | high |
| E010 | Physical witness (assay/isotope fingerprint) | concept | Not an affirmation of origin — a statistical consistency/exclusion statement vs a reference set | 04_Tracing_Technologies/Technologies.md | §1 | high |
| E011 | Cryptographic binding (signed manifest) | concept | Not deployed for hardware or minerals — exists as a pattern (C2PA) for media only | 04_Tracing_Technologies/Technologies.md | §5 | high |
| E012 | Assurance ceiling | concept | Not a confidence rating — the definitional limit of what a mechanism can prove | 01_Background/Concepts.md | §5 | high |
| E013 | Transformation ledger | concept | Not a blockchain — a format + verification protocol with pluggable storage, append-only through transformations | 05_Origin_Record_Design/Design.md | §3 | medium |
| E014 | Cross-assay reconciliation rule | concept | Not a new assay method — a rule requiring two independent methods for a "witnessed" claim | 05_Origin_Record_Design/Design.md | §4 | medium |
| E015 | Origin-integrity coverage metric (OIC) | concept | Not an HHI substitute — a complementary verifiability metric that scores paper-only chains at zero | 05_Origin_Record_Design/Design.md | §5 | medium |
| E016 | Claim-class ladder (attested / witnessed / reconciled) | concept | Not a confidence scale — a vocabulary for evidence class of origin claims | 05_Origin_Record_Design/Design.md | §4 | medium |
| E017 | Mineral-Origin Record | artefact | Not a central registry and not a physical-marking system — a record schema + verification protocol | 05_Origin_Record_Design/Design.md | §1–§2 | medium |
| E018 | Bureau of Industry and Security (BIS) | organization | Not a customs authority — the US export-control regulator | 01_Background/Regimes.md | §1.1 | high |
| E019 | Export Administration Regulations (EAR) | instrument | Not a sanctions list — the US export-control regulation containing de minimis, FDP, and end-use rules | 01_Background/Regimes.md | §5 | high |
| E020 | Entity List | instrument | Not an ownership rule — a US denial-party list extended to ≥50%-owned affiliates by the Affiliates Rule | 01_Background/Regimes.md | §1.1 | high |
| E021 | Ministry of Commerce of the PRC (MOFCOM) | organization | Not a customs agency — China's export-licensing and trade-control regulator | 01_Background/Regimes.md | §1.3 | high |
| E022 | MOFCOM Announcement No. 61/62 (2025) | instrument | Not a ban — a licensing regime with 0.1% de minimis and extraterritorial FDP-analog reach, suspended to Nov 10 2026 | 01_Background/Regimes.md | §1.3 | high |
| E023 | Uyghur Forced Labor Prevention Act (UFLPA) | instrument | Not an EU-style investigation regime — a US rebuttable-presumption regime burdening the importer | 01_Background/Regimes.md | §3 | high |
| E024 | Regulation (EU) 2024/3015 (Forced Labour Regulation) | instrument | Not a UFLPA analogue in burden allocation — the investigating authority bears the burden; applies from Dec 14 2027 | 01_Background/Regimes.md | §3 | high |
| E025 | Regulation (EU) 2024/1252 (Critical Raw Materials Act) | instrument | Not an export-control regime — supply-security benchmarks and strategic-project permitting | 01_Background/Regimes.md | §2 | high |
| E026 | OECD Due Diligence Guidance (minerals) | instrument | Not a verification standard — an attestation-based five-step due-diligence framework | 02_Origin_Evidence/OriginEvidence.md | §2 | high |
| E027 | Regulation (EU) 2017/821 (conflict minerals) | instrument | Not a ban — importer due-diligence obligations for 3TG aligned to the OECD framework | 02_Origin_Evidence/OriginEvidence.md | §4 | high |
| E028 | Regulation (EU) 2023/1542 (Battery Regulation) | instrument | Not the ESPR — the sector regulation carrying due-diligence duties and the Battery Passport | 04_Tracing_Technologies/Technologies.md | §4 | high |
| E029 | EU Battery Passport | instrument | Not proof of origin — a QR-accessible structured record whose data is self-attested unless tied to audits/assays | 04_Tracing_Technologies/Technologies.md | §4 | high |
| E030 | Regulation (EU) 2024/1781 (ESPR) and its Digital Product Passport | instrument | Not the battery passport regime — the general product framework; batteries excluded; product delegated acts pending | 04_Tracing_Technologies/Technologies.md | §4 | high |
| E031 | EU Falsified Medicines Directive safety features (Dir 2011/62/EU + Reg (EU) 2016/161) | instrument | Not a mineral scheme — the pharma serialization template (unique ID + EU hub + national verification) | 04_Tracing_Technologies/Technologies.md | §3 | high |
| E032 | US Drug Supply Chain Security Act (DSCSA) | instrument | Not a mineral or chip scheme — package-level electronic pharmaceutical traceability in a legally closed channel | 04_Tracing_Technologies/Technologies.md | §3 | high |
| E033 | GS1 standards family (GTIN/GLN, EPCIS 2.0, Digital Link) | standard | Not a provenance system — the identifier and event-layer standards under serialization and passports | 04_Tracing_Technologies/Technologies.md | §4 | high |
| E034 | Coalition for Content Provenance and Authenticity (C2PA) | standard | Not a hardware standard — signed-manifest provenance for media; no hardware equivalent deployed | 04_Tracing_Technologies/Technologies.md | §5 | high |
| E035 | BGR Analytical Fingerprint (AFP) | technology | Not a proof of origin — LA-ICP-MS + U-Pb grain analysis vs a BGR-internal >2,000-sample database yielding consistency statements | 04_Tracing_Technologies/Technologies.md | §1 | high |
| E036 | Electronic Chip ID (ECID) | technology | Not a public provenance system — a die-level unique register verifiable only by electrical query, mappings privately held | 04_Tracing_Technologies/Technologies.md | §5 | high |
| E037 | DNA ink marking (DLA / Applied DNA) | technology | Not universal coverage — a spot-check physical witness for marked military-standard microcircuits | 04_Tracing_Technologies/Technologies.md | §5 | high |
| E038 | ITSCI | scheme | Not an enforcement body — an industry tag-and-trace scheme for 3T with documented coverage holes | 03_Laundering_Cases/Cases.md | §4 | high |
| E039 | Initiative for Responsible Mining Assurance (IRMA) | scheme | Not a provenance scheme — third-party mine-site ESG audits at audit time only | 02_Origin_Evidence/OriginEvidence.md | §3 | high |
| E040 | Responsible Minerals Initiative / RMAP | scheme | Not a physical-trace system — smelter-audit program at the blending point | 02_Origin_Evidence/OriginEvidence.md | §3 | high |
| E041 | Tracr | system | Not an industry-wide ledger — De Beers' closed single-operator provenance system | 04_Tracing_Technologies/Technologies.md | §2 | high |
| E042 | Circulor | system | Not an independent verifier — a supplier-attested event ledger used by Volvo/Polestar | 04_Tracing_Technologies/Technologies.md | §2 | high |
| E043 | Re\|Source | system | Not a confirmed commercial operation — a 2021 cobalt batch-tracking pilot with no confirmed commercialization | 04_Tracing_Technologies/Technologies.md | §2 | medium |
| E044 | Everledger | company | Not an operating ledger — a provenance startup that entered voluntary administration in May 2023 | 04_Tracing_Technologies/Technologies.md | §2 | high |
| E045 | Perth Mint | company | Not an accredited-origin guarantor — a refinery whose 2023 dilution/AML findings illustrate pool-blending provenance loss | 03_Laundering_Cases/Cases.md | §6 | high |
| E046 | Nexperia | company | Not a sanctioned product — a Wingtech-owned chipmaker seized by the Netherlands whose Dongguan-made chips were counter-banned by China | 04_Tracing_Technologies/Concentration.md | §4 | high |
| E047 | MP Materials | company | Not a provenance system — a US rare-earth producer backed by the DoD price-floor deal | 04_Tracing_Technologies/Concentration.md | §3 | high |
| E048 | UN Group of Experts on the DRC | organization | Not a court — a UN Sanctions Committee expert body whose reports document coltan flows | 03_Laundering_Cases/Cases.md | §4 | high |
| E049 | European Anti-Fraud Office (OLAF) | organization | Not a customs service — the EU investigative body whose caseload documents false-origin fraud | 02_Origin_Evidence/OriginEvidence.md | §1 | high |
| E050 | G7 Antwerp diamond node | system | Not a global traceability system — a G7 verification node covering a size band of rough diamonds | 03_Laundering_Cases/Cases.md | §2 | high |
