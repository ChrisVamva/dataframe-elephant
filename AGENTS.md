# AGENTS.md — dataframe-elephant

Data-research workspace: Markdown corpus in `research/raw/` → DuckDB citation intelligence in `data/` → follow-up agenda in `research/processed/`, plus an encrypted-archive (ECA) pipeline. Core logic in `src/*_core.py`, thin CLIs in `scripts/`.

## Interpreter (Windows)

- Plain `python` may resolve to a system 3.13 without deps (verified: no `duckdb`). Use the repo venv:
  `.\.venv\Scripts\python.exe -m pytest src/tests -q`
  `.\.venv\Scripts\python.exe src/ingest_citations.py`
- If deps missing: `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` (`duckdb`, `pytest`, `hypothesis`, `cryptography`).
- `data/README.md` mentions a `datascience` conda env, but the verified working interpreter here is `.venv`; prefer whichever env imports `duckdb`.

## Commands (run from repo root; `pytest.ini` sets `pythonpath=.`)

- All tests: `.\.venv\Scripts\python.exe -m pytest src/tests -q`
- Single file: `.\.venv\Scripts\python.exe -m pytest src/tests/test_ingest_citations.py -q`
- Rebuild citation DB (defaults: `research/raw` → `data/citations.duckdb` + `data/citation_ingestion_warnings.jsonl` via `schemas/citations.sql`):
  `.\.venv\Scripts\python.exe src/ingest_citations.py [--raw-dir PATH --database PATH --warnings PATH --schema PATH]`
- Archive dry-run first (safe): `.\.venv\Scripts\python.exe scripts/archive_stage1.py --dry-run`
- Follow-ups: `.\.venv\Scripts\python.exe scripts/formulate_research_questions.py [--stage2-dir PATH --database PATH --output-dir PATH]`
- Restore/inspect: `.\.venv\Scripts\python.exe scripts/restore_archive.py --archive <file.tar.gz.enc> --list` (add `--dest DIR [--overwrite]` to extract)

## Gotchas that will bite

- `scripts/archive_stage1.py` **deletes source `.md` files after a verified roundtrip** unless `--keep-originals` or `--dry-run`. Never run it against real data without one of those flags first.
- Archive passphrase order: `--passphrase` flag → `$ARCHIVE_PASSPHRASE` env → `.env` file (`ARCHIVE_PASSPHRASE=...`, gitignored, never commit) → interactive prompt. `restore_archive.py` prompts once (no confirm); `archive_stage1.py` prompts twice.
- ECA key derivation is PBKDF2-HMAC-SHA256 at 600k iterations — archive/encrypt tests are slow; the hypothesis roundtrip tests (`test_archive_roundtrip.py`, `test_ingest_citations.py` Wave 6) are the expensive suite.
- `src/ingest_citations.py:build_database` writes via temp file + atomic replace, carries forward unchanged files by SHA-256 cache, and derives `run_id` from content — identical corpus ⇒ identical `run_id`. A broken schema leaves the existing DB untouched (rollback test covers this).
- Parser does **no fuzzy matching by design**: publisher-only URLs, multi-URL cells, truncated URLs, and unmapped classifications produce `unresolved`/`ambiguous` rows + `ingestion_warning` entries, not sources. Claim tables require `claim` + `claim type` + `confidence` columns or they are skipped with an `unsupported_table_shape` warning. Do not infer claim links from prose.
- `First-Ratings.md` is classified `internal_evaluation` and excluded from external recurrence/claims. `source.status`/`directness` stay `NULL` (not `"unknown"`) when unrecorded — preserve that distinction.
- `build_database` also ingests `analysis/**/*.md` when `raw_dir` is under repo root (see `ROOT`-relative `candidate_roots`); tests monkeypatch `ingest_citations.ROOT` to isolate this.
- `schemas/*.sql` and `analysis/*.sql` are **DuckDB dialect** (`CREATE OR REPLACE VIEW`, `FILTER (WHERE ...)`, `ADD COLUMN IF NOT EXISTS`) — don't "fix" to T-SQL. `.vscode/settings.json` already disables the mssql T-SQL checker for these paths.
- Derived artifacts `*.duckdb`, `*.jsonl`, `.env` are gitignored; don't commit `data/citations.duckdb` or passphrases.
