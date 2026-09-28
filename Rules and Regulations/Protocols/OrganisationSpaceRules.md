---
status: accepted
scope: Rules and Regulations/ and all descendants
created: 2026-09-28
accepted: 2026-09-28
---

# Organisation Space Rules

## Status and Adoption

The workspace maintainer accepted this protocol by explicitly directing that
implementation of the Commander Plan begin on 2026-09-28. It governs the
organization work in this scope. That authorization does **not** authorize
file moves, renames, archive operations, or deletions; those remain subject to
the approvals and safeguards below and in
[`CommanderPlan.md`](../Commander%20Deck/Plans/CommanderPlan.md).

## 1. Purpose

These rules define how to organize and maintain the internal governance space
at `Rules and Regulations/`. The goal is for a reader to find the current
governing rule, the procedure for applying it, the rationale for planned
changes, incident history, and prior state without confusing one kind of
document for another.

This is an internal workspace structure, not a legal or regulatory filing
scheme. It does not establish external legal retention periods or replace any
applicable legal obligations.

The design is informed by the reviewed
[Organisation Principles Authority Document](../Commander%20Deck/Plans/OrganisationPrinciplesAuthority.md).
Those four source notes are proposals; the rules below make repository-specific
recommendations and are not direct transcriptions of their example trees.

## 2. Governing Sources and Document Authority

Use each document type for one job. A document's folder or polished format
does not grant it authority beyond its explicit scope.

| Document type | Location | Authority and use |
| --- | --- | --- |
| Core rule | `Core Rules/` | A durable, cross-cutting workspace obligation. `MaintainingProsperity.md` is the current recurrence-prevention contract. |
| Protocol | `Protocols/` | A mandatory, repeatable procedure once accepted. A protocol owns its detailed operational rules, inputs, outputs, and checks. |
| Authority document | As scoped by its document control, currently the supporting synthesis in `Commander Deck/Plans/` | A provenance-linked map/synthesis. It does not create policy, replace sources, or upgrade evidence. Follow `AuthorityDocumentCreation.md`. |
| Plan | `Commander Deck/Plans/` | A proposal or approved implementation sequence. A draft/proposed plan is not permission to alter files. Record its status and approval explicitly. |
| Problem or incident report | `Commander Deck/Problems/` | Evidence of an observed issue, risk, or defect. It does not by itself amend a rule or protocol. A remediation becomes authoritative only through an approved change to its owning document. |
| State-change record | `Commander Deck/State changes/` | Dated history of an implemented change. It reports what changed; it is not a substitute for the current rule, plan, or code. |
| Prompt pointer | `Commander Deck/prompts/` | A thin navigation/compatibility pointer to the canonical prompt library. Reusable prompt logic remains in repository-level `prompts/`; do not fork copies. |
| Archive | `Commander Deck/Archive/` | Superseded or completed material retained for history. Archived material is not current instruction. Use the ECA protocol when archiving. |
| Folder index | `Rules and Regulations/README.md` | Entry point and link map to the current documents. It summarizes locations; it does not duplicate their rules. |

### 2.1 Source precedence and conflicts

1. The document that owns a rule is the source of truth for that rule. An
   index, authority document, plan, problem report, or state-change report may
   point to it but must not create a competing copy.
2. `Core Rules/MaintainingProsperity.md` owns its standing R1-R12 recurrence
   rules. Each protocol owns the procedure within its declared scope.
3. Accepted amendments to an owning document take precedence over summaries
   and older records of that document. Historical records remain available
   for provenance but must be marked historical or superseded when appropriate.
4. A plan remains proposed until its approval is recorded. Approval of a plan
   does not silently change an existing protocol; update the protocol through
   its own review and acceptance process.
5. When two live sources conflict and no existing rule resolves precedence,
   do not guess. Record the conflict, stop the affected change, and request a
   maintainer decision. After the decision, amend the owning source and link
   the state-change record.
6. Do not create a second `Protocols/` tree at repository root to satisfy
   broken references. The canonical directory is
   `Rules and Regulations/Protocols/`; repair references to its actual paths.

## 3. Organization Principles

1. **Classify by purpose and lifecycle.** Group by the work the information
   supports and by its lifecycle (governing, applying, proposing, reporting,
   recording history, or archiving), not by an incidental tool or topic label.
2. **Keep the taxonomy shallow.** Add a folder only when it separates a real
   document role, access/maintenance boundary, or lifecycle need. Do not
   create empty or one-document folders just to imitate a sample layout.
3. **Preserve relationships through links.** When a rule, plan, incident, and
   state-change record concern the same subject, keep each in its proper role
   and link between them instead of combining them into an oversized document.
