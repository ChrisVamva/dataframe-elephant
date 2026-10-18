# AI Agent Memory — Memory as a Product Feature and a Privacy Boundary

**Wave:** 7 (`research/raw/Stage 1/Wave 7/`; created as Wave 6, renumbered by the user 2026-10-11)
**Origin:** CAM agent-tools landscape, idea 1.3 "Memory Is a Product Feature—and a Privacy Boundary" (`Artifacts/Article Ideas/6/CAMidea.md`), rated first in `Artifacts/Article Ideas/6/CAMidearatings.md` (2026-10-11); promoted to a Stage 1 research subject by the user on 2026-10-11
**Protocol context:** `FreeBrainstorming.md` / `ArticleCreation.md` framing; external, product-grounded research (no internal project dependencies)

## Research Question

What do AI agents actually remember, who controls that memory, how is stale or sensitive context removed, and what does the evidence — product documentation, reproducible behaviour, regulation, and security research — support?

## Research Questions (decomposed)

- **RQ1 — Taxonomy and scope:** What counts as "memory" for an AI agent — session/context window, explicit project instructions, searchable conversation history, summarised/compacted state, external memory services, knowledge/temporal graphs — and what does each actually preserve, for how long, and across which boundary (session / project / user / team / tenant)?
- **RQ2 — Mechanisms and failure modes:** How is each memory type implemented (retrieval/RAG, compaction, graph extraction, tool-driven writes), and where does it fail — retrieval precision, staleness, silent compaction loss, contaminated or hallucinated memory, cross-session bleed? What do the technical and academic sources show?
- **RQ3 — Product reality:** What do shipped products (coding agents, AI assistants, enterprise agent platforms, memory-infrastructure vendors) actually *document*, and which capability claims are primary-source-backed versus marketing? Storage location, scope, inspection/edit/delete controls, and version.
- **RQ4 — Control, privacy, and security:** Who can inspect, edit, delete, export, or pin memory; how is stale or sensitive content removed; how do GDPR Arts. 15–17, the EU AI Act, and data-residency rules interact with agent memory; and what is documented about memory poisoning, indirect prompt injection that persists in memory, secret/PII leakage, and multi-tenant isolation?
- **RQ5 — Evaluation and record design:** How is memory quality measured (benchmarks, adversarial tests), and what would an auditable **Memory Governance Record** require — provenance of each memory, its source turn, its scope, its confidence, and an append-only change history?

## Method Sketch

Adapt the `ArticleCreation.md` evidence discipline to a product-research subject:

- Every factual claim in folders 01–05 cites an `S##` entry in `06_Evidence/Sources.md`.
- Claim-type tags follow `Research-Evaluation.md`: `[documented fact]` (official docs / specification / peer-reviewed / regulator), `[reported signal]` (company self-claim, single-source reporting), `[inference]` (survey synthesis).
- Vendor capability claims stay labelled as vendor claims until a primary document or reproducible test confirms them.
- Date-stamp findings; superseded material moves to `99_Archive/`, never deleted.

Deliverables: (a) a verified product-capability matrix, (b) a memory failure-mode taxonomy, (c) a **Memory Governance Record** design v0 (`05_Memory_Record_Design/`).

## Folder Skeleton

| Folder | Purpose | Status |
|--------|---------|--------|
| `00_Index/` | Status tracker + Synthesis (RQ answers) | Done |
| `01_Background/` | What agent memory is: six-type taxonomy, the context-vs-memory distinction, scope, why it matters | Done |
| `02_Mechanisms/` | How memory is implemented (retrieval, compaction, graph extraction, tool writes, dreaming/flush) and its documented failure modes | Done |
| `03_Products/` | Product landscape: coding agents, consumer assistants, enterprise platforms, **autonomous/personal agents (Hermes, OpenClaw)**, infrastructure vendors | Done |
| `04_Privacy_and_Security/` | Control, inspection, deletion, retention, portability; GDPR / AI Act; memory poisoning, leakage, multi-tenant isolation; incidents | Done |
| `05_Memory_Record_Design/` | The deliverable: Memory Governance Record design v0 | Done |
| `06_Evidence/` | `Sources.md` (S## register, `S01`–`S95`) + `Findings.md` | Done |
| `99_Archive/` | Superseded material (never deleted) | Empty |

## Scope and Boundary (settled with the user, 2026-10-11)

The subject is **AI agents**, not coding agents only. The survey covers four product tiers plus the tooling layer:

1. **Coding / developer agents** — Claude Code, Cursor, Copilot, Cline, Codex, Gemini CLI, Aider, Zed, Continue, JetBrains, Amazon Q (group B).
2. **Consumer chat assistants** — ChatGPT, Gemini, Copilot (M365), Meta AI, Perplexity/Comet, Apple Intelligence: general-purpose, cloud-hosted, end-user assistants (group C).
3. **Enterprise agent platforms** — AWS Bedrock AgentCore, Vertex AI Memory Bank, Azure AI Foundry, Agentforce (group C).
4. **Autonomous and personal agent platforms** — Hermes Agent and OpenClaw: open-source, local-first agents that run continuously and build a user model (group H). The user identified these as the more interesting cases, and the research bears it out — they ship the richest memory *and* the strongest controls.
5. **Memory-infrastructure vendors** — Mem0, Letta, Zep, LangMem, Redis, Neo4j (group D).

- **Excluded:** general document RAG with no agent persistence, and model-internal/persona memory that is neither inspectable nor user-controllable (noted only where it overlaps the boundary question).
- **Group H was added in a second pass** after the user widened the scope; it reordered the findings — the local-first personal agents turned out to be the *best-governed* memory systems examined, which no coding-agent or consumer-assistant product matches (see `00_Index/Synthesis.md`).

## Conventions

- Reliability scale: **P** primary (official docs, specification, regulator, peer-reviewed), **T** reputable secondary (major news, established trade press, data-driven think tank), **C** company/self-published claim (verify before relying).
- Every factual claim in folders 01–05 references an `S##` register entry.
- Date-stamp all findings; record current product versions where the source states them.

## Working Pattern (established in Fusion Energy, approved by user; reused in Waves 3–5)

1. Create skeleton → 2. parallel research agents → 3. fill notes citing the `S##` register → 4. Stage 2 promotion when the survey stabilizes.
