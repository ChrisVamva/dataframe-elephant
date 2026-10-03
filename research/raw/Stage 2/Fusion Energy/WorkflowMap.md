---
stage: 2
created: 2026-10-02
extracted_from:
  - research/Research ideas/Fusion Energy/README.md
  - research/Research ideas/Fusion Energy/00_Index/Index.md
  - research/Research ideas/Fusion Energy/06_Evidence/Sources.md
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

# WorkflowMap — Fusion Energy (Current State of Research, October 2026)

Extracted per `Rules and Regulations/Protocols/TransitionStage2.md` §4 Step 7. The Stage 1 workspace is itself a research survey, so the stages below are the seven research-workflow steps Stage 1 defines in `00_Index/Index.md` (Status table) and `README.md`. Stage names are used exactly as Stage 1 states them. Quality gates are the survey's own observable checks (source referencing, date stamping, company-claim flagging); Stage 1 assigns no named roles or tools, so those cells read `[not stated in source]` (see `ExtractionLog.md` L020).

| Stage ID | Stage name | Inputs | Activities | Outputs | Quality gates | Roles | Tools | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W1 | Assemble reading list and source register | Candidate primary, secondary, and company sources | Assemble the source register and assign a reliability class (P/T/C) to each source | `06_Evidence/Sources.md` (50 sources, accessed 2026-10-02) | Every factual claim in folders 01–05 references a register entry (`[S##]`); each source carries a reliability class | [not stated in source] | [not stated in source] | README.md; 06_Evidence/Sources.md | high |
| W2 | Background notes (fundamentals, metrics, fuel cycles) | Source register | Write the fundamentals note (physics, fuel cycles, Q definitions) | `01_Background/Fundamentals.md` | The two gain definitions (target vs wall-plug) are explicitly distinguished; open background questions are listed separately from established facts | [not stated in source] | [not stated in source] | 01_Background/Fundamentals.md | high |
| W3 | Per-approach notes (tokamak, stellarator, ICF, alternates) | Source register; Fundamentals.md | Write one note per confinement approach plus an overview | `02_Approaches/` (6 notes + overview) | Each note covers how it works, date-stamped best verified results, advantages/disadvantages, and representative devices; "Best result" entries are date-stamped because fusion records move | [not stated in source] | [not stated in source] | 02_Approaches/Approaches_Overview.md; approach notes | high |
| W4 | Program and company profiles | Source register; approach notes | Profile major public programs and private companies; tabulate scientific records | `03_State_of_the_Art/State_of_the_Art.md` | Records table is verified and date-stamped ("Records move — re-verify before relying on any entry"); company milestones marked as claims ([C] sources) are flagged as not independently verified | [not stated in source] | [not stated in source] | 03_State_of_the_Art/State_of_the_Art.md | high |
| W5 | Challenges synthesis | Source register; profiles | Synthesize the open problems (materials, tritium, exhaust, economics, regulation) | `04_Challenges/Challenges.md` | Obstacles are ranked by how hard they gate the first plants; every section cites register sources | [not stated in source] | [not stated in source] | 04_Challenges/Challenges.md | high |
| W6 | Outlook and follow-up agenda | Source register; profiles; challenges | Collect announced timelines, rate credibility, and record the follow-up agenda | `05_Outlook/Outlook.md` | Announced dates are collected with per-actor credibility notes before rating; the follow-up agenda is recorded as open checkboxes | [not stated in source] | [not stated in source] | 05_Outlook/Outlook.md | high |
| W7 | Final synthesis note answering RQ1–RQ5 | Folders 01–05; findings log | Write the synthesis answering the five research questions | `00_Index/Synthesis.md` | All five research questions (RQ1–RQ5) are answered; each answer cites the source register | [not stated in source] | [not stated in source] | 00_Index/Synthesis.md; 06_Evidence/Findings.md | high |
