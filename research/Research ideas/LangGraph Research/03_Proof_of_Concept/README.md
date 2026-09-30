# Proof of concept

This prototype models the researched contract without requiring LangGraph or external packages. It is deliberately small and deterministic:

1. Fan out 10 independent worker tasks.
2. Persist a checkpoint after every worker completion.
3. Pause at an approval gate.
4. Resume with an approval decision.
5. Commit each approved operation using an idempotency key.
6. Demonstrate replay safety by committing the same operation twice.

Run from this folder with:

```powershell
python langgraph_boundary_poc.py
```

Expected assertions:

- 10/10 tasks complete.
- A checkpoint exists before approval.
- The first resume is paused until approval.
- Approval permits commit.
- Replaying commit does not duplicate the operation.
- A rejected approval cannot commit.

The code is a behavioral simulation, not a replacement for integration tests against the selected LangGraph version and production checkpointer.
