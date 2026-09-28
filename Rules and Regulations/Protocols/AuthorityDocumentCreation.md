# Authority Document Creation Protocol

## Status

This protocol is mandatory for every person, agent, or process that creates or
maintains an authority document intended to represent the context of a folder
in this workspace.

---

## 1. Purpose

An **authority document** is a maintained, folder-level synthesis that lets a
reader understand a folder's purpose, contents, governing material, current
state, dependencies, decisions, and unresolved questions without first
reconstructing that context from every file.

It is a navigational and contextual authority for the folder it names. It is
not a substitute for the underlying evidence, an archive, or a new source of
truth for claims that belong to source documents. It must link readers to the
documents that establish details and state which document governs when rules
or records differ.

The protocol establishes standards for:

- **Extraction:** identifying and faithfully representing material folder
  content, its source, context, and uncertainty.
- **Compression:** reducing repeated or low-value detail while retaining the
  information needed to understand and navigate the folder.
- **Authority-building documentation:** making the synthesis's scope, status,
  stewardship, provenance, limits, and update path explicit.

Semantic compression is lossy by design. It must not be confused with the
byte-for-byte lossless compression and preservation required by
[Encryption-Compression-Archiving.md](Encryption-Compression-Archiving.md).

---

## 2. Research Basis and Operational Conclusions

The following sources were reviewed on 2026-09-28. Their findings inform this
protocol; they do not prescribe a universal folder-summary format.

