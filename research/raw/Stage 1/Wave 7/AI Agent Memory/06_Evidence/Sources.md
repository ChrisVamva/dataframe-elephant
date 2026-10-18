# Source Register

_Every factual claim in folders 01–05 references an entry here (`[S##]`). Superseded sources get marked, never deleted._

**Reliability scale:**
- **P** — independent primary: peer-reviewed papers and preprints, regulators, standards bodies and their reference implementations, official statistics.
- **T** — reputable secondary: major news, established trade press, data-driven think tank.
- **C** — company/self-published: official vendor product documentation, vendor engineering/research blogs, vendor benchmark and funding claims. C is the primary source for the vendor's *own* claim, but must be verified before it is relied on as fact.

**Notes.** Reliability letters were normalized across seven research passes (2026-10-11/12): official product documentation is graded **C** even when it is the definitive source for that product's behaviour, because it remains a self-published vendor claim until confirmed by a specification or a reproducible test. The same rule was applied to the open-source agent platforms added in the second pass (Hermes Agent, OpenClaw): their documentation is **C**, while their GitHub repositories/releases and independent security papers are **P**. Vendor-authored arXiv preprints (Mem0, Zep) are graded **C** despite being preprints, because their benchmark figures are self-reported. arXiv preprints marked `(preprint)` have not been peer-reviewed. Sources carrying 2026 dates were located during the 2026-10-11 pass; their reported figures are paper-reported and not independently replicated here (see `Findings.md` §Method limits). Undated vendor pages were undated as fetched; the access date (2026-10-11) applies.

## A. Memory mechanisms, architectures, and context research

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S01 | P (preprint) | MemGPT: Towards LLMs as Operating Systems | https://arxiv.org/abs/2310.08560 | 2023-10-12 | virtual context; memory tiers; OS analogy |
| S02 | P (preprint) | A-MEM: Agentic Memory for LLM Agents | https://arxiv.org/abs/2502.12110 | 2025-02-17 | Zettelkasten linking; memory evolution |
| S03 | P (preprint) | MemOS: A Memory OS for AI System (MemTensor) | https://arxiv.org/abs/2507.03724 | 2025-07-04 | MemCube; provenance/version metadata |
| S04 | C | Letta — memory blocks docs | https://docs.letta.com/guides/agents/memory-blocks | undated | core memory blocks; labels; character limits; shared blocks |
| S05 | C | LangMem docs (LangChain) | https://langchain-ai.github.io/langmem/ | undated | semantic/episodic memory; hot-path vs background |
| S06 | C | Zep / Graphiti docs | https://help.getzep.com/graphiti/getting-started/overview | undated | bi-temporal edges; invalidation; hybrid retrieval |
| S07 | C | Mem0 — memory types docs | https://docs.mem0.ai/core-concepts/memory-types | undated | add/search/update/delete; graph memory |
| S08 | C | Anthropic — memory tool docs | https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | undated | client-side `/memories`; six file operations; compaction |
| S09 | C | Anthropic — Effective context engineering for AI agents | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 2025-09-29 | compaction practice; recall-vs-precision; silent loss |
| S10 | C | Chroma — Context Rot research | https://www.trychroma.com/research/context-rot | 2025-07-14 | degradation with input length |
| S11 | P | RULER (COLM 2024) | https://arxiv.org/abs/2404.06654 | 2024-04-09 | real effective context lengths |
| S12 | P | Lost in the Middle (TACL 2023) | https://arxiv.org/abs/2307.03172 | 2023-07-06 | position-sensitive recall |
| S13 | P (preprint) | In Defense of RAG in the Era of Long-Context LMs | https://arxiv.org/abs/2409.01666 | 2024-09-03 | inverted-U; sweet points; RAG vs long context |
| S14 | P | RAG or Long-Context LLMs? (EMNLP 2024) | https://arxiv.org/abs/2407.16833 | 2024-07-23 | LC vs RAG; Self-Route |
| S15 | C (vendor preprint) | Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory | https://arxiv.org/abs/2504.19413 | 2025-04-28 | extraction/consolidation/retrieval; LoCoMo claims |
| S16 | C (vendor preprint) | Zep: A Temporal Knowledge Graph Architecture for Agent Memory | https://arxiv.org/abs/2501.13956 | 2025-01-20 | temporal KG; DMR/LongMemEval claims |

