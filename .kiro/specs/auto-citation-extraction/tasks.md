# Implementation Plan: auto-citation-extraction

## Overview

Implement hook-based auto-triggering, an incremental file cache, and domain/evidence classifiers for the citation ingestion pipeline. Work proceeds in dependency order: schema DDL first, then pure classifier functions, then the cache layer, then integration into `build_database`, then the hook file, and finally tests.

## Tasks

- [x] 1. Extend schema DDL with new classifier columns
  - Add `domain_category VARCHAR NOT NULL DEFAULT 'uncategorised'` column to the `source` table `CREATE TABLE` block.
  - Add `evidence_tier VARCHAR NOT NULL DEFAULT 'unclassified'` column to the `citation_occurrence` table `CREATE TABLE` block.
  - Add `ALTER TABLE source ADD COLUMN IF NOT EXISTS domain_category VARCHAR NOT NULL DEFAULT 'uncategorised';` immediately after the `source` `CREATE TABLE` block.
  - Add `ALTER TABLE citation_occurrence ADD COLUMN IF NOT EXISTS evidence_tier VARCHAR NOT NULL DEFAULT 'unclassified';` immediately after the `citation_occurrence` `CREATE TABLE` block.
  - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.10_

- [x] 2. Add `hypothesis` dependency
  - Append `hypothesis>=6,<7` to `requirements.txt`.
  - _Requirements: Design — Testing Strategy (property-based tests)_

- [x] 3. Implement `_classify_domain` and classifier constants
  - [x] 3.1 Add `DOMAIN_CATEGORIES` frozenset and `_classify_domain` function to `src/ingest_citations.py`
    - Define `DOMAIN_CATEGORIES = frozenset({...})` with all eight values from the design.
    - Implement `_classify_domain(canonical_url, title, publisher) -> str` applying host-level and keyword rules in field-precedence order (canonical_url → publisher → title); return `'uncategorised'` when nothing matches.
    - _Requirements: 10.1, 10.2, 10.3, 10.12_
  - [ ]* 3.2 Write unit tests for `_classify_domain`
    - Verify `uncategorised` for all-null / all-empty inputs.
    - Verify each keyword/host rule fires correctly with one concrete example per rule (url-wins-over-title, publisher-wins-over-title).
    - _Requirements: 10.1, 10.2, 10.3, 10.12_

- [x] 4. Implement `_classify_evidence_tier`
  - [x] 4.1 Add `EVIDENCE_TIERS` frozenset and `_classify_evidence_tier` function to `src/ingest_citations.py`
    - Define `EVIDENCE_TIERS = frozenset({...})` with all four values.
    - Implement `_classify_evidence_tier(recorded_classification: str | None) -> str` using case-insensitive substring matches for `'primary'`, `'secondary'`, `'internal'`; return `'unclassified'` otherwise.
    - _Requirements: 10.4, 10.5, 10.6, 10.7, 10.8, 10.9_
  - [ ]* 4.2 Write unit tests for `_classify_evidence_tier`
    - Verify `unclassified` for `None` and empty string.
    - Verify `tier_1_primary` for `"Primary Evidence"`, `tier_2_secondary` for `"secondary"`, `tier_3_tertiary` for `"internal synthesis"`.
    - Verify case-insensitivity (mixed-case inputs).
    - _Requirements: 10.4, 10.5, 10.6, 10.7, 10.8, 10.9_

- [x] 5. Integrate classifiers into `_source_row_data`
  - Call `_classify_domain(canonical_url, title, publisher)` when building the `source` dict; add `domain_category` key.
  - Call `_classify_evidence_tier(classification)` when building the `occurrence` dict; add `evidence_tier` key.
  - _Requirements: 10.1, 10.4, 10.10_

- [x] 6. Implement `_load_file_cache`
  - [x] 6.1 Add `_load_file_cache(database_path: Path) -> dict[str, str]` to `src/ingest_citations.py`
    - ATTACH the existing database read-only (`ATTACH '...' AS prev (READ_ONLY)`).
    - Query the most recent `ingestion_run` row and its `ingestion_input` rows (`WHERE ir.built_at = (SELECT MAX(built_at) FROM ingestion_run)`).
    - Return `{path: sha256}` dict; catch all exceptions and return `{}` (covers missing file, schema mismatch, corrupt DB).
    - _Requirements: 9.1, 9.7_
  - [ ]* 6.2 Write unit tests for `_load_file_cache`
    - Test missing database path → returns `{}`.
    - Test path pointing to a freshly-created DB with no `ingestion_run` rows → returns `{}`.
    - Test path pointing to a populated DB from a prior `build_database` run → returns correct `{path: sha256}` dict.
    - _Requirements: 9.1, 9.7_

- [x] 7. Implement `_copy_unchanged_rows`
  - Add `_copy_unchanged_rows(connection, old_db_path, unchanged_paths, run_id, source_records, warnings)` to `src/ingest_citations.py`.
  - ATTACH old database once read-only; SELECT rows for `unchanged_paths` from `research_document`, `citation_occurrence`, `source_alias`, `claim`, `claim_source`, and `ingestion_warning` into Python lists; SELECT `source` rows and feed through `_merge_source_metadata` into the shared `source_records` dict; DETACH.
  - Return `(document_rows, occurrence_rows, alias_rows, claim_rows, claim_source_rows)` without inserting.
  - Include `domain_category` in `source` SELECT and `evidence_tier` in `citation_occurrence` SELECT so carried-forward values are preserved.
  - _Requirements: 9.2, 9.3, 9.8, 9.9, 10.11_

