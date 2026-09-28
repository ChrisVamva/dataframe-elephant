---
status: draft
scope: prompts/prompts/
snapshot_date: 2026-09-28
maintainer: workspace maintainer (personal name not recorded)
---

# Checkpoint Authority Prompts

## Document Control

- **Status:** draft pending an independent reader check
- **Covered folder:** `prompts/prompts/`
- **Snapshot / review date:** 2026-09-28
- **Maintainer:** workspace maintainer (personal name not recorded)
- **Intended reader and use:** anyone locating or maintaining the prompt-pointer stubs; explains which files here remain operational and where canonical prompt content is owned
- **Review triggers:** a pointer is added, removed, renamed, retargeted, or reactivated; the prompt library changes location; or the prompt-folder README changes its role

## Purpose and Authority Boundary

This document inventories and explains the current contents of the covered
folder. The folder is an operational compatibility layer: its README says it
contains session pointers, and its three prompt files are explicitly marked
`superseded` with `superseded_by` paths into the repository-level prompt
library.

This authority document is authoritative for the folder inventory, the
observed pointer/README roles, and navigation dependencies as of the snapshot
date. It is **not** authoritative for prompt instructions, evidence standards,
gate definitions, dispatch data, or prompt lifecycle decisions. Those remain
owned by the canonical library, governing protocols, and
`AGENTS.md`. This document does not reactivate superseded stubs or authorize
edits to them.

The local prompt files preserve old paths for compatibility; prompt content
is not maintained here. When a pointer needs to change, make the canonical
library change first and update the stub only to preserve accurate forwarding
information.

## Folder Context

The covered folder has five Markdown files as of this snapshot:

- `README.md` defines the operational folder contract and maps each stub to a
  canonical template or partial.
- `Research Prompt.md`, `FollowUpPrompt.md`, and `NextResearchPrompt.md` are
  superseded stubs. Their frontmatter names the canonical template in
  `prompts/templates/` and says each exists to preserve existing links.
- `CheckpointAuthorityPrompts.md` is this draft authority document. It maps
  the folder and does not contain prompt logic.

The repository-level [`prompts/README.md`](../../../prompts/README.md) calls
`prompts/` the single home for reusable prompt assets and describes this
nested transitional folder as containing only stubs and session pointers. It
identifies the templates and shared partials, specifies the template lifecycle,
and states that dispatch data is generated rather than stored in templates.

### Current pointer map

| Local file | Status in file | Canonical destination | Destination status at snapshot |
| --- | --- | --- | --- |
| [`Research Prompt.md`](Research%20Prompt.md) | `superseded` | [`research_brief`](../../../prompts/templates/research_brief.md), version 2.0 | `active` |
| [`FollowUpPrompt.md`](FollowUpPrompt.md) | `superseded` | [`followup_dispatch`](../../../prompts/templates/followup_dispatch.md), version 2.0 | `active` |
| [`NextResearchPrompt.md`](NextResearchPrompt.md) | `superseded` | [`next_research`](../../../prompts/templates/next_research.md), version 2.0 | `active` |
| [`README.md`](README.md) | operational index | [`prompts/README.md`](../../../prompts/README.md) | index of record for reusable assets |

The local README also lists `The components to investigate.md` as moved to
[`lens_reference.md`](../../../prompts/lib/lens_reference.md). That Markdown
file is **not present in the covered folder inventory**; the destination
exists in the canonical library. Its row is a migration note, not a live
pointer file.

## Governing Sources and Decisions

1. [`MaintainingProsperity.md`](../../Core%20Rules/MaintainingProsperity.md)
   is the standing local contract. Relevant rules include R1 (protocols own
   rules), R3 (one canonical copy under `prompts/`), R5 (named paths must
   exist), and R8 (preserve superseded history).
2. [`prompts/README.md`](../../../prompts/README.md) is the index of record
   for template and partial locations, lifecycle conventions, qualified gate
   IDs, and generated dispatch handling.
3. The owning protocols in
   [`Rules and Regulations/Protocols/`](../../Protocols/) govern evidence,
   research evaluation, follow-up questions, and Stage 2 procedures. A local
   pointer or this summary cannot amend them.
4. The three local prompt files state their own `superseded_by` targets and
   that they remain only to keep existing links resolving. No contrary status
   or decision was found in the four reviewed local files.

If a stub and the canonical library disagree, treat the canonical template
and its governing protocols as the source of truth. Update the stub to match
the current target; do not copy the canonical content back into this folder.

## Source Inventory

