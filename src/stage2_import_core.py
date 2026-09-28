"""Build the typed Stage 2 DuckDB database from research/raw/Stage 2/.

Implements Protocols/FromStagetoDatabases.md: strict frontmatter preflight
(reject on any non-pass gate), deterministic IDs, temp-file + atomic replace,
SHA-256 incremental cache, and a warnings JSONL artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import duckdb

PARSER_VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parents[1]

STAGE2_FILES = (
    "Entities.md",
    "Metrics.md",
    "Claims.md",
    "Sources.md",
    "Predicates.md",
    "WorkflowMap.md",
    "ExtractionLog.md",
)

DECISION_TYPES = frozenset({
    "scope_boundary", "entity_merge", "entity_split",
    "label_resolution", "classification_conflict",
    "evidence_downgrade", "falsifier_absent",
    "boundary_absent", "condition_absent",
    "open_question", "omission",
})

BOUNDARY_MARKER = "[boundary not stated in source]"
CONDITIONS_MARKER = "[conditions not stated in source]"
FALSIFIER_MARKER = "[falsifier not stated]"


class Stage2ImportError(RuntimeError):
    """Raised when preflight gates fail or inputs are missing."""


def stable_id(kind: str, value: str) -> str:
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return f"{kind}_{digest[:24]}"


def _split_markdown_row(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    cells: list[str] = []
    cell: list[str] = []
    escaped = False
    for character in value:
        if character == "|" and not escaped:
            cells.append("".join(cell).strip().replace("\\|", "|"))
            cell = []
        else:
            cell.append(character)
        escaped = character == "\\" and not escaped
        if character != "\\":
            escaped = False
    cells.append("".join(cell).strip().replace("\\|", "|"))
    return cells


def _is_separator(line: str) -> bool:
    cells = _split_markdown_row(line)
    return bool(cells) and all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells
    )


def parse_markdown_table(headers_line: str, rows: list[str]) -> tuple[list[str], list[list[str]]]:
    headers = _split_markdown_row(headers_line)
    return headers, [_split_markdown_row(r) for r in rows if len(_split_markdown_row(r)) == len(headers)]


def extract_tables(markdown: str) -> list[tuple[list[str], list[list[str]]]]:
    lines = markdown.splitlines()
    tables: list[tuple[list[str], list[list[str]]]] = []
    i = 0
    while i + 1 < len(lines):
        if "|" not in lines[i] or not _is_separator(lines[i + 1]):
            i += 1
            continue
        headers = _split_markdown_row(lines[i])
        rows: list[str] = []
        j = i + 2
        while j < len(lines) and "|" in lines[j] and lines[j].strip():
            if len(_split_markdown_row(lines[j])) == len(headers):
                rows.append(lines[j])
            j += 1
        tables.append(parse_markdown_table(lines[i], rows))
        i = j
    return tables


def _header_name(value: str) -> str:
    return re.sub(r"[`*_]", "", value).strip().casefold()


def frontmatter_gate_failures(markdown: str) -> list[str]:
    """Return failure reasons; empty means preflight passes."""
    failures: list[str] = []
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", markdown, re.DOTALL)
    if not match:
        return ["missing frontmatter block"]
    front = match.group(1)
    if re.search(r"(?im)^\s*status\s*:\s*draft\s*$", front):
        failures.append("status: draft")
    gates = re.findall(r"(?im)^\s*(gate_\w+)\s*:\s*(\w+)\s*$", front)
    if not gates:
        failures.append("no gate_results in frontmatter")
    for name, result in gates:
        if result.strip().casefold() != "pass":
            failures.append(f"{name}: {result}")
    return failures


def _find_table(
    tables: list[tuple[list[str], list[list[str]]]], required: tuple[str, ...]
) -> tuple[list[str], list[list[str]]] | None:
    want = {_header_name(c) for c in required}
    for headers, rows in tables:
        have = {_header_name(h) for h in headers}
        if want.issubset(have):
            return headers, rows
    return None


def _col(headers: list[str], row: list[str], name: str) -> str:
    idx = next((i for i, h in enumerate(headers) if _header_name(h) == _header_name(name)), None)
    return row[idx].strip() if idx is not None and idx < len(row) else ""


def _warn(run_id: str, path: str, wtype: str, msg: str, raw: str = "") -> dict[str, str]:
    wid = stable_id("swarn", "\0".join((run_id, path, wtype, msg, raw)))
    return {"warning_id": wid, "run_id": run_id, "input_path": path,
            "warning_type": wtype, "message": msg, "raw_value": raw}


def parse_stage2_file(name: str, markdown: str) -> tuple[list[str], list[list[str]]]:
    """Return (headers, rows) for the contract table in a Stage 2 file.

    Raises Stage2ImportError when no contract table is found.
    """
    required: dict[str, tuple[str, ...]] = {
        "Entities.md": ("Entity ID", "Canonical name", "Type", "Boundary (what it is not)"),
        "Metrics.md": ("Metric ID", "Metric name", "Scope / conditions"),
        "Claims.md": ("Claim ID", "Claim text", "Claim type", "Confidence"),
        "Sources.md": ("ID", "Source", "URL"),
        "Predicates.md": ("Predicate", "Subject type", "Object type"),
        "WorkflowMap.md": ("Stage ID", "Stage name"),
        "ExtractionLog.md": ("Log ID", "Decision type", "Description"),
    }
    tables = extract_tables(markdown)
    found = _find_table(tables, required[name])
    if found is None:
        raise Stage2ImportError(f"{name}: contract table not found (unsupported_table_shape)")
    return found


def build_stage2_database(
    stage2_dir: Path,
    database_path: Path,
    warnings_path: Path,
    schema_path: Path | None = None,
) -> dict[str, Any]:
    stage2_dir = stage2_dir.resolve()
    database_path = database_path.resolve()
    warnings_path = warnings_path.resolve()
    schema_path = (schema_path or ROOT / "schemas" / "stage2.sql").resolve()
    if not stage2_dir.is_dir():
        raise Stage2ImportError(f"Stage 2 directory not found: {stage2_dir}")
    database_path.parent.mkdir(parents=True, exist_ok=True)
    warnings_path.parent.mkdir(parents=True, exist_ok=True)

    # --- Preflight: all files present, all gates pass ---
    snapshots: list[dict[str, Any]] = []
    contents: dict[str, str] = {}
    for name in STAGE2_FILES:
        path = stage2_dir / name
        if not path.is_file():
            raise Stage2ImportError(f"Missing required Stage 2 file: {path}")
        data = path.read_bytes()
        markdown = data.decode("utf-8", errors="replace")
        failures = frontmatter_gate_failures(markdown)
        if failures:
            raise Stage2ImportError(f"{name}: gate preflight failed: {'; '.join(failures)}")
        rel = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.name
        snapshots.append({
            "name": name, "path": rel,
            "sha256": hashlib.sha256(data).hexdigest(),
            "modified_at": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).replace(tzinfo=None),
        })
        contents[name] = markdown

    run_id = stable_id("run", "\n".join(f"{s['path']}\0{s['sha256']}" for s in snapshots) + f"\n{PARSER_VERSION}")
    input_root = stage2_dir.relative_to(ROOT).as_posix() if stage2_dir.is_relative_to(ROOT) else stage2_dir.as_posix()
    built_at = datetime.now(timezone.utc).replace(tzinfo=None)

    tmp_path = database_path.with_name(
        f"{database_path.stem}_tmp{hashlib.sha256(str(database_path).encode()).hexdigest()[:12]}{database_path.suffix}")
    con = duckdb.connect(str(tmp_path))
    con.execute(schema_path.read_text(encoding="utf-8"))

    warnings: list[dict[str, str]] = []
    documents: list[dict[str, Any]] = []
    entities: list[dict[str, Any]] = []
    metrics: list[dict[str, Any]] = []
    claims: list[dict[str, Any]] = []
    mirrors: list[dict[str, Any]] = []
    predicates: list[dict[str, Any]] = []
    stages: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []

    file_cache = _load_file_cache(database_path)
    unchanged = {s["path"] for s in snapshots if file_cache.get(s["path"]) == s["sha256"]}
    cached = _copy_unchanged_rows(database_path, unchanged, run_id, warnings)
    for doc in cached["documents"]:
        documents.append(doc)
    entities.extend(cached["entities"])
    metrics.extend(cached["metrics"])
    claims.extend(cached["claims"])
    mirrors.extend(cached["mirrors"])
    predicates.extend(cached["predicates"])
    stages.extend(cached["stages"])
    decisions.extend(cached["decisions"])
    cached_doc_ids = {d["document_id"] for d in cached["documents"]}

    source_local_ids: set[str] = {m["local_id"].casefold() for m in mirrors}
    pending_coverage: list[tuple[str, str, str]] = []  # (input_path, ref, context)

    for snap in snapshots:
        rel, name, markdown = snap["path"], snap["name"], contents[snap["name"]]
        if rel in unchanged and any(d["path"] == rel for d in documents):
            continue
        # Drop stale carried-forward rows for changed files (full re-parse below).
        documents = [d for d in documents if d["path"] != rel]
        doc_id = stable_id("doc", rel.casefold())
        if doc_id in cached_doc_ids:
            for bucket in (entities, metrics, claims, mirrors, predicates, stages, decisions):
                bucket[:] = [r for r in bucket if r["document_id"] != doc_id]
        documents.append({"document_id": doc_id, "path": rel,
                          "content_sha256": snap["sha256"], "modified_at": snap["modified_at"]})
        try:
            headers, rows = parse_stage2_file(name, markdown)
        except Stage2ImportError as exc:
            warnings.append(_warn(run_id, rel, "unsupported_table_shape", str(exc)))
            continue
        for row in rows:
            if name == "Entities.md":
                lid = _col(headers, row, "Entity ID")
                boundary = _col(headers, row, "Boundary (what it is not)")
                entities.append({
                    "entity_id": stable_id("entity", f"{doc_id}\0{lid}"),
                    "local_id": lid, "canonical_name": _col(headers, row, "Canonical name"),
                    "type": _col(headers, row, "Type"), "boundary": boundary,
                    "boundary_stated": BOUNDARY_MARKER not in boundary,
                    "stage1_source": _col(headers, row, "Stage 1 source"),
                    "section": _col(headers, row, "Section"),
                    "confidence": _col(headers, row, "Confidence"), "document_id": doc_id})
            elif name == "Metrics.md":
                lid = _col(headers, row, "Metric ID")
                scope = _col(headers, row, "Scope / conditions")
                sref = _col(headers, row, "Source ID")
                metrics.append({
                    "metric_id": stable_id("metric", f"{doc_id}\0{lid}"),
                    "local_id": lid, "metric_name": _col(headers, row, "Metric name"),
                    "value": _col(headers, row, "Value"), "unit": _col(headers, row, "Unit"),
                    "scope_conditions": scope, "conditions_stated": CONDITIONS_MARKER not in scope,
                    "claim_type": _col(headers, row, "Claim type"),
                    "confidence": _col(headers, row, "Confidence"),
                    "source_ref": sref, "stage1_source": _col(headers, row, "Stage 1 source"),
                    "section": _col(headers, row, "Section"), "document_id": doc_id})
                if sref:
                    pending_coverage.append((rel, sref, f"Metrics.md {lid}"))
            elif name == "Claims.md":
                lid = _col(headers, row, "Claim ID")
                falsifier = _col(headers, row, "Falsifier")
                srefs = _col(headers, row, "Source IDs")
                claims.append({
                    "claim_id": stable_id("s2clm", f"{doc_id}\0{lid}"),
                    "local_id": lid, "claim_text": _col(headers, row, "Claim text"),
                    "claim_type": _col(headers, row, "Claim type"),
                    "confidence": _col(headers, row, "Confidence"),
                    "falsifier": falsifier, "falsifier_stated": FALSIFIER_MARKER not in falsifier,
                    "workflow_stage": _col(headers, row, "Workflow stage"),
                    "source_refs": srefs, "stage1_source": _col(headers, row, "Stage 1 source"),
                    "section": _col(headers, row, "Section"), "document_id": doc_id})
                for label in re.findall(r"\bS\d+[A-Za-z]?\b", srefs, re.IGNORECASE):
                    pending_coverage.append((rel, label, f"Claims.md {lid}"))
            elif name == "Sources.md":
                lid = _col(headers, row, "ID")
                mirrors.append({
                    "source_id": stable_id("s2src", f"{doc_id}\0{lid}"),
                    "local_id": lid, "title": _col(headers, row, "Source"),
                    "url": _col(headers, row, "URL"),
                    "publisher": _col(headers, row, "Publisher"),
                    "classification": _col(headers, row, "Classification"),
                    "publication_date": _col(headers, row, "Publication date"),
                    "document_id": doc_id})
                source_local_ids.add(lid.casefold())
            elif name == "Predicates.md":
                pred = _col(headers, row, "Predicate")
                predicates.append({
                    "predicate_id": stable_id("pred", f"{doc_id}\0{pred}\0{len(predicates)}"),
                    "predicate": pred, "subject_type": _col(headers, row, "Subject type"),
                    "object_type": _col(headers, row, "Object type"),
                    "direction": _col(headers, row, "Direction"),
                    "example": _col(headers, row, "Example (from Stage 1)"),
                    "stage1_source": _col(headers, row, "Stage 1 source"),
                    "document_id": doc_id})
            elif name == "WorkflowMap.md":
                lid = _col(headers, row, "Stage ID")
                stages.append({
                    "stage_id": stable_id("wstage", f"{doc_id}\0{lid}"),
                    "local_id": lid, "stage_name": _col(headers, row, "Stage name"),
                    "inputs": _col(headers, row, "Inputs"),
                    "activities": _col(headers, row, "Activities"),
                    "outputs": _col(headers, row, "Outputs"),
                    "quality_gates": _col(headers, row, "Quality gates"),
                    "roles": _col(headers, row, "Roles"), "tools": _col(headers, row, "Tools"),
                    "evidence": _col(headers, row, "Evidence"),
                    "confidence": _col(headers, row, "Confidence"), "document_id": doc_id})
            elif name == "ExtractionLog.md":
                lid = _col(headers, row, "Log ID")
                dtype = _col(headers, row, "Decision type")
                if dtype not in DECISION_TYPES:
                    warnings.append(_warn(run_id, rel, "unknown_decision_type",
                                          f"Log {lid} has unknown decision type {dtype!r}.", dtype))
                    continue
                decisions.append({
                    "decision_id": stable_id("dec", f"{doc_id}\0{lid}"),
                    "local_id": lid, "step": _col(headers, row, "Step"),
                    "stage1_source": _col(headers, row, "Stage 1 source"),
                    "decision_type": dtype, "description": _col(headers, row, "Description"),
                    "resolution": _col(headers, row, "Resolution"), "document_id": doc_id})

    # G1 source coverage (after all files parsed so order is irrelevant).
    for rel, ref, ctx in pending_coverage:
        for label in re.findall(r"\bS\d+[A-Za-z]?\b", ref, re.IGNORECASE):
            if label.casefold() not in source_local_ids:
                warnings.append(_warn(run_id, rel, "source_ref_unresolved",
                                      f"{ctx} references {label!r} with no Sources.md row.", label))

    try:
        con.execute("BEGIN TRANSACTION")
        _insert(con, "stage2_run", [{"run_id": run_id, "built_at": built_at,
                                     "parser_version": PARSER_VERSION, "input_root": input_root}])
        _insert(con, "stage2_input", [
            {"run_id": run_id, "path": s["path"], "sha256": s["sha256"], "modified_at": s["modified_at"]}
            for s in snapshots])
        _insert(con, "stage2_document", documents)
        _insert(con, "entity", entities)
        _insert(con, "metric", metrics)
        _insert(con, "stage2_claim", claims)
        _insert(con, "source_mirror", mirrors)
        _insert(con, "predicate", predicates)
        _insert(con, "workflow_stage", stages)
        _insert(con, "extraction_decision", decisions)
        dedup = list({w["warning_id"]: w for w in warnings}.values())
        _insert(con, "stage2_warning", dedup)
        warnings = dedup
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise
    finally:
        con.close()

    tmp_path.replace(database_path)
    with warnings_path.open("w", encoding="utf-8", newline="\n") as fh:
        for w in sorted(warnings, key=lambda x: (x["input_path"], x["warning_id"])):
            fh.write(json.dumps(w, ensure_ascii=True, sort_keys=True) + "\n")

    return {"run_id": run_id, "database_path": str(database_path),
            "documents": len(documents), "entities": len(entities),
            "metrics": len(metrics), "claims": len(claims),
            "sources": len(mirrors), "predicates": len(predicates),
            "workflow_stages": len(stages), "decisions": len(decisions),
            "warnings": len(warnings)}


def _insert(con: duckdb.DuckDBPyConnection, table: str, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    cols = tuple(rows[0])
    con.executemany(f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({', '.join('?' for _ in cols)})",
                    [tuple(r[c] for c in cols) for r in rows])


def _load_file_cache(database_path: Path) -> dict[str, str]:
    if not database_path.exists():
        return {}
    con: duckdb.DuckDBPyConnection | None = None
    try:
        con = duckdb.connect(str(database_path), read_only=True)
        return {r[0]: r[1] for r in con.execute(
            "SELECT ii.path, ii.sha256 FROM stage2_input ii "
            "JOIN stage2_run ir ON ir.run_id = ii.run_id "
            "WHERE ir.built_at = (SELECT MAX(built_at) FROM stage2_run)").fetchall()}
    except Exception:
        return {}
    finally:
        if con is not None:
            con.close()


def _copy_unchanged_rows(
    old_db: Path, unchanged: set[str], run_id: str, warnings: list[dict[str, str]]
) -> dict[str, list[dict[str, Any]]]:
    out = {"documents": [], "entities": [], "metrics": [], "claims": [],
           "mirrors": [], "predicates": [], "stages": [], "decisions": []}
    if not unchanged or not old_db.exists():
        return out
    con: duckdb.DuckDBPyConnection | None = None
    try:
        con = duckdb.connect(str(old_db), read_only=True)
        paths = list(unchanged)
        ph = ", ".join("?" for _ in paths)

        def fetch(sql: str) -> list[dict[str, Any]]:
            cur = con.execute(sql, paths)
            cols = [d[0] for d in cur.description]
            return [dict(zip(cols, r)) for r in cur.fetchall()]

        out["documents"] = fetch(f"SELECT * FROM stage2_document WHERE path IN ({ph})")
        doc_ids = [d["document_id"] for d in out["documents"]]
        if not doc_ids:
            return out
        dph = ", ".join("?" for _ in doc_ids)

        def fetch_doc(table: str) -> list[dict[str, Any]]:
            cur = con.execute(f"SELECT * FROM {table} WHERE document_id IN ({dph})", doc_ids)
            cols = [d[0] for d in cur.description]
            return [dict(zip(cols, r)) for r in cur.fetchall()]

        out["entities"] = fetch_doc("entity")
        out["metrics"] = fetch_doc("metric")
        out["claims"] = fetch_doc("stage2_claim")
        out["mirrors"] = fetch_doc("source_mirror")
        out["predicates"] = fetch_doc("predicate")
        out["stages"] = fetch_doc("workflow_stage")
        out["decisions"] = fetch_doc("extraction_decision")
        cur = con.execute(f"SELECT * FROM stage2_warning WHERE input_path IN ({ph})", paths)
        cols = [d[0] for d in cur.description]
        for row in cur.fetchall():
            carried = dict(zip(cols, row))
            warnings.append(_warn(run_id, carried["input_path"], carried["warning_type"],
                                 carried["message"], carried.get("raw_value", "") or ""))
        return out
    except Exception:
        return {"documents": [], "entities": [], "metrics": [], "claims": [],
                "mirrors": [], "predicates": [], "stages": [], "decisions": []}
    finally:
        if con is not None:
            con.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage2-dir", type=Path, default=ROOT / "research" / "raw" / "Stage 2")
    parser.add_argument("--database", type=Path, default=ROOT / "data" / "stage2.duckdb")
    parser.add_argument("--warnings", type=Path, default=ROOT / "data" / "stage2_ingestion_warnings.jsonl")
    parser.add_argument("--schema", type=Path, default=ROOT / "schemas" / "stage2.sql")
    args = parser.parse_args()
    try:
        print(json.dumps(build_stage2_database(args.stage2_dir, args.database, args.warnings, args.schema), indent=2))
    except Stage2ImportError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
