---
modified: 2026-10-01T15:00:00+03:00
---

# No More Code Reliance on Irrelevant Directories and Files

## Status

**Mandatory for every person, agent, or automation that edits prompts, protocols, commands, or research artifacts in `dataframe-elephant`. This document is the recurrence-prevention contract for obsolete directories and files. The design rationale lives in this file; the enforcement is through manual review and automated tests.

## 1. What "irrelevant directories and files" mean here

The project has purged several directories and files that are no longer part of the active architecture:

- **`analysis/`** – Retired; citation ingestion no longer scans it; all references migrated to DuckDB queries.
- **`prompts/`** – Retired; template library moved to `src/prompt_templates/`; CLI tools now in `scripts/assemble_prompt.py`.
- **`scratch/`** – Development leftovers (`build_stage2.py`, `check_parser.py`, `extract.py`, `extracted.json`); should be audited for useful logic.
- **`State changes/`** — Was binary docs; user deleted them. Directory is now empty except `Archive/`.
- **`.deepeval/`** – Empty directory not mentioned in documentation; should be deleted.

## 2. The failures we refuse to repeat

| # | Failure that actually happened | Where it is recorded | Cost |
|---|------------------------------|----------------------|------|
| F1 | **Stale references to obsolete directories** — README.md, 1102026Report.md, data/README.md, and former `CommanderDeck/prompts/` paths still point to missing `analysis/` and `prompts/` directories. | AGENTS.md, README.md, 1102026Report.md | New agents wasted time on dead paths; false assumptions about codebase layout. |
| F2 | **Mixed documentation paths** — AGENTS.md and the report cite non‑existent `analysis/` and `prompts/` while the working code lives in `src/` and `scripts/`. | AGENTS.md, 1102026Report.md | Inconsistent onboarding experience. |
| F3 | **External file reliance** — Binary files in `State changes/` rely on foreign format conversion; they cannot be diffed, versioned, or parsed by automation. | `State changes/` directory | Human‑only workflow, loss of reproducibility. |

## 3. Standing rules (the contract)

Each rule names what it prevents and how it is enforced.

**R1 — No reliance on `analysis/`.** Evidence extraction, claim linking, and research scanning live only in `src/ingest_citations.py` and DuckDB queries. Never copy or reference files in `analysis/` (including `citation_evaluator.sql`). Prevents: F1, F2. Enforced by: manual verification in `AGENTS.md` and 1102026Report.md updates.

**R2 — No reliance on `prompts/`.** Prompt templates live in `src/prompt_templates/`; the assembler is `scripts/assemble_prompt.py`. Never reference the retired `prompts/` directory. Prevents: F1, F2. Enforced by: manual verification in `AGENTS.md` and 1102026Report.md updates.

**R3 — `scratch/` is not a production zone.** Files in `scratch/` (`build_stage2.py`, `check_parser.py`, `extract.py`, `extracted.json`) are development leftovers; they must be reviewed for useful logic and moved to `src/` or `scripts/` if kept. Prevents: F1. Enforced by: manual audit before commit.

**R4 — No binary files in `State changes/`.** Only markdown‑based state changes are allowed. Binary files (`Νέο Έγγραفو du Microsoft Word.docx`, `State3092026.odt`) must be converted to markdown or removed. Prevents: F3. Enforced by: file‑type check on `State changes/` before merge.

**R5 — No undocumented or empty directories.** `.deepeval/` is empty and documented; it was removed. All directories referenced in documentation must be present and contain at least one non‑empty file or a README explaining purpose. Prevents: F2. Enforced by: `git status` + doc scan.
**R6 — `Rules and Regulations/Commander Deck` is notes only, never a code dependency.** The Commander Deck directory contains user notes, plans, and reference artifacts. No code (`src/`, `scripts/`) shall import, parse, or depend on files in `Rules and Regulations/Commander Deck`. Notes are for human reference; code reads only canonical sources (`src/`, `scripts/`, `schemas/`, `research/`). Prevents: notes accidentally becoming code dependencies. Enforced by: path scan of imports in `src/` and `scripts/` before merge.
## 4. The working loop (every session)

1. **Edit the source.** Never add new references to `analysis/`, `prompts/`, `scratch/` (except for cleanup/audit), `State changes/` (binary), or `.deepeval/` (empty). Change `AGENTS.md`, README.md, and 1102026Report.md to reflect the live layout.
2. **Remove obsolete artifacts.** Before commit, ensure no references to `analysis/`, `prompts/`, `scratch/`, binary files in `State changes/`, or `.deepeval/` exist anywhere in the codebase.
3. **Run verification.** Manual check of `AGENTS.md` against actual file tree; `grep -R "analysis/" .; grep -R "prompts/" .; grep -R "State changes/.*\.docx" .; grep -R "State changes/.*\.odt" .; ls .deepeval 2>/dev/null || echo "OK"`
4. **Update contract documentation.** When a rule is breached, edit this document first, then mirror into `src/prompt_templates/lib/verification.md` (if applicable) and run tests.

## 5. When a check fails — smallest correct fix

| Failure | Meaning | Fix |
|---|---|---|
| `grep reports "analysis/"` found | Reference to retired directory | Remove reference from documentation and code |
| `grep reports "prompts/"` found | Reference to retired directory | Remove reference from documentation and code |
| Binary file in `State changes/` | Incompatible format | Convert to markdown or move to appropriate location |
| `.deepeval/` directory exists | Empty undocumented directory | Delete it |
| References in `scratch/` | Development leftovers | Audit files: move useful logic to `src/` or `scripts/`; delete rest |

Never make a failure green by weakening the check.

## 6. Update triggers

Revise this document when:
- Any of the directories or files listed above are referenced in a new location.
- A rule here is violated (i.e., we need to re‑evaluate after a breach).
- The architecture changes to include new long‑term directories that should not be deleted (e.g., `Protocols/`, `research/`, `schemas/`).

Preserve the existing rule IDs when appending — the standing R‑numbers are cited from this file, the documentation, and any automated checks.

## 7. Final principle

> The standard is not that nothing ever changes. The standard is that a later agent can open this workspace and find **one source of truth for every rule**, **one copy of every reusable block**, **prompts that are assembled instead of copied**, **and a green test suite that proves it**. The same goes for directory and file references — only the current, live, and referenced directories and files should appear in documentation and code.

## 8. References

- AGENTS.md — Current architecture overview
- 1102026Report.md — Project State Evaluation Report
- src/ingest_citations.py — Current claim extraction logic
- scripts/assemble_prompt.py — Current prompt assembly CLI
- `State changes/` directory — Only markdown‑based files should exist
- `scratch/` directory — Development leftovers (audit in progress)

*Report generated: October 11, 2026*