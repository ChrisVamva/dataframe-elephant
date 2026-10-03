---
stage: 2
created: 2026-10-02
extracted_from:
  - research/Research ideas/Fusion Energy/README.md
  - research/Research ideas/Fusion Energy/00_Index/Index.md
  - research/Research ideas/Fusion Energy/00_Index/Synthesis.md
  - research/Research ideas/Fusion Energy/01_Background/Fundamentals.md
  - research/Research ideas/Fusion Energy/02_Approaches/Approaches_Overview.md
  - research/Research ideas/Fusion Energy/02_Approaches/Tokamak.md
  - research/Research ideas/Fusion Energy/02_Approaches/Stellarator.md
  - research/Research ideas/Fusion Energy/02_Approaches/ICF.md
  - research/Research ideas/Fusion Energy/02_Approaches/Magnetized_Target.md
  - research/Research ideas/Fusion Energy/02_Approaches/FRC.md
  - research/Research ideas/Fusion Energy/02_Approaches/Z-Pinch.md
  - research/Research ideas/Fusion Energy/03_State_of_the_Art/State_of_the_Art.md
  - research/Research ideas/Fusion Energy/04_Challenges/Challenges.md
  - research/Research ideas/Fusion Energy/05_Outlook/Outlook.md
  - research/Research ideas/Fusion Energy/06_Evidence/Findings.md
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

# ExtractionLog — Fusion Energy (Current State of Research, October 2026)

Record of every extraction decision made during Steps 2–7 of `Rules and Regulations/Protocols/TransitionStage2.md`. Per the protocol this is not a summary: each entry names the Stage 1 source, describes what was found, and states what was decided and why.

