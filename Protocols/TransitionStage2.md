# Stage 1 → Stage 2 Transition Protocol

## Status

This protocol is mandatory for every person, agent, or process that extracts structured content from `research/raw/Stage 1/` and organises it into `research/raw/Stage 2/`. No Stage 2 file may be created or modified without following this procedure.

---

## 1. Purpose

Stage 1 contains consolidated research briefs: large, multi-lens Markdown documents that mix prose, typed claims, evidence tables, source registers, confidence assessments, and open questions. They are the products of a research pass — not yet the structured inputs that modeling, analysis, and the citation database need.

Stage 2 is the **structured extraction layer**. Its purpose is to separate what is established, measurable, or formally typed from the surrounding argument and produce files that can be:

- ingested directly by `src/ingest_citations.py` without parser ambiguity;
- queried against `schemas/citations.sql` without reconstruction;
- read by a later agent or researcher without needing to re-read Stage 1.

Stage 2 does **not** re-argue, re-interpret, or synthesise further. It extracts, restates faithfully, and records every decision that was made during extraction.

---

## 2. Non-negotiable rules

1. **Never paraphrase a sourced claim.** Copy the exact wording from Stage 1 if the claim is attributed to a primary source. Paraphrase only when condensing prose that itself contains no direct citation, and mark such condensations with `[paraphrase]`.
2. **Never promote evidence class.** A `[S]` (reported signal) in Stage 1 is a `[S]` in Stage 2. A `[I]` (inference) remains an inference. Do not re-label a claim as a documented fact because it appears in a well-structured table.
3. **Never merge ambiguous entities.** If Stage 1 names two things with the same label but different boundaries (e.g. two products called "Agent Framework"), keep them as separate rows with distinct identifiers and a disambiguation note.
4. **Never discard uncertainty.** Every limitation, conflict, low-confidence finding, and open question from Stage 1 must be carried forward. Stage 2 is more structured than Stage 1, not more confident.
5. **Preserve provenance at every level.** Each extracted record must trace to the exact Stage 1 source file, section heading, and — where possible — table row or line number.
6. **Record the extraction decision.** Any judgement call made during extraction (scope boundary, entity merging choice, label resolution) must be documented in the Stage 2 file's extraction log.

---

## 3. Inputs and outputs

### 3.1 Inputs — Stage 1 files

| File | Primary content relevant to Stage 2 |
| --- | --- |
| `CNE DPS 4.1 F.md` | Canonical entity register, predicate register, claim table, DuckDB handoff spec |
| `CP L6.md` | Source table, workflow stage map, ELT workflow |
| `C.md` | Consolidated multi-lens research brief (skills, market positions, technology, methodology, agents) |
| `DC L5.6.md` | Data-centric workflow, tool comparisons, skill/role boundaries |
| `DPS.md` | Data pipeline and storage lens |
| `FAI.md` | Full atlas index; entity relationships and cross-lens dependencies |
| `ANT GP H.md` | Agent, orchestration, and governance lens |
| `OP MS 1.3F.md` | Operational and market-signal lens |
| `Q.md` | Quality, provenance, and testing lens |
| `G0.md` – `G3.md` | Granular sub-topics (individual lenses or sub-lens passes) |
| `Citations/Citation.md` | Citation inventory and broad classifications |
| `Citations/Report.md` | Source-quality summaries and classification limitations |

All files are read-only inputs. **Stage 1 files must not be modified by the transition process.**

### 3.2 Outputs — Stage 2 files

Each Stage 2 file is a standalone Markdown document. The full set of Stage 2 files together must contain everything needed to run `build_database` and to answer the three original intelligence questions: which sources recur, which have stronger evidence, and where to investigate next.

Mandatory Stage 2 files:

| File | Contents |
| --- | --- |
| `Entities.md` | Canonical entity register: one row per entity, with stable identifier, type, boundaries, and Stage 1 provenance |
| `Predicates.md` | Predicate/relationship register: one row per predicate, with subject type, object type, directionality, and example |
| `Claims.md` | Claim table: one row per atomic claim, with type, confidence, source(s), falsifier, and Stage 1 provenance |
| `Sources.md` | Source table ingestible by `ingest_citations.py`: ID, title, URL, publisher, classification, date |
| `Metrics.md` | Extracted quantitative values and measurable signals: metric name, value, unit, scope, confidence, source |
| `WorkflowMap.md` | Workflow stage definitions, inputs, outputs, quality gates, and role/tool assignments |
| `ExtractionLog.md` | Record of every extraction decision, conflict resolution, and ambiguity noted during this transition |