## B. Coding-agent memory products

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S17 | C | Claude Code — Memory docs | https://code.claude.com/docs/en/memory | undated | CLAUDE.md ladder; auto memory store; `/memory`, `/context` controls |
| S18 | C | Cursor — Rules docs | https://cursor.com/docs/context/rules | undated | `.cursor/rules`; Team/Project/User rules; precedence |
| S19 | C | Cursor — changelog | https://cursor.com/changelog | 2026-09/10 | Projects/shared context; absence of a Memories feature |
| S20 | C | GitHub — Adding repository custom instructions | https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions | undated | `copilot-instructions.md`; `AGENTS.md`; precedence |
| S21 | C | GitHub — Custom instructions support matrix | https://docs.github.com/en/copilot/reference/custom-instructions-support | undated | per-surface instruction file support |
| S22 | C | Cline — Memory Bank docs | https://docs.cline.bot/features/memory-bank | undated | `memory-bank/` convention; session reset |
| S23 | C | Windsurf/Devin — Cascade Memories docs | https://docs.devin.ai/desktop/cascade/memories | undated | auto-generated memories; local store; legacy/locality caveats |
| S24 | C | OpenAI — Codex Memories docs | https://learn.chatgpt.com/codex/customization/memories | undated | local memory files; `/memories`; delete controls |
| S25 | C | OpenAI — Codex AGENTS.md docs | https://learn.chatgpt.com/docs/agent-configuration/agents-md | undated | AGENTS.md chain; 32 KiB cap; "no cache to clear" |
| S26 | C | Google — Gemini CLI GEMINI.md docs | https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md | undated | GEMINI.md hierarchy; `/memory show`, `/memory reload` |
| S27 | C | Google — Gemini CLI Auto Memory docs | https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/auto-memory.md | undated | experimental session-mining; `/memory inbox` review |
| S28 | C | Aider — Conventions docs | https://aider.chat/docs/usage/conventions.html | undated | `CONVENTIONS.md` read-only; no persistent memory |
| S29 | C | Zed — Rules docs | https://raw.githubusercontent.com/zed-industries/zed/main/docs/src/ai/rules.md | undated | Rules → Skills/Instructions (v1.4.0); `.rules` compat |
| S30 | C | Continue — Rules docs | https://docs.continue.dev/customize/rules | undated | `.continue/rules`; no memory store |
| S31 | C | JetBrains — Configure project rules | https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html | 2026-05-27 | `.aiassistant/rules`; rule modes |
| S32 | C | Amazon Q Developer — Project rules | https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/context-project-rules.html | undated | `.amazonq/rules`; no memory feature |
| S33 | P (standard) / C (list) | AGENTS.md — open instruction format | https://agents.md/ | undated | cross-tool instruction convention; 60k+ projects claim |
| S34 | P | modelcontextprotocol/servers — `memory` server | https://github.com/modelcontextprotocol/servers/tree/main/src/memory | undated | knowledge-graph memory; `memory.jsonl`; tools |
| S35 | C | Basic Memory docs | https://docs.basicmemory.com/ | undated | Markdown knowledge-graph memory via MCP |

