# Products — The Documented Memory Landscape

_Date: 2026-10-11. Every factual claim cites `[S##]` from `../06_Evidence/Sources.md`. Reliability of the *source* is shown as P/T/C — note that nearly every product row rests on a **C** (vendor) source, because the vendor's own documentation is the only public description of its memory. That is itself a finding._

## 1. Capability matrix — coding agents

| Product | Memory mechanism(s) | Storage / scope | Documented controls | Rel. | S## |
|---------|--------------------|-----------------|---------------------|------|-----|
| Claude Code | `CLAUDE.md` ladder (managed → user → project → local) + auto memory notes | Project `./CLAUDE.md`; auto memory machine-local `~/.claude/projects/<proj>/memory/` (`MEMORY.md` index + topic files), keyed to git repo; first 200 lines/25 KB loaded | `/memory` (list locations, toggle auto memory, edit), `/context`, settings `claudeMdExcludes`, `autoMemoryEnabled`, `autoMemoryDirectory`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`; after `/compact` the project `CLAUDE.md` is re-read | C | `[S17]` |
| Anthropic API memory tool | Client-side files under `/memories` | **Your** storage; persistence is the app's job | Six ops: `view`, `create`, `str_replace`, `insert`, `delete`, `rename`; path-traversal warning | C | `[S08]` |
| Cursor | Rules (`.cursor/rules/*.mdc`) + **Projects "shared context"** (agent-written) | Rules in repo; Project context syncs across cloud/local machines (Cloud by default; Enterprise needs Cursor ≥ 3.21.9) | Edit rules; Projects are run by a "coordinator agent" that "doesn't write code itself" and grows shared context "over months"; docs still state models "don't retain memory between completions"; **no branded Memories feature** | C | `[S18, S19, S102, S103]` |
| GitHub Copilot | Custom instructions only (`.github/copilot-instructions.md`, path `.instructions.md`, `AGENTS.md`) | Repo files | Edit files; per-surface support differs; **no memory store documented** | C | `[S20, S21]` |
| Cline | "Memory Bank" convention (`memory-bank/…`) | Repo files (`projectbrief.md` … `progress.md`) | Agent re-reads because it "resets completely between sessions"; no store to clear | C | `[S22]` |
| Windsurf (Cascade, legacy) | Auto-generated / requested **Memories** + rules | Local `~/.codeium/windsurf/memories/`, workspace-associated, **not committed** | Edit via Customizations; global rules ≤6,000 chars, workspace ≤12,000; **legacy Cascade only** | C | `[S23]` |
| **Devin** (Cognition) | **Memory** — "Devin writes memories automatically, refined by dreaming" | **Memory drive**: a persistent Git repo of Markdown notes with a **`MEMORY.md`** entry point (built on the "Agent Memory Repo" standard); per-session checkout | Read-only in the app; change by asking Devin ("forget that I prefer npm"); **on by default**; **personal** scope (not shared with org); Enterprise Default on / Always on / Always off; "dreaming" ~daily | C | `[S100, S101]` |
| **Kiro** (AWS) | **Memory** (agent-written) + human-authored **steering** files + spec files | `/memories`; repository-level scope (`repo:github/<owner>/<repo>`); workspace-trust gate blocks writes in untrusted repos; **requires Kiro CLI V3** | Access levels **read & write / read only / off** (write needs read & write); CLI "Automatic memory updates" auto-creates/refines memories "including after a session ends"; steering in `.kiro/steering/` (human) | C | `[S96, S97, S98, S99]` |
| OpenAI Codex | **Memories** (local files) + `AGENTS.md` | `~/.codex/memories/`; AGENTS.md chain root→cwd, ≤1 file/dir, 32 KiB cap | `/memories`; Settings > Personalization; "Enable/Delete Codex memories"; config `[features] memories`; redacts secrets, skips short sessions; "no cache to clear" for AGENTS.md | C | `[S24, S25]` |
| Gemini CLI | `GEMINI.md` hierarchy + experimental **Auto Memory** | Global `~/.gemini/GEMINI.md` + workspace; auto memory mines past sessions into a per-project inbox (off by default) | `/memory show`, `/memory reload`; `/memory inbox` to promote/discard skills & patches; ignores sessions <3 h idle/<10 messages | C | `[S26, S27]` |
| Aider | `CONVENTIONS.md` (read-only) | Repo file | `/read CONVENTIONS.md` or `--read`; **no persistent memory** | C | `[S28]` |
| Zed | Rules → **Skills/Instructions** (v1.4.0); `.rules` compat | `%APPDATA%\Zed\AGENTS.md` / `~/.config/zed/AGENTS.md` | Skills library; only earliest compat file used; **no persistence** | C | `[S29]` |
| Continue | Rules (`.continue/rules`) | Repo files | Edit files; no memory store | C | `[S30]` |
| JetBrains AI Assistant | Project rules (`.aiassistant/rules/<file>.md`) | Repo files | Modes: Always / Manually / By model decision / By file patterns / Off | C | `[S31]` |
| Amazon Q Developer | Project rules (`.amazonq/rules`) | Repo files | Per-chat Rules toggle | C | `[S32]` |
| AGENTS.md | Cross-tool instruction file format | Repo files; nesting = closest wins | Stewarded by the Agentic AI Foundation (Linux Foundation); "explicit user chat prompts override everything" | P (format) / C (tool list) | `[S33]` |
| MCP `memory` server | Knowledge graph (entities/relations/observations) | Local `memory.jsonl` (`MEMORY_FILE_PATH`); exclusive `.lock` | `create_entities`, `add_observations`, `delete_*`, `read_graph`, `search_nodes`; resource `memory://knowledge-graph` | P | `[S34]` |
| Basic Memory | Markdown knowledge graph via MCP | Local files or Basic Memory Cloud | Edit Markdown | C | `[S35]` |

**Reading the column.** Instruction layers are still the norm, but **agent-written persistent memory is spreading fast and converging on one design.** At least **six** tools now ship it — Claude Code auto memory `[S17]`, Codex Memories `[S24]`, Gemini CLI Auto Memory (off by default) `[S27]`, **Kiro Memory** `[S96]`, **Devin Memory** `[S100]`, and legacy Windsurf Cascade `[S23]` — with **Cursor Projects** a partial seventh (agent-written "shared context", no branded Memories feature) `[S102]`. They largely share one shape: **a `MEMORY.md` entry point plus Markdown notes on disk, consolidated in the background** ("dreaming", "auto memory", "automatic memory updates") `[S17, S82, S88, S96, S100]`. The remaining tools (Copilot, Aider, Zed, Continue, JetBrains, Amazon Q) still document only human-authored instruction files `[S20–S22, S28–S32]`.

**Correction note (2026-10-12).** This reading supersedes the first-pass version, which said only *four* tools shipped memory and that Cursor and Devin had none. Both were incomplete: Devin Memory is now first-class and on by default `[S100]`, and Cursor Projects ship agent-written context `[S102]`; Kiro was missing entirely and has been added `[S96]`.

## 2. Capability matrix — assistants and enterprise platforms

| Product | Memory mechanism(s) | Storage / scope | Documented controls | Rel. | S## |
|---------|--------------------|-----------------|---------------------|------|-----|
| ChatGPT | Saved memories + insights from past chats ("reference chat history") | Cloud, per account | Settings > Personalization > Memory; view/edit/delete; "Don't mention this again"; Temporary Chat excludes memory; deletion can lag; logs of deleted saved memories may be kept up to 30 days | C | `[S36, S37]` |
| Gemini | "Saved Info"/"Instructions for Gemini" + past-chat personalization | Cloud; activity auto-deletes at 18 months default (3/36/∞ adjustable); temporary chats 72 h; human-reviewed up to 3 y | Manage at gemini.google.com/saved-info; view/edit/delete; requires "Memory turned on" | C | `[S38, S39]` |
| Microsoft Copilot | Saved memories + inferred details + custom instructions | User's **Exchange mailbox**, hidden folder (`<CopilotMemory>`) | On by default, no action required; admins can't restrict content type; Purview retention policies don't apply; **memory actions don't generate audit log entries**; preview | C | `[S40]` |
| Meta AI | Remembers details shared in **1:1** chats (WhatsApp/Messenger) | Cloud | Delete any time; not group chats; default not stated | C | `[S41]` |
| Perplexity / Comet | Single account-level memory across devices | Cloud | Only searches/questions saved (agent actions not stored); toggle "Reference saved memories"/"search library"; edit/delete | C | `[S42]` |
| Apple Intelligence | "Personal context"; on-device + Private Cloud Compute | On-device / PCC ("never retained") | Not a user-editable memory store spec | C | `[S43]` |
| AWS Bedrock AgentCore Memory | Short-term (single session) + long-term (cross-session preferences, facts, summaries) | Managed service | Not specified on the overview page (no retention window) | C | `[S44]` |
| Vertex AI Agent Engine Memory Bank | Long-term preferences/facts; memory profiles; revisions | Managed; IAM conditions, VPC-SC, CMEK, residency, HIPAA | Memory generation/ingestion/retrieval; revision history; access via IAM | C | `[S45]` |
| Azure AI Foundry Agent Service (preview) | User profile, chat summary, procedural — **default-enabled** | Managed; store-level default TTL (seconds) | Item-level CRUD; direct remember/forget; 100 scopes/store, 10,000 memories/scope; 30-day session deletion on inactivity | C | `[S46]` |
| Salesforce Agentforce | — | — | **Unverified** — official pages failed to render | — | — |

## 3. Capability matrix — autonomous and personal agent platforms

| Product | Memory mechanism(s) | Storage / scope | Documented controls | Rel. | S## |
|---------|--------------------|-----------------|---------------------|------|-----|
| **Hermes Agent** (Nous Research) | `MEMORY.md` (agent notes) + `USER.md` (profile) + FTS5 session search + journey/learning graph + "Honcho dialectic user modeling" | `~/.hermes/memories/`; per-profile isolation `~/.hermes/profiles/<name>/memories/`; sessions in SQLite `~/.hermes/state.db`; **On by default** (`memory_enabled: true`, `user_profile_enabled: true`, `write_approval: false`) | `/memory pending`, `/memory approve <id>\|all`, `/memory reject <id>`, `/memory approval on\|off`; `memory` tool **add/replace/remove**; plain-Markdown hand edit; `/memory approve` "lists the full text of every entry it overwrote or removed"; a write is refused if the target changed after staging; background writes tagged `[auto]` | C | `[S81, S82, S83, S84, S85, S86]` |
| **OpenClaw** | `MEMORY.md` (long-term) + daily `memory/YYYY-MM-DD.md` + optional `USER.md` + `DREAMS.md`; tools `memory_search`/`memory_get`/`intent`; "dreaming" distillation; automatic **memory flush before compaction** | Workspace `~/.openclaw/workspace` ("there is no hidden state"); config `~/.openclaw/openclaw.json`; transcripts in `~/.openclaw/agents/<id>/agent/openclaw-agent.sqlite`; engines builtin SQLite (default) / Honcho / LanceDB | `openclaw memory status\|search\|index --force`; Settings → Import Memory; `/new`, `/reset`; `openclaw sessions cleanup --dry-run\|--enforce`; incognito "New thread" (24 h, no flush, no archive); cross-conversation recall **opt-in** (`rememberAcrossConversations`); per-conversation sessions | C | `[S87, S88, S89, S90, S91]` |

**Notes.** `[documented fact]` Hermes' built-in memory is flat Markdown — explicitly **no vector store, knowledge graph, Mem0 or Letta in the core** — with optional providers (Honcho, Mem0, Supermemory, RetainDB, etc.) running "alongside built-in memory (never replacing it)" `[S83]`. `[documented fact]` OpenClaw is local-first ("No subscription. No hosted tier"), with loopback-only gateway by default and a `openclaw security audit` / policy tooling `[S87, S90]`.

`[inference]` These two are the **best-governed** memory systems in the survey. Hermes gives an approval queue and prints exactly what was overwritten or removed; OpenClaw gives on-disk Markdown, incognito, and per-conversation scoping the user can inspect. No cloud product examined (consumer or enterprise) offers the equivalent `[S82, S88]`. This inverts the assumption that the more capable agent has the weaker controls — here the open, self-hosted agents have both the richest memory and the strongest controls.

## 4. The infrastructure layer

- `[documented fact]` **Mem0** documents `add`/`search`/`update`/`delete` plus graph memory; its pricing page gates graph memory and "Dream" consolidation to **Pro ($249/mo)** and Enterprise, with a free Hobby tier of 10,000 add / 1,000 retrieval requests per month `[S07, S49]`.
- `[reported signal]` Mem0 raised a reported **$24M** ($3.9M seed + $20M Series A led by Basis Set, with Peak XV and the GitHub Fund); valuation undisclosed; adoption figures (41k+ GitHub stars, 186M API calls in Q3 2025, "exclusive memory provider for AWS's new Agent SDK") are **company-supplied** `[S50]`. Its homepage claims "150,000+ Developers" and cites LoCoMo/LongMemEval/BEAM without publishing scores there `[S48]`.
- `[reported signal]` **Zep** publishes LoCoMo 94.7% / 155 ms / 5,760 tokens and LongMemEval 90.2% / 162 ms / 4,408 tokens, and lists Samsung, Zscaler, HoneyBook, Twin Health as customers — all self-reported `[S54]`.
- `[reported signal]` **Letta** (formerly MemGPT) markets stateful-agent memory; advisors include Ion Stoica and Jeff Dean; the Sep 2024 announcement states no funding figure `[S52, S53]`.
- `[documented fact]` **Redis** offers "Redis Agent Memory" citing "86.5% accuracy, ~$0.07 per session"; **Neo4j** promotes an "Agent Memory Service" and context graphs `[S56, S57]`.
- `[inference]` The benchmark numbers in this layer are **not comparable**: they come from vendor-authored papers `[S15, S16]`, name different subsets (DMR vs LoCoMo vs LongMemEval vs BEAM), and none was reproduced under a shared protocol. A June 2026 TechCrunch summary of two Writer papers argues memory/personalization can *degrade* outputs; it used Mem0 and Zep, named no standard benchmark, and gave no accuracy figures `[S51]`.

## 5. Claims we could not verify (carried to Findings)

- Cursor: no *branded* "Memories" feature found in docs or changelog `[S18, S19]`; whether **Projects** "shared context" is session-persistent memory or a scoped context store is unresolved `[S102, S103]`.
- GitHub Copilot memory/preview: no "memory" capability in the official instruction pages or support matrix `[S20, S21]`.
- Claude Code `#` memory shortcut: not present in the current Memory page, which documents `/memory` `[S17]`.
- Salesforce Agentforce memory: all official pages failed to render `[—]`.
- Meta AI and Perplexity memory default on/off states: not stated `[S41, S42]`.
- Mem0 valuation and Letta funding amount: not disclosed `[S50, S53]`.
- Hermes Agent launch date: not published; the GitHub repo creation (2025-07-22) is a proxy `[S85]`.
- OpenClaw "OpenClaw Enterprise" (blog 2026-09-29) capabilities, and whether it introduces any org-level memory store: not confirmed from primary docs `[S87]`.
- No independent memory benchmark of Hermes Agent was located; its only memory evaluation is its own Hermes Bench "Memory" category `[S86]`.
