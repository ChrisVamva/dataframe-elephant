# Citation Report — Source Classification by Document
**Compiled:** 2026-09-27  
**Scope:** All documents in `research/raw`. For each document, every citation is listed with its classification, followed by a brief source-quality summary.

**Classification definitions:**
- **Primary** — First-party official documentation, peer-reviewed / academic papers, W3C / NIST / BLS / O*NET standards, official product pages, official GitHub repositories, first-party job postings, formally published ontology releases (Zenodo + journal).
- **Secondary** — Blog posts, comparison guides, news articles, newsletters, career-advice sites, vendor marketing comparisons, aggregator/ranking sites, Wikipedia, secondhand surveys.
- **Mixed** — A single cited group contains both primary and secondary sub-sources; noted where applicable.

---

## 1. ANT GP H.md

**Document type:** Structured research brief (Research-to-Data Capability Atlas)

| Citation | Classification | Notes |
|----------|----------------|-------|
| freelancermap.com, upriverdata.com — role definitions | Secondary | Career/freelance marketplace sites; no primary authority |
| getdbt.com — ETL vs ELT methodology | Primary | Official dbt Labs documentation |
| medium.com, secoda.co — ETL/ELT and provenance | Secondary | Blog/vendor marketing content |
| langchain.com, crewai.com, pydantic.dev — agent frameworks | Primary | Official vendor/framework documentation |
| codecentric.de, medium.com — tool comparisons | Secondary | Engineering blog and community posts |

**Source quality summary:** Lightly cited. Uses a mix of official vendor docs (Primary) and third-party blogs/career sites (Secondary). No academic papers or standards cited. Evidence confidence is anchored mostly on vendor docs rather than independent benchmarks.

---

## 2. C.md

**Document type:** Comprehensive evidence-grounded synthesis brief

| # | Citation | Classification |
|---|----------|----------------|
| 1 | Analytics Vidhya — pandas vs Polars vs DuckDB | Secondary |
| 2 | Chat2DB — DuckDB vs Polars vs Pandas | Secondary |
| 3 | Level Up Coding (Yang Zhou) — Beyond pandas | Secondary |
| 4 | MotherDuck blog — DuckDB vs pandas vs Polars | Secondary |
| 5 | Wikipedia — Polars (software) | Secondary |
| 6 | Analytics Insight — pandas vs Polars vs DuckDB | Secondary |
| 7 | CodeCut — pandas vs Polars vs DuckDB | Secondary |
| 8 | Codecentric — benchmark comparison (Dec 2025) | Secondary |
| 9 | Danilchenko.dev — DuckDB vs Polars 2026 | Secondary |
| 10 | GitHub munesoft/agent — MCP bridge | Secondary |
| 11 | Atlan — AI Agent Frameworks Compared | Secondary |
| 12 | LangChain — Best AI agent frameworks 2026 | Primary |
| 13 | Turing — Top 6 AI Agent Frameworks | Secondary |
| 14 | GitHub artnitolog — agent-framework resources | Secondary |
| 15 | TechAhead — Top Agent Frameworks | Secondary |
| 16 | Pickaxe — Top 15 AI Agent Frameworks 2026 | Secondary |
| 17 | Medium — Top 9 AI Agent Frameworks 2026 | Secondary |
| 18 | Arsum — AI agent frameworks (critical) | Secondary |
| 19 | Basedash — Best Open Source BI Tools 2026 | Secondary |
| 20 | elest.io — Superset vs Metabase vs Redash | Secondary |
| 21 | Basedash — BI tools for Supabase | Secondary |
| 22 | Coefficient — Open Source BI Tools 2026 | Secondary |
| 23 | The Bricks — Metabase vs Superset (Dec 2025) | Secondary |
| 24 | DEV Community — Superset vs Metabase | Secondary |
| 25 | The Bricks — Metabase vs Superset vs Redash | Secondary |
| 26 | Definite — Metabase alternatives | Secondary |
| 27 | ToolRadar — dbt vs Metabase | Secondary |
| 28 | The Data School — data roles comparison | Secondary |
| 29 | DePaul University — data architect career resource | Secondary |
| 30 | Towards Data Science — roles in data ecosystem | Secondary |
| 31 | WsCube Tech — Data Analyst vs Data Engineer | Secondary |
| 32 | SIGIA-L archive (2006) — information architect debate | Secondary |
| 33 | Wikipedia — DuckDB | Secondary |
| 34 | Atlan — Knowledge Graph vs Graph Database | Secondary |
| 35 | Energent.ai — knowledge graph industry report | Secondary |
| 36 | Galaxy — Top Knowledge Graph Platforms 2026 | Secondary |
| 37 | Neo4j AI Product Keynote (July 2026) | Primary |
| 38 | FutureAGI — enterprise knowledge-graph comparison | Secondary |
| 39 | Scour.ing — Neo4j/GraphAware acquisition news | Secondary |
| 40 | Rajesh Kumar — knowledge graph construction tools | Secondary |
| 41 | Nutrient — Best Reducto alternatives 2026 | Secondary |
| 42 | Nutrient — Best LlamaParse alternatives (Aug 2026) | Secondary |
| 43 | LlamaIndex — Best Alternatives to Reducto | Secondary |
| 44 | Reducto — AI data extraction tools guide | Secondary |
| 45 | Firecrawl blog — Best data extraction tools | Secondary |
| 46 | ToolJunction — document parsing API comparison | Secondary |
| 47 | Extend.ai — Unstructured review (Mar 2026) | Secondary |
| 48 | TheDrive.ai — Best Document Extraction APIs 2026 | Secondary |
| 49 | AI Epoch newsletter — deep research tools | Secondary |
| 50 | Dupple — Best AI Research Tools 2026 | Secondary |
| 51 | CB Insights — Consensus competitors | Secondary |
| 52 | Deepak Gupta — research tools comparison | Secondary |
| 53 | GWU Engineering — AI for literature review recap | Secondary |
| 54 | Bentley University libguides (truncated) | Secondary |