4. **Keep one canonical copy.** Rules, procedures, prompt assets, and reusable
   blocks each have one owner. Other documents use short explanations and
   links. Stubs may remain temporarily for compatibility, but must identify
   their target and must not contain a parallel source of truth.
5. **Make status visible.** Clearly distinguish proposed/draft, accepted and
   current, under review, superseded, and historical material. Do not infer
   current status from a filename or location alone.
6. **Preserve context and history.** Keep rationale, scope, provenance,
   affected paths, validation, and known limitations when changing governance
   documents. Do not silently delete or rewrite historical records.
7. **Prefer stable, descriptive names.** Preserve existing names unless a
   specific ambiguity or usability problem justifies a rename. Use a clear
   subject or procedure name; avoid unexplained abbreviations and vague names
   such as `Plan 2` for new material.
8. **Keep metadata proportional.** New or materially revised governance
   documents must state status, scope, and review/creation date. Add a named
   owner when one is assigned. Do not mass-edit all legacy frontmatter solely
   to make it uniform; record unknown legacy status as unknown until reviewed.
9. **Do not make the index a rulebook.** The root index lists purpose, current
   source, status, and links. Detailed requirements remain in the owning rule
   or protocol.

## 4. Target Layout

The target preserves the existing three main ownership areas and current
Commander Deck lifecycle folders. The only new top-level artifact proposed is
the root navigation index.

```text
Rules and Regulations/
|-- README.md                         # proposed index of record
|-- Core Rules/
|   `-- MaintainingProsperity.md     # standing cross-cutting rules
|-- Protocols/
|   |-- AuthorityDocumentCreation.md
|   |-- OrganisationSpaceRules.md
|   `-- [other protocols]
`-- Commander Deck/
    |-- Plans/                        # proposals and approved roadmaps
    |-- Problems/                     # incident and risk records
    |-- State changes/                # dated implementation history
    |-- prompts/                       # thin pointers only; assets live in /prompts
    `-- Archive/                       # historical archive plus its manifest
```

The tree is a purpose map, not an instruction to move every file. The
renovation plan must establish whether an item fits its current role before
proposing any relocation. Do not add a `Decisions/`, `Standards/`, or
`Reference/` folder unless an approved inventory identifies a distinct
maintained content class that cannot fit the current layout without ambiguity.

## 5. Document Lifecycle and Minimum Control

Use these statuses for new governance documents and when legacy status is
reviewed:

| Status | Meaning |
| --- | --- |
| `draft` | Being prepared; not an effective rule. |
| `proposed` | Ready for a decision; not effective until accepted. |
| `accepted` | Approved by the workspace maintainer and effective within its stated scope. |
| `under_review` | Existing accepted content is being reconsidered; it remains effective unless explicitly suspended. |
| `superseded` | Replaced by a named current document or version; retained or archived with provenance. |
| `historical` | Retained for record; not current operational instruction. |
| `unknown` | Legacy status has not been verified. Do not represent it as accepted. |

Each new or materially revised rule, protocol, authority document, or plan
must state:

- status and scope;
- purpose and intended reader/use;
- maintainer or responsible role, if assigned;
- creation or review date and update triggers;
- related governing sources and local links;
- approval and validation record when the document is accepted.

An implementation record should additionally identify the change date,
changed paths, validation performed, result, and deviations from the approved
plan.

## 6. Change Safety Rules

1. Inventory all in-scope items and references before proposing moves or
   renames. Identify links from `AGENTS.md`, repository prompts, tests, scripts,
   other protocols, and neighboring plans.
2. Make one bounded, reviewable change batch at a time. Update references in
   the same batch as a move or rename; validate links and applicable tests
   before starting the next batch.
3. For relocations, retain original content and history until the replacement
   has been checked. Never delete a file merely because a new index or summary
   exists.
4. Destructive archive or source cleanup follows
   [Encryption-Compression-Archiving.md](Encryption-Compression-Archiving.md),
   including dry-run and verified round-trip requirements. This protocol does
   not weaken those safeguards.
5. Do not weaken a test or lint rule just to make an organizational change
   pass. Repair dead paths, update the canonical source, or explain a real
   exception in the owning rule.
6. Keep changes reversible until the workspace maintainer accepts the result.

## 7. Repository Path and Link Rules

1. The repository-relative canonical prefix for these files is
   `Rules and Regulations/`. Inside this directory, use links relative to the
   linking document where practical; from outside it, include the full
   repository-relative path.
2. A link must resolve to an existing file or directory. A proposed future
   file must be clearly labeled as proposed until it exists.
3. Avoid bare filenames when more than one file can have that name. Use the
   complete repository-relative path in prose or a working relative link.
