---
status: proposed
scope: research corpus, Stage 1/2 extractions, citation intelligence, follow-up agendas
created: 2026-09-29
approval: pending maintainer review
---

# Research Plan: Corpus-Driven Research Directions

## Document Control

- **Status:** proposed — synthesized from existing follow-up agendas and citation intelligence
- **Covered folder:** `research/` (raw Stage 1/2 + processed FollowUps)
- **Snapshot date:** 2026-09-29
- **Prepared by:** Desktop Commander, based on workspace corpus
- **Intended use:** guide next-wave research; not authoritative until maintainer acceptance
- **Governing protocol:** `Rules and Regulations/Protocols/FollowUpResearch.md`

---

## 1. Executive Recommendation

The corpus (Wave 2 Smart Homes research, two Stage 2 extractions, 31 follow-up research questions, and citation intelligence) clusters into five actionable research directions:

1. **Data-Platform Boundary** — DuckDB, MotherDuck, DuckLake, Semantic Layer, pandas, Polars, dbt
2. **Agent & Protocol Architecture** — MCP, A2A, LangGraph, Microsoft Agent Framework, Research/scout agent
3. **Source Integrity** — Bundled source disambiguation (6 unresolved URLs), alias disambiguation (S5/S6), missing primary evidence for internal vault notes
4. **Smart-Home Domain Coverage** — Matter interoperability, AI/voice control, energy flexibility, security lifecycle, emerging categories
5. **Benchmark & Evaluation Gap** — No benchmark conditions formulated yet; evidence validation pending

---

## 2. Source-of-Truth Inventory

### 2.1 Research corpus structure

```text
research/
  raw/
    Stage 1/
      Citations/           Citation.md, Report.md
      Wave 2/
        SmartHomes_Key_Tech_Trends/   7 domain folders (Matter, AI/Voice, Energy, Security, Emerging, Business)
        FollowUp/          Category-by-Category Assessment, Coordinated Energy Flexibility,
                             Device Types & Feature Consistency, Dominant Barriers,
                             Home-AI Intent Interpretation, Mixed-Method Study Design,
                             Reproducible Test Protocol, Safe Autonomy,
                             Security & Privacy Lifecycle Scorecard, Support Periods
      Pending research/    unmigrated raw
      Archive/             historical Wave 1 material (ECA-protected)
    Stage 2/
      Extraction 1/        Claims.md, Entities.md, Metrics.md, Sources.md, Predicates.md, WorkflowMap.md, ExtractionLog.md
      Extraction 2/        same contract (smarthome.duckdb)
  processed/
    FollowUps/
      ResearchAgenda.md                    31 questions (15 P1, 16 P2)
      Wave2_Architectural_Open_Questions.md  8 questions (all P1)
      Wave2_Entity_Boundaries.md           22 questions (7 P1, 15 P2)
      Wave2_Primary_Evidence_Gaps.md        1 question (P2)
      Wave2_Benchmark_Conditions.md         0 questions (empty — gap!)
```

### 2.2 Existing follow-up coverage (from `ResearchAgenda.md`)

| Gap Code | Category | Count | Top Score |
|----------|----------|------:|----------:|
| `GAP-BND` | Entity Boundary | 20 | 20.0 (DuckDB, MCP) |
| `GAP-OPN` | Bundled Source Disambiguation | 6 | 16.0 |
| `GAP-CON` | Unresolved Source Alias | 2 | 12.0 (S5, S6) |
| `GAP-EPI` | Missing Direct URL | 1 | 9.0 (Internal vault notes) |

**Notable absence:** `GAP-BEN` (Benchmark Conditions) — Wave2_Benchmark_Conditions.md is empty; no benchmark/evaluation research questions have been formulated.

---

## 3. Proposed Research Directions

### 3.1 Data-Platform Boundary (P1)

**Rationale:** DuckDB and MCP score 20.0 (highest); pandas, Polars, dbt, MotherDuck score 12–16. The corpus treats these as architectural unknowns.

