---
modified: 2026-09-27T21:18:26+03:00
---
The spec is ready for implementation. The task waves in dependency order:

- Wave 0 — Schema DDL additions + `hypothesis` dependency (unblock everything)
- Wave 1 — `_classify_domain`, `_classify_evidence_tier`, `_load_file_cache` (three independent pure functions, parallelisable)
- Wave 2 — Their unit tests + integrate classifiers into `_source_row_data`
- Wave 3 — `_copy_unchanged_rows`
- Wave 4 — Wire incremental cache into `build_database` + create hook file (independent of each other)
- Waves 5–6 — Integration tests and all 7 property-based tests