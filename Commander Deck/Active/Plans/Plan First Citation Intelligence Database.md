---
modified: 2026-09-27T17:35:41+03:00
---
## Plan: First Citation Intelligence Database

  

Build a reproducible first DuckDB database from the research citation corpus. Use it to answer three initial questions: which sources recur, which recurring sources have stronger evidence characteristics, and where a research agent should investigate next. Start with deterministic citation/source ingestion and explicit provenance; defer probabilistic claim extraction and agent orchestration until the evidence mappings are reliable.

  

**Steps**

  

### Phase 1: Define the local data contract

  

1. Reuse the citation and evidence concepts already established in `Protocols/Research-Evaluation.md`: primary/secondary/internal evidence class, documented fact/reported signal/inference/recommendation claim type, high/medium/low confidence, source limitations, and falsifiers.

2. Use `research/raw/Citations/Citation.md`, `research/raw/Citations/Report.md`, the structured source register in `research/raw/CNE DPS 4.1 F.md`, and the explicit source table in `research/raw/CP L6.md` as seed inputs.

3. Define stable identifiers and preserve the original text. Normalize URLs and source aliases separately; never merge ambiguous citations silently.

4. Add a reproducible snapshot policy: record database build date, input file paths, file hashes or modification metadata, parser version, and ingestion warnings.

  

### Phase 2: Implement the first database schema

  

5. Create a DuckDB-compatible schema in `schemas/citations.sql` with these core tables:

   - `research_document`: stable document ID, path, title, document type, evaluation date, evaluation decision, and quality rating.

   - `source`: canonical source ID, URL, title, publisher, author, source type, evidence class, publication/access dates, status, bias notes, and metadata notes.

   - `citation_occurrence`: local citation label, raw citation text, source ID, document ID, locator, recorded classification, and extraction method.

   - `source_alias`: source aliases and normalization notes.

   - `claim`: only explicitly represented claims from existing documents at first, with claim type, confidence, workflow stage, falsifier, and validity dates.

   - `claim_source`: supports/conflicts/contextualizes relationship, evidence locator or quote/span, and independence group.

6. Add derived views for `source_recurrence`, `source_reputation`, `document_citation_coverage`, `source_conflicts`, and `next_research_candidates`. Keep recurrence, authority, directness, freshness, independence, and limitations as separate dimensions; do not collapse them into an ungrounded single “reputation” score.

7. Add integrity constraints or validation queries for unique IDs, valid evidence classes, valid claim types/confidence levels, resolvable foreign keys, and no duplicate occurrence IDs.

  

### Phase 3: Add deterministic ingestion

  

8. Create `src/ingest_citations.py` using Python and DuckDB. Parse Markdown tables and known source-register formats first; preserve raw rows and source references even when parsing is incomplete.

9. Create a small normalization module or functions for canonical URL cleanup, source-type classification, date parsing, and alias matching. Use deterministic URL matching first and place fuzzy matches into a review queue rather than auto-merging them.

10. Ingest every Markdown document under `research/raw/` as a `research_document`, including `Citations/Citation.md`, `Citations/Report.md`, and `First-Ratings.md` only if the database contract explicitly marks it as an internal evaluation artifact rather than substantive source evidence.

11. Ingest structured citations from the citation registry and source tables. Capture inline labels where they can be unambiguously associated with a local source. Mark grouped source lists as source-level evidence, not claim-level evidence.

12. Write `data/citation_ingestion_warnings.jsonl` or an equivalent warning artifact for truncated URLs, missing titles, unresolved aliases, duplicate candidates, unsupported table shapes, and source rows lacking direct URLs.

13. Write `data/citations.duckdb` as the reproducible local database. Do not overwrite raw research documents.

  

### Phase 4: Provide evaluator queries and tests

  

14. Create `analysis/citation_evaluator.sql` with documented queries for:

   - most frequently recurring sources by distinct documents and total occurrences;

   - recurring sources filtered by primary or official evidence class;

   - repeated sources grouped by independence group;

   - sources with missing metadata, stale/unknown status, or weak source classification;

   - documents with citations but low claim-level coverage;

   - low-confidence claims, claims lacking sources, and claims relying only on secondary evidence;

   - recommended next research areas grouped by workflow stage, claim type, confidence, and missing primary evidence.

