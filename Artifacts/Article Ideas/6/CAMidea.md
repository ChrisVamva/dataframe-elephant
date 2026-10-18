# CAMidea — Article Ideas for AI Agent Memory (Wave 7)

> **Origin and status.** This bank serves the Stage 1 Wave 7 subject "AI Agent Memory" (`research/raw/Stage 1/Wave 7/AI Agent Memory/`). The original `CAMidea.md` referenced in the Wave 7 README was not present in the repository at generation time; this file is a fresh bank that preserves the one documented stable ID — idea **1.3 "Memory Is a Product Feature—and a Privacy Boundary"**, the originating CAM pitch rated first on 2026-10-11 — and adds new pitches generated from the Stage 1 survey. All other pitch IDs are new.
>
> **Evidence boundary.** These pitches are research proposals, not findings. Every `S##` anchor refers to the source register in `research/raw/Stage 1/Wave 7/AI Agent Memory/06_Evidence/Sources.md` and is a lead to verify, not an established fact. Reliability classes follow the register: **P** primary (peer-reviewed/preprint/regulator/standard), **T** reputable secondary, **C** company/self-published. Nearly every product claim in the survey rests on a **C** source — the vendor's own documentation is the only public description of its memory. Preserve `[documented fact]` / `[reported signal]` / `[inference]` distinctions; keep vendor claims, preprints, and open follow-ups qualified. Do not invent source IDs, quotes, or product facts.

## 1. What "Memory" Actually Is

### 1.1 Six Things Called Memory
- **Angle:** A taxonomy piece. "Memory" in AI products is at least six different mechanisms — session/context, explicit instruction files, searchable history, summarised/compacted state, extracted memory records, and knowledge/temporal graphs — plus a seventh implementation pattern (local-first Markdown on disk). The word does one job in marketing and six different jobs in engineering.
- **Research question:** When a product says it has "memory," which of the six types does it actually ship — and what does each preserve, for how long, and across which boundary (session / project / user / team / tenant)?
- **Evidence to build:** The six-type taxonomy with per-type lifetime, scope, and control surface `[S01, S17, S37, S09, S07, S06]`; the local-first Markdown pattern `[S82, S88]`; the ambiguity of "what it remembers" for a single product `[S17, S07]`; the inspectable end of the spectrum — AGENTS.md and the MCP memory server `[S33, S34]`.
- **Target reader:** Practitioners and technical buyers comparing "memory" features across tools; product readers who have been burned by the label.
- **Potential thesis:** "Memory" is a label, not a mechanism — the useful question is never "does it remember?" but "which of six things does it remember, where does it live, and who can see it?"
- **Anchors:** S01 (P preprint), S06/S16 (C), S07/S15 (C), S09 (C), S17 (C), S33 (P standard), S34 (P), S37 (C), S82 (C), S88 (C). Product rows are vendor claims current as fetched 2026-10-11; verify before use.

### 1.2 Your Context Window Is Not Memory
- **Angle:** A myth-busting piece for practitioners. The advertised context window is not memory, and effective context falls far below nominal — long context delays the memory problem, it does not remove it.
- **Research question:** How much of the nominal context window do models actually use, and what does that imply for teams choosing between bigger windows and explicit memory?
- **Evidence to build:** RULER — only half of 17 long-context LMs maintain satisfactory performance at 32K `[S11]`; Lost in the Middle's position-sensitive recall `[S12]`; Chroma's Context Rot study (18 models, 8 input lengths) `[S10]`; the split long-context-vs-RAG literature `[S13, S14]`; MemGPT's fast/slow memory framing `[S01]`.
- **Target reader:** Engineering leads deciding between long-context models and memory/RAG architectures; practitioners hitting context limits.
- **Potential thesis:** Effective context is far below nominal and position-sensitive — long context defers the memory problem but makes selective storage and retrieval unavoidable.
- **Anchors:** S01 (P preprint), S10 (C), S11 (P), S12 (P), S13 (P preprint), S14 (P). The context-length degradation findings are rated high-confidence in the Synthesis.