4. When changing paths, search and update every identified inbound link,
   including prompt references. Repository prompt lint is a required check;
   record pre-existing failures separately from regressions caused by the
   change.
5. Maintain the command and interpreter source of truth in `AGENTS.md` as
   required by `MaintainingProsperity.md` R4. Do not copy command blocks into
   plans or this protocol unless they are verified against that source.

## 8. Adoption and Renovation Procedure

### Step 1: Approve scope and owner

The workspace maintainer accepts or revises this protocol and assigns the
responsible maintainer for `Rules and Regulations/`. Until then, the
`CommanderPlan.md` is a proposal and no reorganization is authorized.

### Step 2: Establish the baseline

Create the root `README.md` index and a source-of-truth inventory with each
document's path, role, status, owner (or `unassigned`), scope, and inbound
references. Classify encrypted archive contents from their readable manifest;
do not decrypt an archive solely for inventory unless a separate decision
requires it.

### Step 3: Resolve authority and path defects

For every rule or process, identify the owning source and competing copies.
Resolve path references to the actual canonical locations. Do not create
parallel root-level protocol copies. Submit any unresolved precedence question
to the maintainer before moving content.

### Step 4: Pilot a small change

Choose one low-risk, high-value example, such as documenting links and roles
in the new index. Measure the gates in §9. Do not move existing plans or
protocols in the first pilot.

### Step 5: Reclassify and migrate in approved batches

Use the approved source-of-truth matrix. For each batch: record proposed
source and destination paths; identify inbound links; update links; preserve
the old version/history; run link checks and relevant tests; record the
result in `Commander Deck/State changes/`. Stop on an unexplained broken
reference or source-of-truth conflict.

### Step 6: Accept and maintain

The maintainer reviews the final index, status/source-of-truth inventory,
conflict log, path checks, and suite results. Record acceptance and residual
work in a dated state-change record. Revisit affected parts when rules,
protocols, folder scope, or inbound references change.

## 9. Acceptance Checks

The renovation is complete only when all checks pass or an exception is
explicitly accepted with an owner and follow-up:

| Check | Acceptance condition |
| --- | --- |
| Scope and inventory | Every in-scope item is listed with a role and disposition; the encrypted archive is accounted for via its manifest. |
| Ownership | Every active rule and procedure has one canonical source; summaries and prompts link rather than duplicate. |
| Status | New or reviewed documents have an explicit status; unknown legacy status is not silently upgraded. |
| Navigation | The root index links to every current governing rule, active protocol, current plan, and archive manifest. |
| Path integrity | All changed and newly maintained internal references resolve, including references from repository prompts. |
| Historical integrity | Superseded material and prior state changes remain recoverable; archive operations follow the ECA protocol. |
| Validation | The repository's required tests run. Pre-existing failures are identified and separated from regressions; no lint is weakened to conceal a dead reference. |
| Usability | A reader unfamiliar with the tree can identify which document governs a question and where to find procedure, proposal, incident, and history. |

## 10. External Research and Limits

This protocol adapts principles from records-management guidance, not its
jurisdiction-specific legal requirements:

- [UN Archives, File Classification Schemes](https://archives.un.org/en/content/advisory-services/file-classification-schemes): function/activity-based hierarchy, retrieval, context, consistent terminology, and ownership.
- [The National Archives (UK), Filing structures](https://www.nationalarchives.gov.uk/information-management/manage-information/public-inquiry-guidance/filing-structures/): understandable, activity-based filing, retrieval, context, metadata, and controlled access.
- [U.S. National Archives, Knowing Your Records](https://www.archives.gov/records-mgmt/scheduling/knowing): scope an inventory to purpose, describe how records are used, verify findings, and revisit them as processes change.
- [The National Archives (UK), Information principles](https://www.nationalarchives.gov.uk/information-management/manage-information/planning/information-principles/): information should be fit for purpose, managed, linkable, and reusable.
- Workspace [`MaintainingProsperity.md`](../Core%20Rules/MaintainingProsperity.md), [`AuthorityDocumentCreation.md`](AuthorityDocumentCreation.md), and [`Encryption-Compression-Archiving.md`](Encryption-Compression-Archiving.md): local requirements for single-source rules, history, provenance, and safe archiving.

The guidance does not establish an optimal universal directory tree, exact
folder count, mandatory numbering scheme, or review cadence. Those choices
remain subject to the maintainer's approval and the measured usability of the
local pilot.

## 11. Final Principle

Organize the governance space so that every rule has one owner, every
procedure is findable, every proposal is visibly a proposal, and every change
leaves a trace. The folder structure serves those responsibilities; it does
not replace them.