## C. AI assistants and enterprise agent platforms

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S36 | C | OpenAI — Memory and new controls for ChatGPT | https://openai.com/index/memory-and-new-controls-for-chatgpt/ | 2024-02-13 (+ 2024-09-05, 2025-04-10, 2025-06-03) | ChatGPT memory launch; rollout; controls |
| S37 | C | OpenAI — Memory FAQ | https://help.openai.com/en/articles/8590148-memory-faq | undated (screens 2026-06-04) | saved vs reference-chat-history; 30-day deletion; defaults |
| S38 | C | Google — Gemini Apps Privacy Hub / Privacy Notice | https://support.google.com/gemini/answer/13594961 | 2026-06-29 | Saved Info; past-chat personalization; retention |
| S39 | C | Google — "Your instructions for Gemini" (Saved Info) | https://support.google.com/gemini?p=pn_saved_info | undated | view/edit/delete paths; "Memory turned on" |
| S40 | C | Microsoft Learn — Manage Copilot personalization and memory | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory | 2026-09-02 | Copilot memory store; default-on; retention gap; admin limits |
| S41 | C | Meta — Building toward a smarter, more personalized assistant | https://about.fb.com/news/2025/01/building-toward-a-smarter-more-personalized-assistant/ | 2025-01-27 | Meta AI memory rollout; 1:1 chats only; delete |
| S42 | C | Perplexity — Comet memory help | https://www.perplexity.ai/help-center/comet/en/articles/12658438-comet-memory | 2026-09-03 | single cross-device memory; search-only saves |
| S43 | C | Apple — Introducing Apple Intelligence | https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/ | 2024-06-10 | personal context; on-device; Private Cloud Compute |
| S44 | C | AWS — Bedrock AgentCore Memory docs | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html | undated | short-term vs long-term memory; managed service |
| S45 | C | Google Cloud — Agent Engine Memory Bank overview | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/memory-bank/overview | undated | memory generation; revisions; IAM/residency |
| S46 | C | Microsoft Learn — What is Memory? (Azure AI Foundry) | https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-memory | 2026-06-02 | memory types; TTL; quotas; CRUD |
| S47 | C | Anthropic — Claude memory (claude.com blog) | https://claude.com/blog/memory | 2025-09-11 (upd. 2025-10-23) | optional memory; view/edit; project memory; incognito |

## D. Memory-infrastructure vendors and market signals

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S48 | C | Mem0 — homepage | https://mem0.ai/ | undated | "150,000+ developers"; benchmark names (BEAM) |
| S49 | C | Mem0 — pricing | https://mem0.ai/pricing | undated | graph memory/Dream gated to Pro ($249/mo) |
| S50 | T | TechCrunch — Mem0 raises $24M | https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/ | 2025-10-28 | funding; adoption figures (company-supplied) |
| S51 | T | TechCrunch — How memory tools can make AI models worse | https://techcrunch.com/2026/06/10/how-memory-tools-can-make-ai-models-worse/ | 2026-06-10 | contesting vendor memory benchmarks |
| S52 | C | Letta — homepage | https://www.letta.com/ | undated | MemGPT roots; case studies |
| S53 | C | Letta — Announcing Letta | https://www.letta.com/blog/announcing-letta/ | 2024-09-23 | positioning; no funding figure |
| S54 | C | Zep — homepage | https://www.getzep.com/ | undated | self-reported LoCoMo/LongMemEval scores; customers |
| S55 | C | Zep — blog | https://blog.getzep.com/ | posts 2026-07..09 | agent-memory engineering/governance posts |
| S56 | C | Redis — AI solutions / Agent Memory | https://redis.io/solutions/ai/ | undated | Redis Agent Memory; "86.5%" claim |
| S57 | C | Neo4j — agent memory blog | https://neo4j.com/blog/?s=agent+memory | undated | Agent Memory Service; context graphs |

## E. Privacy, control, and data-protection law

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S58 | P | EDPB — Opinion 28/2024 on AI models | https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en | 2024-12-18 | anonymity; legitimate-interest three-step test |
| S59 | P | EDPB — ChatGPT Taskforce report | https://www.edpb.europa.eu/our-work-tools/our-documents/other/report-work-undertaken-chatgpt-taskforce_en | 2024-05-24 | EU regulator positions (scope) |
| S60 | T | EU AI Act — Article 50 (text mirror) | https://artificialintelligenceact.eu/article/50/ | in force 2026-08-02 | transparency obligations; no memory-specific duty |
| S61 | T | GDPR — Article 17 (text mirror) | https://gdpr-info.eu/art-17-gdpr/ | n.d. | erasure right and exceptions |
| S62 | P | California OAG — CCPA/CPRA | https://oag.ca.gov/privacy/ccpa | upd. 2026-08-28 | deletion/access rights; 45-day window |
| S63 | P | Garante — OpenAI €15M fine (Decision No. 755/2024) | https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432 | 2024-12-20 | enforcement: rectification/deletion; later court suspension |
| S64 | T | PPC Land — Council of Europe drafts privacy rules for AI chatbots and agents | https://ppc.land/council-of-europe-drafts-privacy-rules-for-ai-chatbots-and-agents/ | 2026-09-03 | draft T-PD(2025)3rev4: memory-off default; cross-layer delete |

