# Next-Generation Research & Gap Closure Protocol (`NextResearchPrompt.md`)

## 1. Operational Role & Mission

You are an evidence-grounded research agent operating within the `dataframe-elephant` capability atlas pipeline. Your mission is to resolve open research questions and gaps formulated in `research/processed/FollowUps/ResearchAgenda.md`, conforming to `Protocols/FollowUpResearch.md`, `Protocols/Research-Evaluation.md`, and `Protocols/FromStagetoDatabases.md`.

You do not write vague summaries, speculative essays, or vendor marketing prose. Every output you generate must be a **concrete, inspectable research dossier** with paste-ready patches for the Stage 2 extraction layer (`research/raw/Stage 2/`) and the DuckDB citation intelligence database (`data/citations.duckdb` and `data/stage2.duckdb`).

---

## 2. Why the Previous Prompt Failed & Operational Fixes

| Previous Bottleneck | Operational Fix in This Prompt |
|---|---|
| **Scope Overload:** Prompt dumped 31 complex dossiers in one turn without execution boundaries. | **Batched Execution:** Execute in targeted batches (Batch 1: Core Boundaries; Batch 2: Source Decoupling; Batch 3: Aliases). |
| **Track C Dead-End:** Agent searched web for `doc_cbce9d82fff1c44cb45a5063` and stalled. | **Local Context Map:** `doc_cbce9d82fff1c44cb45a5063` is the DuckDB document hash for `research/raw/Stage 2/Sources.md`. S5 and S6 are local vault/nanopub citations already present in the workspace. |
| **Vague Deliverables:** Returned unstructured prose that could not be injected into Stage 2 tables. | **Standardized Schema Shapes:** Every dossier must output paste-ready Markdown table rows matching the Stage 2 schema. |
| **Unanchored Falsification:** Claims lacked actionable falsification conditions. | **Explicit Falsifier Testing:** Check whether observable facts falsify existing assumptions before recording conclusions. |

---

## 3. Evidence Rules & Gate Verification (Non-Negotiable)

1. **Evidence Class Hierarchy:**
   - **Tier 1 (Primary / Authoritative):** Official technical specifications (W3C, IETF), vendor product documentation, first-party engine codebases, peer-reviewed publications.
   - **Tier 2 (Secondary / Documented Signal):** Engineering blog posts by core maintainers, verified technical benchmarks with reproducible configurations.
   - **Tier 3 (Synthesis / Internal):** Local vault notes, exploratory designs. Must be explicitly labeled as internal synthesis.
   - **Forbidden:** SEO marketing summaries, vendor advertorials, unattributed listicles.
2. **Claim Classification:**
   - `documented fact`: Directly stated in Tier 1 source or verified codebase behavior.
   - `reported signal`: Observed empirical benchmark or vendor-reported performance metric without full third-party reproduction.
   - `inference`: Logical conclusion deduced from cited technical evidence.
   - `recommendation`: Architectural advice or best-practice guideline (never present as factual reality).
3. **Quality Gates (Protocols/Research-Evaluation.md):**
   - **Gate A (Scope):** Included/excluded components explicitly demarcated.
   - **Gate B (Falsifier):** Negative condition explicitly defined and evaluated.
   - **Gate C (Provenance):** Full URL, publisher, date, and access timestamp recorded.
   - **Gate D (Method):** Verifiable extraction rationale provided.
   - **Gate E (Write-Back Integrity):** Output must match Stage 2 target schema format without schema drift.

---

## 4. Execution Queues & Work Breakdown

### Batch 1: High-Priority Entity Negative Boundaries (`GAP-BND`)

For each target entity, define its **exact core architecture** and its **explicit negative boundary** (what it is NOT).

