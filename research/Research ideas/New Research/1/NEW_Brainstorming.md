# Research Ideas

## 1. Prompt Engineering as an Independent Research Domain

**Question:** How do structured prompt assembly systems (template resolution, variable substitution, partial inclusion) compare to ad-hoc prompting in producing verifiable, citation-backed research outputs?

**Scope:** Study prompt engineering frameworks *across the field* — not this repo's `scripts/assemble_prompt.py`. Survey 10–15 open-source prompt orchestration tools (e.g., LangChain prompt templates, Guidance, DSPy, Semantic Kernel, PromptSource, PromptFlow, Mirascope, Instructor, Outlines, BAML, Promptfoo, Helix, PromptLayer, Langfuse, Humanloop) and measure:

| Dimension | Metric |
|-----------|--------|
| Template composability | Number of reusable partials; inclusion depth; cycle detection |
| Variable resolution | Typed vs. string-only; default/override precedence; schema validation |
| Execution model | Static assembly vs. dynamic chaining; streaming support |
| Verification hooks | Built-in schema checks, citation enforcement, falsifier requirements |
| Output schema enforcement | JSON Schema, Pydantic, TypeScript, custom validators |
| Observability | Logging, tracing, versioning, A/B testing support |

**Deliverable:** A comparative matrix + recommendation on whether any external framework justifies replacing/removing the `src/prompt_templates/` + `src/prompt_core.py` + `scripts/assemble_prompt.py` stack.

---

## 2. Citation Extraction Quality: Prompt-Based vs. Rule-Based Pipelines

**Question:** Does an LLM-driven prompt pipeline extract claims/citations from Markdown corpora more accurately than the current deterministic `ingest_citations.py` (regex + table parsing)?

**Design:**
- Same input corpus: `research/raw/Stage 2/Extraction 1/` Markdown tables
- Two pipelines:
  1. **Rule-based (baseline):** Current `ingest_citations.py` → `data/citations.duckdb`
  2. **Prompt-based:** Structured prompt (from external framework in #1) → LLM → same DuckDB schema
- Evaluation: Precision/recall/F1 on a manually labeled 200-row test set (claim boundaries, source linking, metric extraction, evidence class)
- Vary: Model (3–4 providers), temperature (0, 0.3), few-shot examples (0, 3, 10)

**Deliverable:** Evidence-backed decision: keep `ingest_citations.py`, replace with prompt pipeline, or hybrid.

---

## 3. Smart Home Failure Mode Taxonomy: External Validation

**Question:** Do the three failure classes in the "Three ways your smart home die" articles (border router loss, WAN outage, vendor cloud retirement) generalize across independent smart home deployments?

**Method:**
- Collect 5+ public datasets / forum corpora (Home Assistant logs, Thread/Matter issue trackers, Reddit r/homeautomation, vendor support forums)
- Extract failure narratives → classify into the three classes + "other"
- Measure inter-rater agreement (Cohen's κ) and class distribution stability
- Test whether the distinction between "router down" vs. "internet down" holds in real deployments

**Deliverable:** Validated taxonomy (or revised) + labeled dataset for future notebook regeneration.

---

## 4. Evidence Grading Standards Across Domains

**Question:** How do evidence grading frameworks (GRADE, CASP, ROBINS-I, PROV-O, this project's `claim_taxonomy.md`) differ in classifying the same set of smart home claims?

**Method:**
- Sample 50 claims from `data/citations.duckdb` (mix of documented facts, reported signals, inferences)
- Apply 4–5 grading frameworks independently (blind)
- Measure agreement, systematic biases, actionability of resulting confidence scores

**Deliverable:** Mapping table + recommendation on whether to adopt/adapt an external standard.

---

## 5. Longitudinal Citation Drift in Evolving Specifications

**Question:** How do citations to evolving specs (Matter, Thread, Zigbee, Home Assistant) change over time — do they cite newer versions, supersede old claims, or accumulate contradictions?

**Method:**
- Identify all spec-versioned sources in `data/citations.duckdb`
- Build temporal citation graph (source version → claim → citing document)
- Detect: version upgrades without claim updates, contradictory claims citing different versions, orphaned claims (source version deprecated)

**Deliverable:** Drift report + automated alert rules for `ingest_citations.py`.

---

## 6. Automated Research Gap Detection: Benchmarking External Tools

**Question:** Can existing research-gap detection tools (Semantic Scholar API, Connected Papers, Elicit, Scite, Iris.ai, Litmaps, ResearchRabbit) identify gaps in this corpus that `followup_core.py` misses?

**Method:**
- Export `ResearchAgenda.md` questions as queries
- Run each tool; collect top-20 suggested gaps/papers
- Human evaluation: novelty, relevance, actionability vs. `followup_core.py` output

**Deliverable:** Cost/benefit analysis of integrating external gap detection.

---

## 7. Archive Format Interoperability: ECA vs. Standards

**Question:** How does the custom ECA format (`archive_core.py`: AES-256-GCM + PBKDF2 600k) compare to standard archival formats (WARC, BagIt, OCFL, CAR) on: restoration time, tool ecosystem, verification, long-term readability?

**Method:** Benchmark each format on a 10 GB `research/raw/Stage 1/` sample.

**Deliverable:** Migration recommendation (keep ECA, adopt standard, hybrid).

---

## 8. Visualization Notebook Portability: Jupyter vs. Observable vs. Marimo vs. Quarto

**Question:** Can the wave 1/2 notebooks (`notebooks/1/`, `notebooks/2/`) be losslessly ported to other reactive notebook platforms?

**Method:** Transpile 3 representative notebooks to Observable, Marimo, Quarto; compare:
- Runtime parity (Plotly → native charts)
- Interactivity preservation (ipywidgets → platform equivalents)
- Reproducibility (environment capture, dependency locking)
- Authoring ergonomics for the research team

**Deliverable:** Porting guide + platform recommendation.

---

## Notes on Prompt Templates

Current status: **unconnected to the core pipeline**. No core module imports it; `scripts/assemble_prompt.py` is a standalone CLI. The templates (`research_brief`, `next_research`, `followup_dispatch`) are elaborate but unvalidated against external frameworks.

**Decision gate:** If Research Idea #1 or #2 shows an external framework is superior, or if the prompt-based pipeline doesn't beat the rule-based baseline, refactor `src/prompt_core.py` and `scripts/assemble_prompt.py`.