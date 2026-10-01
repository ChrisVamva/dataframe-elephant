---
status: current
scope: Rules and Regulations/ and all descendants
as_of: 2026-09-28
maintainer: workspace maintainer (personal name not recorded)
---

# Rules and Regulations

This directory contains the workspace's standing rules, repeatable protocols,
governance plans, issue records, change history, prompt pointers, and preserved
archive material. It is internal workspace governance, not a substitute for
external legal advice or records-retention requirements.

## Where Authority Lives

| Question | Source of truth |
| --- | --- |
| What are the cross-cutting workspace rules? | [MaintainingProsperity.md](Core%20Rules/MaintainingProsperity.md) |
| What procedure governs a workflow? | The accepted protocol in [Protocols/](Protocols/) for that workflow. |
| Is a proposed organization change approved? | The current plan's status and explicit approval record in [Commander Deck/Plans/](Commander%20Deck/Plans/). A plan does not silently amend a protocol. |
| Where are issues and change history? | [Commander Deck/Problems/](Commander%20Deck/Problems/) and [Commander Deck/State changes/](Commander%20Deck/State%20changes/). These are evidence/history, not standing rules. |
| Where are reusable prompt assets? | Prompt templates live in `src/prompt_templates/`; `src/prompt_core.py` lints them and `scripts/assemble_prompt.py` handles assembly. |
| How is archived material handled? | [Encryption-Compression-Archiving.md](Protocols/Encryption-Compression-Archiving.md) and the readable [Commander Deck archive manifest](Commander%20Deck/Archive/commander_deck_archive_20260928_122517_manifest.json). |

When sources conflict, follow the owning rule or protocol only when its scope
and status resolve the conflict. Otherwise record the conflict and request a
maintainer decision; do not treat a summary, plan, incident, or old report as
an amendment.

## Core Rules

| Document | Status | Scope |
| --- | --- | --- |
| [MaintainingProsperity.md](Core%20Rules/MaintainingProsperity.md) | Mandatory per document | Standing rules R1-R12 for prompts, protocols, commands, and research artifacts. |

## Protocols

| Document | Status | Scope |
| --- | --- | --- |
| [AuthorityDocumentCreation.md](Protocols/AuthorityDocumentCreation.md) | Mandatory per document | Creation and maintenance of folder-level authority documents. |
| [Encryption-Compression-Archiving.md](Protocols/Encryption-Compression-Archiving.md) | Mandatory per document | Lossless encrypted archive and restore workflow. |
| [ExportDatabase.md](Protocols/ExportDatabase.md) | Mandatory per export | Read-only CSV/Parquet export of the production DuckDB databases, with restoration and fidelity verification. |
| [FollowUpResearch.md](Protocols/FollowUpResearch.md) | Mandatory per document | Follow-up question formulation and prioritization. |
| [FromStagetoDatabases.md](Protocols/FromStagetoDatabases.md) | Mandatory per document | Stage 2 Markdown import into DuckDB. |
| [Hook-Based-Auto-Trigger-Extraction.md](Protocols/Hook-Based-Auto-Trigger-Extraction.md) | Governing protocol; metadata review needed | Hook-triggered and on-demand citation ingestion. |
| [Research-Evaluation.md](Protocols/Research-Evaluation.md) | Mandatory per document | Research evaluation, evidence, confidence, and review gates. |
| [TransitionStage2.md](Protocols/TransitionStage2.md) | Mandatory per document | Stage 1 to Stage 2 extraction. |
| [OrganisationSpaceRules.md](Protocols/OrganisationSpaceRules.md) | Accepted 2026-09-28 | Organization and maintenance of this governance space. |

## Commander Deck

| Area | Role and status |
| --- | --- |
| [Plans/](Commander%20Deck/Plans/) | Proposals, design rationale, and approved implementation plans. See the plan register below. |
| [Problems/](Commander%20Deck/Problems/) | Issue and review findings; check each finding's present resolution in its owning source. |
| [State changes/](Commander%20Deck/State%20changes/) | Dated history. Do not edit a past snapshot to make it match current state. |
| `src/prompt_templates/` | Prompt templates and shared `lib/` partials (lint rules live in `src/prompt_core.py`). |
| [Archive/](Commander%20Deck/Archive/) | ECA archive payload and readable manifest; the payload is not current guidance. |

### Plan Register

| Document | Status | Purpose / note |
| --- | --- | --- |
| [OptimalSPrompt.md](Commander%20Deck/Plans/OptimalSPrompt.md) | Plan; current status needs maintainer review | Prompt-system design rationale. Its references to a separate repository-level `prompts/` library are now stale; prompts live in `src/prompt_templates/`. |
| [ProcessEstablishment.md](Commander%20Deck/Plans/ProcessEstablishment.md) | Frontmatter says `active`; closure/status needs review | ECA application. The document records a verified archive run; current operation is governed by the ECA protocol. |
| [OrganisationPrinciplesAuthority.md](Commander%20Deck/Plans/OrganisationPrinciplesAuthority.md) | Draft | Provenance-linked synthesis of the four Obsidian examples and external guidance. |
| [CommanderPlan.md](Commander%20Deck/Plans/CommanderPlan.md) | In progress; initial no-move scope authorized | Implementation plan for this governance-space renovation. |
| [ExportPlan](Commander%20Deck/Plans/ExportPlan) | Implemented 2026-09-28 | Database export design (file has no extension). Execution is now governed by [Protocols/ExportDatabase.md](Protocols/ExportDatabase.md). |