**Source quality summary:** Heavily secondary. Of 54 citations, only 2 are primary (LangChain official docs and Neo4j keynote). The majority are blog posts, vendor comparison guides, and aggregator sites. The document itself acknowledges this, flagging several claims as "reported signal" and identifying the company/provenance lens as the weakest. Findings from this document should be cross-verified with primary sources before formal data modeling.

---

## 3. CP L6.md

**Document type:** Source-grounded raw research brief on ETL vs ELT

| ID | Citation | Classification |
|----|----------|----------------|
| S1 | Google Cloud BigQuery — Loading, transforming, and exporting data | Primary |
| S2 | Google Cloud BigQuery — Overview of BigQuery storage | Primary |
| S3 | Snowflake — Key concepts and architecture | Primary |
| S4 | Google Cloud BigQuery — Introduction to loading data | Primary |
| S5 | Snowflake — Overview of data loading | Primary |
| S6 | Databricks — Medallion lakehouse architecture | Primary |
| S7 | Google Cloud BigQuery — Data governance | Primary |
| S8 | Snowflake — Overview of Access Control | Primary |
| S9 | dbt Labs — What is dbt? | Primary |
| S10 | dbt Labs — Add data tests to your DAG | Primary |

**Source quality summary:** Exclusively primary sources. All 10 citations are first-party official documentation from Google BigQuery, Snowflake, Databricks, and dbt Labs. This is the highest-quality document in the corpus from an evidentiary standpoint. The document itself is careful to distinguish between documented facts and inferences derived from those sources.

---

## 4. DC L5.6.md

**Document type:** Evidence-grounded atlas with claim-centric modeling recommendation

