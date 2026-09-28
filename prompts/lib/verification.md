<!-- prompts/lib/verification.md — THE single copy of verification commands under
     prompts/. Every command here must appear verbatim in AGENTS.md; if a command
     changes, change AGENTS.md first, then here. Run from the repo root. -->

```powershell
.\.venv\Scripts\python.exe -m pytest src/tests -q
```

After any write-back into Stage 2 or the citation corpus:

```powershell
.\.venv\Scripts\python.exe scripts/import_stage2.py
.\.venv\Scripts\python.exe src/ingest_citations.py
```

Regenerate the follow-up agenda after gap-producing changes:

```powershell
.\.venv\Scripts\python.exe scripts/formulate_research_questions.py
```

Archive safety — dry-run first; the archiver deletes source `.md` files after a
verified roundtrip unless `--keep-originals` or `--dry-run` is given:

```powershell
.\.venv\Scripts\python.exe scripts/archive_stage1.py --dry-run
```

Do not hand-edit these commands; a lint test fails when they drift from
`AGENTS.md`.
