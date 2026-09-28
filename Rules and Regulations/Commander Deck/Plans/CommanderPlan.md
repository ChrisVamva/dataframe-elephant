---
status: in_progress
scope: Rules and Regulations/ and all descendants
created: 2026-09-28
approval: "Initial no-move implementation authorized by workspace maintainer, 2026-09-28"
---

# Commander Plan: Rules and Regulations Renovation

## Document Control

- **Status:** in progress; initial scope is index, ownership/status inventory, and canonical path repair only
- **Covered folder:** `Rules and Regulations/`
- **Snapshot date:** 2026-09-28
- **Prepared by:** GitHub Copilot, at the workspace maintainer's request
- **Decision owner:** workspace maintainer (role confirmed; personal name not recorded)
- **Intended use:** staged organization renovation preserving one source of truth, folder provenance, and recoverable history
- **Governing design protocol:** [OrganisationSpaceRules.md](../../Protocols/OrganisationSpaceRules.md) (accepted 2026-09-28)
- **Research synthesis:** [OrganisationPrinciplesAuthority.md](OrganisationPrinciplesAuthority.md) (draft)
- **Approval:** initial non-destructive implementation scope authorized by direct user instruction on 2026-09-28; moves, renames, archive operations, and deletions remain unauthorized

## 1. Executive Recommendation

Renovate the governance space first through **clear ownership, a root index,
status and scope visibility, and repaired references**. Keep the current major
directory roles and paths during the first pass:

```text
Rules and Regulations/
|-- README.md                         # add as the index of record
|-- Core Rules/                       # durable cross-workspace rules
|-- Protocols/                        # accepted repeatable procedures
`-- Commander Deck/
    |-- Plans/                        # proposals and implementation plans
    |-- Problems/                     # incidents and risk records
    |-- State changes/                # dated implementation history
    |-- prompts/                       # pointer stubs only
    `-- Archive/                       # ECA-protected historical material
```

No physical file move is recommended at this stage. The current folders
already express useful lifecycle roles; the observed defects are more
immediately about missing navigation, unverified document status, stale
references, and time-bound plans being mistaken for current truth. The
maintainer can authorize a later move only after the source-of-truth and
inbound-link checks in §7.

This plan follows [OrganisationSpaceRules.md](../../Protocols/OrganisationSpaceRules.md)
and the [Authority Document Creation Protocol](../../Protocols/AuthorityDocumentCreation.md).
The user instruction to start implementation authorizes the bounded scope
above. It does not authorize physical relocation or deletion.

## 2. Desired Outcome

A reader new to the workspace should be able to answer quickly:

1. Which document owns the rule or requirement?
2. Which accepted protocol explains how to apply it?
3. Is a plan approved, proposed, completed, or superseded?
4. Where is the issue history and what was actually changed?
5. Which prompt file is canonical, and which is only a pointer?
6. What archived material exists, and how is it safely inspected or restored?

The renovation should produce one index and one source-of-truth inventory;
retain every historical artifact; make statuses explicit when confirmed; and
resolve broken paths without creating duplicate rule copies.

## 3. Source Principles and Research

The supplied Obsidian folder is summarized in
[OrganisationPrinciplesAuthority.md](OrganisationPrinciplesAuthority.md).
Its four notes are proposals rather than measured outcomes. Their useful
shared principles for this renovation are purpose-based grouping, clear
document-role boundaries, an index, stable names and metadata, separation of
current from historical content, and gradual implementation. Their different
sample taxonomies are not treated as a single prescribed tree.

External source material, retrieved 2026-09-28:

