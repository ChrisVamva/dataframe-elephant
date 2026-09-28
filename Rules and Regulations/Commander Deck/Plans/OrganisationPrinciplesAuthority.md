# Organisation Principles Authority Document

## Document Control

- **Status:** draft
- **Covered folder:** `C:\Users\user\Documents\Obsidian Vaults\Code\Arch\Opp Atlas\ByDesign\Organisation Principles\`
- **Snapshot / review date:** 2026-09-28
- **Maintainer:** workspace maintainer (assignment not recorded)
- **Intended reader and use:** workspace maintainer designing a more navigable and maintainable `Rules and Regulations/` structure
- **Review triggers:** source notes change; the destination scope changes; existing rules or file ownership change; or the authority document is approved or superseded

## Purpose and Authority Boundary

This document is a traceable synthesis of the four Markdown files found in the
covered Obsidian folder, supplemented by public records and knowledge
management guidance. It explains which organization principles can reasonably
inform a proposed renovation of this repository's `Rules and Regulations/`
area.

It is authoritative only as an inventory and interpretation of that reviewed
source set for this proposed renovation. It does not govern the source vault,
approve a repository reorganization, establish legal records obligations, or
replace the repository's existing governing documents. All four local source
notes are proposals/examples, not primary evidence that their suggested
layouts have been implemented or evaluated successfully. Recommendations
below are labeled as synthesis or recommendation rather than source-established
facts.

The actual source path is a folder named `Organisation Principles`, containing
four files named `Organisation Example*.md`; the supplied description
`Organisation Principles.` was not itself a file.

## Folder Context

### Common principles across the four examples

The examples propose organizing knowledge so readers can find, understand,
and use it. Across their different scopes, the recurring ideas are:

| Synthesized principle | Source support | Application to this repository |
| --- | --- | --- |
| Organize by durable purpose, activity, or domain rather than by whichever tool or note happens to be current. | Examples 1, 2, and 3 make this distinction explicitly in their proposed folder models. | Group governance documents by their function and lifecycle; do not create a folder for every individual protocol or issue. |
| Separate unlike content and distinguish ownership. | Examples 2 and 3 distinguish architecture, projects, workflows, tools, research, prompts, and strategic work; Example 4 recommends separate opportunity, research, experiment, and system layers. | Keep rules, procedures, plans, incidents, status history, and prompt pointers distinguishable; each rule should have one owning source. |
| Give readers an index or other clear navigation entry point. | Examples 1, 2, 3, and 4 each recommend an index or dashboard. | Add a concise `Rules and Regulations/README.md` index that links to the existing authoritative documents. |
| Preserve context and support discovery through consistent names and metadata. | Examples 1, 2, and 4 suggest descriptive naming and lightweight status/type/date metadata; Example 3 provides a prompt metadata example. | Use descriptive document titles and a small set of status/scope/owner fields where they aid lifecycle control. Do not require frontmatter in every file until the owner decides on a standard. |
| Introduce structure incrementally and avoid over-modeling. | Example 1 says to move obvious files first and add metadata gradually; Example 2 says not to create every subfolder until needed; Example 3 separates system layers but describes proposed placements; Example 4 recommends a large proposed taxonomy. | Inventory and classify first; make reversible, batched changes only after link and ownership checks. Treat detailed example trees as hypotheses, not templates to copy wholesale. |
| Separate current material from superseded or historical material without losing it. | Examples 1, 2, 3, and 4 include archive/history areas and status values. | Preserve prior plans, incidents, and state changes; do not delete or silently overwrite governing history. Use the existing archive protocol for encrypted archives. |

### Differences and tensions in the source set

The examples address different hypothetical folders and do not prescribe one
shared taxonomy. Their proposed top-level trees vary substantially. They also
place related content differently: Examples 2 and 3 distinguish tools from
workflows and prompts from research, while other examples group material by
project or learning domain. Example 4 recommends a more extensive multi-layer
tree; Example 2 cautions against creating folders before the material warrants
them. These are not factual contradictions so much as context-dependent
proposals. The synthesis therefore carries forward the principles and leaves
the actual target structure to a repository-specific decision.

No source note supplies an observed inventory of the current repository's
`Rules and Regulations/` tree, measured retrieval results, a named approving
owner, or empirical proof that its suggested taxonomy works. Those gaps must
not be filled by inference.

### External guidance reviewed

| Source | What it supports | Limits on use |
| --- | --- | --- |
| [United Nations Archives, File Classification Schemes](https://archives.un.org/en/content/advisory-services/file-classification-schemes) | A file plan can use a hierarchy from functions to activities to transactions; classification should reflect what an organization does and support retrieval, context, consistent terminology, and ownership. | UN records guidance; used as a design analogy, not as a binding structure for this repository. |
| [The National Archives (UK), Filing structures](https://www.nationalarchives.gov.uk/information-management/manage-information/public-inquiry-guidance/filing-structures/) | A file plan should be understandable to users, classify information by activities, support efficient filing and retrieval, preserve the context of records, and allow metadata and access controls to be managed. | Guidance is written for public inquiries; used here as design guidance, not as a legal requirement for this private repository. |
| [The National Archives (UK), Information principles](https://www.nationalarchives.gov.uk/information-management/manage-information/planning/information-principles/) | Information should be managed, fit for purpose, standardized/linkable, and reusable; public-sector principles are organized as a shared framework. | UK public-sector context; only the general design lessons are applied. |
| [The National Archives (UK), Knowledge principles](https://www.nationalarchives.gov.uk/information-management/manage-information/planning/knowledge-principles/) | Knowledge capture and sharing can support organizational learning and reuse; captured information is not a substitute for a broader knowledge-management practice. | Written for the Civil Service; informs, but does not dictate, this repository's choices. |
| [U.S. National Archives, Guide to the Inventory, Scheduling, and Disposition of Federal Records](https://www.archives.gov/records-mgmt/scheduling) | Records management proceeds through knowing/inventorying records, scheduling, approvals, implementation, and updates. | Federal agency guidance; not binding here. The relevant analogy is inventory, explicit lifecycle, and review before disposition. |
| [U.S. National Archives, Knowing Your Records](https://www.archives.gov/records-mgmt/scheduling/knowing) | An inventory's scope and detail should match its goal; inventories help identify what exists, how it is used, and opportunities to consolidate, while verification checks the accuracy of findings. | Federal agency guidance; the proposed plan borrows the inventory-and-verify sequence, not federal disposition rules. |
| [U.S. National Archives, Records Management Regulations and Guidance](https://www.archives.gov/records-mgmt/policy) | Records management has policies, schedules, and guidance for creation, management, and disposition. | Federal scope; repository-specific policy remains controlling. |

Search note: a targeted DuckDuckGo HTML search for official file-plan and
records-management guidance returned the UN Archives and NARA results above.
The pages were then retrieved directly and checked. The configured Tavily
search service returned an invalid-key error, and Google search returned a
JavaScript challenge, so discovery was limited to the working DuckDuckGo
results and the listed official pages; it was not a systematic literature
review.

## Governing Sources and Decisions

This is a source synthesis, not a new repository rule. The proposed
`Rules and Regulations/` renovation remains subordinate to:

- [MaintainingProsperity.md](../../Core%20Rules/MaintainingProsperity.md), which owns the standing workspace recurrence-prevention rules.
- [AuthorityDocumentCreation.md](../../Protocols/AuthorityDocumentCreation.md), which governs folder-level authority documents.
- [Encryption-Compression-Archiving.md](../../Protocols/Encryption-Compression-Archiving.md), which governs lossless archives and preservation of history.
- [Research-Evaluation.md](../../Protocols/Research-Evaluation.md), which governs claim/evidence distinctions and uncertainty.

The suggested decisions for downstream consideration are recommendations,
not approved rules:

1. Keep the existing division between `Core Rules/`, `Protocols/`, and
   `Commander Deck/`, but make their boundaries and links explicit.
2. Make the folder's actual index the navigation layer, and keep each rule or
   procedure in one owning document.
3. Pilot a small, reversible organization rather than copying one of the
   source folder trees wholesale.
4. Inventory and classify before moving, renaming, archiving, or deleting.

## Source Inventory

All four in-scope Markdown files were read in full. Their status is
`proposal/example` because they describe suggested layouts and use future or
recommendation language; no implementation verification is included in the
notes.

| Path | Role | Status | Review mode | Disposition |
| --- | --- | --- | --- | --- |
| `C:\Users\user\Documents\Obsidian Vaults\Code\Arch\Opp Atlas\ByDesign\Organisation Principles\Organisation Example.md` | Research1 organization example | Proposal/example; modified 2026-09-27 | Full content reviewed | Source for purpose-based domains, staged implementation, index, naming, and non-overfragmentation principles. |
| `C:\Users\user\Documents\Obsidian Vaults\Code\Arch\Opp Atlas\ByDesign\Organisation Principles\Organisation Example 2.md` | Working Environment Architecture example | Proposal/example; modified 2026-09-27 | Full content reviewed | Source for separating architecture, active projects, reports, workflows, tools, decisions, templates, and archive; avoid adopting its exact tree without local evidence. |
| `C:\Users\user\Documents\Obsidian Vaults\Code\Arch\Opp Atlas\ByDesign\Organisation Principles\Organisation Example 3.md` | Python learning/workspace example | Proposal/example; modified 2026-09-27 | Full content reviewed | Source for distinguishing conceptual reference, setup, workflows, learning, apps, projects, and metadata. |
| `C:\Users\user\Documents\Obsidian Vaults\Code\Arch\Opp Atlas\ByDesign\Organisation Principles\Organisation Example 4.md` | Opp Atlas system example | Proposal/example; modified 2026-09-27 | Full content reviewed | Source for distinguishing durable project state, architecture, opportunities, research, experiments, prompts, Commander Deck strategy, and archive; emphasizes Commander Deck as strategic workspace rather than permanent system state. |

## Uncertainty, Conflicts, and Gaps

- The four examples are internal recommendations, not validated standards or
  measured outcomes.
- The source folder contains no unified vocabulary or cross-example decision
  record selecting one taxonomy.
- The source notes do not document a completed inventory of the current
  `Rules and Regulations/` directory. That inventory is maintained separately
  in the proposed [CommanderPlan.md](CommanderPlan.md).
- The owner/maintainer who can approve policy changes is not named in the
  reviewed sources.
- Search-engine research was limited by unavailable search access; the direct
  official guidance above is a small, scoped source set.
- Whether status metadata, numbered directories, or additional subfolders are
  worth maintaining requires an owner decision and a pilot.

## Update and Review Record

| Date | Reviewer | Gate results | Changes or limitations |
| --- | --- | --- | --- |
| 2026-09-28 | GitHub Copilot (author self-check) | AD:Scope pass; AD:Inventory pass; AD:Coverage pass; AD:Fidelity pass; AD:Provenance pass; AD:Conflict pass; AD:Authority pass; AD:Navigation pass; AD:Maintenance pass | Draft pending maintainer approval. Local sources reviewed in full; official external pages retrieved directly; live search unavailable. |

## Synthesis Method

The four notes were reviewed as separate proposals, not merged as if they
described one implemented system. Shared recommendations were grouped by
principle; differences in scope and proposed taxonomy were retained. External
guidance was used as an independent design check for retrieval, context,
metadata, inventory, lifecycle, and update practices. No folder was modified
and no local source was moved or renamed while preparing this document.