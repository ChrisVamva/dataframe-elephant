"""Tests for the Stage 2 -> DuckDB import (Protocols/FromStagetoDatabases.md)."""

import duckdb
import pytest

from src.stage2_import_core import (
    Stage2ImportError,
    build_stage2_database,
    frontmatter_gate_failures,
)

FRONTMATTER_OK = """---
stage: 2
created: 2026-09-27
extracted_from:
  - research/raw/Stage 1/C.md
extractor: test
gate_results:
  gate_1_source_coverage: pass
  gate_2_claim_traceability: pass
  gate_3_evidence_class_integrity: pass
  gate_4_metric_conditions: pass
  gate_5_entity_completeness: pass
  gate_6_extraction_log_completeness: pass
  gate_7_ingestibility: pass
---
"""

FILES = {
    "Entities.md": FRONTMATTER_OK + """
| Entity ID | Canonical name | Type | Boundary (what it is not) | Stage 1 source | Section | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| E001 | DuckDB | Software | [boundary not stated in source] | C.md | T | medium |
| E002 | Metabase | Software | A dashboard tool, not a database engine | C.md | T | high |
""",
    "Metrics.md": FRONTMATTER_OK + """
| Metric ID | Metric name | Value | Unit | Scope / conditions | Claim type | Confidence | Source ID | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
""",
    "Claims.md": FRONTMATTER_OK + """
| Claim ID | Claim text | Claim type | Confidence | Source IDs | Falsifier | Workflow stage | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C001 | DuckDB is fast | reported signal | low | S1 | [falsifier not stated] | execution | C.md | F |
""",
    "Sources.md": FRONTMATTER_OK + """
| ID | Source | URL | Publisher | Classification | Publication date |
| --- | --- | --- | --- | --- | --- |
| S1 | DuckDB docs | https://duckdb.org/docs/ | DuckDB | Primary |  |
""",
    "Predicates.md": FRONTMATTER_OK + """
| Predicate | Subject type | Object type | Direction | Example (from Stage 1) | Stage 1 source |
| --- | --- | --- | --- | --- | --- |
""",
    "WorkflowMap.md": FRONTMATTER_OK + """
| Stage ID | Stage name | Inputs | Activities | Outputs | Quality gates | Roles | Tools | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
""",
    "ExtractionLog.md": FRONTMATTER_OK + """
| Log ID | Step | Stage 1 source | Decision type | Description | Resolution |
| --- | --- | --- | --- | --- | --- |
| L001 | Step 5 | C.md | open_question | DuckDB vs MotherDuck trade-off | carry forward |
""",
}


def _write_stage2(tmp_path, overrides=None):
    d = tmp_path / "Stage 2"
    d.mkdir()
    for name, text in {**FILES, **(overrides or {})}.items():
        (d / name).write_text(text, encoding="utf-8")
    return d


def test_frontmatter_reject_on_fail(tmp_path):
    bad = FRONTMATTER_OK.replace("gate_1_source_coverage: pass", "gate_1_source_coverage: fail")
    assert frontmatter_gate_failures(bad) == ["gate_1_source_coverage: fail"]
    assert frontmatter_gate_failures("no frontmatter") == ["missing frontmatter block"]
    d = _write_stage2(tmp_path, {"Entities.md": bad + "\n| Entity ID | Canonical name | Type | Boundary (what it is not) |\n| --- | --- | --- | --- |\n"})
    with pytest.raises(Stage2ImportError, match="preflight failed"):
        build_stage2_database(d, tmp_path / "s.duckdb", tmp_path / "w.jsonl")


def test_import_markers_and_views(tmp_path):
    d = _write_stage2(tmp_path)
    from pathlib import Path as P
    schema = P("schemas/stage2.sql")
    res = build_stage2_database(d, tmp_path / "s.duckdb", tmp_path / "w.jsonl", schema)
    assert res["entities"] == 2 and res["claims"] == 1 and res["decisions"] == 1
    assert res["metrics"] == 0 and res["predicates"] == 0  # empty tables valid
    con = duckdb.connect(str(tmp_path / "s.duckdb"), read_only=True)
    try:
        assert con.execute("SELECT COUNT(*) FROM unstated_boundaries").fetchone()[0] == 1
        assert con.execute("SELECT COUNT(*) FROM missing_falsifiers").fetchone()[0] == 1
        assert con.execute("SELECT COUNT(*) FROM open_questions").fetchone()[0] == 1
        assert con.execute("SELECT COUNT(*) FROM unstated_conditions").fetchone()[0] == 0
        row = con.execute("SELECT boundary_stated FROM entity WHERE local_id='E002'").fetchone()
        assert row[0] in (True, 1)
    finally:
        con.close()


def test_deterministic_run_id(tmp_path):
    d = _write_stage2(tmp_path)
    from pathlib import Path as P
    schema = P("schemas/stage2.sql")
    r1 = build_stage2_database(d, tmp_path / "a.duckdb", tmp_path / "a.jsonl", schema)
    r2 = build_stage2_database(d, tmp_path / "b.duckdb", tmp_path / "b.jsonl", schema)
    assert r1["run_id"] == r2["run_id"]


def test_missing_file_rejected(tmp_path):
    d = _write_stage2(tmp_path)
    (d / "Metrics.md").unlink()
    with pytest.raises(Stage2ImportError, match="Missing required Stage 2 file"):
        build_stage2_database(d, tmp_path / "s.duckdb", tmp_path / "w.jsonl")


def test_unresolved_source_ref_warns(tmp_path):
    files = dict(FILES)
    files["Claims.md"] = FRONTMATTER_OK + """
| Claim ID | Claim text | Claim type | Confidence | Source IDs | Falsifier | Workflow stage | Stage 1 source | Section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C009 | Mystery claim | reported signal | low | S99 | A falsifier | execution | C.md | F |
"""
    d = _write_stage2(tmp_path, files)
    from pathlib import Path as P
    res = build_stage2_database(d, tmp_path / "s.duckdb", tmp_path / "w.jsonl", P("schemas/stage2.sql"))
    assert res["warnings"] >= 1
    text = (tmp_path / "w.jsonl").read_text(encoding="utf-8")
    assert "source_ref_unresolved" in text