15. Create focused tests under `src/tests/` or an equivalent test location for URL normalization, deterministic IDs, citation table parsing, source alias preservation, idempotent reloads, and schema invariants.

16. Add a small README section or `data/README.md` explaining setup, database build command, snapshot semantics, and the difference between recurrence and reputation.

  

### Phase 5: Install and verify locally

  

17. Add the minimal dependency manifest, preferably `requirements.txt` or `pyproject.toml`, with `duckdb` and the project’s chosen test dependency. Add Markdown/date/fuzzy packages only if the parser actually needs them.

18. Create or use a project-local Python environment, install dependencies, run the ingestion from a clean database, and run the focused tests.

19. Verify with DuckDB queries that the database is non-empty, all source occurrences retain their originating documents, reloads are idempotent, unresolved records are visible, and evaluator queries return interpretable results.

20. Perform a manual review of a sample from `CP L6.md`, `CNE DPS 4.1 F.md`, and the citation registries against the loaded rows. Record known limitations and the next ingestion improvement.

  

**Relevant files**

  

- `c:\Users\user\dataframe-elephant\Protocols\Research-Evaluation.md` — governing quality, evidence, confidence, and falsifier rules.

- `c:\Users\user\dataframe-elephant\research\raw\Citations\Citation.md` — current citation inventory and broad classifications.

- `c:\Users\user\dataframe-elephant\research\raw\Citations\Report.md` — source-quality summaries and known classification limitations.

- `c:\Users\user\dataframe-elephant\research\raw\CNE DPS 4.1 F.md` — strongest existing source register, canonical names, claim model, predicates, and DuckDB handoff.

- `c:\Users\user\dataframe-elephant\research\raw\CP L6.md` — clean structured source-table example.

- `c:\Users\user\dataframe-elephant\research\raw\First-Ratings.md` — document-level decisions and evidence gaps to carry into metadata and warnings.

- `c:\Users\user\dataframe-elephant\schemas\citations.sql` — new relational schema and derived views.

- `c:\Users\user\dataframe-elephant\src\ingest_citations.py` — new deterministic ingestion entry point.

- `c:\Users\user\dataframe-elephant\analysis\citation_evaluator.sql` — evaluator-facing query set.

- `c:\Users\user\dataframe-elephant\data\citations.duckdb` — generated first database artifact.

  

**Verification**

  

1. Build from a clean database twice and confirm stable row counts and IDs.

2. Run parser and normalization tests, including malformed/truncated references and duplicate aliases.

3. Query recurrence separately from evidence class and independence; confirm a frequently repeated secondary source is not automatically ranked as reputable.

4. Query claims with low confidence, missing source mappings, or no primary evidence and confirm they produce next-research candidates.

5. Validate foreign keys and allowed enum values through DuckDB checks.

6. Spot-check loaded rows against the original Markdown tables and confirm raw citation text and source document provenance are preserved.

7. Run the full test suite and report any pre-existing failures separately from database work.

  

**Decisions**

  

- Use a local single-file DuckDB database first; no server, dbt, graph database, vector database, or LLM framework is required for the initial version.

- Use Python for ingestion and tests because the repository has no existing runtime or dependency conventions.

- Treat “reputable” as a queryable profile of authority, evidence class, directness, independence, recency, recurrence, and limitations rather than a single opaque score.

- Keep the first implementation deterministic and auditable. Do not infer claim-source mappings from prose when the raw documents do not provide explicit evidence spans.

- Preserve unresolved and ambiguous records for review instead of guessing canonical identity.

- Scope the first version to citation/source intelligence and evaluator queries; agent prompting and automated research routing are a follow-up layer built on the database outputs.

  

**Further Considerations**

  

1. Recommended default: create a local project environment and dependency manifest rather than installing DuckDB globally, so the database build is reproducible.

2. The first database can include `First-Ratings.md` as an internal evaluation artifact, but its citations must not be counted as independent external evidence; the schema should preserve that distinction.

3. A later iteration can add source snapshots, exact evidence spans, document versioning, and agent research tasks after the deterministic seed load is validated.