Additional files are permitted for lens-specific content (e.g. `Skills.md`, `MarketPositions.md`, `Technology.md`) if the volume or structure of the content warrants separation. Each additional file must follow the same conventions and reference `ExtractionLog.md` for any non-obvious extraction decisions.

---

## 4. Extraction process — step by step

### Step 1: Orient before extracting

Before extracting from any Stage 1 file:

1. Read the file's frontmatter and executive synthesis in full.
2. Record the file's stated research question, scope, and intended use in `ExtractionLog.md`.
3. Note the evidence class tags used in the file (`[F]`, `[S]`, `[I]`, `[R]`) and confirm they map to the project's standard taxonomy (`documented fact`, `reported signal`, `inference`, `recommendation`).
4. List every section heading. Identify which sections contain: entity definitions, metrics, claim tables, source tables, and open questions.

Do not begin extraction until this orientation is recorded.

### Step 2: Extract the source register

From every source table found in Stage 1 files, copy each row into `Sources.md` in the format required by `ingest_citations.py`:

```markdown
| ID | Source | URL | Publisher | Classification | Publication date |
| --- | --- | --- | --- | --- | --- |
```

Rules:

- Use the exact source title as it appears in Stage 1.
- Use `Primary`, `Secondary`, or `Internal` in the Classification column. If Stage 1 uses a non-standard term, note the mapping in `ExtractionLog.md`.
- If a Stage 1 file lists a source without a URL, record the row with the URL cell blank and add a warning note in `ExtractionLog.md`.
- If the same source appears in multiple Stage 1 files with different classifications, record it once in `Sources.md` with the classification left blank and add a `classification_conflict` entry in `ExtractionLog.md` naming both files.
- Assign a stable local identifier (`S1`, `S2`, …) in document order. If an identifier was already assigned in Stage 1, preserve it exactly.

### Step 3: Extract the entity register

From the entity definitions, entity tables, and canonical-name registers in Stage 1, build `Entities.md`:

```markdown
| Entity ID | Canonical name | Type | Boundary (what it is not) | Stage 1 source | Section | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
```

Rules:

- An **entity** is any named concept that will become a node in the data model: a skill, role, workflow stage, tool, methodology, artefact type, quality dimension, or agent type.
- The **boundary** column must state what the entity is *not* — this is required, not optional. If Stage 1 does not state a boundary, record `[boundary not stated in source]` and flag in `ExtractionLog.md`.
- If two Stage 1 files use the same label for different concepts, assign distinct Entity IDs (`E12a`, `E12b`) and add a disambiguation note.
- Do not create an entity for concepts mentioned only in passing with no definition.

### Step 4: Extract the predicate register

From the relationship statements, cross-lens dependency notes, and `Relationships to other lenses` sections in Stage 1, build `Predicates.md`:

```markdown
| Predicate | Subject type | Object type | Direction | Example (from Stage 1) | Stage 1 source |
| --- | --- | --- | --- | --- | --- |
```

Rules:

- A **predicate** is a typed, directional relationship between two entity types: `uses`, `performed_by`, `governs`, `produces`, `requires`, `implemented_by`, `appears_in`, `supports`, `conflicts_with`.
- Use the exact predicate label as it appears in Stage 1 where possible. Where Stage 1 uses informal phrasing, choose the closest standard verb and record the original phrasing in `ExtractionLog.md`.
- Do not infer predicates from prose. A predicate is extracted only when Stage 1 explicitly states a relationship.

### Step 5: Extract atomic claims

From every claim table, findings narrative, and executive synthesis in Stage 1, extract each atomic claim into `Claims.md`:

