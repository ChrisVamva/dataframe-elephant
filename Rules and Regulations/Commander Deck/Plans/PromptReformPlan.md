---
status: proposed
created: 2026-09-28
scope:
  - prompts/
  - prompts/prompts/
approval: pending
---

# Prompt Reform Plan

## Document Control

- **Status:** proposed; no prompt files are moved, archived, or rewritten by this plan alone
- **Decision owner:** workspace maintainer (personal name not recorded)
- **Purpose:** converge prompt assets on one functional canonical system, resolve governance and location conflicts, and deliver a self-contained smart-home market research prompt
- **Problem record:** [ProblemPrompts.md](../Problems/ProblemPrompts.md)
- **Applicable core contract:** [MaintainingProsperity.md](../../Core%20Rules/MaintainingProsperity.md)
- **Applicable protocols:** [Research-Evaluation.md](../../Protocols/Research-Evaluation.md), [FollowUpResearch.md](../../Protocols/FollowUpResearch.md), [FromStagetoDatabases.md](../../Protocols/FromStagetoDatabases.md), [Encryption-Compression-Archiving.md](../../Protocols/Encryption-Compression-Archiving.md)
- **Plan update triggers:** a change to prompt ownership, the assembler, protocol references, archive lifecycle, portability requirements, or a validation failure

## 1. Decision Requested

Approve a staged reform with these intended outcomes:

1. Keep repository-level [`prompts/`](../../../prompts/) as the single
   canonical prompt-system root, subject to the conflict and portability
   checks below.
2. Retire the nested duplicate [`prompts/prompts/`](../../../prompts/prompts/)
   as a live prompt location. Preserve superseded content using the
   prompt-lifecycle rules before removing the nested directory.
3. Separate repository-connected prompts, which legitimately require
   workspace inputs, from portable prompts, which must work without access to
   `C:\Users\user\dataframe-elephant` or any other private repository.
4. Resolve the portable-export conflict with the rule that protocols own
   standing evidence standards before encoding those standards in a portable
   output.
5. Produce and present a copy/paste-ready prompt for exploring the smart-home
   market across whatever research media the recipient can access.

This proposal does not authorize immediate archival or deletion. Approval
must name the intended scope; each destructive or relocating batch still
requires its own path map, backup/recovery plan, and validation.

## 2. Problem and Design Basis

The user reports that prompts have asked a research agent to access the local
`dataframe-elephant` repository to complete tasks. The user says this has
stalled research quality and progress. The specific prompt versions, number
of occurrences, and exact failed sessions have not yet been supplied or
independently reproduced. The report is recorded as open in
[ProblemPrompts.md](../Problems/ProblemPrompts.md).

The prompt library also has an observed architecture distinction that the
reform must preserve:

- Some current templates are deliberately repository-connected. For example,
  follow-up and next-research templates list the local agenda, Stage 2 files,
  protocols, and repository write-back as inputs or context.
- Other prompts can be standalone research tasks. They should not silently
  inherit the repository-dependent inputs, commands, or file paths of the
  integrated workflow.

The design is governed by the workspace recurrence-prevention contract:

- **MaintainingProsperity R1/R3/R9:** protocols own rules and reusable blocks
  have one source; prompts reference rather than fork those rules.
- **R4/R5:** update canonical commands in `AGENTS.md` first and ensure every
  named path resolves.
- **R7:** run the full test suite after prompt, protocol, or rule changes.
- **R8:** superseded prompt sources are versioned and archived, not silently
  deleted.
- **R10:** do not claim prompt quality improved without measurement.
- **R12:** generated dispatch artifacts stay generated and are not hand-edited.

`Research-Evaluation.md` remains the authority for research scope, evidence,
claim support, uncertainty, counterevidence, and decision criteria.
`FollowUpResearch.md` and `FromStagetoDatabases.md` govern the repository
write-back workflow. A portable market prompt must not pretend it can execute
those repository operations when it is run outside the repository.

## 3. Current-State Inventory

Filesystem snapshot checked on 2026-09-28. The root prompt library exists. The
nested `prompts/prompts/` exists. The previously used
`Rules and Regulations/Commander Deck/prompts/` path does **not** currently
exist; do not recreate it merely to match an older index or to make a stale
scope statement appear true.