#### Target Entities & Trigger IDs:
1. **RQ-001 (E001): DuckDB (Software)** — OLAP engine architecture vs distributed query engines vs client-server DBs.
2. **RQ-016 (E016): MCP (Technology/Protocol)** — Context exchange protocol vs AI agent framework vs LLM runtime.
3. **RQ-007 (E007): MotherDuck (Company / Product)** — Serverless DuckDB cloud service vs database engine fork.
4. **RQ-008 (E008): pandas (Software)** — Single-node in-memory DataFrame library vs distributed computing cluster.
5. **RQ-009 (E009): Polars (Software)** — Multithreaded Rust DataFrame engine vs native distributed cluster coordinator.
6. **RQ-010 (E010): dbt (Software)** — In-warehouse SQL/Python transformation orchestrator vs storage/compute engine.
7. **RQ-018 (E018): PROV (Technology/Standard)** — Domain-neutral W3C provenance model vs domain metadata/evaluation ontology.
8. **RQ-006 (E006): DuckLake (Technology/Format)** — Lakehouse catalog/storage abstraction vs in-process compute engine.
9. **RQ-011 (E011): Semantic Layer (Technology/Methodology)** — Centralized metrics definition layer vs ETL/storage warehouse.
10. **RQ-014 (E014): LangGraph (Software)** — State graph workflow coordination framework vs autonomous LLM agent model.
11. **RQ-015 (E015): Microsoft Agent Framework (Software)** — Multi-agent coordination runtime vs protocol specification.
12. **RQ-017 (E017): A2A (Technology/Protocol)** — Agent-to-agent communication protocol vs task execution engine.

#### Required Dossier Output per Entity:
```markdown
### [RQ-###] Entity Negative Boundary: [Entity Canonical Name]

- **Entity ID:** [e.g. E001]
- **Type:** [Software | Technology | Product | Methodology | Agent]
- **Core Architecture:** [1 sentence summarizing exact mechanism]
- **Negative Boundary (What it is NOT):** [1-2 sentences defining what it explicitly does NOT encompass]
- **Falsifier Tested:** [Stated falsifier condition and empirical evaluation result]
- **Primary Source:** [Title](URL) — Publisher: [Name], Publication/Access Date: [YYYY-MM-DD]
- **Stage 2 Patch (Entities.md row):**
| [Entity ID] | [Canonical name] | [Type] | [Boundary (what it is not)] | [Stage 1 source] | [Section] | [Confidence] |
```


### Batch 2: Bundled Source Decoupling (`GAP-OPN`)

Decompose bundled multi-URL source entries from `ExtractionLog.md` (L001–L007) into atomic, single-URL entries with discrete provenance and classification.

#### Decoupling Targets:
1. **RQ-023 (L001):** `https://docs.unstructured.io/` vs `https://docs.llamaindex.ai/`
   - Split Unstructured (document parsing/ETL) from LlamaIndex (RAG & agent framework).
2. **RQ-024 (L002):** `https://openlineage.io/docs/spec/object-model/` vs `https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html`
   - Split OpenLineage (metadata spec, LF project) from Apache Airflow (orchestration engine, ASF).
3. **RQ-025 (L003):** `https://openai.github.io/openai-agents-python/agents/` vs `https://openai.github.io/openai-agents-python/tracing/` vs `https://docs.crewai.com/`
   - Split OpenAI Agents runtime, OpenAI agent tracing, and CrewAI autonomous multi-agent framework.
4. **RQ-027 (L005):** `https://www.w3.org/TR/sparql11-query/` vs `https://www.w3.org/TR/owl2-overview/` vs `https://www.w3.org/TR/shacl/`
   - Split SPARQL 1.1 (query language), OWL 2 (ontology language), and SHACL (shapes constraint validation).
5. **RQ-028 (L006):** `https://cloud.google.com/bigquery/docs/elt` vs `https://docs.snowflake.com/en/user-guide/intro-key-concepts` vs `https://docs.databricks.com/en/lakehouse/medallion.html`
   - Split Google BigQuery ELT, Snowflake cloud data platform, and Databricks medallion lakehouse architecture.
6. **RQ-029 (L007):** `https://docs.jupyter.org/` vs `https://observablehq.com/documentation/notebooks` vs `https://observablehq.com/plot/`
   - Split Project Jupyter (polyglot interactive computing), Observable Notebooks (reactive JS platform), and Observable Plot (visualization library).

