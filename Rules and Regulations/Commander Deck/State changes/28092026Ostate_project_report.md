---
date: 2026-09-28
author: Desktop Commander
type: state_change_report
target: Rules and Regulations/Commander Deck/State changes/28092026Ostate_project_report.md
scope: dataframe-elephant workspace
validation: 73 passed, 2 failed from repository root
---

# Current Project Report — 28 September 2026

## 1. Executive summary

`dataframe-elephant` is a Python-based research and citation-intelligence workspace. Its main flow is:

```text
research Markdown → citation ingestion → DuckDB sources of truth
                    ↓
              Stage 2 extraction → gap detection → follow-up research
```

The project also contains a prompt-library assembler/linter and an ECA
(encrypted-compression-archiving) pipeline for preserving historical research
and governance material.

The implementation is substantially operational: the repository-root test run
completed with **73 passing tests and 2 failing tests**. The failures are both
prompt-governance lint failures, not database, archive, or Stage 2 import
failures. The live result supersedes older dated notes reporting 67 or 68
passing tests.

## 2. Review basis

This report was prepared from the current workspace on 2026-09-28 by reviewing:

- `README.md`, `AGENTS.md`, and `implementation_plan.md`;
- the `Rules and Regulations/` index and governing protocols;
- source modules under `src/` and their tests under `src/tests/`;
- Stage 2 research files and follow-up agenda files;
- existing Commander Deck state-change reports;
- current Git status and the latest commit;
- a fresh full test run from the repository root.

No project files were changed during the review other than creating this report.

## 3. Current architecture

### Research and data pipeline

- `src/ingest_citations.py` parses Markdown source and claim tables, normalizes
  URLs, preserves unresolved or ambiguous citations, and builds
  `data/citations.duckdb` atomically.
- `src/stage2_import_core.py` imports the seven required Stage 2 Markdown files
  into the separate `data/stage2.duckdb` database after strict frontmatter gate
  checks.
- `src/followup_core.py` scans Stage 2 gaps and citation intelligence, assigns
  deterministic priority scores, and generates falsifiable research dossiers.
- `src/db_export_core.py` exports the two production databases to verified,
  timestamped CSV and Parquet bundles without treating exports as sources of
  truth.

### Prompt system

- `prompts/lib/` contains shared rule and content partials.
- `prompts/templates/` contains reusable research and follow-up prompt
  templates.
- `scripts/assemble_prompt.py` resolves includes and variables.
- `src/prompt_core.py` enforces lint rules R1–R5 for include resolution, gate
  naming, rule-block centralization, path references, and documented commands.

### Preservation and governance

- `src/archive_core.py` implements ECA-v1 using tar/gzip, AES-256-GCM, and
  PBKDF2-HMAC-SHA256.
- `Rules and Regulations/` is the governance source area; its `Protocols/`
  directory defines workflow requirements.
- `Commander Deck/State changes/` is historical evidence and must not be
  rewritten to match later state.
- The Commander Deck archive has a readable manifest and an encrypted payload.

## 4. Current repository state

- Latest commit: `5bac9c3` — `Reorganise workspace under Rules and Regulations, add export and prompt pipelines, add database quality report`.
- Working tree modification observed: `AGENTS.md` is modified.
- No source, database, archive, or historical report was modified for this
  review.
- The canonical Stage 2 input set is present:
  `Claims.md`, `Entities.md`, `ExtractionLog.md`, `Metrics.md`,
  `Predicates.md`, `Sources.md`, and `WorkflowMap.md`.
- Both production DuckDB files are present:
  `data/citations.duckdb` and `data/stage2.duckdb`.
- Follow-up outputs are present under `research/processed/FollowUps/`, including
  the master agenda and four Wave 2 thematic packs.
- The Commander Deck contains plans, problems, state history, and the ECA
  archive/manifest structure.

## 5. Validation result

The prescribed command was run from the repository root:

