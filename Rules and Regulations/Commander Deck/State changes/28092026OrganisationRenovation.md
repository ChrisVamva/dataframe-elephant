---
date: 2026-09-28
author: GitHub Copilot
type: state_change_report
plan: Rules and Regulations/Commander Deck/Plans/CommanderPlan.md
phases: 0-2
---

# State Change: Rules and Regulations Index and Path Repair

## Scope

Implemented the initial, non-destructive slice authorized by the workspace
maintainer's instruction to start the Commander Plan. The governing protocol
is [OrganisationSpaceRules.md](../../Protocols/OrganisationSpaceRules.md); the
plan and current index are [CommanderPlan.md](../Plans/CommanderPlan.md) and
the [Rules and Regulations index](../../README.md).

## Changes

- Accepted `OrganisationSpaceRules.md` for the governance-space renovation.
- Created `Rules and Regulations/README.md` with a navigation map, source
  ownership summary, status limitations, and a 2026-09-28 inventory.
- Updated CommanderPlan to record authorization and completion of Phases 0-2.
- Replaced stale root-relative `Protocols/...` references in maintained
  prompt documentation, partials, and templates with canonical
  `Rules and Regulations/Protocols/...` paths.
- Regenerated `prompts/dispatch/2026-09-28_research_brief.md` from the
  `research_brief` template; no generated dispatch was hand-edited.

## Preservation and Limits

- No folders or files were moved or renamed.
- No historical state-change report was edited.
- The ECA archive payload and manifest were left unchanged; the encrypted
  payload was not decrypted.
- Legacy owner/status questions remain flagged for review in the root index.
- The reader-task pilot and plan closeout remain outstanding.

## Validation

| Check | Result |
| --- | --- |
| `test_r4_all_referenced_paths_exist` | Pass |
| Full suite: `\.venv\Scripts\python.exe -m pytest src/tests -q` | 68 passed |
| Editor diagnostics for changed governance documents | No errors reported |