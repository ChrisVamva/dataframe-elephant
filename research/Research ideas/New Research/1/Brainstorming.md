# Research Ideas

## 5. Prompt Assembly Effectiveness Study (templates vs. follow‑up quality)

### 5.1 Research Question

How does the choice of prompt template and prompt structure affect the quality of follow‑up research agendas produced by `followup_core.py`?

### 5.2 Hypotheses

- **H1 (structure):** Templates that enforce explicit negative boundaries (`"is not…"`) produce higher‑quality `FormulatedQuestion` outputs than templates that omit them.
- **H2 (batching):** Templates that decompose work into explicit batches (e.g., `next_research.md` §4) produce more complete, less redundant question sets than monolithic prompts.
- **H3 (gate enforcement):** Templates that embed protocol gate checks (`FU:Gate A/B/C`, `RE:Gate D`) in their self‑check section produce questions that pass `validate_questions()` at a higher rate.
- **H4 (context):** Templates that require explicit context variables (e.g., `--var study=…`) produce outputs that are more traceable and less hallucinated than those assembled without them.

### 5.3 Experimental Design

**Independent variables (manipulated):**
1. **Template identity** — `research_brief`, `next_research`, `followup_dispatch`
2. **Prompt structure variants** — assembled with/without:
   - Negative‑boundary language
   - Batched execution queues
   - Embedded gate‑check self‑verification sections
3. **Context variables** — presence/absence of `--var study=…` and `--context FILE.json`

**Dependent variables (measured):**
1. **Output volume** — number of `FormulatedQuestion` objects generated per run
2. **Gate pass rate** — fraction of questions passing `validate_questions()` gates A–D
3. **Falsifier quality** — scored 0–3 per question: 0 = no falsifier, 1 = vague, 2 = specific but untestable, 3 = specific and testable
4. **Schema compliance** — fraction of questions whose output matches the Stage 2 schema shape (Entities.md / Sources.md / Metrics.md row formats)
5. **Redundancy** — duplicate or near‑duplicate `rq_id` across runs
6. **Coverage** — fraction of detected `ResearchGap` types (GAP‑BND, GAP‑OPN, GAP‑CON, GAP‑EPI, GAP‑FAL, GAP‑CND) addressed

**Control variables:**
- Same `stage2_dir`, `database_path`, and input corpus for all runs
- Same LLM/model used for any generation steps
- Same `followup_core.py` version

### 5.4 Procedure

1. **Baseline assembly** — Assemble each template with `scripts/assemble_prompt.py` using the default context. Record assembled prompt length and structure.
2. **Gap scanning** — Run `scripts/formulate_research_questions.py` with each assembled prompt as the system instruction (or run the existing pipeline and capture its output).
3. **Question generation** — For each template variant, generate `FormulatedQuestion` sets from the same `ResearchGap` pool.
4. **Validation** — Pass each set through `validate_questions()` and score falsifiers and schema compliance.
5. **Analysis** — Compute the dependent variables per condition. Run ANOVA or Kruskal‑Wallis tests to assess significance of template identity and structure variants.

### 5.5 Data Sources

- Prompt templates under `src/prompt_templates/` (lint and assembly logic in `src/prompt_core.py`)
- `scripts/assemble_prompt.py` (template assembly)
- `scripts/formulate_research_questions.py` (question formulation pipeline)
- `src/followup_core.py` (`validate_questions`, `build_research_agenda_markdown`)
- `research/processed/FollowUps/ResearchAgenda.md` (existing output for comparison)
- `research/raw/Stage 2/Extraction 1/` (Entities.md, Sources.md, Metrics.md, ExtractionLog.md)
- `data/citations.duckdb`, `data/stage2.duckdb`

### 5.6 Analysis Plan

1. **Descriptive** — Tabulate dependent variables by template and structure variant.
2. **Inferential** — Test whether template identity significantly affects gate pass rate and falsifier quality.
3. **Qualitative** — Manually review a sample of outputs per condition to identify systematic failure modes (e.g., missing negative boundaries, over‑broad scope).
4. **Recommendation** — Based on results, propose concrete modifications to the three templates (e.g., add explicit negative‑boundary language to `research_brief`, add batch decomposition to `followup_dispatch`).

### 5.7 Expected Deliverables

- `research/processed/FollowUps/PromptEffectivenessStudy.md` — full report
- Updated prompt templates with evidence‑backed modifications
- A `scripts/run_prompt_study.py` script that automates the assembly → generation → validation pipeline for reproducibility

---

## Other Research Ideas

- Temporal citation network analysis: track how claim citations evolve across research documents over time, using stable IDs to map claim propagation.
- Domain‑specific claim extraction validation: compare claim extraction accuracy across domains (e.g., smart home, energy, security) to identify domain biases.
- Impact of data source diversity on citation clustering: evaluate how adding different source types (web, academic, blog) affects clustering quality and downstream analytics.
- Smart home failure mode reproducibility: run the "Three ways your smart home die" notebooks on multiple datasets to assess reproducibility of failure mode identification.
- Archive compression trade‑offs: benchmark ECA encryption speed, size, and decryption time for various compression algorithms (e.g., Zstandard vs. Gzip) to guide optimal archiving.
- LLM provider capability impact on claim classification: analyze whether using different LLM providers (e.g., DeepInfra vs. Qwen) affects claim classification accuracy in `ingest_citations.py`.
- Visualization notebook performance: profile notebook runtime and memory usage across wave 1 and wave 2 to identify bottlenecks in `viz_core.py`.
- Multi‑modal claim linking: explore integrating textual claims with images or video frames from smart home datasets to enrich claim provenance.
- Automated research gap detection: extend `followup_core.py` to automatically detect missing claim‑metric relationships and propose concrete research questions.