| # | Citation | Classification |
|---|----------|----------------|
| 1 | W3C — PROV-O: The PROV Ontology (2013) | Primary |
| 2 | W3C — PROV-DM: The PROV Data Model (2013) | Primary |
| 3 | W3C — DCAT v3 (2024) | Primary |
| 4 | DuckDB — Why DuckDB / Documentation | Primary |
| 5 | pandas — User Guide | Primary |
| 6 | Polars — User Guide | Primary |
| 7 | Apache Arrow | Primary |
| 8 | Jupyter — Documentation | Primary |
| 9 | dbt Labs — What is dbt? | Primary |
| 10 | Metabase — Documentation | Primary |
| 11 | Apache Airflow — Core concepts / DAGs | Primary |
| 12 | OpenLineage — Home and Object Model | Primary |
| 13 | JSON Schema — Specification | Primary |
| 14 | Playwright — Official documentation | Primary |
| 15 | OpenAI Agents SDK — Agents and tracing | Primary |
| 16 | NIST — AI Risk Management Framework: Generative AI Profile (2024) | Primary |
| 17 | U.S. Bureau of Labor Statistics — Operations Research Analysts | Primary |
| 18 | U.S. Bureau of Labor Statistics — Data Scientists | Primary |
| 19 | O*NET OnLine — Career exploration and job analysis | Primary |
| 20 | Internal vault note — PROV-K Ontology | Primary (internal) |
| 21 | Internal vault note — Components to investigate | Primary (internal scope) |

**Source quality summary:** All primary. Every external citation is a first-party official source: W3C standards, official tool documentation, U.S. federal agencies (BLS, NIST), or open standards bodies. Two citations reference internal vault notes, which are primary within the project context. This document, alongside CP L6.md, represents the strongest evidentiary basis in the corpus.

---

## 5. DPS.md

**Document type:** Research-to-Data Capability Atlas — Structured Research Brief (initial synthesis)

| # | Citation | Classification |
|---|----------|----------------|
| 1 | DuckDB System Architecture (via mintlify mirror of duckdb.org) | Primary |
| 2 | DuckDB Introduction (via mintlify mirror) | Primary |
| 3 | Codecentric — DuckDB vs. Polars vs. Pandas (Dec 2025) | Secondary |
| 4 | Querio — Best DuckDB-Powered Analytics Tools | Secondary |
| 5 | SciGraph-LLM (ACM DL) — evidence-grounded extraction pipeline | Primary |
| 6 | Multi-Agent AI Open-Source Ecosystem (ACL 2026) | Primary |
| 7 | Zenodo — Provenance, Timestamp Evidence, and Source-Chain Auditability | Primary |
| 8 | Springer — Systematic Review of Automation in Data Warehouse Design | Primary |
| 9 | Research Engineer Job Posting (ZipRecruiter) | Primary |
| 10 | Knowledge Engineer Job Posting (SmartRecruiters) | Primary |
| 11 | Data Analyst Job Posting (Accel Job Board) | Primary |
| 12 | AI Automation Specialist Job Posting (Upwork) | Primary |
| 13 | Information Architect Job Posting (ZipRecruiter) | Primary |
| 14 | dbt Documentation | Primary |
| 15 | Jupyter Documentation (IBM Cloud) | Primary |
| 16 | Camoufox Research (PyPI) | Primary |
| 17 | MotherDuck Product Page | Primary |
| 18 | Hex Product Page | Primary |
| 19 | Evidence Documentation | Primary |
| 20 | Lightdash Documentation | Primary |
| 21 | Polars Lazy API Documentation | Primary |
| 22 | ORKG (EOSC Association) | Primary |
| 23 | CAS Intelligence Hub | Primary |
| 24 | Sharpr (Dynata) | Primary |
| 25 | Agent Infrastructure Commoditization (Forkast) | Secondary |
| 26 | Global Data Extraction Software Market Report (marketresearch.com) | Secondary |

**Source quality summary:** Predominantly primary (20 of 26). Peer-reviewed papers (ACM, ACL, Springer), Zenodo records, official documentation, and first-party job postings form the backbone. The 4 secondary sources cover comparison benchmarks and a market report; these are appropriately flagged in the document as "reported signal." Strong source basis overall.

