# Validation protocol

## Gate A — Scope

- Confirm the implementation uses LangGraph graph semantics, persistence, HITL, and adapters.
- Exclude vendor-specific infrastructure tuning and throughput benchmarking.
- Record LangGraph and adapter versions.

## Gate B — Falsification

Run tests that attempt to:

1. Resume after a crash with the same `thread_id`.
2. Resume with a new thread ID and confirm it does not silently inherit state.
3. Commit after rejection and confirm permission failure.
4. Replay a successful operation and confirm no duplicate mutation.
5. Alter state after approval and confirm stale approval is rejected.
6. Exhaust retries and confirm controlled terminal state.

## Gate C — Provenance

Every result must retain source IDs, agent/task ID, input hash, operation ID, checkpoint ID, reviewer identity, decision timestamp, and adapter response reference.

## Gate D — Score coverage

Original priority score: **16.0** = centrality 4 × severity 4 ÷ difficulty 1. Re-score if the affected pipeline stage changes.

## Required simulation

- 10 concurrent tasks.
- At least one worker retry.
- One process restart after a checkpoint.
- One approval and one rejection path.
- One duplicate commit replay.
- One injected unknown remote outcome.
- Assertions on state preservation, authorization, idempotency, and audit completeness.

## Review gate

A senior agent/designer/maintainer must review the ADR and test evidence before the dossier is moved into `research/processed/FollowUps/`. The original skeleton remains unchanged as the research input; this folder is the organized completed dossier.