## Current Source Inventory

Inventory snapshot: 2026-09-28. `Needs owner review` means the index does not
promote a legacy document to accepted/current status. Confirm status and
maintainer before relying on it as active policy.

| Path | Role | Status / disposition |
| --- | --- | --- |
| [README.md](README.md) | This index | Current navigation and source-of-truth inventory. |
| [Core Rules/MaintainingProsperity.md](Core%20Rules/MaintainingProsperity.md) | Standing cross-cutting rules | Mandatory per document; owner and scope as stated in file. |
| [Protocols/AuthorityDocumentCreation.md](Protocols/AuthorityDocumentCreation.md) | Authority-document procedure | Mandatory per document. |
| [Protocols/Encryption-Compression-Archiving.md](Protocols/Encryption-Compression-Archiving.md) | Archive and restore procedure | Mandatory per document; governs the encrypted archive. |
| [Protocols/ExportDatabase.md](Protocols/ExportDatabase.md) | Database export procedure | Mandatory per export; governs `data/exports/` bundles. |
| [Protocols/FollowUpResearch.md](Protocols/FollowUpResearch.md) | Follow-up research procedure | Mandatory per document. |
| [Protocols/FromStagetoDatabases.md](Protocols/FromStagetoDatabases.md) | Stage 2 database import | Mandatory per document. |
| [Protocols/Hook-Based-Auto-Trigger-Extraction.md](Protocols/Hook-Based-Auto-Trigger-Extraction.md) | Citation-ingestion automation | Governing protocol; metadata review needed. |
| [Protocols/Research-Evaluation.md](Protocols/Research-Evaluation.md) | Research evaluation | Mandatory per document. |
| [Protocols/TransitionStage2.md](Protocols/TransitionStage2.md) | Stage transition extraction | Mandatory per document. |
| [Protocols/OrganisationSpaceRules.md](Protocols/OrganisationSpaceRules.md) | Organization rules | Accepted 2026-09-28 for this space. |
| [Commander Deck/Plans/OptimalSPrompt.md](Commander%20Deck/Plans/OptimalSPrompt.md) | Prompt architecture plan | Status needs review; preserve dated rationale and distinguish stale inventory statements. |
| [Commander Deck/Plans/ProcessEstablishment.md](Commander%20Deck/Plans/ProcessEstablishment.md) | ECA establishment plan | Frontmatter `active`; completion/status needs owner review. Retain verification record. |
| [Commander Deck/Plans/OrganisationPrinciplesAuthority.md](Commander%20Deck/Plans/OrganisationPrinciplesAuthority.md) | Source authority synthesis | Draft; provenance for this renovation. |
| [Commander Deck/Plans/CommanderPlan.md](Commander%20Deck/Plans/CommanderPlan.md) | Governance renovation plan | In progress; no physical moves authorized. |
| [Commander Deck/Problems/Report1.md](Commander%20Deck/Problems/Report1.md) | Citation database review / findings | Historical findings; verify resolution in current sources before treating as open or closed. |
| `scripts/assemble_prompt.py` | Prompt assembly script. |
| `src/prompt_templates/` | Prompt templates and shared `lib/` partials. |
| `scripts/formulate_research_questions.py` | Follow-up research question generation. |
| `scripts/assemble_prompt.py` | Next research prompt assembly. |
| [Commander Deck/State changes/28092026Report.md](Commander%20Deck/State%20changes/28092026Report.md) | Dated state report | Historical snapshot; 67/67 tests predates the current 68-pass result. |
| [Commander Deck/State changes/28092026OrganisationRenovation.md](Commander%20Deck/State%20changes/28092026OrganisationRenovation.md) | Dated implementation record | Records implementation and validation of CommanderPlan Phases 0-2. |
| [Commander Deck/Archive/commander_deck_archive_20260928_122517_manifest.json](Commander%20Deck/Archive/commander_deck_archive_20260928_122517_manifest.json) | Archive inventory and provenance | Readable; reports four members and `VERIFIED_OK`. |
| `Commander Deck/Archive/commander_deck_archive_20260928_122517.tar.gz.enc` | Encrypted archive payload | Preserved; not decrypted for this inventory. Follow the ECA protocol to list or restore. |

The manifest identifies `Plan 2.md`, `Plan First Citation Intelligence
Database.md`, `Solutions1.md`, and `state change 001.md` inside the archive.
Their contents were not re-read for this index.

## Implementation State

- **Authorized scope:** index/source inventory and canonical protocol path
  repair. CommanderPlan Phases 0-2 are complete.
- **Not authorized:** moving, renaming, decrypting, archiving, or deleting
  files; changing historical records; changing test rules.
- **Validation:** focused `test_r4_all_referenced_paths_exist` passes; full
  suite reports 68 passed on 2026-09-28. The previous baseline had 22 stale
  prompt references to root-level `Protocols/...`; they now resolve under
  `Rules and Regulations/Protocols/`.
- **Implementation record:** [28092026OrganisationRenovation.md](Commander%20Deck/State%20changes/28092026OrganisationRenovation.md).
- **Next review:** confirm legacy document statuses and owners, then run the
  reader-task pilot and close remaining CommanderPlan gates. No relocation is
  authorized by this completed slice.