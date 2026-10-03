---
stage: 2
created: 2026-10-02
extracted_from:
  - research/Research ideas/Fusion Energy/00_Index/Synthesis.md
  - research/Research ideas/Fusion Energy/01_Background/Fundamentals.md
  - research/Research ideas/Fusion Energy/02_Approaches/Tokamak.md
  - research/Research ideas/Fusion Energy/02_Approaches/Stellarator.md
  - research/Research ideas/Fusion Energy/02_Approaches/FRC.md
  - research/Research ideas/Fusion Energy/02_Approaches/Z-Pinch.md
  - research/Research ideas/Fusion Energy/04_Challenges/Challenges.md
  - research/Research ideas/Fusion Energy/05_Outlook/Outlook.md
  - research/Research ideas/Fusion Energy/06_Evidence/Findings.md
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

# Predicates — Fusion Energy (Current State of Research, October 2026)

Extracted per `Rules and Regulations/Protocols/TransitionStage2.md` §4 Step 4. Only relationships stated explicitly in Stage 1 are recorded; prose that merely implies a relationship is excluded. Stage 1 uses informal phrasing, so the closest standard verb is chosen and the original wording kept verbatim in the `Example (from Stage 1)` column (see `ExtractionLog.md` L007). `Direction` states the asserted direction of the relation.

| Predicate | Subject type | Object type | Direction | Example (from Stage 1) | Stage 1 source |
| --- | --- | --- | --- | --- | --- |
| confines | Confinement approach | Plasma | subject -> object | "A toroidal (doughnut-shaped) vessel uses strong magnetic coils to confine a >100-million-°C plasma." | Tokamak.md |
| drives | Device component | Plasma current | subject -> object | "A central solenoid drives a large plasma current that creates the poloidal field." | Tokamak.md |
| requires | Fuel cycle | Breeding capability | subject -> object | "tritium does not occur in nature — must be bred from lithium in the plant (see Challenges)". | Fundamentals.md |
| pursues | Company | Fuel cycle | subject -> object | "TAE pursues p–¹¹B; Helion D–³He — but far harder conditions; both companies currently operate on D–T or precursor fuels". | Fundamentals.md |
| demonstrated | Device | Milestone | subject -> object | "Only NIF has demonstrated it" (ignition). | Fundamentals.md |
| targets | Device | Milestone | subject -> object | "SPARC targets Q>1 as a milestone; ARC and ITER target Q≈10+". | Fundamentals.md |
| operates | Organization | Device | subject -> object | "W7-X (IPP Greifswald, the flagship)". | Stellarator.md |
| stabilizes | Mechanism | Instability | subject -> object | "Zap Energy's sheared-flow variant stabilizes them with axial flow velocity shear." | Z-Pinch.md |
| compresses | Mechanism | Plasma | subject -> object | "in Helion's scheme two FRCs collide and are compressed by pulsed magnets to induce a fusion pulse with direct electricity recovery via induction." | FRC.md |
| breeds | Component | Fuel | subject -> object | "must be bred from lithium in the plant"; "No integrated breeding blanket has ever operated in a fusion neutron environment." | Challenges.md |
| regulates | Regulator | Technology | subject -> object | "NRC chose the byproduct-materials framework (10 CFR Part 30), not the reactor framework (Part 50) — May 2023". | Challenges.md |
| funds | Funder | Program | subject -> object | "milestone-based program awarded $46M to 8 companies (2023)". | Findings.md |
| merged_with | Company | Company | subject <-> object | "announced >$6B all-stock merger with Trump Media (DJT), pending as of Oct 2026". | FRC.md |
| invested_in | Investor | Company | subject -> object | "CFS raised $863M Series B2 (Aug 2025, investors incl. Nvidia and Google)". | Findings.md |
| signed_offtake_with | Offtaker | Company | subject -> object | "Google 200 MW + Eni >$1B offtakes signed — real demand signal." | Outlook.md |
| tests | Facility | Component | subject -> object | "ITER will test blanket mockups, not a self-sufficient cycle." | Challenges.md |