| Source | Relevant finding | Application here |
| --- | --- | --- |
| [UN Archives, File Classification Schemes](https://archives.un.org/en/content/advisory-services/file-classification-schemes) | A function/activity-based hierarchy supports retrieval, context, consistent terminology, and ownership; levels can distinguish functions, activities, and transactions. | Keep the structure shallow and classified by what each document does. Do not add subfolders without a real responsibility or lifecycle boundary. |
| [The National Archives (UK), Filing structures](https://www.nationalarchives.gov.uk/information-management/manage-information/public-inquiry-guidance/filing-structures/) | Filing plans should be understandable, activity-based, retrievable, contextual, and capable of carrying metadata and access controls. | The index and ownership inventory should help users locate and interpret material. |
| [U.S. National Archives, Knowing Your Records](https://www.archives.gov/records-mgmt/scheduling/knowing) | Inventory depth depends on purpose; a baseline identifies what exists, use, format, and location. Findings should be verified and revisited as processes change. | Inventory all material first, but keep the initial inventory proportionate; verify local status rather than infer it. |
| [The National Archives (UK), Information principles](https://www.nationalarchives.gov.uk/information-management/manage-information/planning/information-principles/) | Information should be managed, fit for purpose, standardized/linkable, and reusable. | Prefer one canonical owner, reliable links, and concise summaries over duplicated policy text. |

These sources address government records and information management. They are
used as organizational analogies, not as legal requirements for this private
workspace. The search was targeted, not a systematic review.

## 4. Baseline Inventory

This is the baseline snapshot of visible files under `Rules and Regulations/`
before this plan's implementation began. It records every Markdown file at
that time, plus the readable archive manifest and encrypted archive. The
encrypted payload was not decrypted; its four member paths and hashes are
available in the manifest.
Status descriptions below reflect visible document intent, not approval
unless the document itself establishes it. Unknown status must be confirmed
in Phase 1.

| Path | Current role / status indication | Proposed disposition |
| --- | --- | --- |
| [Core Rules/MaintainingProsperity.md](../../Core%20Rules/MaintainingProsperity.md) | Standing recurrence-prevention contract; describes itself as mandatory. | Keep as sole owner of R1-R12; index it. Verify links and status during inventory. |
| [Protocols/AuthorityDocumentCreation.md](../../Protocols/AuthorityDocumentCreation.md) | Mandatory protocol for authority documents. | Keep in `Protocols/`; index as governing protocol. |
| [Protocols/Encryption-Compression-Archiving.md](../../Protocols/Encryption-Compression-Archiving.md) | Mandatory archive-preservation and ECA procedure. | Keep in `Protocols/`; preserve its dry-run and verified round-trip safeguards. |
| [Protocols/FollowUpResearch.md](../../Protocols/FollowUpResearch.md) | Mandatory follow-up research procedure. | Keep in `Protocols/`; index and repair any stale cross-reference only through a separate reviewed change. |
| [Protocols/FromStagetoDatabases.md](../../Protocols/FromStagetoDatabases.md) | Mandatory Stage 2 database import procedure. | Keep in `Protocols/`; link from its workflow entry. |
| [Protocols/Hook-Based-Auto-Trigger-Extraction.md](../../Protocols/Hook-Based-Auto-Trigger-Extraction.md) | Governs on-demand and hook-triggered citation ingestion. | Keep in `Protocols/`; verify path assumptions when auditing references. |
| [Protocols/Research-Evaluation.md](../../Protocols/Research-Evaluation.md) | Mandatory research-quality and evidence evaluation protocol. | Keep as owner of claim/evidence evaluation rules. |
| [Protocols/TransitionStage2.md](../../Protocols/TransitionStage2.md) | Mandatory research extraction procedure. | Keep in `Protocols/`; index as extraction authority. |
| [Protocols/OrganisationSpaceRules.md](../../Protocols/OrganisationSpaceRules.md) | New proposed protocol; status `draft`. | Keep proposed until maintainer acceptance; do not treat as effective policy before approval. |
| [Commander Deck/Plans/OptimalSPrompt.md](OptimalSPrompt.md) | Prompt-system architecture proposal; contains a point-in-time inventory. | Keep as design rationale/history. Review claims against current repo state before citing as current guidance. |
| [Commander Deck/Plans/ProcessEstablishment.md](ProcessEstablishment.md) | ECA application plan with a recorded `VERIFIED_OK` result. | Keep as completed decision/process history; current operation remains governed by the ECA protocol. |
| [Commander Deck/Plans/OrganisationPrinciplesAuthority.md](OrganisationPrinciplesAuthority.md) | New synthesis of four external source notes and public guidance; status `draft`. | Keep as provenance for this renovation; pending maintainer review. |
| [Commander Deck/Plans/CommanderPlan.md](CommanderPlan.md) | This proposed renovation plan; approval not recorded. | Keep as proposed until approval and implementation decision. |
| [Commander Deck/Problems/Report1.md](../Problems/Report1.md) | Historical citation-database review with findings and remediation proposals. | Keep as incident/review evidence. Confirm each finding's present resolution in the owning code, protocol, or state record; do not make the report a live rule. |
| [Commander Deck/prompts/README.md](../prompts/README.md) | Declares this folder an operational pointer layer; root `prompts/` is the prompt asset index of record. | Keep; ensure individual stubs remain thin, working pointers. |
| [Commander Deck/prompts/Research Prompt.md](../prompts/Research%20Prompt.md) | Prompt pointer/operational stub by directory role. | Keep pending link and content check; canonical prompt logic stays in root `prompts/`. |
| [Commander Deck/prompts/FollowUpPrompt.md](../prompts/FollowUpPrompt.md) | Prompt pointer/operational stub by directory role. | Keep pending link and content check; canonical prompt logic stays in root `prompts/`. |
| [Commander Deck/prompts/NextResearchPrompt.md](../prompts/NextResearchPrompt.md) | Prompt pointer/operational stub by directory role. | Keep pending link and content check; canonical prompt logic stays in root `prompts/`. |
| [Commander Deck/State changes/28092026Report.md](../State%20changes/28092026Report.md) | Dated state-change report with a 2026-09-28 suite snapshot. | Keep as immutable historical record. Its reported 67/67 test state is not the current baseline; link a newer validation record rather than editing history. |
| [Commander Deck/Archive/commander_deck_archive_20260928_122517_manifest.json](../Archive/commander_deck_archive_20260928_122517_manifest.json) | Readable ECA-v1 manifest; four files, `VERIFIED_OK`. | Keep as the archive inventory and provenance record. |
| `Commander Deck/Archive/commander_deck_archive_20260928_122517.tar.gz.enc` | Encrypted ECA-v1 archive payload. | Preserve unchanged; inspect/list/restore only using `Encryption-Compression-Archiving.md`. |

The archive manifest names four historical members: `Plan 2.md`, `Plan First
Citation Intelligence Database.md`, `Solutions1.md`, and `state change 001.md`.
This plan does not infer their current policy status from their names or
decrypt the payload. Their exact archive paths and SHA-256 hashes remain in
the manifest.

### 4.1 Known freshness and path risks

- `OptimalSPrompt.md` contains an earlier inventory that describes the
  repository-level `prompts/` library as not yet present. The library is
  present now; treat that section as a dated design snapshot, not current
  filesystem truth.
- `State changes/28092026Report.md` reports 67/67 tests passing at its
  recorded snapshot. The latest check available at the start of this task was
  67 passed and 1 failed: `test_r4_all_referenced_paths_exist`, with 22
  missing prompt references including `Protocols/Research-Evaluation.md`.
- The only protocol directory found is `Rules and Regulations/Protocols/`;
  no repository-root `Protocols/` directory exists. Do not create one as a
  duplicate. The prompt references and test baseline should be fixed against
  the canonical directory instead.
- The prompt directory README identifies the prompt files as pointer stubs;
  their current targets must be checked before any move or rename.
- Some legacy plans and incident findings may no longer describe current
  state. No status is promoted or issue marked resolved solely from an old
  plan or report.

## 5. Proposed Operating Model

### 5.1 Keep existing folders; clarify their contract

| Folder | Contract after renovation |
| --- | --- |
| `Core Rules/` | Small set of durable cross-cutting workspace rules. Do not copy these into protocols or plans. |
| `Protocols/` | Accepted repeatable operating procedures. Each protocol owns a declared scope and acceptance/update rules. Drafts are visible as draft. |
| `Commander Deck/Plans/` | Proposed or approved structural/design work, rationale, and decision status. Plans are not effective policy unless adopted in the owning document. |
| `Commander Deck/Problems/` | Findings, incidents, and unresolved risks. A problem report records observations; it is not a standing rule. |
| `Commander Deck/State changes/` | Dated history of implementation. Append new records; do not rewrite the meaning of earlier snapshots. |
| `Commander Deck/prompts/` | Backward-compatible pointer stubs and an index only. Canonical reusable assets live under repository-level `prompts/`. |
| `Commander Deck/Archive/` | Completed/superseded history stored according to ECA. The readable manifest is the inventory; payload handling follows the ECA protocol. |

### 5.2 Add one navigation index, not another rule copy

Create `Rules and Regulations/README.md` with:

- a one-paragraph purpose and authority boundary;
- a link to each current Core Rule and protocol, with status and one-line
  purpose;
- a link to the Commander Deck plan, problem, state-change, prompt-pointer,
  and archive sections;
- a short source-of-truth map that distinguishes current rules from proposed
  and historical documents;
- the link to `AGENTS.md` and repository-level `prompts/README.md` for their
  owning operational guidance.

The index must not restate protocol content. Update links and status whenever
an owning source changes.

## 6. Implementation Phases

All phases require maintainer approval. Do not begin a later phase while the
prior phase has an unresolved authority conflict or an unexplained broken
reference.

### Phase 0: Approve and freeze the baseline (complete)

1. Accept [OrganisationSpaceRules.md](../../Protocols/OrganisationSpaceRules.md) for this renovation based on the explicit instruction to start implementation.
2. Record the workspace maintainer as decision owner; personal name remains unrecorded.
3. Preserve the current files and record the baseline inventory from §4.
4. Record test output and existing lint failures without modifying existing
   tests, source paths, or archived payloads.

**Gate:** pass. Scope is limited to the index, inventory/status map, and canonical path repair. No existing paths changed.

### Phase 1: Publish navigation and ownership (complete)

1. Add `Rules and Regulations/README.md` using §5.2.
2. Turn the §4 inventory into a maintained source-of-truth/status map. Confirm
   each current/proposed/historical status with the owner instead of inferring
   it from names.
3. Identify one canonical source for every active requirement. Record
   conflicts and unknowns instead of resolving them editorially.

**Gate:** pass for this initial slice. The index covers the baseline files,
assigns roles/dispositions, and flags unverified legacy status for owner
review. Active rules map to their canonical files.

### Phase 2: Repair canonical references (complete)

1. Search all workspace Markdown for `Protocols/<name>.md` and other paths
   that assume the protocols are at repository root.
2. Update references to the single canonical location
   `Rules and Regulations/Protocols/<name>.md`, using links appropriate to
   the source file's location. Keep intra-folder links relative where they
   already resolve.
3. Check links in `prompts/`, `AGENTS.md`, the Commander Deck prompt stubs,
   and all plans before changing any path.
4. Run the prompt lint and full test suite. Resolve the existing 22 missing
   prompt references in the owning prompt sources; do not add a duplicate
   root-level protocol tree and do not weaken `check_paths`.

**Gate:** pass. The prompt-path lint has zero violations, all changed local
references resolve, no protocol bodies were copied, and the full test suite
passes (68 tests).

### Phase 3: Normalize document controls without mass churn

1. For each new or materially revised governance document, state status,
   scope, purpose, review date, maintainer (or unassigned), update triggers,
   and governing links.
2. Review existing documents in small batches. Add or correct only the fields
   needed to distinguish accepted/current from draft, unknown, and historical.
3. Mark time-sensitive statements in `OptimalSPrompt.md`, `Report1.md`, and
   old state records as snapshots. Do not rewrite historical conclusions;
   add a dated follow-up record for current findings.
4. Ensure the authority synthesis and this plan remain `draft`/`proposed`
   until reviewed; acceptance of a proposal is recorded explicitly.

**Gate:** a reader can tell which documents are operative and which are
historical without changing historical records or duplicating policies.

### Phase 4: Pilot, validate, and decide whether moves are needed

1. Ask a reader not involved in drafting, if available, to complete the six
   navigation questions in `AuthorityDocumentCreation.md` §8.1 using only the
   new index and target files. Otherwise record a maintainer self-check and
   its limitation.
2. Verify every new/changed link; run relevant protocol checks and the full
   suite. Compare failures with the baseline from Phase 0.
3. Measure the acceptance criteria in §8. If the current tree is navigable
   and has clear ownership, stop without relocating files.
4. Propose any necessary relocation separately, with its rationale, full
   inbound-reference list, source/destination mapping, rollback, and approval.

**Gate:** acceptance criteria pass or the maintainer accepts a named
exception/follow-up. No move is implied by passing this phase.

## 7. Change Controls and Rollback

- This plan authorizes no filesystem moves, renames, deletions, or archive
  operations.
- For an approved path change, prepare a complete old-path/new-path map and
  update all inbound references in the same reviewable change set.
- Preserve prior content and state-change records. For archive operations,
  use `Encryption-Compression-Archiving.md`; never use a plan or index as a
  reason to remove source files.
- If a link, prompt lint, protocol rule, or test regresses, stop the next
  batch. Revert only the authorized changes in that batch or repair the
  broken references while preserving user edits; record the result.
- Avoid renaming existing folders or files merely for stylistic consistency.
  Compatibility risk must be justified against demonstrated navigation
  benefit.

## 8. Acceptance Criteria and Evidence

| Measure | Target |
| --- | --- |
| Inventory coverage | 100% of visible in-scope files and archive artifacts have a role and disposition; encrypted contents are represented by the verified manifest without pretending to have been inspected. |
| Rule ownership | 100% of active requirements map to one canonical rule or protocol; no unexplained duplicate normative text. |
| Status clarity | 100% of new/revised documents state status; unknown legacy status remains explicitly unknown until reviewed. |
| Index completeness | Every current governing source and Commander Deck lifecycle folder is linked from the root index. |
| Path integrity | Zero unexplained broken links for new/changed materials and zero prompt-path lint violations after Phase 2. |
| Safety | No unapproved move/delete; any later archive action follows ECA dry-run and verified roundtrip. |
| Test integrity | Full repository test suite passes, or each remaining pre-existing failure has a documented baseline and approved follow-up. No test is weakened to make the renovation appear complete. |
| Reader task test | Reader can identify rule owner, procedure, plan status, issue/history location, canonical prompt location, and archive inspection process without reconstructing the tree. |

The baseline available at plan creation is `67 passed, 1 failed` for
`test_r4_all_referenced_paths_exist`; its 22 reported misses are existing
prompt path references. Phase 2 must re-run the command and report the new
result rather than assume this failure is caused by the proposed documents.

## 9. Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| A polished plan or summary is mistaken for accepted policy. | Keep status visible and require maintainer approval before rules become effective. |
| A second protocol copy appears to fix broken links. | Maintain the single canonical protocol directory and repair references in place. |
| Moving/renaming breaks prompts, tests, scripts, or historical links. | No moves in the pilot; inventory inbound links and validate in the same batch for any later move. |
| Reports with stale findings are treated as current. | Preserve reports; point the index to current owner/status and append a dated resolution record. |
| Archive contents are misrepresented as reviewed. | Use the readable ECA manifest as inventory and label encrypted payload as not decrypted. |
| Excessive hierarchy increases maintenance. | Keep existing top-level categories; add no new taxonomy until distinct roles and user need are demonstrated. |

## 10. Decision Record

| Decision | Status | Rationale | Decision owner |
| --- | --- | --- | --- |
| Retain current top-level organization and lifecycle folders during the first pass. | Approved for initial implementation scope | Current folders distinguish rules, procedures, plans, problems, changes, pointers, and archive; no physical relocation is needed to repair navigation. | Workspace maintainer; direct instruction 2026-09-28 |
| Create one root `Rules and Regulations/README.md` index. | Implemented | Index created with authority map, protocol register, plan register, inventory, and status limitations. | Workspace maintainer; direct instruction 2026-09-28 |
| Keep `Rules and Regulations/Protocols/` as the only canonical protocol directory. | Implemented and validated | Updated prompt sources and regenerated dispatch to use the existing canonical paths; did not create duplicate protocols. | Workspace maintainer; direct instruction 2026-09-28 |
| Do not move or decrypt archive files for this plan. | Confirmed for current scope | Manifest establishes the archive inventory and verification state; ECA defines the safe inspection/restore path. | Workspace maintainer; direct instruction 2026-09-28 |

## 11. Review and Change Log

| Date | Reviewer | Results | Notes |
| --- | --- | --- | --- |
| 2026-09-28 | GitHub Copilot (author self-review) | Proposed; approval pending | Source inventory, authority synthesis, path risk, archive manifest, and baseline test failure recorded. No directory contents were moved or deleted. |
| 2026-09-28 | GitHub Copilot (implementation record) | Phases 0-2 pass | Workspace maintainer directed implementation. Added the root index, accepted `OrganisationSpaceRules.md` for this scope, repaired canonical prompt protocol references, regenerated the dated dispatch, and recorded the result in [28092026OrganisationRenovation.md](../State%20changes/28092026OrganisationRenovation.md). Full suite: 68 passed. No folders or archive payloads moved. |

Update this plan if the maintainer changes scope, accepts or rejects a
decision, a new governing source changes the target structure, or an approved
migration reveals a material link or history risk. Record completed changes in
`Commander Deck/State changes/`, not by rewriting this proposal as though it
had authorized itself.