### 1.3 Memory Is a Product Feature—and a Privacy Boundary
- **Angle:** The originating CAM pitch, now backed by a full Stage 1 survey. Memory is shipped as a product feature with default-on behaviour in consumer assistants — and the same feature is a privacy boundary the user often cannot inspect or audit.
- **Research question:** What do AI agents actually remember, who controls that memory, how is stale or sensitive context removed, and what does the evidence — product documentation, reproducible behaviour, regulation, and security research — support?
- **Evidence to build:** The full Wave 7 survey: the taxonomy `[S01–S16]`, the product matrices `[S17–S47, S81–S103]`, the governance and security layer `[S58–S80]`, and the Memory Governance Record design (`05_Memory_Record_Design/Design.md`). Hook: consumer memory on by default with no audit log `[S40, S37]`; contrast: the self-hosted agents let you read, approve, and delete memory `[S82, S88]`.
- **Target reader:** The CAM audience — technically literate readers interested in AI products, privacy, and practical governance.
- **Potential thesis:** Agent memory is a product feature whose recall is improving faster than its governance — and the governance gap is a property of *cloud* memory, not of memory as such.
- **Anchors:** The whole register S01–S103; high-confidence items per `00_Index/Synthesis.md`. This pitch subsumes the survey's central finding; it is the umbrella piece the other pitches feed.

## 2. Coding Agents: The Memory Layer Spreads