- [x] 8. Integrate incremental cache into `build_database`
  - At the start of `build_database` (after snapshot computation), call `_load_file_cache(database_path)` to get `file_cache`.
  - Partition snapshots into `unchanged_paths` (path and sha256 both match cache) and `changed_snapshots` (all others).
  - After opening the temp connection and executing schema DDL, call `_copy_unchanged_rows` with `unchanged_paths`; extend the appropriate row lists with returned rows.
  - Parse only `changed_snapshots` in the existing per-file loop.
  - Keep the merge, transaction, rename, and warning-write steps unchanged.
  - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9_

- [x] 9. Checkpoint — Verify existing tests still pass
  - Ensure all tests pass, ask the user if questions arise.

- [x] 10. Create hook file
  - Create `.kiro/hooks/ingest-citations.json` with two hook entries: one for `PostFileSave` and one for `PostFileCreate`.
  - Both entries use `matcher: "research/raw/.*\\.md"` and invoke `.venv/Scripts/python src/ingest_citations.py --raw-dir research/raw --database data/citations.duckdb --warnings data/citation_ingestion_warnings.jsonl --schema schemas/citations.sql`.
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 8.1, 8.2, 8.3, 8.4_

- [x] 11. Write unit tests for new components
  - [x] 11.1 Test incremental cache produces same result as full rebuild
    - Build on a two-file corpus; run again with the first run's database; assert all content table row counts and IDs match.
    - _Requirements: 9.6, 3.1, 3.2_
  - [x] 11.2 Test schema migration is idempotent
    - Execute `citations.sql` DDL twice on the same DuckDB connection; assert no exception is raised and `domain_category` / `evidence_tier` columns exist with correct defaults.
    - _Requirements: 10.10_
  - [x] 11.3 Test `domain_category` and `evidence_tier` columns are populated after `build_database`
    - Run `build_database` on a minimal corpus; query `source.domain_category` and `citation_occurrence.evidence_tier`; assert both are non-null and within their respective enumerations.
    - _Requirements: 10.1, 10.4, 10.10_

- [ ] 12. Write property-based tests
  - [-]* 12.1 Property 1 — Incremental build equals full rebuild
    - Use `hypothesis` to generate random 2–10-file Markdown corpora; run `build_database` twice (second run with first run's DB); compare row sets across all content tables and return-dict counts.
    - **Property 1: Incremental build equals full rebuild**
    - **Validates: Requirements 3.1, 3.2, 3.3, 3.6, 9.6**
  - [-]* 12.2 Property 2 — Incremental build reflects changed files
    - Generate a corpus, run once, mutate one file's source table, run again; assert mutated file rows changed and unmodified file rows are identical.
    - **Property 2: Incremental build reflects changed files**
    - **Validates: Requirements 9.2, 9.3, 9.5**
  - [-]* 12.3 Property 3 — `domain_category` is always a valid enumeration value
    - Generate random `(canonical_url, title, publisher)` triples using `hypothesis.strategies`; call `_classify_domain`; assert result is in `DOMAIN_CATEGORIES`.
    - **Property 3: domain_category is always a valid enumeration value**
    - **Validates: Requirements 10.1, 10.2, 10.3**
  - [-]* 12.4 Property 4 — `evidence_tier` is always a valid enumeration value
    - Generate random strings (including `None`, empty, and strings with keyword substrings at arbitrary positions and capitalizations); call `_classify_evidence_tier`; assert result is in `EVIDENCE_TIERS`.
    - **Property 4: evidence_tier is always a valid enumeration value**
    - **Validates: Requirements 10.4, 10.5, 10.6, 10.7, 10.8, 10.9**
  - [ ]* 12.5 Property 5 — `domain_category` precedence is respected
    - Generate inputs where `canonical_url` contains a `technical_standard` keyword and `title` contains an `ai_ml_technology` keyword; assert `_classify_domain` returns `'technical_standard'`.
    - **Property 5: domain_category precedence is respected**
    - **Validates: Requirements 10.12**
  - [ ]* 12.6 Property 6 — One alias per occurrence
    - Generate random corpora; run `build_database`; assert `COUNT(source_alias) == COUNT(citation_occurrence)` and every `occurrence_id` has exactly one alias row.
    - **Property 6: one alias per occurrence**
    - **Validates: Requirements 7.5**
  - [ ]* 12.7 Property 7 — Classification conflict warning on cross-run source merge
    - Construct two files sharing a canonical URL with differing non-null `evidence_class` values; run once (both files), change one file's classification, run again with cache; assert `evidence_class IS NULL` on merged source and `classification_conflict` warning present.
    - **Property 7: classification_conflict warning fires on cross-run source merge**
    - **Validates: Requirements 9.8**

- [~] 13. Final checkpoint — Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for a faster MVP.
- Each task references specific requirements for traceability.
- Checkpoints at tasks 9 and 13 ensure incremental validation.
- Property tests are annotated with their property number and validating requirements clauses.
- Unit tests and property tests are complementary — unit tests cover concrete examples, property tests cover universal invariants.
- The hook file (task 10) can be created independently of the Python changes (tasks 3–8).
- Tasks 3.1 and 4.1 (pure functions) have no dependencies on each other and can be implemented in parallel.

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1", "2"] },
    { "id": 1, "tasks": ["3.1", "4.1", "6.1"] },
    { "id": 2, "tasks": ["3.2", "4.2", "5", "6.2"] },
    { "id": 3, "tasks": ["7"] },
    { "id": 4, "tasks": ["8", "10"] },
    { "id": 5, "tasks": ["11.1", "11.2", "11.3", "12.3", "12.4", "12.5"] },
    { "id": 6, "tasks": ["12.1", "12.2", "12.6", "12.7"] }
  ]
}
```
