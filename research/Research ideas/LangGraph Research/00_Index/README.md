# LangGraph Workflow Orchestration Boundary

**Research ID:** RQ-AGT-03  
**Gap:** GAP-AGT-03  
**Status:** Completed research dossier  
**Completed:** 2026-09-29

## Decision summary

Use a compiled `StateGraph` with explicit state, deterministic nodes, conditional edges, and a persistent checkpointer. Treat each super-step/node boundary as the recovery unit. Place `interrupt()` immediately before any consequential MCP/A2A/tool side effect that requires approval; resume with `Command(resume=...)` using the same `thread_id`.

The design does **not** rely on a LangGraph `Signal` node: `Signal` is not a canonical LangGraph graph primitive in the current official API. External signals are represented as interrupt payloads, state updates, or application-level events.

## Folder map

- [[LangGraphSkeleton|Original skeleton]] - initial research brief.
- [[../01_Evidence/Sources|Sources]] - authoritative documentation and evidence ledger.
- [[../01_Evidence/Findings|Findings]] - synthesized answers to the skeleton questions.
- [[../02_Architecture/LangGraph_Specification|Formal specification / ADR]].
- [[../03_Proof_of_Concept/README|Proof-of-concept guide]].
- [[../04_Risk_and_Validation/Risk_Analysis|Risk analysis]].
- [[../04_Risk_and_Validation/Validation_Protocol|Validation protocol]].

## Quality gates

- **Gate A — Scope:** in/out boundaries and intended use are explicit.
- **Gate B — Falsifier:** failure conditions are testable.
- **Gate C — Provenance:** findings trace to official sources and the originating skeleton.
- **Gate D — Scoring:** P1 priority is retained from the skeleton: centrality 4, severity 4, difficulty 1 = 16.0.

## Research conclusion

The minimal safe topology is:

`START → intake → plan → fan-out(worker × N) → aggregate → approval interrupt → commit → END`

Failures before approval are retried or routed to review. Failures after approval are compensated or marked for operator recovery; they are never silently replayed as if the external side effect had not happened.

## Reproduction

The POC uses only the Python standard library and is intentionally independent of LangGraph packages. It demonstrates the behavioral contract; the ADR maps each simulated step to the corresponding LangGraph primitive.

Last reviewed: 2026-09-29.