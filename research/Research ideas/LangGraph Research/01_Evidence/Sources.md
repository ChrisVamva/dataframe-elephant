# Evidence ledger

**Accessed:** 2026-09-29  
**Minimum evidence class:** official LangChain/LangGraph documentation and official MCP specification.

## LangGraph sources

1. [Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api) — defines state, nodes, edges, `StateGraph`, reducers, super-steps, `Send`, `Command`, recursion limits, node re-execution, and graph migrations.
2. [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) — distinguishes thread-scoped checkpointers from cross-thread stores; documents production persistence and retention concerns.
3. [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) — defines dynamic interrupts, checkpoint requirements, `thread_id`, resume semantics, approval/rejection, validation, and idempotency rules.
4. [Subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs) — documents checkpoint namespaces and the need for checkpointing for durable subgraph execution.
5. [Fault tolerance](https://docs.langchain.com/oss/python/langgraph/fault-tolerance) — operational guidance for retries, handling failures, and idempotent work.
6. [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) — positions LangGraph as an orchestration runtime with durable execution, persistence, streaming, and HITL.

## MCP source

7. [MCP Tools specification, 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) — defines model-controlled tools, JSON schemas, protocol vs execution errors, input validation, access control, rate limiting, confirmation for sensitive operations, and audit logging.
8. [MCP Sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) — describes nested model calls and client-side oversight; relevant when an MCP server requests model assistance.
9. [MCP Elicitation](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation) — describes interactive user-input requests initiated by servers.

## Evidence notes

- The skeleton's `langgraph.readthedocs.io` target is superseded by the current LangChain documentation URLs above.
- The skeleton's `Signal` terminology should not be treated as a native LangGraph node type without a project-specific adapter.
- MCP provides a protocol surface for tools and user interaction; it does not provide LangGraph checkpointing, graph topology, rollback, or transaction semantics.
- Official documentation establishes semantics and constraints, not a universal checkpoint interval in seconds. The recommendation in the ADR is therefore a policy derived from those semantics, not a vendor guarantee.
