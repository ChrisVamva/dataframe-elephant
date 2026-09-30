# Research findings

## 1. Minimal graph semantics

LangGraph requires three conceptual elements: **state** (shared snapshot), **nodes** (functions that compute updates), and **edges** (routing). Execution proceeds in discrete super-steps. Parallel nodes in one super-step must use reducers that define how concurrent updates combine.

The minimal safe workflow therefore needs:

- Typed state with task IDs, statuses, evidence, approvals, errors, and an audit trail.
- Deterministic routing functions for normal, retry, review, and terminal paths.
- A bounded loop with an explicit retry counter and recursion limit.
- Idempotent node logic because a paused or retried node can execute again from its beginning.

## 2. Checkpointing strategy

Checkpointing occurs at graph/super-step boundaries, not arbitrary instruction lines inside a node. A durable checkpointer keyed by `thread_id` is mandatory for crash recovery and HITL. In-memory savers are suitable only for development because process restart loses state.

Recommended policy:

- Checkpoint after intake, planning, each worker super-step, aggregation, approval, and commit.
- Persist after every worker batch rather than only at the end.
- Use a database-backed saver in production; SQLite is acceptable for local development and PostgreSQL for shared/production operation.
- Apply retention and encryption policies; checkpoint data can contain sensitive prompts, tool inputs, and results.

## 3. Human approval

Use `interrupt(payload)` at the last safe point before a consequential external action. Surface a JSON-serializable review object containing proposed action, target, evidence, risk, and required role. Resume with `Command(resume=...)` on the same `thread_id`.

Approval must be explicit. Rejection routes to a cancelled/revision state, not to the commit node. Multiple parallel interrupts require stable interrupt IDs and a mapping from each ID to its response.

## 4. MCP/A2A integration boundary

MCP/A2A calls should be wrapped in adapter nodes. LangGraph owns orchestration state, retries, approval, and recovery. The adapter owns protocol serialization, authentication, timeout handling, and remote error classification. Never assume that a LangGraph checkpoint rolls back a remote system: compensating actions or idempotency keys are required.

## 5. Rollback semantics

LangGraph time travel/state updates can alter graph state, but they do not undo an already completed external side effect. The system must record an operation ID before/with the call, use idempotent upsert semantics where possible, and define a compensating action or manual recovery path for non-reversible effects.

## 6. Resolved question

**Answer:** The minimum safe topology is a typed `StateGraph` with deterministic nodes and conditional edges, persistent thread-scoped checkpoints at super-step boundaries, an explicit interrupt immediately before consequential side effects, and idempotent/compensatable adapters. This preserves HITL without losing pipeline position after interruption or process failure.

## 7. Falsifiers

The design is invalid if a test demonstrates any of the following:

1. A process crash followed by the same `thread_id` loses completed task state.
2. A worker can reach a consequential adapter without an approval record when policy requires approval.
3. A retry duplicates a remote mutation despite the same operation ID.
4. A rejected approval can still reach commit.
5. A parallel fan-out produces nondeterministic or overwritten aggregate state because its reducer is not associative/defined.
6. An unbounded loop can exceed the configured safety limit without a controlled terminal outcome.