## F. Security and memory poisoning

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S65 | P (preprint) | MINJA — Memory Injection Attacks on LLM Agents | https://arxiv.org/abs/2503.03704 | 2025-03-05 | query-only memory poisoning |
| S66 | P (preprint) | AgentPoison | https://arxiv.org/abs/2407.12784 | 2024-07-17 | RAG/memory backdoor; <0.1% poison rate; >80% ASR |
| S67 | P (preprint) | MemoryGraft | https://arxiv.org/abs/2512.16962 | 2025-12-18 | persistent behavioral drift from poisoned "experiences" |
| S68 | P (preprint) | MemLeak | https://arxiv.org/abs/2610.04195 | 2026-10-03 | cross-user leakage via shared vector store |
| S69 | P (preprint) | Salami Attack / MemCollusion | https://arxiv.org/abs/2608.01637 | 2026-08-03 | fragmented collusive poisoning; 75% ASR |
| S70 | P (preprint) | Mind Your HEARTBEAT | https://arxiv.org/abs/2603.23064 | 2026-03-24 | background execution; pollution without prompt injection |
| S71 | P (preprint) | PipePoison | https://arxiv.org/abs/2609.00523 | 2026-09-01 | write/retrieve/utilize optimization; survives defenses |
| S72 | P (preprint) | PASAC — 2026 agent-security incidents | https://arxiv.org/abs/2610.12463 | 2026-10-08 | OpenAI/Anthropic/Gemini agent incidents (2026) |

## G. Evaluation, benchmarks, and audit design

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S73 | P (preprint) | LoCoMo — Evaluating Very Long-Term Conversational Memory | https://arxiv.org/abs/2402.17753 | 2024-02-27 | long-dialogue benchmark; no privacy dimension |
| S74 | P | LongMemEval (ICLR 2025) | https://arxiv.org/abs/2410.10813 | 2024-10-14 | five memory abilities; ~30% drop |
| S75 | P (preprint) | MemoryAgentBench | https://arxiv.org/abs/2507.05257 | 2025-07-07 | four competencies incl. selective forgetting |
| S76 | P | MemBench (ACL 2025 Findings) | https://arxiv.org/abs/2506.21605 | 2025-06-20 | factual vs reflective memory; capacity |
| S77 | P (preprint) | MemSecBench | https://arxiv.org/abs/2607.27080 | 2026-07-29 | write–execute–forget security benchmark |
| S78 | P (preprint) | MemSentry | https://arxiv.org/abs/2609.08747 | 2026-09-08 | write-gating defense; accept/review/quarantine |
| S79 | P (preprint) | Memory Provenance Laundering (PPMF) | https://arxiv.org/abs/2607.29167 | 2026-07-31 | consolidation launders low-trust content; provenance gate |
| S80 | P (preprint) | MemGauge | https://arxiv.org/abs/2608.30177 | 2026-08-31 | utility–risk tradeoffs |

## H. Autonomous and personal agent platforms (second pass, 2026-10-11)

