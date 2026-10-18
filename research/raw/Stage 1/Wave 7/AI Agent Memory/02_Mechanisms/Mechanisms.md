# Mechanisms — How Agent Memory Is Implemented, and How It Fails

_Date: 2026-10-11. Every factual claim cites `[S##]` from `../06_Evidence/Sources.md`. Claim-type tags: `[documented fact]` / `[reported signal]` / `[inference]`._

## 1. The write path — the least-standardised stage

- `[documented fact]` Mem0's documented write path: new messages trigger a context lookup, LLM fact extraction, deduplication/embedding, and entity extraction; `search` ranks semantic, keyword, entity, and temporal signals `[S07]`.
- `[documented fact]` Letta's core memory blocks carry a label, description, value, and a character limit (examples 5000/4000/6000 chars), are prepended to the prompt in XML-like form, and can be shared across agents via `block_ids` `[S04]`.
- `[documented fact]` Anthropic's memory tool exposes six operations — `view`, `create`, `str_replace`, `insert`, `delete`, `rename` — against files under a `/memories` prefix, executed by the *host application*, not the model `[S08]`.
- `[inference]` The **write decision** (what to store, dedupe, overwrite, or ignore) is the least-standardised and least-inspectable stage across every system examined. Letta block updates "replace the entire block content rather than appending" `[S04]`, while Mem0 extraction is additive unless `update`/`delete` is called `[S07]`. Two systems with the same "memory" label can therefore have opposite overwrite semantics.

## 2. Storage and retrieval

- `[documented fact]` Service-backed memory is a vector + metadata store with hybrid retrieval. Graphiti does vector similarity + BM25 + graph traversal with no LLM reranking, on Neo4j, FalkorDB, or Amazon Neptune `[S06]`.
- `[documented fact]` Graph-structured memory adds time: Graphiti/ Zep store "episodes," entity nodes, and relationship edges with "explicit bi-temporal tracking," support point-in-time queries, and "invalidate" edges contradicted by newer facts `[S06, S16]`.
- `[documented fact]` Research systems add self-organisation. A-MEM creates a note per memory with "contextual descriptions, keywords, and tags," links similar notes, and allows "memory evolution" where new memories update older representations `[S02]`. MemOS introduces a "MemCube" that "encapsulates both memory content and metadata such as provenance and versioning" and unifies "plaintext, activation-based, and parameter-level memories" `[S03]`.
- `[documented fact]` MemGPT's original design moves data between "fast" (context) and "slow" (external) tiers using "interrupts to manage control flow" `[S01]`.
- `[documented fact]` A third storage design skips the database entirely: the personal agents store memory as **flat Markdown files** on disk — Hermes explicitly ships no vector store, knowledge graph, Mem0 or Letta in its core `[S82, S83]`; OpenClaw defaults to a builtin SQLite index over a Markdown workspace `[S88]`. Retrieval is keyword/FTS-first rather than embedding-first by default, and both are scoped to the local profile/workspace.
- `[inference]` Only the research line (MemOS, and provenance-aware work `[S79]`) treats *provenance and versioning* as first-class. Production services mostly store content plus filters, which is exactly why consolidation can later launder a low-trust observation into apparent user history `[S79]`.

## 3. Summarisation / compaction — lossy by construction

- `[documented fact]` Anthropic describes compaction as summarising a near-limit conversation and restarting with the summary, preserving key decisions/bugs/implementation details while dropping redundant tool outputs; it advises tuning "for recall first, then precision" `[S09]`.
- `[documented fact]` Letta persists all state (messages, reasoning, tool calls) in a database so that after "compaction / eviction" old messages remain retrievable via API and retrieval tools `[S04]` — i.e., compaction removes data from the *prompt*, not from the *system*.
- `[documented fact]` Letta's docs describe "Dreaming": background subagents review recent conversations and "consolidate useful lessons," triggered after a set number of steps or on compaction `[S04]`. LangMem similarly separates a "hot path" from a "Background memory manager" that "extracts, consolidates, and updates" knowledge `[S05]`.
- `[documented fact]` The personal agents make consolidation **explicit**: OpenClaw runs a memory flush before compaction (default on) and a "dreaming" pass that distils daily notes into `MEMORY.md` `[S88]`; Hermes renders memory as a "frozen snapshot" at session start that never mutates mid-session, writing to disk immediately but only loading next session `[S82]`. Both state when consolidation happens — unlike the cloud tools, where it is invisible `[S40]`.
- `[inference]` Silent loss is structural: block systems overwrite whole blocks `[S04]`, summaries are lossy by definition `[S09]`, and background consolidation rewrites content without a user-visible diff `[S05, S79]`. Discarded detail is unrecoverable unless the raw transcript is separately persisted, as in Letta's database `[S04]` or OpenClaw's session archive `[S89]`.