```markdown
| Claim ID | Claim text | Claim type | Confidence | Source IDs | Falsifier | Workflow stage | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Rules:

- An **atomic claim** makes exactly one assertion. A sentence containing `and` that makes two independent assertions must be split.
- Use the Stage 1 claim type tags directly: `documented fact`, `reported signal`, `inference`, `recommendation`.
- Confidence levels are `high`, `medium`, or `low`. When Stage 1 uses compound values such as `Medium-High`, record the lower level and note the original value in `ExtractionLog.md`.
- The Falsifier column must be populated when Stage 1 provides one. If Stage 1 does not provide a falsifier for a material claim, record `[falsifier not stated]`.
- Do not create a claim row for open questions, caveats, or methodological notes. Open questions go into `ExtractionLog.md`.
- Claim IDs are assigned sequentially per document (`C001`, `C002`, …). Cross-file duplicates — the same claim extracted from two Stage 1 files — are merged into one row; both Stage 1 sources are listed, separated by `;`.

### Step 6: Extract metrics and quantitative values

From benchmark figures, measurable signals, and quantitative findings in Stage 1, build `Metrics.md`:

```markdown
| Metric ID | Metric name | Value | Unit | Scope / conditions | Claim type | Confidence | Source ID | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Rules:

- A **metric** is any numerical value, ratio, count, proportion, or measurable threshold asserted in Stage 1 (e.g. benchmark duration, error rate, document count, version number, year of release).
- The **Scope / conditions** column must record the exact conditions under which the value applies: hardware, dataset size, version, geography, time period. If Stage 1 does not state these conditions, record `[conditions not stated in source]` — never strip the conditions silently.
- Vendor-reported benchmarks that are not corroborated by an independent source are always `reported signal` at `low` or `medium` confidence, regardless of how they are presented in Stage 1.
- Version numbers and release dates from official documentation are `documented fact` at `high` confidence.
- Do not average, aggregate, or transform values from Stage 1. Record them as stated.

### Step 7: Extract the workflow map

From workflow tables, pipeline diagrams, and stage-by-stage descriptions in Stage 1, build `WorkflowMap.md`:

```markdown
| Stage ID | Stage name | Inputs | Activities | Outputs | Quality gates | Roles | Tools | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Rules:

- Use the stage names exactly as they appear in Stage 1. If different Stage 1 files use different names for the same stage, record all names and add a note in `ExtractionLog.md`.
- Every cell in the Quality gates column must describe an observable check, not a goal. `"Metric-owner sign-off"` is a gate; `"high quality"` is not.
- The Roles and Tools columns list named roles and tools. Do not infer either from prose — extract only when Stage 1 explicitly assigns them to the stage.

### Step 8: Complete the extraction log

`ExtractionLog.md` is not a summary. It is a record of every decision made during Steps 2–7. For each entry, record:

```markdown
| Log ID | Step | Stage 1 source | Decision type | Description | Resolution |
| --- | --- | --- | --- | --- | --- |
```

Decision types:

| Type | When to use |
| --- | --- |
| `scope_boundary` | A concept was in scope for extraction in one Stage 1 file but out of scope in another |
| `entity_merge` | Two distinct Stage 1 names were judged to refer to the same entity |
| `entity_split` | One Stage 1 name was judged to refer to two distinct entities |
| `label_resolution` | An informal Stage 1 label was mapped to a canonical term |
| `classification_conflict` | The same source appeared with different classifications across Stage 1 files |
| `evidence_downgrade` | A claim's confidence was lowered relative to Stage 1 for a stated reason |
| `falsifier_absent` | A material claim had no falsifier in Stage 1 |
| `boundary_absent` | An entity definition had no stated boundary in Stage 1 |
| `condition_absent` | A metric had no stated conditions in Stage 1 |
| `open_question` | A Stage 1 open question carried forward without resolution |
| `omission` | Content present in Stage 1 was deliberately excluded from Stage 2, with reason |

Every log entry must name the Stage 1 file and section, describe what was found, and state what was decided and why.

---

## 5. Quality gates before a Stage 2 file is complete

A Stage 2 file is not complete until all of the following checks pass. Record the gate result in `ExtractionLog.md`.

### Gate 1: Source coverage

Every source referenced in any Stage 2 claim, metric, or entity row is present in `Sources.md` with a matching Source ID. No claim cites a source not in the register.

### Gate 2: Claim traceability

Every claim in `Claims.md` traces to a specific Stage 1 file, section, and — where feasible — table row. Claims that cannot be traced to a Stage 1 passage are removed or placed in a `[untraced]` section for manual review.

### Gate 3: Evidence class integrity

No claim has a higher evidence class in Stage 2 than in Stage 1. If a Stage 1 `[I]` inference has been recorded as a `documented fact` in Stage 2, it is a defect requiring correction.

### Gate 4: Metric conditions

Every metric row with `[conditions not stated in source]` in the Scope column is flagged as `low` confidence regardless of the Stage 1 rating.

### Gate 5: Entity completeness

Every entity in `Entities.md` has a non-empty Boundary column (which may say `[boundary not stated in source]` if the source did not provide one, but must not be left blank).

### Gate 6: Extraction log completeness

Every non-obvious extraction decision made during Steps 2–7 has a corresponding entry in `ExtractionLog.md`. A decision is non-obvious if it required choosing between two valid interpretations.

### Gate 7: Ingestibility

`Sources.md` must be parseable by `src/ingest_citations.py` without producing `unsupported_table_shape` warnings. Run the ingestion pipeline against the Stage 2 directory and confirm the warning count for `Sources.md` is zero or that every warning is explained in `ExtractionLog.md`.

```powershell
.venv\Scripts\python src/ingest_citations.py `
  --raw-dir "research/raw/Stage 2" `
  --database data/citations.duckdb `
  --warnings data/citation_ingestion_warnings.jsonl `
  --schema schemas/citations.sql