_Added when the user widened the scope from coding agents to AI agents generally, naming Hermes and OpenClaw as the more interesting cases. These are persistent personal/autonomous agents — the class with the richest, longest-lived memory and therefore the most interesting governance questions._

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S81 | C | Hermes Agent — homepage (Nous Research) | https://hermes-agent.nousresearch.com/ | 2026 (undated) | identity; MIT/open-source; "self-improving" agent; persistent memory claim |
| S82 | C | Hermes Agent — Memory System docs | https://hermes-agent.nousresearch.com/docs/user-guide/features/memory | undated | `MEMORY.md`/`USER.md`; char limits; storage paths; controls |
| S83 | C | Hermes Agent — Features overview docs | https://hermes-agent.nousresearch.com/docs/user-guide/features/overview | undated | memory providers; skills; journey graph |
| S84 | C | Hermes Agent — Security docs | https://hermes-agent.nousresearch.com/docs/user-guide/security | undated | eight-layer model; cross-session isolation; disclosed incidents |
| S85 | P | GitHub — `NousResearch/hermes-agent` repo + API metadata | https://github.com/NousResearch/hermes-agent | created 2025-07-22; release v0.21.6 2026-10-08 | license; release; activity |
| S86 | C | Nous Portal — Hermes Index / Bench | https://portal.nousresearch.com/bench | 2026 | "Memory" task category (5 of 150) |
| S87 | C | OpenClaw — official site | https://openclaw.ai | 2026 | local-first; "no hosted tier"; persistent memory |
| S88 | C | OpenClaw — Memory docs | https://docs.openclaw.ai/concepts/memory | undated | `MEMORY.md`, daily notes, `USER.md`, `DREAMS.md`; dreaming; flush |
| S89 | C | OpenClaw — Session docs | https://docs.openclaw.ai/session | undated | storage paths; DM scope; incognito; cleanup |
| S90 | C | OpenClaw — Gateway Security docs | https://docs.openclaw.ai/gateway/security | undated | loopback default; sandboxing; security-audit tooling |
| S91 | P | GitHub — `openclaw/openclaw` repo + releases | https://github.com/openclaw/openclaw | 2026-10-11 | license; version 2026.10.1; changelog |
| S92 | P | OpenClaw blog — Introducing OpenClaw | https://openclaw.ai/blog | 2026-01-29 | naming/launch |
| S93 | T | Wikipedia — OpenClaw | https://en.wikipedia.org/wiki/OpenClaw | 2026 | name history; OpenAI donor link |
| S94 | P (preprint) | Security of OpenClaw Agents (arXiv 2605.25435) | https://arxiv.org/abs/2605.25435 | 2026-05-25 | persistent-memory threats; skill poisoning; cascading failures |
| S95 | P (preprint) | Foundations for Agentic AI Investigations … OpenClaw (arXiv 2604.05589) | https://arxiv.org/abs/2604.05589 | 2026-04-07 | forensic artifacts of agent loops |

## I. Additional IDE/agent comparison (third pass, 2026-10-12)

_Added after the user compared the current IDE's memory with Kiro, Devin, and Cursor. This pass corrected two earlier rows and closed a coverage gap._

**Corrections (third pass, 2026-10-12).** Two earlier rows were **incomplete on the memory question** and are superseded here: `S23` (Windsurf/Devin) recorded only the legacy Cascade caveat — Cognition's current **Devin Memory** is a first-class, on-by-default, Git-backed feature `[S100, S101]`; `S19` (Cursor) recorded "no Memories feature" from the changelog — accurate for a *branded* feature, but Cursor **Projects** ship agent-written "shared context" that persists across sessions `[S102, S103]`. **Kiro was absent from the register entirely** and is now covered `[S96–S99]`.

| ID | Rel. | Source | URL | Date | Used for |
|----|------|--------|-----|------|----------|
| S96 | C | Kiro — Memory docs (AWS) | https://kiro.dev/docs/memory/ | upd. 2026-10-09 | Kiro agent-written Memory; `/memories`; access levels; repo scope |
| S97 | C | Kiro — Steering docs (AWS) | https://kiro.dev/docs/steering/ | undated | human-authored steering files (`.kiro/steering/`, `AGENTS.md`) |
| S98 | C | Kiro — docs home + changelog (AWS) | https://kiro.dev/docs/ · https://kiro.dev/changelog/ | 2026-10-07/09 | identity; versions (IDE 1.2.56; CLI 2.29.0) |
| S99 | C | Kiro — "Introducing Kiro" blog (AWS) | https://kiro.dev/blog/introducing-kiro/ | 2025-07-14 | launch date/description |
| S100 | C | Devin — Memory docs (Cognition) | https://docs.devin.ai/product-guides/memory | undated | Devin Memory: memory drive, `MEMORY.md`, dreaming, default on |
| S101 | C | Devin — release notes (Knowledge → Skills) (Cognition) | https://docs.devin.ai/release-notes/overview | 2026-09-18 | legacy Knowledge deprecated/migrated to Skills |
| S102 | C | Cursor — Projects docs | https://cursor.com/docs/agent/projects | undated | agent-written "shared context"; coordinator agent |
| S103 | C | Cursor — changelog | https://cursor.com/changelog | 2026-09-10 (through 2026-10-06) | Projects launch; no branded "Memory" entry |