---

## 6. FAI.md

**Document type:** Evidence-grounded atlas with tagged claim types (documented fact / reported signal / inference)

| # | Citation | Classification |
|---|----------|----------------|
| 1 | dbt Labs — "What is analytics engineering?" | Primary |
| 2 | DuckDB official site | Primary |
| 3 | DuckDB GitHub repository | Primary |
| 4 | DuckDB history page | Primary |
| 5 | Wikipedia — W3C PROV overview | Secondary |
| 6 | ACM paper on W3C PROV (dl.acm.org) | Primary |
| 7 | Agenta — guide to structured outputs with LLMs | Secondary |
| 8 | Towards Data Science — structured outputs with LLMs | Secondary |
| 9 | OpenAI — "Introducing Deep Research" | Primary |
| 10 | LangChain — LangGraph | Primary |
| 11 | arXiv — LLM data preparation survey (2601.17058) | Primary |
| 12 | AWS — ETL vs ELT explainer | Primary |
| 13 | Rivery — ETL vs ELT blog | Secondary |
| 14 | Chartio — distinguishing data roles | Secondary |
| 15 | LearnSQL — dbt analytics engineer | Secondary |
| 16 | The Hartford — Knowledge Graph Engineer job posting | Primary |
| 17 | Vintti — Knowledge Engineer job description template | Secondary |
| 18 | pandas official site | Primary |
| 19 | Polars GitHub | Primary |
| 20 | pgvector GitHub | Primary |
| 21 | Medium — ontology standards overview | Secondary |
| 22 | dev.to — DuckDB comprehensive guide | Secondary |
| 23 | Polars official site | Primary |
| 24 | Polars documentation | Primary |
| 25 | Wikipedia — Project Jupyter | Secondary |
| 26 | Observable HQ | Primary |
| 27 | ScrapingBee — Playwright for Python web scraping | Secondary |
| 28 | Wikipedia — MotherDuck | Secondary |
| 29 | Wikipedia — Semantic data model | Secondary |
| 30 | Medium — structured output generation in LLMs | Secondary |
| 31 | TechCrunch — Google Deep Research (Dec 2025) | Secondary |
| 32 | Azure blog — Deep Research in Azure AI Foundry | Primary |
| 33 | OpenAI — "Introducing ChatGPT agent" | Primary |
| 34 | Observable blog — exploration to data apps | Primary |

**Source quality summary:** Good balance of primary (18) and secondary (14). The document uses explicit evidence tags (documented fact, reported signal, inference) which aligns well with source type. Primary sources cover official product docs, academic papers, and first-party announcements. Secondary sources are used for framing roles and comparisons where no single authoritative source exists.

---

## 7. G0.md

**Document type:** Structured research brief with entity/relationship candidates

| # | Citation | Classification |
|---|----------|----------------|
| 1 | DuckDB official site & docs | Primary |
| 2 | DuckLake blog post (May 2025) | Secondary |
| 3 | Polars benchmarks 2024 (pola.rs own benchmarks) | Primary |
| 4 | dbt Developer Hub & modeling guides | Primary |
| 5 | Metabase vs Superset — Metabase LP (comparison page) | Secondary |
| 5b | Apache Superset GitHub/docs | Primary |
| 6 | Project Jupyter | Primary |
| 7 | Job postings for Knowledge Engineer (Indeed, LinkedIn) | Primary |
| 8 | Role comparison articles (secondary sites) | Secondary |
| 9 | Unstructured.io & LlamaIndex docs | Primary |
| 10 | Academic papers — IE, EvidenceBench, provenance, nanopublications | Primary |
| 11 | LangChain, LlamaIndex, CrewAI documentation | Primary |
| 12 | MotherDuck materials | Primary |

**Source quality summary:** Predominantly primary. The majority of sources are official documentation, academic literature, and first-party job postings. Secondary sources are limited to the DuckLake blog post, Metabase comparison page, and role comparison articles. The academic citations (EvidenceBench, EvidenceNet, provenance/nanopublication papers) are the strongest evidential anchors for the extraction and provenance lenses.