### Canonical root candidate: `prompts/`

| Path or group | Current role/status | Proposed disposition |
| --- | --- | --- |
| [`README.md`](../../../prompts/README.md) | Calls root `prompts/` the single home for reusable assets; documents lifecycle and assembly conventions. | Keep as index of record; revise after the target architecture is approved. |
| [`lib/`](../../../prompts/lib/) (8 Markdown partials) | Shared role, evidence pointers, deliverable shapes, quality bar, verification, claim taxonomy, and lens reference. | Keep one canonical copy of each approved reusable block; inventory dependencies and classify which are portable-safe versus workspace-bound. |
| [`templates/`](../../../prompts/templates/) (3 active v2.0 templates) | `research_brief`, `followup_dispatch`, `next_research`. The latter two depend on local research agenda/Stage 2 data; all declare protocol references. | Preserve as the repository-connected source templates. Add portable prompts only after the portability profile is approved and tested. |
| [`dispatch/`](../../../prompts/dispatch/) | Contains a README and at least one generated research-brief dispatch (2026-09-28). | Regenerate from a template when required; do not hand-edit or use ECA as a default archive for regenerable dispatches (MaintainingProsperity R12). |
| [`archive/`](../../../prompts/archive/) | Contains an archive README defining the prompt-specific supersession convention. | Keep as the history destination for superseded templates/partials under R8; do not confuse this with encrypted governance-history archives. |
| [`prompts/`](../../../prompts/prompts/) (nested transitional folder; 6 Markdown files) | A copied pointer index, three superseded stubs, `CheckpointAuthorityPrompts.md`, and the user-requested standalone smart-home prompt. | Treat old pointer copies as non-canonical. Preserve the smart-home prompt at its explicitly requested path during this transition; decide whether the finalized system keeps this portable-output area or relocates/indexes it under the canonical root before closing Phase 1. |

The five nested files are:

| Path | Observed state | Initial disposition |
| --- | --- | --- |
| [`prompts/prompts/README.md`](../../../prompts/prompts/README.md) | Calls itself the Commander Deck prompts operational index and points to root `prompts/`. | Redundant pointer index; archive after all live references have been redirected to root `prompts/README.md`. |
| [`prompts/prompts/Research Prompt.md`](../../../prompts/prompts/Research%20Prompt.md) | Frontmatter says `status: superseded`, `superseded_by: prompts/templates/research_brief.md`. | Preserve as historical pointer under `prompts/archive/` using R8; do not keep as an active template. |
| [`prompts/prompts/FollowUpPrompt.md`](../../../prompts/prompts/FollowUpPrompt.md) | Frontmatter says `status: superseded`, `superseded_by: prompts/templates/followup_dispatch.md`. | Preserve as historical pointer under `prompts/archive/` using R8. |
| [`prompts/prompts/NextResearchPrompt.md`](../../../prompts/prompts/NextResearchPrompt.md) | Frontmatter says `status: superseded`, `superseded_by: prompts/templates/next_research.md`. | Preserve as historical pointer under `prompts/archive/` using R8. |
| [`prompts/prompts/CheckpointAuthorityPrompts.md`](../../../prompts/prompts/CheckpointAuthorityPrompts.md) | Draft authority document whose declared scope is the absent `Rules and Regulations/Commander Deck/prompts/`; links were written for that former location and may now be stale. | Do not treat as a prompt. Reconcile its scope and links, then relocate it to the governance plan area or archive it as a superseded checkpoint, preserving provenance. Decision remains open until link review. |
| [`prompts/prompts/smart-homemarketpromp.md`](../../../prompts/prompts/smart-homemarketpromp.md) | User-requested standalone smart-home market prompt; portable deliverable. | Keep at the exact requested path for now. It has no repository-local paths, but is not yet classified as a canonical template in the final root system; resolve placement during Phase 1 and validate in a clean context during Phase 4. |

The nested README says its stubs point to the root templates, and the three
stubs' `superseded_by` metadata names those templates. The root templates are
present and active at version 2.0. The nested authority document's old folder
scope is not consistent with its current location. No live incoming-link
count has been established; that must be measured before retirement.

