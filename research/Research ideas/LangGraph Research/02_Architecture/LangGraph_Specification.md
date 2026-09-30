# ADR: Safe LangGraph orchestration boundary

- **Status:** Proposed for implementation review
- **Date:** 2026-09-29
- **Research ID:** RQ-AGT-03
- **Gap:** GAP-AGT-03
- **Decision owners:** Research pipeline maintainers

## Context

The Stage 2 research pipeline needs multi-agent execution with durable recovery and human approval before consequential actions. The original skeleton names Task, Function, Signal, and Loop nodes, but current LangGraph documentation models these as ordinary node functions, edges/conditional edges, `interrupt()`, and bounded routing—not as four mandatory node classes.

## Decision

Adopt the following topology:

```text
START
  -> intake
  -> plan
  -> fan_out (conditional edge / Send)
  -> worker_1 ... worker_N
  -> aggregate
  -> approval_gate (interrupt)
  -> commit_adapter
  -> END
```

Failure routes are explicit:

```text
worker failure -> retry (bounded) -> worker
retry exhausted -> review_required -> approval_gate or END(rejected)
approval rejected -> revise or END(cancelled)
commit failure -> compensate/recover -> END(manual_recovery)
```

## State contract

Required fields:

- `run_id`, `thread_id`, `schema_version`
- `tasks`: task ID, assigned agent, status, attempt, input hash, output reference
- `evidence`: source IDs, claims, confidence, provenance
- `approval`: required, reviewer role, decision, decision ID, timestamp
- `operations`: idempotency key, adapter, request hash, remote result, compensation status
- `errors`: normalized class, retryable flag, attempt, last checkpoint
- `audit`: append-only event records

Use reducers explicitly for lists and maps modified in parallel. Do not rely on implicit last-writer-wins behavior for aggregated evidence.

## Checkpoint policy

1. Compile with a durable checkpointer in production.
2. Require a stable, bounded `thread_id`; never use a new ID to resume an interrupted run.
3. Accept the super-step boundary as the minimum recovery unit.
4. Checkpoint after intake, plan, each fan-out batch, aggregate, approval, and commit outcome.
5. Keep irreversible side effects in a separate adapter node after approval.
6. Use task-level checkpointing only when a node contains multiple deterministic operations that benefit from replay avoidance.
7. Apply retention, access control, encryption, and redaction to checkpoint storage.

## HITL contract

The approval payload must be JSON-serializable and include:

```json
{
  "kind": "approval_request",
  "operation_id": "op-<stable-id>",
  "action": "publish_research_result",
  "target": "<system/resource>",
  "evidence": ["source-id"],
  "risk": "high",
  "required_role": "research-maintainer",
  "expires_at": "<timestamp>"
}
```

Call `interrupt(payload)` exactly once per node invocation for a simple gate. Keep interrupt order stable if a node has multiple interrupts. On resume, the node restarts from its beginning, so all pre-interrupt effects must be idempotent; preferably put effects after the interrupt.

Allowed decisions are `approve`, `reject`, and `request_revision`. Any other value is invalid and loops to a validation node. An approval is scoped to one `operation_id`, one state hash, and one graph schema version.

## MCP/A2A adapter contract

Adapters must:

- Validate inputs and permissions before network calls.
- Attach `run_id`, `thread_id`, `operation_id`, and a request hash.
- Classify errors as retryable, authorization, validation, rate-limit, remote-side-effect-unknown, or permanent.
- Use idempotency keys or a read-before-write check.
- Return structured results and never hide partial success.
- Emit an audit record for request, response, retry, approval, and compensation.

MCP tool confirmation is complementary to LangGraph approval. MCP does not provide the graph checkpoint or rollback semantics; the adapter boundary must connect the two explicitly.

## Alternatives rejected

- **Checkpoint only at end:** loses partial progress and makes crash recovery unsafe.
- **Human approval after commit:** cannot prevent the consequential action.
- **In-memory saver in production:** state disappears on process restart.
- **Unbounded self-correction loop:** can consume resources and evade review.
- **Assuming checkpoint restore rolls back remote calls:** checkpoint state and remote state are separate systems.

## Consequences

Positive: deterministic recovery points, explicit authorization, testable failure paths, and a clean integration boundary for MCP/A2A agents.

Costs: durable storage, schema/version management, idempotency work, approval UI/queue, checkpoint retention, and operational handling for manual recovery.

## Acceptance criteria

- POC passes 10 concurrent tasks with no lost task result.
- Crash/restart resumes from the last checkpoint using the same thread ID.
- Replayed worker does not duplicate its operation.
- Commit is unreachable without approval when approval is required.
- Rejection and retry exhaustion produce terminal, auditable states.
- Senior maintainer reviews this ADR before merge.

## Source basis

See [[../01_Evidence/Sources|Evidence ledger]] and [[../01_Evidence/Findings|Findings]].