All four pre-existing in-scope Markdown files were read in full. This new
authority document was checked by author self-review and is included as the
fifth inventory item. The external template, library, protocol, and core-rule
files below are linked dependencies, not part of the inventory boundary.

| Path | Role | Status | Review mode | Disposition |
| --- | --- | --- | --- | --- |
| [`README.md`](README.md) | Operational index for local stubs | Current by content; modified 2026-09-28 | Full content reviewed | Retain as the local folder's pointer map. It identifies the root prompt library as the index of record and describes safe editing rules. |
| [`Research Prompt.md`](Research%20Prompt.md) | Compatibility pointer to research brief | `superseded`; modified 2026-09-28 | Full content reviewed | Retain while old links may exist. Do not edit canonical prompt logic here; `superseded_by` names the active template. |
| [`FollowUpPrompt.md`](FollowUpPrompt.md) | Compatibility pointer to follow-up dispatch | `superseded`; modified 2026-09-28 | Full content reviewed | Retain while old links may exist. `superseded_by` names the active template. |
| [`NextResearchPrompt.md`](NextResearchPrompt.md) | Compatibility pointer to next-research template | `superseded`; modified 2026-09-28 | Full content reviewed | Retain while old links may exist. `superseded_by` names the active template. |
| [`CheckpointAuthorityPrompts.md`](CheckpointAuthorityPrompts.md) | Folder-level authority map | `draft`; created 2026-09-28 | Author self-review; independent review pending | Retain as the folder inventory and orientation document; draft status does not authorize prompt changes. |

### Linked dependencies checked

The following targets were checked for existence on 2026-09-28. They are
outside this authority document's folder scope:

| Path | Role | Status at snapshot |
| --- | --- | --- |
| [`prompts/README.md`](../../../prompts/README.md) | Canonical prompt-library index | Current; calls itself the single home for reusable prompt assets. |
| [`prompts/templates/research_brief.md`](../../../prompts/templates/research_brief.md) | Canonical research template | `active`, version 2.0. |
| [`prompts/templates/followup_dispatch.md`](../../../prompts/templates/followup_dispatch.md) | Canonical follow-up template | `active`, version 2.0. |
| [`prompts/templates/next_research.md`](../../../prompts/templates/next_research.md) | Canonical next-research template | `active`, version 2.0. |
| [`prompts/lib/lens_reference.md`](../../../prompts/lib/lens_reference.md) | Moved lens-reference partial | Exists in library; local former source is absent by design. |
| [`MaintainingProsperity.md`](../../Core%20Rules/MaintainingProsperity.md) | Core rules governing source ownership and history | Current standing rules document. |
| [`AuthorityDocumentCreation.md`](../../Protocols/AuthorityDocumentCreation.md) | Governing authority-document procedure | Mandatory protocol. |

## Uncertainty, Conflicts, and Gaps

- No conflict was found between the local README, three stub frontmatters, and
  the root prompt-library README about where reusable content lives.
- The number of incoming links to the three superseded stubs was not
  exhaustively measured. Keep them until a separate link audit establishes
  that removal is safe and an approved decision authorizes it.
- The local README's moved-file row is historical/navigation context; it does
  not establish when or by whom the file was moved. The canonical target
  exists, but the migration activity record was not found in this folder.
- The personal identity of the prompt-library maintainer is not recorded in
  the reviewed materials.
- Current `prompts/dispatch/` outputs are generated and outside the covered
  folder. This authority document does not inventory every dispatch or claim
  they are permanent.
- No independent reader review has been completed; the authority document
  remains `draft` until the navigation check in `AuthorityDocumentCreation.md`
  §8.1 is performed.

## Update and Review Record

| Date | Reviewer | Gate results | Changes or limitations |
| --- | --- | --- | --- |
| 2026-09-28 | GitHub Copilot (author self-review) | AD:Scope pass; AD:Inventory pass; AD:Coverage pass; AD:Fidelity pass; AD:Provenance pass; AD:Conflict pass; AD:Authority pass; AD:Navigation pass; AD:Maintenance pass | Four pre-existing scoped Markdown files read in full; this authority file self-reviewed; 12 local links checked. Independent reader review and inbound-link count remain pending, so status is draft. |

## Synthesis Method

Read all four local Markdown files, retained their stated roles and statuses,
and verified the three `superseded_by` targets plus the README's moved lens
reference. Compared local statements about ownership with the repository
prompt index and the governing core rule. The document summarizes roles and
paths without copying prompt instructions. No source files were moved or
modified while preparing this authority document.