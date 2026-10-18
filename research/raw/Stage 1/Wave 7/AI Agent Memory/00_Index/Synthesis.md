# Synthesis — AI Agent Memory (Wave 7)

_Date: 2026-10-11. Answers to RQ1–RQ5 with falsifiers. Every claim cites `[S##]` from `../06_Evidence/Sources.md`. Claim-type tags: `[documented fact]` / `[reported signal]` / `[inference]`._

## Central finding

**Agent memory is a product feature whose recall is improving faster than its governance — but the governance gap is a property of *cloud* memory, not of memory as such.** Memory takes at least seven forms with different lifetimes and control surfaces `[S01, S17, S37, S09, S07, S06, S82]`; the mechanisms that improve recall — extraction, consolidation, background "dreaming," graph invalidation `[S15, S04, S05, S06]` — are the same mechanisms that silently rewrite what the system believes. The privacy risk and the security risk are two views of one defect: a memory record does not carry **where it came from**, so erasure cannot find derived copies `[S61, S64]` and consolidation can launder a low-trust observation into apparent user history at up to 1.000 ASR `[S79]`. Control tracks where the memory physically lives. The **consumer assistants** are default-on with soft delete and no audit log `[S40, S37]`; the **enterprise platforms** already ship the CRUD/TTL/revision primitives a fix would need `[S46, S45]`; and the **local-first personal agents** — Hermes and OpenClaw — keep memory as on-disk Markdown with an approval queue and, in Hermes, an explicit overwrite listing, making them the best-governed systems in the survey `[S82, S88]`. The sharpest finding is that inversion: the agents with the richest memory and the least central control are also the ones whose memory the user can actually read, audit, and delete.

## RQ1 — What counts as memory

- Six types, one label: session/context, instruction files, searchable history, summarised state, extracted records, knowledge/temporal graphs `[S01, S17, S37, S09, S07, S06]`.
- Coding agents still lean on **human-owned instruction files**, but agent-written memory is spreading fast (Claude Code, Codex, Gemini CLI, Kiro, Devin, legacy Cascade; Cursor Projects partial) `[S17–S32, S96, S100, S102]`.
- The design has **converged** on a `MEMORY.md` entry point plus Markdown notes on disk, consolidated in the background `[S17, S82, S88, S96, S100]`.
- The **autonomous/personal agents** add a seventh pattern — local-first Markdown on disk (`MEMORY.md`, `USER.md`, daily notes), on by default, that the user can read and edit `[S82, S88]`.
- Scope (session / project / user / team) is the axis that decides whether memory is useful or dangerous `[S17, S23, S68]`.

## RQ2 — Mechanisms and failure modes

- The **write decision** (store / dedupe / overwrite) is the least-standardised and least-inspectable stage; overwrite semantics differ between two systems both labelled "memory" `[S07, S04]`.
- Compaction and background consolidation are **lossy by construction** `[S09, S04, S05]`.
- Long context **delays** but does not remove the memory problem — effective context is far below nominal `[S11, S12, S10]` and the literature is split on LC vs RAG `[S13, S14]`.
- Seven failure modes: staleness, silent loss, retrieval imprecision, confabulation, poisoning, cross-boundary bleed, non-determinism `[S06, S09, S12, S15, S65, S68]`.

## RQ3 — Product reality

- The tiers are: **coding agents** (instruction-file dominated) `[S17–S32]`; **consumer assistants** — cloud, general-purpose chat assistants for end users: ChatGPT, Gemini, Copilot, Meta AI, Perplexity, Apple Intelligence `[S36–S43]`; **enterprise platforms** `[S44–S46]`; and **autonomous/personal agents** (Hermes, OpenClaw) `[S81–S95]`.
- Consumer memory is **on by default** with soft, non-local deletion and no audit log `[S40, S37]`.
- The **personal-agent tier is the best-governed**: on-disk Markdown, an approval queue (Hermes) and incognito/per-conversation scoping (OpenClaw) `[S82, S88, S89]`; enterprise platforms expose CRUD/TTL/revisions but no consumer-facing audit `[S46, S45]`; Agentforce could not be verified `[—]`.
- Infrastructure benchmark numbers are **self-reported and non-comparable** `[S15, S16, S51, S54]`.