```

---

## 6. What Stage 2 must not contain

| Prohibited | Reason |
| --- | --- |
| New claims not present in Stage 1 | Stage 2 extracts; it does not produce new research |
| Merged entities with unresolved naming conflicts | Silent merges destroy traceability |
| Confidence values higher than Stage 1 | Promotion without new evidence is fabrication |
| Vendor benchmark values without stated conditions | Decontextualised numbers are misleading |
| Open questions resolved without evidence | Resolution requires new research, not editorial judgement |
| Modified Stage 1 source files | Stage 1 is immutable during this process |

---

## 7. File naming and structure conventions

- Stage 2 files use `Title Case` names with no spaces: `Claims.md`, `Entities.md`, `Sources.md`, `Metrics.md`, `WorkflowMap.md`, `Predicates.md`, `ExtractionLog.md`.
- Every Stage 2 file begins with a YAML frontmatter block:

```yaml
---
stage: 2
created: YYYY-MM-DD
extracted_from:
  - research/raw/Stage 1/<file>.md
  - research/raw/Stage 1/<file>.md
extractor: <agent or person identifier>
gate_results:
  gate_1_source_coverage: pass | fail
  gate_2_claim_traceability: pass | fail
  gate_3_evidence_class_integrity: pass | fail
  gate_4_metric_conditions: pass | fail
  gate_5_entity_completeness: pass | fail
  gate_6_extraction_log_completeness: pass | fail
  gate_7_ingestibility: pass | fail
---
```

- The frontmatter `extracted_from` list must name every Stage 1 file that contributed content to this Stage 2 file, even if only one row came from it.
- A Stage 2 file whose frontmatter shows any gate as `fail` is not ready for use by downstream processes. It may be committed to the repository as work in progress but must carry a `status: draft` frontmatter field.

---

## 8. Update triggers

Re-run this transition protocol — or update affected Stage 2 files — when any of the following occurs:

- A Stage 1 file is revised to correct a factual error or add new evidence.
- A new Stage 1 file is added to `research/raw/Stage 1/`.
- The entity register, predicate register, or schema changes in a way that requires re-classification of existing rows.
- An open question in `ExtractionLog.md` is resolved by new research.
- The citation ingestion pipeline (`src/ingest_citations.py`) introduces a new warning type that affects Stage 2 source table structure.

When updating, preserve the previous gate results and extraction log entries. Do not silently overwrite history. Append new entries with a revised date.

---

## 9. Final principle

Stage 2 is judged not by how clean or complete it looks, but by whether a researcher who has never read Stage 1 can use Stage 2 alone to:

1. Identify every established fact and its direct primary source.
2. Distinguish that fact from a signal, inference, or recommendation.
3. Trace every metric to the conditions under which it was measured.
4. See exactly what remains uncertain and what would resolve that uncertainty.

If any of those four tests fail, the transition is incomplete.