The user has explicitly requested the first portable deliverable at
`prompts/prompts/smart-homemarketpromp.md`. Preserve this location during the
reform; decide whether it becomes a permanent portable-output area or is
moved/indexed under the canonical root before declaring the final structure
complete.

The baseline full suite run on 2026-09-28 reports 67 passed and 1 failed.
`test_r4_all_referenced_paths_exist` identifies two stale references to
`Rules and Regulations/Commander Deck/prompts/`: one in
`prompts/README.md` and one in
`prompts/prompts/CheckpointAuthorityPrompts.md`. This failure is the first
measurable repair target; it was not caused by this plan or the problem
record.

## 4. Target System

The final system should have one discoverable root and explicit prompt
profiles. The proposed conceptual layout is:

```text
prompts/
|-- README.md                     # index of record, ownership, lifecycle, profiles
|-- lib/                          # single-source reusable task/evidence blocks
|-- templates/                    # versioned canonical prompt sources
|   |-- research_brief.md         # repository-connected research workflow
|   |-- followup_dispatch.md      # repository-connected follow-up workflow
|   |-- next_research.md          # repository-connected gap-closure workflow
|   `-- smart_home_market.md      # proposed portable market-research source
|-- dispatch/                     # generated, repo-connected session outputs only
|-- archive/                      # superseded prompt source versions per R8
`-- prompts/                      # removed only after link audit and archival gate
```

The tree is an end-state proposal, not authorization to remove the nested
directory now. Keep the existing repository-connected workflows available.
Portable mode must be explicit and must not request private files, local
paths, repository scripts, DuckDB state, hidden environment variables, or
workspace-only protocols as prerequisites.

### 4.1 Portable prompt contract

A portable prompt must:

1. Work when copied into a clean session or any research medium without this
   repository. It must neither request nor assume access to
   `C:\Users\user\dataframe-elephant`.
2. State its research question, scope, defaults, time horizon, geography, and
   user-adjustable assumptions. Ask only for missing inputs that materially
   change the result; otherwise state transparent defaults.
3. Adapt to available media (web search, browser, academic indexes, official
   reports, product documentation, user-provided documents, or other
   accessible sources). Disclose inaccessible sources or unavailable tools
   and continue with the available evidence rather than asking for the repo.
4. Require traceable sources, dates, claim-to-source alignment, uncertainty,
   conflicts, limitations, and counterevidence, consistent with the intended
   quality profile in `Research-Evaluation.md`.
5. Avoid repository write-back sections and commands. Offer them only as a
   separate, explicitly optional integration step when the user is running in
   the repo and requests it.
6. Be tested as a rendered, copy/paste-ready artifact with no unresolved
   includes, template variables, private paths, or undeclared inputs.

### 4.2 Smart-home market prompt deliverable

After the portable profile and assembly method are approved and tested,
assemble and provide one standalone smart-home market research prompt. It
should allow the researcher to specify or default the geography and period,
work across multiple research media, distinguish market segments and value
chain participants, cover demand/adoption, technology/interoperability,
competition, routes to market, regulation, economics, and barriers, and
produce a traceable evidence table, explicit uncertainty, counterevidence,
and next research questions. It must not assume repository access or ask the
recipient to run local scripts.

This is a deliverable of the final implementation phase. Do not claim it has
been generated from a finalized system until the portable-mode gates pass.

## 5. Conflicts to Resolve