## RQ4 — Control, privacy, security

- Deletion is partial: it removes the memory object, not derived logs, chats, embeddings, or summaries `[S37, S61, S64]`.
- Memory change history is tier-dependent: absent in cloud products `[S40]`, present in Hermes (approval + overwrite listing) `[S82]`.
- Memory poisoning is a **named, benchmarked attack class** surviving most defenses `[S65, S66, S67, S69, S70, S71]`; cross-tenant leakage is demonstrated `[S68]`.
- The CoE **draft** proposes memory-off-by-default and cross-layer deletion `[S64]`, but official text was not confirmed; the Garante enforcement precedent is unsettled `[S63]`.

## RQ5 — Evaluation and record design

- Public benchmarks test **utility only** (LoCoMo, LongMemEval, MemoryAgentBench, MemBench) `[S73–S76]`; security benchmarks are new and show high failure (MemSecBench: 84.2% harmful persistence) `[S77, S79]`.
- A **benchmark mismatch** persists: vendors cite recall leaderboards while write-time integrity fails `[S15, S54, S77]`.
- **Design answer:** a Memory Governance Record v0 — append-don't-overwrite, monotone trust classes, scope-enforced retrieval, tombstones that propagate, visible write history — buildable on primitives that already exist `[S03, S34, S45, S46, S79]` (`../05_Memory_Record_Design/`).

## Material claims and their falsifiers

| Claim | Falsifier |
|-------|-----------|
| Consumer memory is on by default with no audit log `[S40, S37]` | An official page showing memory off by default, or audit-log entries, for a major consumer assistant |
| Memory change history exists in the self-hosted agents (Hermes `[S82]`) but not in cloud products `[S40]` | A cloud assistant or enterprise platform exposing a per-memory change history |
| Consolidation can launder low-trust content `[S79]` | A production memory service that preserves provenance through consolidation as a default |
| Deletion does not reach derived memory `[S37, S61]` | A product demonstrating erasure across summaries, embeddings, and graph edges on request |
| Memory poisoning persists across sessions `[S67, S69, S71]` | A deployed system with no observed drift after a benchmarked poisoning attempt |
| Effective context ≪ nominal context `[S11, S12, S10]` | Reproduced studies showing uniform performance across full nominal context |
| Vendor benchmarks are non-comparable `[S15, S16, S51, S54]` | A shared protocol reproducing vendor LoCoMo/LongMemEval figures |

## Confidence

- **High:** the six-type taxonomy and the instruction-file dominance of coding agents `[S17–S32]`; the context-length degradation findings `[S11, S12, S10]`; the existence and mechanics of memory poisoning as a research class `[S65–S71]`.
- **Medium:** product-specific controls and defaults (all rest on C sources, current-as-fetched only) `[S36–S47]`; the governance-law picture (draft text unconfirmed; enforcement unsettled) `[S63, S64]`.
- **Low / to verify:** all vendor benchmark figures `[S15, S16, S51, S54]`; the 2026 security-preprint numbers `[S67–S72, S77–S80]`; any real-world incident rate `[—]`.

## What this wave enables

- **Article (CAMidea 1.3):** the privacy-boundary piece becomes writable — hook (consumer memory is on by default and you cannot audit it `[S40, S37]`), a sharper contrast (the self-hosted agents do let you read, approve, and delete memory `[S82, S88]`), evidence (the taxonomy, the poisoning class, the deletion gap), honest limits (lab evidence, C sources, self-reported benchmarks).
- **Next steps:** (1) verify the open follow-ups in `../06_Evidence/Findings.md`; (2) re-rate CAM idea 1.3 evidence once primary verification is done; (3) when the survey stabilises, promote to Stage 2 (`research/raw/Stage 2/`) and a `agent_memory.duckdb` for the notebook/claims pipeline.