### 2.1 The MEMORY.md Convergence
- **Angle:** A design-convergence piece. At least six coding tools now ship agent-written persistent memory, and they have independently converged on the same shape: a `MEMORY.md` entry point plus Markdown notes on disk, consolidated in the background.
- **Research question:** Is `MEMORY.md` becoming the de facto standard for agent memory — and what does the convergence (plus the newest, still-unfamiliar features) tell us about how the design space is settling?
- **Evidence to build:** The six-tool comparison — Claude Code auto memory `[S17]`, Codex Memories `[S24]`, Gemini CLI Auto Memory `[S27]`, Kiro Memory `[S96]`, Devin Memory `[S100]`, legacy Windsurf Cascade `[S23]` — with Cursor Projects a partial seventh `[S102]`; the shared `MEMORY.md` pattern `[S17, S82, S88, S96, S100]`; Kiro's access levels (read & write / read only / off) and CLI V3 gating `[S96, S98]`; Devin's Git-backed memory drive `[S100]`; the field note that a practitioner reported not encountering comparable agent-written memory in Kiro/Devin/Cursor (single observation, 2026-10-12 — a lead for re-testing, not evidence of absence).
- **Target reader:** Developers and engineering managers choosing or building coding agents; tooling watchers.
- **Potential thesis:** Agent-written memory is spreading fast and converging on one inspectable design — but the newest features (Kiro V3-gated, Devin's first-class Memory) are so recent that practitioner experience lags the documentation.
- **Anchors:** S17, S23, S24, S27 (C); S96–S103 (C, third-pass corrections); S82, S88 (C). Field note: `06_Evidence/Findings.md` RQ3 — single observation, unverified.

### 2.2 Who Writes the Memory?
- **Angle:** A mechanisms piece. The write decision — what to store, dedupe, overwrite, or ignore — is the least-standardised and least-inspectable stage across every system examined, and two systems both labelled "memory" have opposite overwrite semantics.
- **Research question:** How do production memory systems decide what to write, and why do overwrite semantics differ so sharply between systems carrying the same label?
- **Evidence to build:** Mem0's additive extraction path (add unless `update`/`delete` is called) `[S07, S15]`; Letta's whole-block replacement `[S04]`; Anthropic's six client-side file operations (`view`, `create`, `str_replace`, `insert`, `delete`, `rename`) `[S08]`; Hermes' add/replace/remove `[S82]`; the staleness (F1) and silent-loss (F2) failure modes `[S06, S04, S09]`.
- **Target reader:** Engineers building or integrating agent memory; readers of systems-design explainers.
- **Potential thesis:** The write decision is where memory systems actually differ — and it is the stage users cannot inspect, which is why the same "memory" label can mean append-only facts or wholesale replacement.
- **Anchors:** S04, S06, S07, S08, S09, S15, S82 (all C). Overwrite-vs-append semantics are undocumented for most products; only Letta and Mem0 were explicit.

### 2.3 The Agent That Dreams
- **Angle:** A mechanisms piece with a vivid hook. Background "dreaming" and consolidation processes rewrite memory overnight, with no user-visible diff — the system's beliefs change while you sleep.
- **Research question:** What do background consolidation processes (Letta's dreaming, OpenClaw's dreaming, Devin's dreaming, LangMem's background manager) actually change, and what is lost?
- **Evidence to build:** Letta's dreaming subagents `[S04]`; LangMem's background memory manager `[S05]`; OpenClaw's dreaming distiller and automatic memory flush before compaction `[S88]`; Devin's ~daily dreaming `[S100]`; Anthropic's compaction guidance — tune "for recall first, then precision"; aggressive compression "can lose subtle critical context" `[S09]`; the silent-loss failure mode `[S09, S04, S05]`.
- **Target reader:** Practitioners whose agents "change their minds"; readers of AI-systems explainers.
- **Potential thesis:** Consolidation is lossy by construction and invisible by default — the same background processes that improve recall are the ones that silently rewrite what the system believes.
- **Anchors:** S04, S05, S08, S09, S100 (all C). No primary source quantifies production consolidation-loss rates; treat as an open question.

## 3. Consumer Assistants: Memory On by Default

### 3.1 Memory On by Default
- **Angle:** The privacy hook piece. The major consumer assistants ship memory on by default, and at least one vendor states in writing that memory actions generate no audit log entries and sit outside retention policies.
- **Research question:** What do the major consumer assistants (ChatGPT, Gemini, Copilot, Meta AI, Perplexity/Comet, Apple Intelligence) actually document about memory defaults, storage location, and controls — and which capability claims are primary-source-backed versus marketing?
- **Evidence to build:** Microsoft Copilot — on by default ("No action is required"), stored in the user's Exchange mailbox in a hidden folder, Purview retention policies "don't apply," admins "can't restrict what type of information is added," memory actions "don't generate audit log entries" `[S40]`; ChatGPT — memory rolled out across Free/Plus/Team/Enterprise 2024–25, view/edit/delete, "Don't mention this again," Temporary Chat `[S36, S37]`; Gemini — Saved Info, 18-month default auto-delete, "Memory turned on" required `[S38, S39]`; Meta AI — 1:1 chats only `[S41]`; Perplexity/Comet — search-only saves `[S42]`; Apple Intelligence — on-device + Private Cloud Compute `[S43]`.
- **Target reader:** Everyday users of AI assistants; privacy-conscious readers; IT admins.
- **Potential thesis:** Consumer memory is default-on with soft delete and no audit log — the memory layer sits, by design, outside the audit and DLP controls that govern the rest of the product.
- **Anchors:** S36–S43 (all C — vendor docs, current as fetched 2026-10-11). Rated medium-confidence in the Synthesis; verify defaults before publication.

### 3.2 The Erasure Gap
- **Angle:** A privacy-law piece. Deletion is soft and non-local — turning memory off does not delete past chats, deleted-memory logs can persist for 30 days, and deleting a memory does not remove its mentions elsewhere — and GDPR Art. 17 has no mechanism that reaches derived memory.
- **Research question:** How do GDPR Arts. 15–17, the EU AI Act, and data-residency rules interact with agent memory — and what would erasure that reaches summaries, embeddings, and graph edges require?
- **Evidence to build:** OpenAI's soft-deletion statements (30-day log retention, propagation lag, mentions persist) `[S37]`; Claude's documented view/edit with no explicit delete control `[S47]`; Art. 17's erasure duty and the derived-representation gap `[S61, S64]`; EDPB Opinion 28/2024 (models not automatically anonymous) `[S58]`; EU AI Act Art. 50 (transparency duties, no memory-specific duty, in force 2026-08-02) `[S60]`; CCPA/CPRA's 45-day window `[S62]`; the Garante €15M fine and its unsettled enforcement status `[S63]`; the Council of Europe draft's cross-layer deletion `[S64]` — secondary source only.
- **Target reader:** Privacy professionals, legal readers, and users exercising deletion rights.
- **Potential thesis:** The law grants erasure, but memory is redistributed across caches, vector stores, summaries, and derived logs — Art. 17 has no mechanism that reaches the derived copies.
- **Anchors:** S37, S47 (C); S58 (P); S60 (T); S61 (T); S62 (P); S63 (P); S64 (T — draft, secondary reporting; official text unconfirmed). The governance-law picture is rated medium/low-confidence; enforcement is unsettled.

## 4. Personal Agents: The Governance Inversion

### 4.1 The Best-Governed Memory Runs on Your Own Machine
- **Angle:** The inversion piece. The agents with the richest memory and the least central control — Hermes and OpenClaw — are also the ones whose memory the user can actually read, audit, and delete.
- **Research question:** What do the local-first personal agents ship that no cloud product in the survey matches, and what does the inversion imply for the "capability vs control" tradeoff?
- **Evidence to build:** Hermes — bounded `MEMORY.md` (≤2,200 chars) and `USER.md` (≤1,375 chars), FTS5 session search, per-profile isolation, on by default `[S82]`; OpenClaw — `MEMORY.md`, daily `memory/YYYY-MM-DD.md` notes, `USER.md`, `DREAMS.md`, "there is no hidden state," incognito mode (24 h, no flush, no archive), per-conversation scoping with opt-in cross-conversation recall `[S88, S89]`; the three-control-reality ranking (local-first > enterprise > consumer) `[06_Evidence/Findings.md RQ3]`; the cloud contrast `[S40, S37]`.
- **Target reader:** Self-hosters, tinkerers, and readers interested in the privacy/control tradeoff in AI tools.
- **Potential thesis:** Control tracks where the memory physically lives — the open, self-hosted agents have both the richest memory and the strongest controls, inverting the assumption that more capable means less governable.
- **Anchors:** S82–S85, S87–S93 (C docs + P repo metadata); contrast S37, S40 (C). No independent memory benchmark of Hermes was located; its only evaluation is its own Hermes Bench "Memory" category `[S86]`.

### 4.2 Approve Before It Remembers
- **Angle:** A mechanism piece. Hermes ships the only write-approval mechanism found in the survey — staged writes, an approval queue, and an explicit overwrite listing — and it defaults to off.
- **Research question:** What would a human review point for memory writes look like in practice, and why does the one shipping example default to off?
- **Evidence to build:** Hermes' approval flow — `/memory pending`, `/memory approve <id>|all`, `/memory reject <id>`, `/memory approval on|off`; approval output "lists the full text of every entry it overwrote or removed"; background writes tagged `[auto]`; `write_approval: false` default `[S82]`; MemSentry's Accept/Review/Quarantine write-gating `[S78]`; the Council of Europe draft's "point of effective human review" `[S64]`; the MGR's R8 review rule (`05_Memory_Record_Design/Design.md`).
- **Target reader:** Users of personal agents; product designers; governance readers.
- **Potential thesis:** The review primitive exists and is latent — the protection ships but is switched off, which makes the default, not the mechanism, the governance decision.
- **Anchors:** S78 (P preprint), S82 (C), S64 (T — draft). Whether any cloud product exposes an equivalent remains an open follow-up; none was found `[S40]`.

### 4.3 Self-Hosting Is Not Automatically Safer
- **Angle:** The counterpoint piece. The same local-first agents with the best controls are named targets of the newest memory-poisoning research — OpenClaw is the MemCollusion target — and Hermes' own security docs admit its guards are "not a hard boundary."
- **Research question:** Does moving memory off the cloud reduce risk, or does it move the attack surface — skill poisoning, cascading failures, persistent memory — onto the user's own machine?
- **Evidence to build:** Salami Attack / MemCollusion — 81.3% save rate / 75.0% success on OpenClaw, surviving dilution defenses `[S69]`; the OpenClaw security paper — "continuously running, skill-augmented system with persistent memory" exposed to skill poisoning and multi-agent cascading failures `[S94]`; Hermes' eight-layer security model admitting the guards are "not a hard boundary" `[S84]`; OpenClaw's gateway security (loopback-only default, security-audit tooling) `[S90]`; the broader poisoning evidence `[S65–S71]`.
- **Target reader:** Self-hosters and security-minded readers; the "run it locally" audience.
- **Potential thesis:** Self-hosting changes who bears the risk rather than removing it — the best-controlled memory in the survey is also a named target of the newest poisoning research.
- **Anchors:** S69, S94 (P preprints); S84, S90 (C). 2026-dated preprints; paper-reported, not independently replicated.

## 5. Security: Memory as an Attack Surface

### 5.1 Memory Poisoning Is a Real Attack Class
- **Angle:** A survey piece. Memory poisoning has moved from hypothetical to a named, benchmarked attack class — from sub-0.1% poison rates to query-only and background-saving attacks that need no prompt injection at all.
- **Research question:** What do the poisoning studies (AgentPoison, MINJA, MemoryGraft, Salami/MemCollusion, PipePoison, Mind Your HEARTBEAT) actually demonstrate, and how well do current defenses hold?
- **Evidence to build:** AgentPoison — <0.1% poison rate, >80% average attack success, <1% benign impact `[S66]`; MINJA — query-only poisoning, "any user" can influence memory `[S65]`; MemoryGraft — persistent behavioural drift across sessions `[S67]`; Salami/MemCollusion — 81.3% save / 75.0% success, survives dilution `[S69]`; PipePoison — jointly optimises write/retrieve/utilize, survives eight defenses `[S71]`; Mind Your HEARTBEAT — routine background saving moves untrusted content into durable memory without prompt injection `[S70]`; the MemSentry defense `[S78]`; reported 2026 agent-security incidents (PASAC) `[S72]`.
- **Target reader:** Security practitioners, AI red-teamers, and readers of AI-security research.
- **Potential thesis:** Memory poisoning persists, drifts behaviour across sessions, and survives most current defenses — the attacks now target the whole write/retrieve/utilize pipeline, not just the prompt.
- **Anchors:** S65–S72, S78 (P preprints, 2026-dated; paper-reported, not independently replicated). No disclosed real-world incident of memory poisoning was located; all evidence is lab/benchmark.

### 5.2 Provenance Laundering
- **Angle:** A mechanisms-security piece. Consolidation can launder a low-trust observation into apparent user history — without provenance, vulnerable memories reached up to 1.000 ASR; a provenance-preserving gate blocked the unauthorised high-risk actions.
- **Research question:** How does the absence of provenance let machine-inferred content be served as if the user said it — and what would provenance-preserving consolidation require?
- **Evidence to build:** The Memory Provenance Laundering study — consolidation rewrites low-trust observations as user history; up to 1.000 ASR without provenance; provenance gate blocked unauthorised actions `[S79]`; MemOS's MemCube treating provenance and versioning as first-class `[S03]`; MemSentry's write-gating `[S78]`; the MGR's monotone trust classes and append-don't-overwrite rule (`05_Memory_Record_Design/Design.md`); the Synthesis' root-cause claim that the privacy and security failures are two views of one defect.
- **Target reader:** Engineers building memory systems; security researchers; governance readers.
- **Potential thesis:** The privacy failure and the security failure are two views of one defect — a memory record that does not carry where it came from.
- **Anchors:** S03, S79 (P preprints); S78 (P preprint). The 1.000 ASR figure is paper-reported; the design rules are a proposal, not a finding.

### 5.3 The Tenant Next Door
- **Angle:** A multi-tenancy piece. When agents share a vector store, ordinary similarity retrieval leaks across users — and ownership gating is what restored the clean baseline.
- **Research question:** How does cross-tenant leakage occur in shared agent-memory deployments, and what isolation mechanisms actually hold?
- **Evidence to build:** MemLeak — cross-user semantic leakage through "ordinary similarity retrieval" on a shared vector store; ownership gating restored the clean baseline `[S68]`; scope as the second axis (session / project / user / team) `[S17, S23, S68]`; Mem0's `user_id`/`agent_id`/`run_id` scoping `[S07]`; Azure Foundry's scope quotas (100 scopes/store, 10,000 memories/scope) `[S46]`; the MGR's scope-enforced retrieval rule (`05_Memory_Record_Design/Design.md`).
- **Target reader:** Platform engineers, enterprise buyers, and anyone deploying multi-tenant agents.
- **Potential thesis:** Cross-boundary bleed is a scope failure, not a model failure — and the fix (ownership gating) is architectural, which makes it a deployment concern, not a benchmark one.
- **Anchors:** S68 (P preprint, 2026-dated); S07, S17, S23, S46 (C). Real-world (non-benchmark) leakage rates are unknown; no disclosed incident was located.

## 6. Enterprise, Law, and Evaluation

### 6.1 The Enterprise Has the Fix
- **Angle:** A market-structure piece. The enterprise platforms already ship the CRUD/TTL/revision primitives that a governance fix would need — the gap is a property of cloud consumer memory, not of the available technology.
- **Research question:** What do AWS Bedrock AgentCore, Vertex AI Memory Bank, and Azure AI Foundry actually document about memory controls — and why do consumer tools lack the equivalent?
- **Evidence to build:** Azure AI Foundry (preview) — item-level CRUD, store-level TTL, direct remember/forget, 100 scopes/store, 10,000 memories/scope, 30-day session deletion on inactivity `[S46]`; Vertex Memory Bank — memory generation/ingestion/retrieval, revision history, IAM conditions, VPC-SC, CMEK, residency `[S45]`; Bedrock AgentCore — short-term (single session) + long-term memory `[S44]`; the three-control-reality ranking `[06_Evidence/Findings.md RQ3]`; the MGR's build-on-existing-primitives argument (`05_Memory_Record_Design/Design.md`).
- **Target reader:** Enterprise architects, procurement readers, and governance professionals.
- **Potential thesis:** The market has three control realities, not two — local-first agents, enterprise platforms, and consumer assistants — and the primitives a fix needs already exist in the enterprise tier.
- **Anchors:** S44–S46 (C — preview/undated docs; verify current state). Salesforce Agentforce memory could not be verified (official pages failed to render) — an open follow-up, not a gap to paper over.

### 6.2 A Law with No Mechanism for Memory
- **Angle:** A regulation piece. GDPR grants erasure, the AI Act imposes transparency, and a Garante fine established precedent — but none of it has a mechanism that reaches derived memory, and a Council of Europe draft would change that.
- **Research question:** How do GDPR Arts. 15–17, the EU AI Act, and the Council of Europe draft interact with agent memory — and what is settled versus unsettled in enforcement?
- **Evidence to build:** GDPR Art. 17's erasure duty `[S61]`; EDPB Opinion 28/2024 and the ChatGPT Taskforce report `[S58, S59]`; EU AI Act Art. 50 — transparency duties, no memory-specific duty `[S60]`; CCPA/CPRA's 45-day window `[S62]`; the Garante €15M fine (Decision No. 755, 2 Nov 2024) and its temporary removal after a Court of Rome judgment (2026-03-18) `[S63]`; the CoE draft — memory-off-by-default, cross-layer deletion, separate read vs create/modify/transmit/delete permissions, agent inventories, revocable credentials `[S64]`.
- **Target reader:** Legal and compliance readers; policy watchers; privacy professionals.
- **Potential thesis:** The law is applicable but not memory-specific — the nearest legislated beachheads are a draft instrument and an unsettled enforcement precedent, not the statutes themselves.
- **Anchors:** S58 (P), S59 (P), S60 (T), S61 (T), S62 (P), S63 (P), S64 (T — draft, secondary reporting only). The governance-law picture is rated medium/low-confidence; treat the CoE draft as a reported signal.

### 6.3 The Benchmark Mismatch
- **Angle:** An evaluation piece. Vendors cite recall leaderboards (LoCoMo, LongMemEval) while the security literature shows the same class of system failing write-time integrity — MemSecBench found harmful memory persisted in 84.2% of cases.
- **Research question:** What do the mainstream memory benchmarks actually measure — and what would a shared, reproducible benchmark reporting utility *and* integrity/leakage together look like?
- **Evidence to build:** LoCoMo (long-dialogue QA, no privacy dimension) `[S73]`; LongMemEval (five abilities, ~30% accuracy drop over sustained interaction) `[S74]`; MemoryAgentBench (four competencies including selective forgetting) `[S75]`; MemBench (factual vs reflective) `[S76]`; MemSecBench (84.2% harmful persistence, 50.3% write-to-execute, 56.1% selective repair) `[S77]`; MemGauge's utility–risk framing `[S80]`; the vendor benchmark claims the leaderboards rest on `[S15, S16, S48, S54]`; the open follow-up calling for a shared reproducible benchmark `[06_Evidence/Findings.md]`.
- **Target reader:** Researchers, evaluators, and practitioners choosing memory systems.
- **Potential thesis:** A memory that scores well on recall and can be poisoned or leak across tenants is not a safe memory — the field's leaderboards measure the wrong axis.
- **Anchors:** S73–S80 (P; 2026-dated security preprints not independently replicated); S15, S16, S48, S54 (C — vendor benchmark claims, non-comparable).

## 7. Design and Infrastructure

### 7.1 A Record for Every Memory
- **Angle:** A design-proposal piece. The Memory Governance Record v0 — an envelope of provenance, trust class, scope, and append-only history that any existing memory store could carry.
- **Research question:** What would an auditable memory record require — and which of its rules can be built on primitives that already exist?
- **Evidence to build:** The MGR v0 fields and rules R1–R8 — append-don't-overwrite, monotone trust classes, scope-enforced retrieval, tombstones that propagate, visible write history, human review point (`05_Memory_Record_Design/Design.md`); the existing primitives it would ride on — MemOS's MemCube `[S03]`, MemSentry `[S78]`, the PPMF provenance gate `[S79]`, Azure/Vertex CRUD/TTL/revisions `[S46, S45]`, the MCP memory server's explicit delete/search operations `[S34]`, Hermes' approval queue `[S82]`; the CoE draft's requirements list `[S64]`.
- **Target reader:** Engineers and standards-minded readers; governance professionals.
- **Potential thesis:** The governance gap is addressable with existing primitives — the missing piece is a record that travels with the memory, not a new storage engine.
- **Anchors:** S03, S34, S45, S46, S64, S78, S79; design doc `05_Memory_Record_Design/Design.md`. This is a design proposal, not a finding — label it as such wherever it is cited.

### 7.2 The Memory Layer's Benchmark Problem
- **Angle:** A market-skepticism piece. The memory-infrastructure vendors' headline numbers are self-reported and non-comparable — and at least one reputable secondary report argues memory can *degrade* outputs.
- **Research question:** How much can be trusted in the memory-infrastructure market's claims — Mem0's adoption figures, Zep's LoCoMo/LongMemEval scores, Redis' accuracy claim — and what would independent verification require?
- **Evidence to build:** Mem0 — reported $24M raise with undisclosed valuation, company-supplied adoption figures (41k+ GitHub stars, 186M API calls in Q3 2025), homepage benchmark names without scores `[S48, S50]`; Mem0's pricing gates (graph memory and "Dream" at Pro, $249/mo) `[S49]`; Zep's self-reported LoCoMo 94.7% / LongMemEval 90.2% `[S54]`; Redis' "86.5%" `[S56]`; the June 2026 TechCrunch summary of two Writer papers arguing memory/personalisation can degrade outputs `[S51]`; the non-comparability finding `[06_Evidence/Findings.md RQ3]`.
- **Target reader:** Buyers evaluating memory-infrastructure vendors; market watchers; skeptics.
- **Potential thesis:** The memory layer's marketing runs ahead of its evidence — the headline numbers name different benchmarks, none was reproduced under a shared protocol, and the one independent report points the other way.
- **Anchors:** S48–S51, S54, S56 (C/T — vendor claims and secondary reporting). Vendor benchmark figures are rated low-confidence; a shared reproducible benchmark is an open follow-up.

## Best First Pitches

1. **"Memory Is a Product Feature—and a Privacy Boundary" (1.3)** — the originating CAM idea, historically rated first, now backed by the full Stage 1 survey; the umbrella piece.
2. **"The Best-Governed Memory Runs on Your Own Machine" (4.1)** — the survey's sharpest finding (the governance inversion), with a strong narrative contrast between tiers.
3. **"Memory On by Default" (3.1)** — the consumer privacy hook; concrete, verifiable against vendor documentation, and the most directly reader-relevant.
4. **"The Benchmark Mismatch" (6.3)** — timely, evidence-dense, and frames the evaluation gap the whole field is missing.
5. **"A Record for Every Memory" (7.1)** — the design deliverable; turns the survey's diagnosis into a constructive proposal with existing primitives.

## Research Guardrails

- **Pitches are proposals, not findings.** Every `S##` anchor is a source lead to verify. Do not promote any claim from idea to finding without primary verification; do not invent source IDs, quotes, or product facts.
- **Vendor-documentation bias.** Nearly every product claim in the survey rests on a **C** source — the vendor's own docs are the only public description of its memory. Treat product capabilities as vendor claims until reproduced; date-stamp everything (access date 2026-10-11 applies to undated vendor pages).
- **Self-reported benchmarks.** Mem0/Zep/Redis figures come from vendor-authored papers or vendor pages, name different benchmark subsets, and are not comparable. Never combine them into a ranking.
- **2026-dated security preprints.** The poisoning, leakage, and provenance-laundering figures (including MemSecBench's 84.2% and the 1.000 ASR result) are paper-reported and not independently replicated. Label them as such.
- **Draft law.** The Council of Europe instrument (T-PD(2025)3rev4) was located via secondary reporting only; the official text was not confirmed. Treat it as a reported signal, not a proposal in force.
- **No real-world incident rate.** No disclosed incident of memory poisoning or cross-tenant leakage was located; all security evidence is lab/benchmark. Do not imply otherwise.
- **Claim-type discipline.** Preserve `[documented fact]` / `[reported signal]` / `[inference]` distinctions; keep vendor claims, preprints, estimates, and unresolved questions explicitly qualified. Keep internal `S##` IDs and local paths out of reader-facing prose — this file is the internal source map.
- **Open follow-ups to respect, not resolve.** The change-log gap (Hermes vs cloud), GDPR Art. 17 erasure reaching derived memory, Agentforce verification, Cursor Projects persistence, a shared reproducible memory benchmark, and real-world poisoning/leakage rates are all open questions in the survey — pitches may target them but must not pretend they are answered.
