# Concepts — What "Memory" Means for an AI Agent

_Date: 2026-10-11. Every factual claim cites `[S##]` from `../06_Evidence/Sources.md`. Claim-type tags: `[documented fact]` / `[reported signal]` / `[inference]`._

## 1. The context window is not memory

- `[documented fact]` The context window is the working set an agent sees for one call; it is bounded and (in most tools) ephemeral. MemGPT's founding framing is that the context window is "fast memory" and external stores are "slow memory," with "virtual context management" moving data between tiers `[S01]`.
- `[documented fact]` Persisting anything beyond the window requires an explicit mechanism: a file the tool reads, a store the service queries, or a summary written back into the prompt. Anthropic's memory tool is explicitly **client-side** — Claude only issues file operations and the *application* executes them against a `/memories` prefix you map to your own storage `[S08]`.
- `[inference]` "Memory" is therefore not one thing but a family of mechanisms with different lifetimes, scopes, and control surfaces. Treating them as one feature is the category error the CAM idea warned about.

## 2. A working taxonomy (six types)

| # | Type | What it is | Where it lives | Anchor |
|---|------|-----------|----------------|--------|
| 1 | **Session / context** | The turns of the current interaction | In-memory, per call | `[S01]` |
| 2 | **Explicit instruction files** | Human-authored rules/notes read into the prompt | Repo or home dir | `[S17, S20, S26, S28]` |
| 3 | **Searchable history** | Prior conversations, retrievable on demand | Vendor cloud or local DB | `[S37, S38, S44]` |
| 4 | **Summarised / compacted state** | A lossy digest written back after context fills | Prompt / store | `[S09]` |
| 5 | **Extracted memory records** | Facts the system decides to store (add/update/delete) | Vector store / DB | `[S07, S15]` |
| 6 | **Knowledge / temporal graphs** | Entities + relations + time, often with invalidation | Graph DB | `[S06, S16, S34]` |

- `[documented fact]` Types 2 and 3 dominate shipping coding agents: Claude Code layers `CLAUDE.md` files (managed → user → project → local) with **auto memory** notes it writes itself `[S17]`; Cline's "Memory Bank" is a file convention the agent re-reads because it "resets completely between sessions" `[S22]`; Copilot ships instructions rather than a memory store `[S20]`.
- `[documented fact]` Type 5/6 dominate memory *services*: Mem0's write path extracts facts, dedupes, embeds, and supports `add`/`update`/`delete` `[S07, S15]`; Zep/Graphiti models entities and edges with "explicit bi-temporal tracking" and "temporal edge invalidation" `[S06, S16]`.
- `[documented fact]` A seventh **implementation pattern** — not a new type — is *local-first Markdown on disk*: Hermes keeps two bounded files (`MEMORY.md` ≤2,200 chars, `USER.md` ≤1,375 chars) plus FTS5 session search `[S82]`; OpenClaw keeps `MEMORY.md`, daily `memory/YYYY-MM-DD.md` notes, `USER.md`, and `DREAMS.md`, with a Markdown workspace and no embedded vector store in the default engine `[S88]`. This is the pattern the personal/autonomous agents use, and it is the most inspectable of all: "there is no hidden state" `[S87]`.
- `[inference]` The user-facing question "what does it remember?" has no single answer: for the same product it can mean an instruction file (human-controlled, inspectable) *and* an auto-extracted record (machine-controlled, often not inspectable).

## 3. Scope is the second axis

- `[documented fact]` Memory is scoped, and the scope is what makes it useful or dangerous. Claude Code's auto memory is keyed to the **git repo** so worktrees and subdirectories share one store, machine-local at `~/.claude/projects/<project>/memory/` `[S17]`.
- `[documented fact]` Windsurf/Devin Cascade memories are workspace-associated and saved locally at `~/.codeium/windsurf/memories/`, not committed `[S23]`; OpenAI Codex memories convert "useful context from eligible prior chats into local memory files" under `~/.codex/memories/` `[S24]`.
- `[documented fact]` Service memory is scoped by identifiers such as `user_id`, `agent_id`, `run_id` (Mem0) `[S07]` or a "scope" quota unit (Microsoft Foundry: max 100 scopes/store, 10,000 memories/scope) `[S46]`.
- `[inference]` The scoping taxonomy is: **session → project/workspace → user → team/tenant**. Cross-session contamination and multi-tenant leakage `[S68]` are both scope failures, differing only in which boundary was crossed.

## 4. Why it matters (the stakes)

- `[documented fact]` Memory is what lets a system stop asking for the same context twice; the CAM framing calls this "better recall can reduce repeated explanation" `[CAMidea 1.3]`. Concretely, Gemini requires "Memory turned on" for saved instructions to apply `[S39]`.
- `[documented fact]` The counter-risk is that a stored assumption becomes a standing instruction. Anthropic's own guidance is to tune compaction "for recall first, then precision" and warns aggressive compression "can lose subtle critical context" `[S09]`.
- `[documented fact]` Microsoft's Copilot memory documentation states admins "can't restrict what type of information is added" and that memory actions "don't generate audit log entries" `[S40]` — an explicit statement that the memory layer is, by design, outside existing audit and DLP controls.
- `[documented fact]` The **control** side of the equation also depends on where memory lives: Hermes can stage every memory write for approval and prints what it overwrote or removed `[S82]`, while Copilot's memory actions "don't generate audit log entries" `[S40]`. Same user need, opposite governance — which is why the local-first tier matters to this wave.
- `[inference]` The central tension is not "memory good or bad" but **recall vs control**: every mechanism that improves recall also widens the surface that must be inspected, scoped, corrected, and deleted.

## 5. Boundary of this wave

- In scope: the six types and seven patterns above, the products that ship them (coding agents, consumer assistants, enterprise platforms, and the local-first personal agents), the failure and attack modes, and the control/law/evaluation layer.
- Out of scope (noted only where they intersect): general document RAG with no agent persistence; model-weight/persona "memory" that is neither inspectable nor user-controllable.