| Question ID | Scope | Target Evidence |
|-------------|-------|-----------------|
| RQ-BND-01 | Operational boundary of DuckDB vs. MotherDuck vs. DuckLake | Primary vendor docs; architecture diagrams; deployment modes |
| RQ-BND-02 | Operational boundary of pandas vs. Polars vs. dbt | Performance benchmarks; memory models; DAG semantics |
| RQ-BND-03 | Semantic layer boundary (Metabase, Superset, dbt) | Query routing; metadata federation; access control |
| RQ-BND-04 | PROV / W3C Provenance boundary | Vocabulary mapping to Stage 2 claims; lineage extraction |

**Acceptance criteria:** Each question resolves to a one-page architecture decision record (ADR) with canonical URLs and evidence class.

---

### 3.2 Agent & Protocol Architecture (P1/P2)

**Rationale:** MCP (P1, score 20.0), A2A (P2, score 8.0), LangGraph (P2, score 8.0), Microsoft Agent Framework (P2, score 8.0).

| Question ID | Scope | Target Evidence |
|-------------|-------|-----------------|
| RQ-AGT-01 | MCP protocol boundary — what constitutes a compliant server? | MCP spec; reference implementations; capability matrix |
| RQ-AGT-02 | A2A vs. MCP — overlap and distinct use cases | Cross-protocol comparison; agent-to-agent vs. model-to-tool |
| RQ-AGT-03 | LangGraph workflow orchestration boundary | Graph semantics; checkpointing; human-in-the-loop |
| RQ-AGT-04 | Research/scout agent operational boundary | Agent taxonomy; task delegation patterns |

**Acceptance criteria:** Protocol comparison matrix with evidence classes; no inferred capabilities.

---

### 3.3 Source Integrity (P1)

**Rationale:** 6 bundled sources unresolved (scores 16.0); 2 alias conflicts (S5/S6, score 12.0); 1 missing direct URL (score 9.0).

| Question ID | Scope | Target Evidence |
|-------------|-------|-----------------|
| RQ-SRC-01 | Decouple `docs.unstructured.io` + `docs.llamaindex.ai` | Individual project docs; canonical URLs per project |
| RQ-SRC-02 | Decouple `openlineage.io` + `openai-agents-python` + `w3.org/sparql11` + `cloud.google.com/bigquery` + `docs.jupyter.org` | Same pattern as RQ-SRC-01 |
| RQ-SRC-03 | Disambiguate alias S5 and S6 | Cross-reference `Sources.md`; verify via `stable_id` determinism |
| RQ-SRC-04 | Validate "Internal vault notes" evidence | Primary official documentation; reject synthetic-only sources |

**Acceptance criteria:** Each bundled source split into atomic single-URL records; alias resolution documented; vault notes either verified or flagged as unverified.

---

### 3.4 Smart-Home Domain Coverage (P2)

**Rationale:** Wave 1 covers 7 domains (Matter, AI/Voice, Energy, Security, Emerging, Business); Wave 2 has follow-up studies (Category-by-Category Assessment, Coordinated Energy Flexibility, Device Types, Dominant Barriers, Home-AI Safety, Mixed-Method Study, Reproducible Test Protocol, Safe Autonomy, Security Lifecycle Scorecard, Support Periods). Gaps in evidence remain.

| Question ID | Scope | Target Evidence |
|-------------|-------|-----------------|
| RQ-DOM-01 | Matter/Thread as connectivity foundation — market adoption vs. spec maturity | Matter spec versions; Thread certification counts; interoperability test results |
| RQ-DOM-02 | Home-AI intent interpretation safety benchmarks | Published benchmark conditions; false-positive/negative rates |
| RQ-DOM-03 | Energy flexibility model (HVAC, heat pumps, batteries, solar) — quantified savings | Measured kWh savings; demand-response participation rates |
| RQ-DOM-04 | Security & Privacy lifecycle scorecard — cross-vendor comparison | Scorecard methodology; vendor participation; update cadence |
| RQ-DOM-05 | Support periods and update mechanisms by device category | Manufacturer disclosure; EOL policies; patch frequency |