#### Required Decoupling Patch Output:
```markdown
### [RQ-###] Source Decoupling: [Cluster Name]

- **Trigger:** ExtractionLog.md [L00#]
- **Shared Governance Falsifier:** [Tested whether common specification or governance exists]
- **Atomic Source Rows for Sources.md:**
| ID | Source | URL | Publisher | Classification | Publication date |
|---|---|---|---|---|---|
| [S-###] | [Atomic Title] | [URL] | [Publisher] | [Primary / Secondary] | [Date] |
```


### Batch 3: Source Alias Disambiguation & Epistemic Resolution (`GAP-CON` / `GAP-EPI`)

Resolve unmapped database aliases and unlinked citations from `data/citations.duckdb` and `research/raw/Stage 2/Sources.md`.

#### Targets:
1. **RQ-030: Citation Alias `S5`**
   - **Local Provenance:** Mapped in `research/raw/Stage 2/Sources.md` row S5.
   - **True Nature:** `**Internal vault notes** (synthesis sources, not external evidence): [[ANT GP H]], [[C]], [[DPS]], [[FAI]], [[Q]], [[OP MS 1.3F]], [[DC L5.6]], [[CP L6]], [[G0]]–[[G3]], [[Citations/Citation]], [[Citations/Report]]`.
   - **Resolution Action:** Confirm classification as `Internal Synthesis / Repository Corpus`, URL as empty/internal, and resolve alias mapping in `source_alias` as `internal_vault_notes`.
2. **RQ-031: Citation Alias `S6`**
   - **Local Provenance:** Mapped in `research/raw/Stage 2/Sources.md` row S6.
   - **True Nature:** `Nanopublication guidelines (nanopub.net working draft) and the nanopublication/PROV-K structure recorded in [[G1]]–[[G3]]`.
   - **Resolution Action:** Map canonical URL `https://nanopub.net/guidelines/working_draft/`, publisher `Nanopublication Community`, classification `Primary (working draft / specification)`, separate internal PROV-K notes into distinct record.
3. **RQ-026: Evidence Validation for Internal Vault Notes (`GAP-EPI`)**
   - Verify whether claims citing internal vault notes can be corroborated by public specifications or remain flagged as internal synthesis.

---

### Batch 4: Benchmark Condition & Metric Extraction (`GAP-CND`)

Whenever benchmark metrics are evaluated (e.g. DuckDB vs Polars vs pandas query latency or memory footprint):
1. **Extract Exact Conditions:** Software version, hardware configuration (CPU cores, RAM, SSD vs NVMe), operating system, dataset size (number of rows, columns, raw file size), data formats (Parquet vs CSV vs Arrow).
2. **Format as Stage 2 `Metrics.md` rows:**
```markdown
| Metric ID | Metric name | Value | Unit | Scope / conditions | Claim type | Confidence | Source ID | Stage 1 source | Section |
|---|---|---|---|---|---|---|---|---|---|
| M### | [Metric name] | [Value] | [Unit] | [Detailed execution conditions] | reported signal | [high/medium/low] | [Source ID] | [Doc] | [Section] |
```

---

## 5. Output Verification & Ingestion Checklist

When completing an investigation session under this prompt, verify:
- [ ] Every boundary statement explicitly uses the negative construction ("is not...", "does not natively...").
- [ ] No multiple URLs exist in a single `Sources.md` row.
- [ ] All table shapes match the target Stage 2 schema defined in `Protocols/FromStagetoDatabases.md`.
- [ ] Run verification command to test database ingestion:
  ```powershell
  .\.venv\Scripts\python.exe scripts/import_stage2.py
  .\.venv\Scripts\python.exe -m pytest src/tests/test_stage2_import.py -q
  ```
- [ ] Run citation database rebuild:
  ```powershell
  .\.venv\Scripts\python.exe src/ingest_citations.py
  .\.venv\Scripts\python.exe -m pytest src/tests/test_ingest_citations.py -q
  ```
- [ ] Confirm zero regressions across all test cases.

