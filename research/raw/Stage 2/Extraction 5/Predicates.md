---
stage: 2
created: 2026-10-07
extracted_from:
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/01_Background/Concepts.md
  - research/raw/Stage 1/Wave 5/Critical Minerals and Semiconductor Supply Chains/01_Background/Regimes.md
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

# Predicates — Wave 5 (Critical Minerals and Semiconductor Supply Chains)

| Predicate | Subject type | Object type | Direction | Example (from Stage 1) | Stage 1 source |
| --- | --- | --- | --- | --- | --- |
| governs | instrument | organization / company | subject → object | UFLPA governs US importers of goods with XUAR inputs | 01_Background/Regimes.md §3 |
| determines_origin_of | concept (jurisdiction test) | product / material | subject → object | Substantial transformation determines origin of third-country-processed diamonds | 01_Background/Concepts.md §3 |
| attests | scheme / party | facility / shipment | subject → object | ITSCI attests tagged 3T bags at scheme-covered points | 02_Origin_Evidence/OriginEvidence.md §4 |
| audits | scheme | facility | subject → object | IRMA audits mine sites on a 100-point scale at audit time | 02_Origin_Evidence/OriginEvidence.md §3 |
| controls | instrument | mineral / technology | subject → object | MOFCOM Announcement No. 61/62 controls 12 rare-earth elements and REE technologies/equipment | 01_Background/Regimes.md §1.3 |
| refines | facility | mineral | subject → object | Chinese refineries refine ~99% of primary low-purity gallium | 04_Tracing_Technologies/Concentration.md §3 |
| blends | facility | material | subject → object | Refinery pools blend doré from many sources, destroying input identity | 03_Laundering_Cases/Cases.md §7 (L1) |
| transships | party | good | subject → object | Intermediaries transship restricted GPUs via Malaysia/Vietnam to Hong Kong/China | 03_Laundering_Cases/Cases.md §5 |
| re_papers_origin_of | party | shipment | subject → object | EAEU intermediaries re-paper origin of Russian gold re-exports | 03_Laundering_Cases/Cases.md §1 |
| traces | technology | material / product | subject → object | BGR AFP traces 3TG concentrates to deposit consistency | 04_Tracing_Technologies/Technologies.md §1 |
| verifies | system | identifier / record | subject → object | National medicines verification systems verify pack unique identifiers at dispensing | 04_Tracing_Technologies/Technologies.md §3 |
| imposes_burden_on | instrument | party | subject → object | UFLPA imposes a raw-material-level tracing burden on importers | 01_Background/Regimes.md §3 |
| backs_financially | organization | company | subject → object | DoD backs MP Materials via $400M preferred stock and a $110/kg NdPr price floor | 04_Tracing_Technologies/Concentration.md §3 |
| produces | facility / company | product | subject → object | TSMC produces ~71% of pure-play foundry output (Q2 2025) | 04_Tracing_Technologies/Concentration.md §1 |
