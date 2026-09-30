"""Dependency-free simulation of the LangGraph orchestration boundary."""
from __future__ import annotations

import concurrent.futures
import json
import tempfile
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class WorkflowState:
    thread_id: str
    tasks: dict[str, str] = field(default_factory=dict)
    results: dict[str, str] = field(default_factory=dict)
    approval: str | None = None
    committed: set[str] = field(default_factory=set)
    audit: list[str] = field(default_factory=list)


class CheckpointStore:
    def __init__(self, path: Path):
        self.path = path

    def save(self, state: WorkflowState) -> None:
        payload = {
            "thread_id": state.thread_id,
            "tasks": state.tasks,
            "results": state.results,
            "approval": state.approval,
            "committed": sorted(state.committed),
            "audit": state.audit,
        }
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load(self) -> WorkflowState:
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        return WorkflowState(
            thread_id=payload["thread_id"],
            tasks=payload["tasks"],
            results=payload["results"],
            approval=payload["approval"],
            committed=set(payload["committed"]),
            audit=payload["audit"],
        )


def worker(task_id: str) -> tuple[str, str]:
    # A real node would call an MCP/A2A adapter here.
    return task_id, f"evidence-result:{task_id}"


def fan_out(state: WorkflowState, store: CheckpointStore) -> None:
    task_ids = [f"task-{index:02d}" for index in range(1, 11)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        futures = [pool.submit(worker, task_id) for task_id in task_ids]
        for future in concurrent.futures.as_completed(futures):
            task_id, result = future.result()
            state.tasks[task_id] = "completed"
            state.results[task_id] = result
            state.audit.append(f"worker_completed:{task_id}")
            # Equivalent policy: persist after each worker super-step.
            store.save(state)


def approval_gate(state: WorkflowState, store: CheckpointStore) -> dict:
    payload = {
        "kind": "approval_request",
        "operation_id": "op-publish-rq-agt-03",
        "required_role": "research-maintainer",
        "result_count": len(state.results),
        "state_checkpoint": str(store.path),
    }
    state.audit.append("approval_requested")
    store.save(state)
    return payload


def resume(state: WorkflowState, store: CheckpointStore, decision: str) -> None:
    if decision not in {"approve", "reject"}:
        raise ValueError("decision must be approve or reject")
    state.approval = decision
    state.audit.append(f"approval:{decision}")
    store.save(state)


def commit(state: WorkflowState, store: CheckpointStore) -> None:
    if state.approval != "approve":
        raise PermissionError("commit requires an explicit approval")
    operation_id = "op-publish-rq-agt-03"
    # Idempotency: replaying the same operation is a no-op.
    if operation_id not in state.committed:
        state.committed.add(operation_id)
        state.audit.append(f"committed:{operation_id}")
    else:
        state.audit.append(f"commit_replay_ignored:{operation_id}")
    store.save(state)


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        store = CheckpointStore(Path(directory) / "checkpoint.json")
        state = WorkflowState(thread_id="rq-agt-03-demo")
        fan_out(state, store)
        assert len(state.results) == 10
        payload = approval_gate(state, store)
        assert payload["kind"] == "approval_request"

        # Simulate a process restart: recover by thread/checkpoint, not memory.
        recovered = store.load()
        assert recovered.thread_id == state.thread_id
        assert len(recovered.results) == 10
        resume(recovered, store, "approve")
        commit(recovered, store)
        commit(recovered, store)  # Safe replay.
        assert len(recovered.committed) == 1

        rejected = WorkflowState(thread_id="rejected-demo")
        rejected_store = CheckpointStore(Path(directory) / "rejected.json")
        fan_out(rejected, rejected_store)
        approval_gate(rejected, rejected_store)
        resume(rejected, rejected_store, "reject")
        try:
            commit(rejected, rejected_store)
        except PermissionError:
            pass
        else:
            raise AssertionError("rejected workflow reached commit")

        print("PASS: 10 concurrent tasks, durable checkpoint, HITL gate, idempotent commit")
        print("Audit events:", len(recovered.audit))


if __name__ == "__main__":
    main()
