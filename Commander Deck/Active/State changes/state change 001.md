---
modified: 2026-09-27T21:46:27+03:00
---
## What changed

### `test_ingest_citations.py` — 8 new tests

**Wave 5 (Integration):** `test_incremental_cache_reprocesses_only_changed_files` — mutates one file in a two-doc corpus and verifies the second run picks up the change while carrying the unchanged file forward from cache.

**Wave 6 (Property-based):** 7 Hypothesis tests covering `normalize_url` (no-raise, idempotent), `stable_id` (deterministic, kind-scoped), `_classify_evidence_tier` (closed enum), `_classify_domain` (closed enum), and `parse_markdown_tables` (heading substring invariant).

### `ingest_citations.py` — real bug fixed

Hypothesis found that `normalize_url("[")` raised `ValueError: Invalid IPv6 URL` from `urlsplit`. Fixed by wrapping `urlsplit` in `try/except ValueError → return None`, consistent with how other malformed inputs are handled.

---

**Result: 25/25 tests pass** (was 17 before this session).