# `prompts/dispatch/` — generated session prompts

Session prompts are **assembled**, not hand-copied: a template from
`prompts/templates/` plus current dispatch data (RQ tables, scores, batch
membership from `research/processed/FollowUps/ResearchAgenda.md`).

```powershell
.\.venv\Scripts\python.exe scripts/assemble_prompt.py --template followup_dispatch --out prompts/dispatch/2026-09-28_wave2.md
```

Add `--var NAME=VALUE` (repeatable) or `--context FILE.json` to fill
`{{NAME}}` placeholders; includes are always resolved.

Rules:

- Files in this directory are regenerable artifacts (gitignored) — never the
  source of truth. If a dispatch file disagrees with `ResearchAgenda.md`, the
  agenda wins; regenerate.
- Record which agenda snapshot a session used in your report, not in a new
  prompt file.