**Acceptance criteria:** Each direction produces a one-page evidence summary with confidence level; no invented metrics.

---

### 3.5 Benchmark & Evaluation Gap (P1 — empty agenda)

**Rationale:** `Wave2_Benchmark_Conditions.md` has 0 questions. The corpus explicitly notes this gap. This is the highest-leverage direction because it unblocks all quantitative claims.

| Question ID | Scope | Target Evidence |
|-------------|-------|-----------------|
| RQ-BEN-01 | Define benchmark conditions for Home-AI intent interpretation | Reproducible test protocol; baseline metrics; success criteria |
| RQ-BEN-02 | Define benchmark conditions for security lifecycle scorecard | Scoring rubric; sample vendor set; evaluation frequency |
| RQ-BEN-03 | Define benchmark conditions for energy flexibility model | Measurable KPIs (kWh saved, peak reduction, cost savings) |
| RQ-BEN-04 | Define benchmark conditions for device support periods | Standardized reporting format; minimum data points per category |

**Acceptance criteria:** Each benchmark has a documented protocol, baseline, and measurement method; no benchmarks invented from corpus-silent data.

---

## 4. Implementation Phases

### Phase 1: Source Integrity (Week 1)
- Decouple 6 bundled sources into atomic records
- Resolve S5/S6 alias conflicts
- Validate or flag "Internal vault notes"
- **Gate:** `Sources.md` has one URL per row; `stable_id` determinism verified

### Phase 2: Data-Platform Boundary (Week 2)
- Resolve DuckDB/MotherDuck/DuckLake boundary
- Resolve pandas/Polars/dbt boundary
- Document PROV/lineage mapping
- **Gate:** Each entity has an ADR with canonical URLs; no inferred capabilities

### Phase 3: Agent & Protocol Architecture (Week 3)
- Resolve MCP protocol boundary
- Compare A2A vs. MCP
- Document LangGraph and Agent Framework boundaries
- **Gate:** Protocol comparison matrix with evidence classes

### Phase 4: Smart-Home Domain Coverage (Weeks 4–5)
- Cover 5 domain gaps (Matter, Home-AI safety, Energy, Security, Support periods)
- **Gate:** Each domain has evidence summary with confidence level

### Phase 5: Benchmark Conditions (Week 6)
- Formulate benchmark conditions for 4 gaps (Home-AI, Security, Energy, Support)
- **Gate:** `Wave2_Benchmark_Conditions.md` populated; each benchmark has protocol + baseline + KPIs

---

## 5. Change Controls

- This plan is proposed, not adopted. Status remains `proposed` until maintainer acceptance.
- No research operations until Phase 1 source-integrity gate passes.
- If a research question reveals a corpus defect (broken schema, missing source), file a Problem record in `Commander Deck/Problems/` before continuing.
- All derived artifacts (new markdown, updated DBs) follow the export protocol with verification roundtrips.
- Archive any superseded plans using ECA before replacing.

## 6. Acceptance Criteria

| Measure | Target |
|---------|--------|
| Source integrity | 0 bundled sources; 0 unresolved aliases; 0 unverified vault notes |
| Data-platform boundary | 1 ADR per entity; all canonical URLs verified |
| Protocol architecture | Comparison matrix with evidence classes; no inferred capabilities |
| Domain coverage | 5 domains with evidence summaries; no invented metrics |
| Benchmark conditions | 4 benchmarks with protocol + baseline + KPIs; none invented from silent data |
| Follow-up agenda | `ResearchAgenda.md` updated; `Benchmark_Conditions.md` populated |

## 7. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Polished plan mistaken for accepted policy | Keep status visible; require maintainer approval before research operations |
| Benchmark conditions invented from corpus-silent data | Explicit gate: corpus must record the metric or state it is missing |
| Alias resolution creates duplicate sources | Verify via `stable_id` determinism; run `test_ingest_citations` after changes |
| ECA archive operations without `--dry-run` | Follow `Encryption-Compression-Archiving.md`; always dry-run first |