| Log ID | Step | Stage 1 source | Decision type | Description | Resolution |
| --- | --- | --- | --- | --- | --- |
| L001 | Orientation | All Stage 1 files | scope_boundary | The Stage 1 corpus is a finished survey workspace under `research/Research ideas/Fusion Energy/` (16 markdown files), not under `research/raw/Stage 1/`. | Treated as the read-only Stage 1 source for this extraction per the approved plan; no Stage 1 file was modified; every contributing file is named in each Stage 2 file's `extracted_from` frontmatter. |
| L002 | Step 5 / Step 6 | All Stage 1 files | label_resolution | Stage 1 tags claims only via source reliability classes P (primary), T (reputable secondary), C (company/self-published) in `06_Evidence/Sources.md`; it uses no claim-type tags. | Mapping rule (never promoting): P-sourced claims → documented fact/high; T-only-sourced claims → documented fact/medium; C-only-sourced claims → reported signal/medium; explicitly hedged company claims ("company claim", "[C]") → reported signal/low; Stage 1 synthesis and hedged judgments → inference/medium. |
| L003 | Step 2 | 06_Evidence/Sources.md | label_resolution | Stage 1 classification `C` (company/self-published claim) has no direct counterpart in the Primary/Secondary/Internal taxonomy. | Mapped C → Primary, since the company is the primary source of its own claim; the reliability caveat is carried into claim type and confidence in `Claims.md` and `Metrics.md` (L002), so no evidence class is lost or promoted. |
| L004 | Step 2 | 06_Evidence/Sources.md | label_resolution | Stage 1 sources carry identifiers S01–S50. | Identifiers preserved exactly per protocol Step 2 ("If an identifier was already assigned in Stage 1, preserve it exactly"); Stage 2 citation columns reference these same IDs. |
| L005 | Step 2 | 06_Evidence/Sources.md | label_resolution | Stage 1 factual statements in `Findings.md` and `Challenges.md` that carry no `[S##]` citation (e.g. IFMIF-DONES construction status, MagLIF neutron benchmark, several funding totals) cannot be traced to a registered source. | Added S51 (internal Stage 1 corpus, Wave 2 precedent) to `Sources.md`; such rows cite S51 and carry the lower confidence described in L011. |
| L006 | Step 3 | Tokamak.md; Stellarator.md; Magnetized_Target.md | entity_merge | Stage 1 uses multiple labels for the same referent: "W7-X" / "Wendelstein 7-X"; "General Fusion" / Nasdaq ticker "GFUZ"; "LM26" / "Lawson Machine 26". | Merged into single entities E022, E053, and E036 respectively, with the alternative labels kept in the canonical name; no ambiguous merges were made (no two distinct Stage 1 concepts shared a label). |
| L007 | Step 4 | Multiple Stage 1 files | label_resolution | Stage 1 states relationships in informal prose rather than typed predicates. | Chose the closest standard verb for each explicitly stated relationship (confines, drives, requires, pursues, demonstrated, targets, operates, stabilizes, compresses, breeds, regulates, funds, merged_with, invested_in, signed_offtake_with, tests) and kept the original Stage 1 wording verbatim in the Example column. Relationships merely implied by prose were not extracted. |
| L008 | Step 5 | Findings.md; State_of_the_Art.md; Challenges.md; Outlook.md | falsifier_absent | Stage 1 provides no falsifiers (its conventions cover sourcing and date stamping, not falsifiability) for 18 material claims: C003, C012, C016, C024, C026, C029, C031, C033, C034, C036, C037, C039, C040, C045, C046, C051, C059, C066. | Each of these rows carries the literal `[falsifier not stated]` marker in `Claims.md`; the remaining 48 claims carry falsifiers stated or directly derivable from Stage 1. The rows surface in the `missing_falsifiers` view of the Stage 2 database. |
| L009 | Step 3 | FRC.md | boundary_absent | Entity E067 (Neutral beam injection) is named in Stage 1 only as the method TAE used for FRC formation, with no statement of what it is not. | Recorded `[boundary not stated in source]` per protocol Step 3; all other entity rows have a boundary derived from explicit Stage 1 contrasts. |
| L010 | Step 6 | State_of_the_Art.md; Challenges.md | condition_absent | Stage 1 states no conditions for three metric values: the ST40 hot-ion temperature (M021, no shot date), CFS cumulative funding (M037, no as-of date), and the early-fusion LCOE span (M055, no plant vintage or geography). | Each row carries `[conditions not stated in source]` in Scope / conditions and is set to `low` confidence per Gate 4. |
| L011 | Step 6 | Z-Pinch.md; State_of_the_Art.md; Challenges.md | evidence_downgrade | Several Stage 1 quantitative values carry no direct citation (M022 MagLIF neutron benchmark, M045 Type One Pre-Series B, M047 Zap cumulative funding) even though Stage 1 states them as facts. | Recorded with S51 at `reported signal` / `low` confidence rather than as stated facts, because the survey's own convention is that unverified figures are not relied upon. |
| L012 | Follow-up | 05_Outlook/Outlook.md | open_question | "FIA 2026 report grid-timing percentages (2026 survey bins not yet in evidence)" is pending in Stage 1. | Carried forward unresolved; also recorded as a Stage 1 follow-up item. |
| L013 | Follow-up | 05_Outlook/Outlook.md | open_question | "Verify KSTAR 102 s claim against a KFE primary release" is pending in Stage 1; reflected as disputed claim C009. | Carried forward unresolved. |
| L014 | Follow-up | 05_Outlook/Outlook.md | open_question | TMTG–TAE merger close (expected Q4 2026) and its consequences for TAE's p–¹¹B program. | Carried forward unresolved; merger recorded as pending in C032. |
| L015 | Open questions | 03_State_of_the_Art/State_of_the_Art.md | open_question | "Which announced 'net electricity' demos are credible against public engineering estimates? (Helion 2028 and Xcimer 2031 are the most aggressive; neither has public net-gain data.)" | Carried forward unresolved; captured in claim C028 and company claims C038, C062. |
| L016 | Open questions | 03_State_of_the_Art/State_of_the_Art.md | open_question | "Does SPARC hit Q>1 in 2027, and does that change public-program schedules (ITER, STEP)?" | Carried forward unresolved; captured in claims C025 and C053. |
| L017 | Open question | 04_Challenges/Challenges.md | open_question | "Which is the true critical path — materials (IFMIF-DONES timescale), tritium self-sufficiency (blankets + Li-6 supply), or economics (LCOE vs firm-power value)?" Stage 1 evidence points to tritium + materials. | Carried forward unresolved as Stage 1 states it; not resolved by extraction. |
| L018 | Open background questions | 01_Background/Fundamentals.md | open_question | Two background questions carried in Stage 1: why the triple product (rather than Q alone) is the right cross-approach yardstick; how much of the tokamak database transfers to stellarators and alternates. | Carried forward unresolved; not converted into claim rows (protocol Step 5: no claim rows for open questions). |
| L019 | Steps 3–7 | 00_Index/Synthesis.md; README.md | omission | The Synthesis "one-paragraph answer" and the README's folder map and conventions text were not extracted into `Claims.md` or `Entities.md`. | Deliberate: the paragraph's content is already recorded as inference claims C053–C056, and the README conventions are captured as WorkflowMap quality gates W1–W7; navigation text has no data-model content. |
| L020 | Step 7 | 00_Index/Index.md; README.md | label_resolution | Stage 1 defines a 7-step research workflow (Index.md Status table) rather than an operational pipeline; quality gates, roles, and tools are not stated as such. | Recorded the seven steps as W1–W7 with Stage 1's observable conventions (source referencing, date stamping, [C] claim flagging) as the Quality gates column; Roles and Tools cells read `[not stated in source]` because Stage 1 assigns none. |
| L021 | Step 2 | 06_Evidence/Sources.md | label_resolution | Source S44 (Scientific American, May 2026) is named in Stage 1 without a URL. | Recorded the row with a blank URL cell per protocol Step 2; flagged here as the protocol's warning note. |
| L022 | Step 5 | 02_Approaches/ICF.md | entity_split | "First Light Fusion" appears in Stage 1 both as a projectile-ICF venture (abandoned 2025) and via its FLARE pivot; the two mentions are the same organization at different times, not two entities. | Kept as a single entity E056 with the pivot recorded in its boundary and in claim C039; no split required. |

