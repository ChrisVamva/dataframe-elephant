---
stage: 2
created: 2026-10-07
extracted_from:
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/01_Background/Concepts.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/02_Origin_Evidence/OriginEvidence.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/03_Laundering_Cases/Cases.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/04_Tracing_Technologies/Technologies.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/05_Origin_Record_Design/Design.md
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

# WorkflowMap — Wave 5 (Critical Minerals and Semiconductor Supply Chains)

_The Stage 1 survey describes the regulated supply-chain workflow through its laundering taxonomy and case corpus rather than as a numbered stage table. The stages below assemble those explicitly described positions (mining → refining → distribution → manufacturing → import → compliance → enforcement); the assembly decision is logged in ExtractionLog.md (L007)._

| Stage ID | Stage name | Inputs | Activities | Outputs | Quality gates | Roles | Tools | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W01 | Mining and upstream extraction | Ore bodies, ASM/LSM operations | Extraction of 3TG, cobalt, REE, Ga/Ge ores; bagging and local tagging | Mineral concentrates, tagged bags | ITSCI-style tag applied at scheme-covered points (observable: tag present; coverage holes documented when scheme suspended) | Miners, cooperatives, scheme field agents | ITSCI tag-and-trace | S21, S26, S27 | high |
| W02 | Refining, smelting and blending | Mineral concentrates, doré, polysilicon feed | Smelting/refining; blending of feedstocks (incl. ASM into industrial feeds) | Refined metals, alloys, polysilicon, wafers | Smelter audit (RMAP/OECD step 4) — attests paper system, not physical origin; refinery output is provenance-destroying (observable: audit certificate exists) | Smelters, refiners, auditors | RMAP audits, assay QC (OREAS-class CRMs) | S21, S23, S28, S40 | high |
| W03 | Component and chip manufacturing | Refined materials, wafers | Wafer fab, die manufacture, packaging (OSAT), chip marking | Semiconductors with surface marks and die-level ECIDs | ECID register entry at fab (observable: die queries back; mapping privately held); trusted-source procurement (DFARS) | Fabs, OSATs, OCMs | ECID, DNA ink marking (spot-check), DFARS purchasing rules | S53, S54, S55, S56 | high |
| W04 | Distribution and transshipment | Refined outputs, components | Cross-border movement, intermediary trade, re-export, polishing/re-labelling steps | Goods in transit, re-issued certificates | Certificate of origin issued at each hand-off (observable: certificate present; no constraint by prior paperwork) | Traders, freight forwarders, intermediary hubs | Certificates of origin, ledger pilots (Tracr/Circulor where enrolled) | S24, S25, S29, S33, S42, S43, S44 | high |
| W05 | Import and customs | Imported goods | Declaration, origin assessment (substantial transformation / de minimis / FDP / ownership tests), duty and prohibition decisions | Entries, detentions, circumvention determinations | Importer evidence submission (UFLPA: clear-and-convincing + full chain tracing); authority-led investigation (EU FLR: burden on authority, adverse inference) | Importers, customs authorities, competent authorities | CBP dashboard, FLR Union Network | S16, S17, S18, S19, S20, S31, S75 | high |
| W06 | Compliance and due diligence | Supply-chain declarations | OECD five-step due diligence; supplier audits; risk registers; scheme membership | Due-diligence reports, audit certificates, scheme ratings | Independent third-party smelter/refiner audit (OECD step 4); annual reporting (OECD step 5) — observable documents, not physical binding | Compliance officers, auditors, scheme secretariats | OECD DDG, RMI/RMAP, IRMA, ITSCI | S21, S22, S27, S39, S47 | high |
| W07 | Enforcement and policy response | Detentions, fraud reports, expert findings | Anti-smuggling campaigns, prosecutions, entity listing, control/suspend cycles, stockpile and price-floor interventions | Indictments, seizures, Entity List additions, MOFCOM announcements, DoD deals | Named-case prosecution (observable: indictment/charge); official campaign publication (observable: "typical cases" release) | BIS, DOJ, CBP, MOFCOM/GAC, DoD, UN GoE, OLAF | Export-control rules, sanctions lists, stockpile purchases | S01, S02, S03, S13, S26, S32, S33, S66, S67, S75 | high |