---

## 8. G1.md

**Document type:** Detailed technical note on nanopublication structure

| # | Citation | Classification |
|---|----------|----------------|
| 1 | Official Nanopublication Guidelines (working draft) — nanopub.net | Primary |
| 2 | nschema ontology — nanopub.net | Primary |

**Source quality summary:** Entirely primary. Both citations are from the authoritative nanopublication project itself. This document is a focused technical reference and exhibits the highest source density relative to length.

---

## 9. G2.md

**Document type:** Detailed overview of the PROV-K ontology

| # | Citation | Classification |
|---|----------|----------------|
| 1 | PROV-K ontology documentation (prov-k.dei.unipd.it / w3id.org) | Primary |
| 2 | PROV-K Zenodo release (record 15187372, v1.0, 2025-04-10) | Primary |
| 3 | PROV-O (W3C) — imported by PROV-K | Primary |
| 4 | SKOS (W3C) — imported by PROV-K | Primary |
| 5 | International Journal on Digital Libraries (2025) — peer-reviewed paper | Primary |

**Source quality summary:** Entirely primary. All five citations are first-party or peer-reviewed: the ontology's own documentation page, its Zenodo archival release, two W3C standards it builds on, and the associated peer-reviewed journal paper. This is the most rigorous document in the corpus by source classification.

---

## 10. G3.md

**Document type:** Detailed note on nanopublication provenance formats and PROV-K extension

| # | Citation | Classification |
|---|----------|----------------|
| 1 | Nanopublication Guidelines (working draft) — nanopub.net | Primary |
| 2 | Nanopublication site — nanopub.net | Primary |
| 3 | PROV-K ontology & paper — Zenodo + International Journal on Digital Libraries (2025) | Primary |
| 4 | Surveys of large nanopublication collections (academic) | Primary |

**Source quality summary:** Entirely primary. All sources are either the authoritative nanopublication project documentation or peer-reviewed academic work. No secondary sources are used.

---

## 11. OP MS 1.3F.md

**Document type:** Detailed research brief with claim-type legend ([F] / [S] / [I] / [R])

| # | Citation | Classification |
|---|----------|----------------|
| 1 | DuckDB homepage + Why DuckDB + SIGMOD 2019 / CIDR 2020 papers | Primary |
| 2 | MotherDuck product pages | Primary |
| 2b | TechCrunch (2023) — MotherDuck funding | Secondary |
| 3 | MotherDuck blog — DuckDB vs pandas vs Polars | Secondary |
| 3b | Polars PDS-H benchmarks (pola.rs) | Primary |
| 3c | prrao87/duckdb-study (GitHub) | Primary |
| 4 | dbt Labs ELT/ETL/model/best-practice docs | Primary |
| 5 | TechTarget / Indeed UK / nCube / ChartIO / Research.com / StrataScratch | Secondary |
| 6 | Guardian, Investopedia, Indeed, H2K Infosys, ITJobsWatch — research analyst | Secondary |
| 7 | Accenture job postings (4×) | Primary |
| 7b | Southampton ontology engineering slides | Primary |
| 7c | ScienceDirect — knowledge engineer entry | Primary |
| 8 | W3C PROV family (DM, Primer, NS, Overview, MSI/DublinCore) | Primary |
| 9 | PRISMA 2020 (BMJ, EQUATOR, PMC) | Primary |
| 10 | BI comparators (Metabase LP, Appaca, Querio, Valiotti, elest.io) | Secondary |
| 11 | Observable + Plot (observablehq.com, GitHub repos) | Primary |
| 12 | Neo4j vector/graph/GraphRAG docs | Primary |
| 13 | Unstructured Extract docs; LlamaExtract/LlamaParse docs | Primary |
| 14 | LangGraph / LangChain docs | Primary |
| 14b | N-IX, meta-intelligence, ailog.fr comparisons | Secondary |
| 14c | IBM developer article | Primary |
| 15 | DeepHalluBench/PING arXiv preprints | Primary |
| 15b | Microsoft AIRT Taxonomy v2.0 (CDN PDF) | Primary |
| 15c | AWS/IBM context-pointer report | Primary |