| Conflict | Current evidence | Planned resolution |
| --- | --- | --- |
| Two prompt locations vs single source of truth | Root `prompts/README.md` says root is the single home; nested README is a copied pointer index; nested stubs are superseded. | Keep root `prompts/` canonical. Redirect references, preserve nested history, then retire the nested folder. |
| Old Commander Deck prompt path vs actual tree | `Rules and Regulations/Commander Deck/prompts/` is absent; nested `prompts/prompts/CheckpointAuthorityPrompts.md` still declares that scope. | Audit Git paths and inbound links. Correct/relocate the authority document only after preserving its prior location/status; do not recreate the absent directory merely to validate its stale claim. |
| Repository-connected tasks vs no-repo usage | Existing follow-up templates list private agenda, Stage 2 files, protocol references, and local write-back. User reports prompts requiring local repository access has stalled research progress. | Classify prompts as repository-connected or portable. Make the user-facing portable profile explicitly self-contained; never silently run a repo workflow in portable mode. |
| Portable self-containment vs protocol single-source rule | A portable output cannot rely on inaccessible local protocols, while MaintainingProsperity R1/R3/R9 require rules to be owned centrally and not copied into prompts. | Before drafting the portable template, decide and document a compliant export design: either assemble approved protocol content into a generated self-contained output, or approve a concise portable profile in the owning protocol and generate from it. Do not hand-copy/maintain an untracked duplicate rule set. |
| Prompt source archives vs ECA archives | MaintainingProsperity R8 and `prompts/archive/README.md` require superseded prompt sources to be versioned under `prompts/archive/`; ECA specifies encrypted archival for research/governance history and the Commander Deck Archive profile. | Use R8 plus the prompt archive convention for superseded prompt sources. Use ECA only when a material is in its scope and the selected destination/process is authorized; do not encrypt generated dispatches or bypass R8 by treating every prompt retirement as Commander Deck governance history. |
| Historical plans vs current implementation | `OptimalSPrompt.md` refers to removed `Commander Deck/Active/prompts/` and a time when root `prompts/` did not exist; the current root library exists. | Preserve the plan as historical design rationale, mark its current status clearly, and link the new plan as the current reform record. Do not overwrite history. |

## 6. Implementation Sequence

Each phase is a separate reviewable batch. No archive, move, rename, or
deletion occurs until its approval, inbound-link inventory, archive path, and
rollback are recorded.

### Phase 0: Baseline and incident

1. Keep [ProblemPrompts.md](../Problems/ProblemPrompts.md) open as
   `user-reported`; collect exact prompt/version/session examples if the user
   can provide them later.
2. Record the current root library and nested folder inventories, statuses,
   input requirements, protocol references, inbound references, generated
   outputs, and existing tests.
3. Confirm the old Commander Deck prompt path is absent and reconcile its
   moved/deleted history without restoring duplicate assets.
4. Preserve the existing full-suite result as a dated baseline and rerun it
   before implementation. Do not use historic reports as current test output.

**Gate:** source-of-truth candidate, duplicate set, link surface, and issue
status are recorded; no files changed.

### Phase 1: Resolve authority and portability conflicts

1. Confirm root `prompts/` as canonical and record the decision in its README.
2. Resolve ownership/status of `CheckpointAuthorityPrompts.md`: correct its
   scope, repair its links, and move it to an appropriate governance location
   only with an approved path change. Preserve a historical record.
3. Review the portability conflict in §5 with the owner of
   `Research-Evaluation.md`. Select an export design that respects R1/R3/R9
   and creates an actually self-contained artifact.
4. Clarify profiles in the root prompt index:
   `repository-connected` (declared private inputs and optional write-back)
   versus `portable` (no repo access required).
5. Update stale location/status descriptions in the prompt README and
   `OptimalSPrompt.md` by appending a current decision/status record or
   explicitly superseding sections; do not silently rewrite historical
   rationale.

**Gate:** one canonical root, explicit prompt profiles, no unresolved
protocol-ownership conflict, and a portable-output mechanism selected.

### Phase 2: Reconcile and archive duplicate sources

1. Search all tracked and untracked Markdown for references to
   `prompts/prompts/`, `Rules and Regulations/Commander Deck/prompts/`, the
   old `Commander Deck/Active/prompts/`, and the three stub names. Include
   `AGENTS.md`, protocols, plans, tests, code, README files, and links from
   outside the repo where feasible.
2. Classify each nested item:
   - three superseded stubs and the duplicate pointer README;
   - the authority document, which is governance documentation rather than a
     prompt template;
   - any added or discovered item not listed in the 2026-09-28 baseline.
3. Redirect valid references to the root `prompts/` library; correct or
   relocate the authority document according to the owner decision.
4. Preserve superseded prompt text in `prompts/archive/` following
   MaintainingProsperity R8 and the archive README naming convention. Keep
   original status, date, former path, and `superseded_by` target. Do not
   delete source copies until path and content checks pass.
5. Apply ECA only to files/archive operations actually in its declared scope.
   If an ECA archive is separately authorized, perform its dry-run, manifest,
   `--keep-originals` verification, and SHA-256 round-trip before deleting
   any source. Generated `prompts/dispatch/` files remain regenerable under
   R12 and are not prompt-source archives.
