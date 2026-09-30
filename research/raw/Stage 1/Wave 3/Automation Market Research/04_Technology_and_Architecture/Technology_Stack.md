# Automation technology stack

## Layered model

```text
User / business interface
  -> workflow definition and policy
  -> orchestration runtime
  -> queue / event / scheduler
  -> connectors, APIs, UI robots, databases
  -> models and agents where useful
  -> identity, secrets, audit, observability
```

## Key technologies

- **Triggers:** webhooks, schedules, queues, database changes, email, UI events.
- **Control flow:** DAGs, state machines, conditional branches, loops, map-reduce, approvals.
- **Execution:** serverless functions, containers, workers, desktop robots, browser automation.
- **Durability:** checkpoints, event history, retries, timers, idempotency keys, compensation.
- **AI:** model calls, tool calling, retrieval, structured output, evaluators, agent handoffs.
- **Interoperability:** REST, GraphQL, webhooks, JSON-RPC, MCP for tools/resources, A2A for agent collaboration.
- **Governance:** identity, RBAC, secrets, data loss prevention, audit logs, policy engines.
- **Observability:** traces, run histories, process mining, metrics, alerts, replay and evaluation.

## Architecture principle

Use deterministic automation for predictable transformations and use agents where interpretation, planning, or adaptation provides real value. Put an explicit boundary around every side effect.