## Gate results

Verified 2026-10-02 against the files in this directory before handoff to the Stage 2 import.

| Gate | Result | Evidence or defect |
| --- | --- | --- |
| Gate 1: Source coverage | pass | All 66 claim rows and 78 metric rows cite only Source IDs declared in `Sources.md` (S01–S51); a scripted comparison found no cited ID missing from the register. |
| Gate 2: Claim traceability | pass | Every claim row names a Stage 1 file and a section heading from that file; no claim was placed in an `[untraced]` section. |
| Gate 3: Evidence class integrity | pass | No claim or metric carries a higher class or confidence than Stage 1; C-class-sourced material was kept at `reported signal` and Stage 1 synthesis at `inference` (L002), and uncited Stage 1 figures were downgraded (L011). |
| Gate 4: Metric conditions | pass | Every metric row whose Scope cell contains the literal marker `[conditions not stated in source]` (M021, M037, M055) is `low` confidence. |
| Gate 5: Entity completeness | pass | No Boundary cell in `Entities.md` is blank; E067 carries `[boundary not stated in source]` and is logged at L009. |
| Gate 6: Extraction log completeness | pass | Entries L001–L022 cover the scope boundary, taxonomy and label mappings, entity merges, absent falsifiers/boundaries/conditions, evidence downgrades, every carried-forward open question, and the deliberate omissions. |
| Gate 7: Ingestibility | pass | All seven files parse with the strict Stage 2 parser (`src/stage2_import_core.py`, same row-splitting semantics as `src/ingest_citations.py`) with zero `unsupported_table_shape` and zero `source_ref_unresolved` warnings; the import preflight passed for all seven files. |