6. Remove the now-empty nested prompt directory only after archive and
   inbound-link gates pass and the user explicitly approves that operation.

**Gate:** no live reference targets a retired path; archived sources remain
inspectable; root prompt lint passes; the exact source-to-archive manifest is
reviewed. Stop if any unique live instruction is discovered.

### Phase 3: Build the portable prompt path

1. Add a versioned smart-home market research template to the canonical root
   library using the approved portable profile.
2. Ensure the researcher can use any available research medium, report tool
   and source limitations, and proceed without private files, local paths,
   repository scripts, database access, or local protocols.
3. Keep repo write-back separate and opt-in; do not ask an external researcher
   to paste results into the repository or access it.
4. Assemble a standalone output and inspect the exact final text for internal
   path, unresolved include, template variable, private-input, and hidden
   access requirements.
5. Provide the assembled copy/paste-ready prompt to the user after the system
   gates pass.

**Gate:** portable prompt works in a clean environment with no dataframe-
elephant access, follows the approved research-quality profile, and returns a
useful market map with evidence, uncertainty, counterevidence, and next
questions.

### Phase 4: Functional validation and closeout

1. Add deterministic tests for root library includes, path validity, prompt
   profile declarations, portable export independence, and absence of
   repository prerequisites in the smart-home artifact.
2. Run the existing Tier 1 lint and full test suite. Add a lightweight
   portability check or simulated clean-context test; do not claim actual
   research performance from a lint pass alone.
3. Validate one portable execution using a research medium the user chooses
   or has available; record inaccessible sources and result limitations.
4. Compare output against an agreed quality rubric derived from
   `Research-Evaluation.md` and this problem's acceptance criteria.
5. Append a dated state-change report, update prompt versions and the root
   README, and close `ProblemPrompts.md` only if its closure criteria pass.

## 7. Prompt Archive and Data-Safety Rules

- Prompt source supersession follows MaintainingProsperity R8 and
  `prompts/archive/README.md`: preserve full text, version/date/status, and
  supersession target.
- Generated dispatches follow R12: regenerate from the source; do not hand-edit
  them or treat them as the only copy of a useful reusable prompt.
- ECA is not a generic alternative to prompt versioning. For operations within
  ECA scope, follow every cryptographic, manifest, dry-run, verification, and
  preserve-before-delete requirement in
  `Encryption-Compression-Archiving.md`.
- No user prompt content or unique market research findings should be archived
  away as disposable duplicates. Classify source versus generated output
  before any removal.

## 8. Acceptance Criteria

| Area | Completion condition |
| --- | --- |
| Canonical ownership | Root `prompts/` is declared the only live prompt library; nested duplicates are archived or explicitly retained only with an approved reason. |
| Conflict resolution | Root/nested README claims, superseded stubs, stale `CheckpointAuthorityPrompts` scope, legacy plan references, and protocol ownership are reconciled without silent overwrites. |
| Repository-connected use | Current research, follow-up, and gap-closure workflows retain declared dependencies and remain functional. |
| Portable use | A recipient can copy the smart-home prompt into an unrelated research medium and use it without this repository or local files. |
| User problem | No portable prompt asks for `C:\Users\user\dataframe-elephant`, repo-only files, local scripts, or a database as a required step. |
| Evidence quality | Smart-home research output is scoped/date-stamped, traceable, uncertainty-aware, checked for conflict/counterevidence, and does not invent market-size numbers. |
| Archive safety | Every superseded source has a recoverable, inspectable archived copy; ECA is used only within its approved scope and passes integrity verification before deletion. |
| Validation | Tier 1 lint and full pytest suite pass; portable artifact check passes; a clean-context run or its limitations are recorded. |

## 9. Completion Record

| Date | Stage | Status | Evidence / limitation |
| --- | --- | --- | --- |
| 2026-09-28 | Planning baseline | proposed | Root library and nested copy inspected; prior Commander Deck prompt path absent. User-reported portability problem recorded separately. Reform and archive operations not yet executed. |

This plan is not permission to silently change protocol policy, move files, or
delete prompt sources. Record those approvals before the relevant phase begins.