**Source quality summary:** Strong primary base with selective use of secondary sources. The document itself employs a [F]/[S]/[I]/[R] tagging system that maps closely to primary/secondary classification. Key anchors: peer-reviewed SIGMOD/CIDR papers for DuckDB; W3C PROV and PRISMA 2020 for standards; Accenture job postings for role evidence; Microsoft AIRT and arXiv for agent failure modes. Secondary sources are mostly used for role-market framing and BI product comparisons.

---

## 12. Q.md

**Document type:** Research-to-Data Capability Atlas with VLM/browser automation focus

| # | Citation | Classification |
|---|----------|----------------|
| 1 | Skyvern Blog — AI Web Agents guide (Nov 2025) | Secondary |
| 2 | Skyvern Blog — Browserbase vs Firecrawl vs Skyvern (Dec 2025) | Secondary |
| 3 | Codecentric — DuckDB vs. Polars vs. Pandas (Dec 2025) | Secondary |
| 4 | Medium (Ramesh Kannan) — Pandas vs Polars vs DuckDB 2026 | Secondary |
| 5 | ORNL / R. Souza et al. — PROV-AGENT (2025) | Primary |
| 6 | Talby — Fact-level provenance in healthcare (Sep 2026) | Secondary |
| 7 | arXiv:2608.22974 — Dynamic Ontology for LLM Agents (Aug 2026) | Primary |
| 8 | Accenture / Simplify.jobs — Knowledge Engineer posting (2026) | Primary |
| 9 | LinkedIn / Secumatic — Agentic AI Workflow Developer posting (2026) | Primary |
| 10 | Bright Data Blog — Best Agentic Browsers 2026 | Secondary |

**Source quality summary:** Split between primary (4) and secondary (6). The strongest primary sources are an ORNL peer-reviewed paper on PROV-AGENT, an arXiv preprint on dynamic ontology for LLM agents, and two first-party job postings. Secondary sources are vendor blogs and benchmark comparisons. This document is notably the most focused on emerging topics (VLM-based automation, regulatory provenance), where primary sources are naturally sparser.

---

## Cross-Document Citation Analysis

### Most-cited primary sources (appearing across multiple documents)

| Source | Documents | Classification |
|--------|-----------|----------------|
| W3C PROV-O / PROV-DM (w3.org/TR/prov-o/, prov-dm/) | DC L5.6.md, FAI.md, G2.md, G3.md, OP MS 1.3F.md | Primary |
| dbt Labs documentation (docs.getdbt.com) | ANT GP H.md, C.md, CP L6.md, DC L5.6.md, DPS.md, FAI.md, G0.md, OP MS 1.3F.md | Primary |
| DuckDB official site / docs (duckdb.org) | DC L5.6.md, DPS.md, FAI.md, G0.md, OP MS 1.3F.md | Primary |
| Nanopublication Guidelines (nanopub.net) | G1.md, G3.md | Primary |
| PROV-K ontology + Zenodo release | G2.md, G3.md | Primary |
| LangChain / LangGraph (langchain.com) | ANT GP H.md, C.md, DC L5.6.md, FAI.md, G0.md, OP MS 1.3F.md | Primary |
| pandas docs (pandas.pydata.org) | DC L5.6.md, FAI.md | Primary |
| Polars docs (docs.pola.rs / pola.rs) | DC L5.6.md, FAI.md, G0.md, OP MS 1.3F.md | Primary |
| OpenAI — Deep Research (openai.com) | FAI.md | Primary |
| PRISMA 2020 (BMJ / EQUATOR) | OP MS 1.3F.md | Primary |
| ACM / ACL peer-reviewed papers | DPS.md, OP MS 1.3F.md | Primary |
| Accenture job postings | FAI.md, OP MS 1.3F.md, Q.md | Primary |
| Codecentric DuckDB/Polars/pandas benchmark | C.md, DPS.md, Q.md | Secondary |

