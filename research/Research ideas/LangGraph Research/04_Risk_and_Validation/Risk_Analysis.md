# Risk analysis

| Risk | Failure mode | Mitigation | Verification |
|---|---|---|---|
| State loss | Process restart loses progress | Durable checkpointer and stable `thread_id` | Kill/restart test |
| Duplicate side effect | Node reruns after interrupt/retry | Idempotency key, upsert, or read-before-write | Replay same operation twice |
| Unauthorized action | Worker reaches adapter without approval | Gate immediately before adapter; verify approval scope | Negative-path test |
| Stale approval | State changes after review | Bind approval to state hash, operation ID, schema version, expiry | Mutate state then resume |
| Partial remote success | Timeout hides whether remote call happened | Query-by-operation ID; classify unknown outcome; compensate/manual recovery | Inject timeout after request |
| Reducer conflict | Parallel updates overwrite one another | Explicit associative reducers and unique task IDs | 10-way fan-out with shuffled completion |
| Infinite loop | Agent keeps retrying/self-correcting | Retry budget, recursion limit, terminal review state | Exhaust retry budget |
| Unserializable payload | Checkpoint or interrupt cannot be encoded | JSON-serializable state and payload schemas | Serialization test |
| Sensitive checkpoint | Prompts/tokens/results exposed | Redaction, encryption, access control, retention | Inspect stored checkpoint |
| Subgraph boundary | Parent cannot see child state or recovery point | Explicit namespace/store contract and checkpointing | Crash inside subgraph |
| Schema drift | Old thread cannot resume safely | Schema versioning and migration tests | Resume old fixture |

## Highest-risk finding

Checkpoint restoration is not a distributed transaction. It restores LangGraph state; it does not roll back MCP/A2A or database side effects. This is the central boundary condition for the design.

## Residual risks

- Remote systems may not support idempotency or compensation.
- Human reviewers may approve stale or maliciously altered content.
- Checkpoint retention can create cost and privacy exposure.
- LangGraph behavior can change across versions; pin and test the selected version.
- A 10-task simulation does not prove production behavior under arbitrary load.
