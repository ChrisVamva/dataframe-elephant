# Design — Memory Governance Record (MGR) v0

_Date: 2026-10-11. This is a **design proposal**, not a finding. Every design rule is anchored to a verified precedent in `../06_Evidence/Sources.md`. Claim-type tags: `[documented fact]` / `[inference]` / `[inference — design]`._

## 1. The problem the record solves

Five documented gaps, taken together, describe a system that is trusted more than its provenance warrants:

- `[documented fact]` Consolidation rewrites low-trust observations as apparent user history; without provenance, vulnerable memories reached up to 1.000 ASR `[S79]`.
- `[documented fact]` Cloud products expose no user-visible memory change log — Microsoft states memory actions "don't generate audit log entries" `[S40]` — though the self-hosted agent Hermes stages writes for approval and lists every overwritten/removed entry, default off `[S82]`.
- `[documented fact]` Deletion is soft and non-local — turning memory off does not delete past chats, deleted saved-memory logs may persist up to 30 days, and deleting a memory does not remove its mentions elsewhere `[S37]`; GDPR Art. 17 has no mechanism for derived representations `[S61, S64]`.
- `[documented fact]` Block-style memory replaces content wholesale while service memory is additive, so overwrite semantics are unstated and inconsistent `[S04, S07]`.
- `[documented fact]` Poisoned memories persist and drift behaviour across sessions and survive most defenses `[S67, S71, S69]`.
- `[inference]` The common root is the absence of a **record**: memorised content moves through the system without carrying where it came from, who wrote it, what it is allowed to cross, or how it changed.

## 2. What already exists to build on

- `[documented fact]` Research has begun to treat provenance as first-class: MemOS "encapsulates both memory content and metadata such as provenance and versioning" `[S03]`; the PPMF provenance gate blocks low-trust writes `[S79]`; MemSentry gates writes with Accept/Review/Quarantine `[S78]`.
- `[documented fact]` Two shipping platforms expose the control primitives: Azure AI Foundry memory has item-level CRUD, store-level TTL, and direct remember/forget with quotas `[S46]`; Vertex Memory Bank records memory revisions under IAM `[S45]`.
- `[documented fact]` One shipping *personal* agent already implements the review primitive: Hermes stages memory writes for approval (`/memory pending|approve|reject`) and its approval output "lists the full text of every entry it overwrote or removed," with background writes tagged `[auto]` — but it defaults off (`write_approval: false`) `[S82]`. OpenClaw ships the on-disk counterpart: plain Markdown memory plus incognito and per-conversation scoping `[S88, S89]`.
- `[documented fact]` The MCP `memory` server already models content as a graph with explicit `delete_*` and `search_nodes` operations `[S34]`.
- `[documented fact]` The Council of Europe draft asks for exactly the missing pieces: cross-layer deletion "including caches and vector stores," separate read vs create/modify/transmit/delete permissions, agent inventories, revocable credentials, and "a point of effective human review" `[S64]`.
- `[inference — design]` The record is therefore an **envelope and a rule set** that any of the above could carry, not a new storage engine.

## 3. The record (MGR fields)

| Field | Meaning | Anchor |
|-------|---------|--------|
| `memory_id` | Stable id, never reused | `[S34]` |
| `content` | The remembered text / fact / preference | `[S07]` |
| `source_type` | `user_statement` \| `observed_tool_output` \| `imported_document` \| `model_inference` \| `agent_consolidation` | `[S79, S65]` |
| `source_ref` | The turn / message / tool-call id, **or** the parent `memory_id`s if derived | `[S03, S79]` |
| `scope` | `session` \| `project` \| `user` \| `team/tenant` | `[S07, S68]` |
| `trust_class` | **attested** (user-stated) > **witnessed** (observed) > **inferred** (machine-derived) | `[S79, S78]` |
| `created_at` / `last_verified_at` / `expires_at` | Timestamps; TTL optional | `[S46, S06]` |
| `write_history` | Append-only `{op, actor, t, reason}` — create / update / merge / invalidate / forget | `[S40, S79]` |
| `status` | `active` \| `superseded` \| `tombstoned` | `[S06, S61]` |
| `sensitivity` | Redaction / do-not-share flag; secrets never persisted | `[S24]` |

## 4. The rules (v0)

- **R1 — Append, don't overwrite.** Consolidation/update creates a *new* record linked to its parents with the derivation stated; the parent becomes `superseded`, not deleted. (Contrast: Letta blocks replace wholesale `[S04]`; Graphiti invalidates edges rather than deleting `[S06]`.) This directly counters provenance laundering `[S79]`.
- **R2 — Trust class is monotone downward.** Consolidation can never upgrade a class: a repeated `model_inference` stays `inferred`, so a summary is never served as if the user said it `[S79]`.
- **R3 — Retrieval is trust-gated.** An action at risk level *X* may consume only records of `trust_class` ≥ the task's threshold; anything `inferred` and action-relevant requires user confirmation. (Precedent: MemSentry's Accept/Review/Quarantine `[S78]`; PPMF's gate `[S79]`.)
- **R4 — Scope is explicit and enforced at retrieval.** Records carry their boundary and retrieval filters on it; ownership gating is what restored the clean baseline in MemLeak `[S68]`.
- **R5 — Forget is a tombstone that propagates.** `forget(id)` writes `tombstoned` and marks derived records `superseded`; the host must be able to separate raw transcripts from served memory so erasure reaches the vector/summary layer, not only the prompt. (Anchors: the draft's cross-layer delete `[S64]`; OpenAI's 30-day log retention `[S37]`; Art. 17 `[S61]`.)
- **R6 — Every record has a visible history.** The user can see what changed, when, and why — closing the "no audit log entries" gap `[S40]`. (Nearest shipping precedent: Hermes' approval / overwrite listing `[S82]`.)
- **R7 — Staleness is re-verified, not served.** A record past `expires_at` is re-checked before use; contradiction creates a new record and invalidates the old (Graphiti pattern `[S06]`; TTL `[S46]`).
- **R8 — A human review point for low-trust writes.** Writes below the trust threshold queue for review rather than silently entering long-term memory `[S78, S64, S82]`.

## 5. Honest limits of this design

- `[inference — design]` The record cannot fix **authoring**, only **provenance**: if the extractor mislabels a model inference as user-stated, R2/R3 inherit the error. Correct labelling is a separate verification problem.
- `[inference — design]` R5 depends on the storage stack exposing its raw → derived chain; where a vendor collapses that chain (cloud memory with no change log `[S40]`), the record is advisory only.
- `[inference — design]` Retention and auditability are **governance** problems before they are technical ones. The nearest legislated beachheads are the CoE draft's cross-layer-delete and split-permission clauses `[S64]` and the enterprise platforms' existing CRUD/TTL/revision primitives `[S46, S45]` — not the consumer tools, which are on-by-default with the weakest controls `[S40, S37]`.
- `[inference — design]` This v0 is a **wedge for the governance debate** (what should a memory record carry?), not an implementation. A shippable version would start where the primitives already exist: enterprise memory stores `[S46, S45]`, the MCP memory server `[S34]`, and — for R6/R8 — the local-first agents, whose files are already inspectable and whose approval queue already exists (switched off) `[S82, S88]`.