### Most-cited secondary sources (appearing across multiple documents)

| Source | Documents | Classification |
|--------|-----------|----------------|
| Codecentric benchmark | C.md, DPS.md, Q.md | Secondary |
| MotherDuck blog comparisons | C.md, OP MS 1.3F.md | Secondary |
| Wikipedia (DuckDB, Polars, Project Jupyter, MotherDuck) | C.md, FAI.md | Secondary |
| Basedash — BI tool comparisons | C.md | Secondary |
| TechCrunch | FAI.md, OP MS 1.3F.md | Secondary |

### Source quality by document (ranked best to weakest)

| Rank | Document | % Primary | Note |
|------|----------|-----------|------|
| 1 | G2.md | 100% | All 5 citations are primary (W3C standards, Zenodo, peer-reviewed journal) |
| 2 | G3.md | 100% | All 4 citations are primary (nanopub project, academic surveys) |
| 3 | G1.md | 100% | All 2 citations are primary (official nanopub guidelines) |
| 4 | CP L6.md | 100% | All 10 citations are primary (Google, Snowflake, Databricks, dbt official docs) |
| 5 | DC L5.6.md | 100% | All 21 citations are primary (W3C, BLS, NIST, official tool docs) |
| 6 | DPS.md | ~77% | 20/26 primary; secondary for benchmarks and market reports |
| 7 | OP MS 1.3F.md | ~60% | Strong primary anchors (SIGMOD, W3C, PRISMA, arXiv); secondary for role framing and BI comparisons |
| 8 | FAI.md | ~53% | 18/34 primary; good mix, uses evidence tags |
| 9 | G0.md | ~67% | 8/12 primary (counting mixed entries partially); secondary for DuckLake blog and role comparisons |
| 10 | ANT GP H.md | ~25% | Light citations overall; relies on vendor/blog sources |
| 11 | Q.md | 40% | 4/10 primary; newer topic area with limited primary sources |
| 12 | C.md | ~4% | 2/54 primary; most heavily secondary document in the corpus |

---

## Key Findings

1. **Standards are well-covered.** W3C PROV (primary) appears across 5 documents; PRISMA 2020 appears in OP MS 1.3F.md with full BMJ/EQUATOR references. These are the most reliably grounded citations in the corpus.

2. **Tool documentation is strong.** dbt, DuckDB, Polars, pandas, and LangGraph are consistently cited from their official primary sources. Claims about these tools' capabilities are well-grounded.

3. **Role/market-position claims are the weakest.** Role definitions rely heavily on secondary sources (career blogs, comparison guides, aggregator sites). The most credible role evidence comes from actual first-party job postings (Accenture, The Hartford, LinkedIn), which appear in DPS.md, FAI.md, OP MS 1.3F.md, and Q.md.

4. **BI tool comparisons are structurally secondary.** Every document acknowledges that Metabase vs. Superset comparisons come from vendor marketing or third-party blogs, not independent audits.

5. **C.md requires caution.** With ~96% secondary sources, it is the weakest evidential document. It self-identifies several claims as "reported signal" and flags the companies lens as under-covered. It should not be used as the sole basis for any factual claim.

6. **G1.md, G2.md, G3.md are the strongest specialized references.** These focused technical notes on nanopublications and PROV-K cite only primary sources and provide the most rigorous grounding for the provenance lens.

7. **Academic papers are sparse but high-value.** Only a handful of documents cite peer-reviewed papers (ACM, ACL, Springer, arXiv, ORNL, IJDL), but where present they provide the strongest independent evidence, particularly for extraction pipelines (SciGraph-LLM in DPS.md), agent failures (DeepHalluBench/PING in OP MS 1.3F.md), and provenance ontologies (PROV-K in G2.md/G3.md).