## 4. Does a bigger context window remove the need for memory?

- `[documented fact]` The literature is split. "RAG or Long-Context LLMs?" reports that with sufficient resources "LC consistently outperforms RAG in terms of average performance," but RAG's "significantly lower cost remains a distinct advantage," proposing Self-Route per query `[S14]`. "In Defense of RAG" counters that long contexts lose focus, with answer quality on an "inverted U-shaped curve" and "sweet points" beating whole-context prompting at far fewer tokens `[S13]`.
- `[documented fact]` Effective capability falls well short of advertised context length: RULER finds "almost all models exhibit large performance drops as the context length increases," and of 17 long-context LMs "only half of them can maintain satisfactory performance at the length of 32K" `[S11]`. Lost in the Middle shows position-sensitive recall even for explicitly long-context models `[S12]`.
- `[documented fact]` Chroma's Context Rot study (18 models, 8 input lengths, 11 needle positions per combination) reports models "do not use their context uniformly" and that performance "grows increasingly unreliable as input length grows" `[S10]`.
- `[inference]` Long context delays the memory problem; it does not remove it. Selective storage and retrieval remain necessary because (a) effective context is far below nominal, (b) position matters, and (c) cost still scales with tokens `[S11, S12, S10, S13, S14]`.

## 5. Documented failure modes (a taxonomy)

| # | Failure | Mechanism | Anchor |
|---|---------|-----------|--------|
| F1 | **Staleness** | Old value persists until an update/overwrite fires | `[S06, S04]` |
| F2 | **Silent loss** | Compaction/block-overwrite drops detail with no diff | `[S09, S04]` |
| F3 | **Retrieval imprecision** | Similarity returns the wrong or a stale record | `[S07, S12]` |
| F4 | **Confabulation** | Extraction stores an LLM-inferred "fact" as if observed | `[S15, S79]` |
| F5 | **Poisoning** | Attacker content enters the store and is retrieved later | `[S65, S66, S69, S70, S71]` |
| F6 | **Cross-boundary bleed** | Wrong `user_id`/scope or shared store returns another's data | `[S68]` |
| F7 | **Non-determinism** | Temperature-driven extraction makes memory irreproducible | `[S15]` |

- `[documented fact]` F1 is managed, not solved: Graphiti "invalidates" contradicted edges rather than deleting history `[S06]`; Letta replaces whole blocks `[S04]`.
- `[documented fact]` F6 is demonstrated: MemLeak shows cross-user semantic leakage when multi-tenant agents share a vector store via "ordinary similarity retrieval," and ownership gating restored the clean baseline `[S68]`.
- `[inference]` These failures share one root: **memory is trusted more than its provenance warrants.** A record's origin, the fact that it was machine-inferred, and its write time are usually not stored with it `[S15, S07]`, so downstream readers cannot tell a user statement from a consolidation artefact `[S79]`.

## 6. Open mechanism questions (carried to Findings)

1. No primary source found quantifying production "cross-session contamination" or "non-determinism" rates.
2. Overwrite-vs-append semantics are undocumented for most products; only Letta (replace) and Mem0 (additive) were explicit.
3. Hermes is the only shipping **write-approval / overwrite-listing** mechanism found, and it defaults off (`write_approval: false`) `[S82]`; no cloud product surfaces an equivalent `[S40]`.