| Source | Finding relevant to this protocol | Operational conclusion |
| --- | --- | --- |
| [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) and [PROV-O](https://www.w3.org/TR/prov-o/) (W3C Recommendations, 2013) | Provenance describes entities, activities, agents, derivations, and responsibility. Provenance helps readers assess trust, and a provenance record itself can have provenance. | Name the source items, synthesis activity/date, responsible maintainer, and derivation links. Folder membership and the act of summarizing are themselves relevant context. |
| [Maynez et al., “On Faithfulness and Factuality in Abstractive Summarization”](https://aclanthology.org/2020.acl-main.173/) (ACL 2020) | Human evaluation found generated summaries prone to unsupported or unfaithful content; text-overlap measures alone did not establish faithfulness. | Validate each material summary statement against the folder sources. Readability or brevity is not evidence of fidelity. Do not fill gaps with plausible-sounding context. |
| [Fabbri et al., “SummEval: Re-evaluating Summarization Evaluation”](https://aclanthology.org/2021.tacl-1.24/) (TACL 2021) | The work compares multiple automatic metrics and human judgments, illustrating that summarization quality is not captured by one measure alone. | Review authority documents across separate dimensions: coverage, factual fidelity, traceability, usability, and uncertainty handling. Do not use length or compression ratio as a proxy for quality. |
| [Diataxis](https://diataxis.fr/) | Documentation content and organization should respond to distinct reader needs and uses. | State the reader and intended tasks first; organize the synthesis for retrieval and use, not as a miniature copy of the folder. |
| [Architectural Decision Records (ADR), templates and practices](https://adr.github.io/adr-templates/) | Common decision records capture context, decision, rationale, status, and consequences; option trade-offs help explain why a decision was made. | Preserve important decisions with their rationale, status, alternatives or trade-offs, and consequences, rather than recording conclusions alone. This is practice guidance, not a formal standard. |
| Workspace [Research-Evaluation.md](Research-Evaluation.md) | Research must be traceable, scoped, uncertainty-aware, and explicit about evidence, limitations, conflicts, and falsifiers. | Apply the workspace's existing claim/evidence distinctions and do not promote confidence while summarizing. |
| Workspace [TransitionStage2.md](TransitionStage2.md) | Extraction must preserve source wording where material, uncertainty, boundaries, and source-to-section provenance; judgment calls belong in a log. | Inventory sources, trace material statements to exact files/sections, carry forward conflicts and gaps, and record synthesis decisions. |

### 2.1 Values Established by the Research

These values are related but distinct. A document does not pass merely because
it is concise or has many links.

| Value | Meaning | Required behavior |
| --- | --- | --- |
| Extraction coverage | Material content is identified, including relevant rules, decisions, relationships, operational state, limitations, and open questions. | Inventory every item in the declared folder scope and account for each item. Do not imply exhaustive content review if files were skipped or only inspected by metadata. |
| Extraction fidelity | The synthesis says no more, and no less materially, than the sources support. | Preserve qualifiers, dates, versions, units, boundaries, conditions, and negative findings. Distinguish fact, reported signal, inference, and recommendation using `Research-Evaluation.md`. |
| Provenance | Readers can inspect where a statement came from and how the synthesis was produced. | Link every material statement or compact grouped statement to source paths and headings; record the inventory snapshot date and maintainer. |
| Useful compression | Repetition is removed while decision-relevant context and navigation survive. | Keep the concepts, dependencies, decisions, exceptions, and caveats needed for the intended reader. Move detail to linked sources instead of duplicating it. |
| Calibrated authority | The document's mandate and limits are clear, and its claims do not gain authority merely by appearing in a polished summary. | Say what the document governs, what remains governed by other documents, which sources are controlling, and where the folder has unresolved conflicts. |
| Maintainability | The synthesis remains dependable as the folder changes. | Record status and review information; update it when sources, decisions, folder scope, or governing rules change. Preserve revision history according to applicable workspace rules. |

There is no universal target for words saved, compression ratio, or summary
length. Choose the smallest synthesis that passes the quality gates in §8 for
its declared audience and use.

---

## 3. Authority and Source Precedence

1. An authority document is authoritative for its **declared folder map,
   scope, source inventory, and synthesized orientation**, as of its stated
   review snapshot.
2. It does not make an underlying claim more reliable, convert an inference
   into a fact, or replace evidence in a cited source.
3. A source document remains the point of inspection for its detailed claims,
   terms, evidence, and original context. A governing protocol or decision
   takes precedence over the authority document's paraphrase of that rule.
4. The authority document must link to the controlling rule or decision when
   one is explicitly designated. Do not invent a hierarchy between sources
   where the workspace has not established one.
5. When sources conflict, preserve the conflict and cite both sides. Identify
   a controlling source only when the source set or an existing rule supports
   that choice. Otherwise record the conflict as unresolved and do not silently
   reconcile it.
6. Historical, superseded, draft, and derivative material must be labeled as
   such. Do not present it as current guidance merely because it is in the
   folder.

---

## 4. Non-Negotiable Rules

1. **Declare the boundary.** State the exact folder covered, what is included
   and excluded, the intended reader, and the tasks the synthesis supports.
2. **Account for every item.** Inventory files under the declared scope,
   including nested folders. Assign each item a disposition and review mode.
   A metadata-only, inaccessible, unreadable, or deliberately excluded item
   must be marked and explained.
3. **Do not claim exhaustive review without it.** If any in-scope material was
   not read or could not be inspected, disclose the gap prominently and limit
   the coverage claim accordingly.
4. **Trace material statements.** Use workspace-relative links to sources,
   with section headings where practical. A citation to a whole folder is not
   enough to support a specific statement.
5. **Do not upgrade evidence.** Preserve source qualifiers, claim types,
   confidence, dates, and uncertainty. A synthesis is not corroboration.
6. **Keep context that changes interpretation.** Do not discard conditions,
   scope boundaries, exceptions, counterevidence, dependencies, or unresolved
   questions to make the document shorter.
7. **Separate description from judgment.** Label synthesis, inference,
   recommendation, and operational status as such; keep decision rationale
   distinct from evidence.
8. **Prefer links over duplicated rules.** Restate only enough to orient the
   reader. Link to the owning protocol, record, or detailed source rather than
   creating a second copy likely to drift.
9. **Show changeability.** Record status, snapshot/review date, maintainer or
   responsible role, and update triggers. Date-sensitive content must show
   when it was checked.
10. **Preserve history.** Revise without silently erasing material decisions or
    prior status. Follow workspace-specific versioning and archive rules.

---

## 5. Source Inventory and Extraction Model

### 5.1 Inventory Fields

Maintain a source inventory in the authority document or an explicitly linked
inventory. Each in-scope item must have:

| Field | Required content |
| --- | --- |
| Path | Workspace-relative path, linked when supported |
| Role | Governing rule, evidence/source, decision record, implementation, status/history, derivative, or other clearly named role |
| Status | Current, draft, superseded, historical, archived, unknown, or the source's stated status |
| Review mode | Full content reviewed, metadata only, inaccessible/unreadable, or excluded |
| Disposition | What context it contributes, why it is omitted, or where its relevant content is represented |

Do not infer that a file is unimportant because it is short, old, or not linked
from another file. If files are grouped for scale, give the group a clear
selection rule and preserve an auditable list of member paths.

### 5.2 Extraction Record

Before drafting the synthesis:

1. Record the folder purpose, reader, intended use, included paths, excluded
   paths, and snapshot date.
2. Read each in-scope text source in full where feasible. For non-text assets,
   use a suitable reader or record the limitation. Mark the review mode for
   each item.
3. Identify, at minimum, the folder's purpose, authoritative sources, key
   entities and relationships, active processes or state, important
   decisions and rationale, dependencies, constraints, exceptions, evidence
   limitations, conflicts, and open questions where present.
4. Trace each material extracted item to a source path and section. Preserve
   exact wording for important rules and claims when paraphrasing could alter
   their meaning. Otherwise label a material paraphrase as a synthesis.
5. Record each non-obvious choice: why an item was included, grouped, omitted,
   classified as current or historical, or treated as controlling.

---

## 6. Compression and Representation Rules

1. **Compress repetition, not distinctions.** Merge genuinely duplicate
   descriptions, but keep different scopes, versions, actors, statuses, and
   interpretations separate.
2. **Retain decision context.** A decision summary includes its problem or
   context, the decision, rationale, material alternatives or trade-offs,
   consequences, status, and source link when those are available.
3. **Retain operational conditions.** Keep relevant dates, version identifiers,
   locations, units, preconditions, inputs, outputs, dependencies, and failure
   conditions. Never detach a metric or claim from its conditions.
4. **Keep absence explicit.** Use clear markers such as `not stated in the
   reviewed sources`, `not reviewed`, or `unresolved`; do not turn an unknown
   into a negative finding.
5. **Preserve meaningful dissent.** Represent conflicting sources and
   alternative positions side by side, with their provenance. Summarize only
   after showing whether and how a conflict was resolved.
6. **Design for retrieval.** Use descriptive headings, stable terms, concise
   tables for inventories and relationships, and links to detail. Organize by
   the reader's likely questions rather than copying source order by default.
7. **Avoid false completeness.** A one-paragraph overview may be useful but
   cannot stand in for inventory, limitations, or provenance where these are
   material to the folder.
8. **Avoid unmeasured compression targets.** Do not optimize for a fixed
   percentage reduction or word count unless a specific consumer imposes that
   constraint. If constrained, document what information was moved, omitted,
   or made less accessible and why.

---

## 7. Creation and Update Procedure

### Step 1: Define the document's mandate

Name the target folder, reader, intended tasks, and explicit exclusions. Decide
whether the document is a navigation map, current-state summary, governance
summary, or a combination. Do not imply that it is a primary research report
or an exhaustive copy of folder contents.

### Step 2: Inventory and classify

List every item within scope. Classify its role, status, review mode, and
disposition under §5.1. Resolve the folder boundary before claiming coverage.

### Step 3: Extract and trace

Read sources, extract the context required in §5.2, preserve evidence classes
and uncertainty, and record judgment calls. Link to path and heading rather
than copying large source passages.

### Step 4: Synthesize for use

Write the overview and structured sections using the required outline in §9.
Use concise paraphrase only where meaning is preserved. Keep material claims,
rules, decisions, exceptions, dependencies, and unresolved issues traceable.

### Step 5: Reconcile and challenge

Check key statements against their cited sources. Compare sources for
contradictions, supersession, scope differences, and date sensitivity. Look
for a credible exception or counterexample in the folder. Do not manufacture
consensus.

### Step 6: Validate navigation and authority

Check every local link, heading anchor, source status, inventory entry, and
stated authority boundary. Confirm the document points to the governing source
for any rule it summarizes and does not contradict it.

### Step 7: Record review and maintain

Record gate results and reviewer/date. Update the document when an in-scope
file is added, removed, renamed, revised, superseded, or reclassified; when a
decision or governing rule changes; when material links break; or when a
stated review date arrives. Preserve applicable history rather than silently
replacing it.

---

## 8. Acceptance Gates

The authority document is `accepted` only when all mandatory gates pass. Record
each result in its review record. A failed gate requires `revise` or `reject`,
with the defect and smallest corrective action named.

| Gate | Pass condition |
| --- | --- |
| AD:Scope | The covered folder, audience, purpose, intended tasks, and exclusions are explicit. |
| AD:Inventory | Every in-scope item is accounted for with status, review mode, and disposition. Any gap is disclosed; the completeness claim matches actual review. |
| AD:Coverage | The synthesis represents the material folder context required for its purpose, including important rules, decisions, relationships, dependencies, state, limitations, and open questions where present. |
| AD:Fidelity | Every material claim is supported by the cited source and retains relevant conditions, dates, boundaries, and uncertainty. No evidence or confidence is promoted. |
| AD:Provenance | A reader can trace material statements to workspace-relative source paths and sections; synthesis decisions and authorship/maintenance are recorded. |
| AD:Conflict | Contradictions, dissent, missing evidence, and status differences are visible and not silently reconciled. |
| AD:Authority | The document states what it governs, what it does not govern, and which sources control details or rules. It does not invent precedence. |
| AD:Navigation | Local links resolve, headings are descriptive, and readers can reach source-level detail without searching the folder from scratch. |
| AD:Maintenance | Status, review/snapshot date, maintainer, and update triggers are present; superseded content is identified. |

### 8.1 Review Questions

Before acceptance, a reviewer who did not draft the synthesis should be able
to answer:

1. What is this folder for, and what is outside its scope?
2. Which documents govern its work, and which are evidence, decisions, or
   historical context?
3. What are the important concepts, relationships, processes, and current
   decisions?
4. Which statements are uncertain, disputed, date-sensitive, or not reviewed?
5. Where can each important statement be checked in the original materials?
6. What change would make this authority document stale?

If the answers require inventing context or treating the summary as proof, the
document does not pass.

---

## 9. Required Document Outline

An authority document may add sections appropriate to its folder, but must
include these elements. A clearly labeled “None identified” is acceptable
where a category genuinely does not apply.

```markdown
# [Folder or subject] Authority Document

## Document Control
- Status: draft | accepted | under_review | superseded
- Covered folder:
- Snapshot / review date:
- Maintainer or responsible role:
- Intended reader and use:
- Review triggers:

## Purpose and Authority Boundary
[What this document represents, what it governs, what it does not replace.]

## Folder Context
[Purpose, scope, key concepts, relationships, processes, and current state.]

## Governing Sources and Decisions
[Linked rules and decisions, their status, rationale, consequences, and precedence when explicit.]

## Source Inventory
| Path | Role | Status | Review mode | Disposition |
| --- | --- | --- | --- | --- |

## Uncertainty, Conflicts, and Gaps
[Disputed interpretations, missing information, limitations, and unresolved questions.]

## Update and Review Record
| Date | Reviewer | Gate results | Changes or limitations |
| --- | --- | --- | --- |
```

For very large folders, the source inventory may be a separate maintained file,
but the authority document must link to it, state its snapshot date, and
describe any inventory grouping rule.

---

## 10. Interpretation of “Entire Folder”

“Entire folder” means that the authority document takes responsibility for
accounting for the declared folder contents, not that every byte or detail is
reproduced in the synthesis.

- Every item is inventoried.
- Every relevant text document is reviewed in full unless its review mode
  explicitly records otherwise.
- Each item is included, represented through a traceable summary, excluded
  with a reason, or marked as unreviewed/inaccessible.
- Generated databases, archives, binaries, and large data artifacts may be
  represented by their manifest, schema, metadata, or declared role where
  reading the raw payload is not appropriate; the choice and limitation must
  be explicit.
- No item may disappear from the account merely because it is redundant,
  inconvenient, historical, or conflicts with the preferred narrative.

---

## 11. Final Principle

An authority document succeeds when a new reader can orient, locate governing
material, understand the folder's important context and limits, and follow
material statements back to their sources. It compresses the work of
reconstruction; it does not erase the evidence, uncertainty, or history that
make reconstruction trustworthy.