```powershell
.\.venv\Scripts\python.exe -m pytest src/tests -q
```

Result:

```text
73 passed, 2 failed in 9.15s
```

The first exploratory invocation was intentionally discarded because it ran
from the wrong working directory and produced path-resolution errors against
`C:\Windows\System32`. The repository-root result above is the authoritative
validation result for this report.

### Passing areas

The following areas passed their current tests:

- citation parsing, URL normalization, source resolution, warnings, and
  incremental ingestion;
- Stage 2 import, frontmatter gates, deterministic IDs, and gap views;
- DuckDB export inventory, restoration, fidelity checks, and view snapshots;
- follow-up gap scoring and research-agenda generation;
- archive encryption/decryption, integrity checks, and Commander Deck prefix
  and manifest exclusion behavior;
- most prompt assembly and lint behavior.

## 6. Open defects found

### R4 — stale prompt paths

Two prompt documents reference a directory that is not present:

1. `prompts/prompts/CheckpointAuthorityPrompts.md`
2. `prompts/README.md`

Both reference:

```text
Rules and Regulations/Commander Deck/prompts/
```

The current Commander Deck listing has no `prompts/` directory. The maintained
prompt assets live at repository-level `prompts/`, while the governance index
still describes the Commander Deck prompt area as historical/operational
pointers. The references need an explicit decision: restore the pointer folder,
change the references to the repository-level prompt library, or mark the old
location as historical without making it a live path.

### R5 — commands missing from AGENTS.md

Three prompt references use commands that the R5 checker cannot find verbatim
in `AGENTS.md`:

- `.venv\\Scripts\\python.exe scripts/formulate_research_questions.py`
- `.venv\\Scripts\\python.exe scripts/assemble_prompt.py`

The affected files are:

- `prompts/dispatch/2026-09-28_research_brief.md`;
- `prompts/dispatch/README.md`;
- `prompts/lib/verification.md`.

This is a documentation-contract mismatch. Either add the canonical commands
to `AGENTS.md`, or update the prompt references to match an already documented
command form. The command paths themselves correspond to real project tools.

## 7. Governance and process observations

- The organization renovation through Commander Plan Phases 0–2 is recorded as
  complete and was non-destructive.
- Remaining governance work is still documented: legacy owner/status review,
  reader-task pilot, and plan closeout.
- Existing historical reports contain stale test totals. They should remain
  unchanged as historical snapshots; this report provides the newer dated
  assessment.
- The project has strong safety controls around database replacement, archive
  deletion, source preservation, export verification, and uncertainty markers.
- The main current risk is not data loss but documentation drift: prompt path
  references and command examples have moved out of sync with the canonical
  layout and lint contract.

## 8. Recommended next actions

1. Resolve the two R4 path references according to the governance source of
   truth; do not recreate a directory merely to silence the test.
2. Align `AGENTS.md` and the three R5-affected prompt documents on the exact
   supported command forms.
3. Re-run the full suite from the repository root and require **75/75 passing**
   before closing this report's open defects.
4. Review the existing modified `AGENTS.md` deliberately before committing;
   determine whether it is the intended documentation update or unrelated work.
5. Continue the already documented reader-task pilot and legacy owner/status
   review before closing the Commander Plan.
6. Preserve this report as a dated snapshot; append a later state-change report
   rather than rewriting it after fixes.

## 9. Source references

- [Project README](../../../README.md)
- [Project operating instructions](../../../AGENTS.md)
- [Rules and Regulations index](../../README.md)
- [Research Evaluation protocol](../../Protocols/Research-Evaluation.md)
- [Stage 1 → Stage 2 protocol](../../Protocols/TransitionStage2.md)
- [Follow-up Research protocol](../../Protocols/FollowUpResearch.md)
- [Database Export protocol](../../Protocols/ExportDatabase.md)
- [Previous state report](28092026Report.md)
- [Organisation renovation record](28092026OrganisationRenovation.md)
