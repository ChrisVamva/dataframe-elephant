"""Unit and integration tests for post-TransitionStage2 follow-up research formulation."""

import pytest
from pathlib import Path

from src.followup_core import (
    ResearchGap,
    FormulatedQuestion,
    parse_markdown_table_rows,
    scan_stage2_entities,
    scan_stage2_extraction_log,
    scan_duckdb_intelligence,
    formulate_question_from_gap,
    build_research_agenda_markdown,
)
from scripts.formulate_research_questions import run_formulation


def test_research_gap_scoring():
    # P1 test: 5 * 4 / 1 = 20.0
    gap_p1 = ResearchGap(
        gap_id="G1",
        gap_code="GAP-BND",
        target_concept="DuckDB",
        category="Entity",
        description="Lacks boundary",
        source_reference="Entities.md E001",
        workflow_centrality=5,
        evidence_severity=4,
        verification_difficulty=1,
    )
    assert gap_p1.priority_score == 20.0
    assert gap_p1.priority_tier == "P1"

    # P2 test: 3 * 3 / 1 = 9.0
    gap_p2 = ResearchGap(
        gap_id="G2",
        gap_code="GAP-BND",
        target_concept="Metabase",
        category="Entity",
        description="Lacks boundary",
        source_reference="Entities.md E012",
        workflow_centrality=3,
        evidence_severity=3,
        verification_difficulty=1,
    )
    assert gap_p2.priority_score == 9.0
    assert gap_p2.priority_tier == "P2"

    # P3 test: 2 * 2 / 1 = 4.0
    gap_p3 = ResearchGap(
        gap_id="G3",
        gap_code="GAP-CND",
        target_concept="Minor Metric",
        category="Metric",
        description="Missing condition",
        source_reference="Metrics.md M001",
        workflow_centrality=2,
        evidence_severity=2,
        verification_difficulty=1,
    )
    assert gap_p3.priority_score == 4.0
    assert gap_p3.priority_tier == "P3"


def test_parse_markdown_table_rows():
    md = """
| Col A | Col B | Col C |
| --- | --- | --- |
| Val 1 | Val 2 | Val 3 |
| Val 4 | Val 5 | Val 6 |
"""
    rows = parse_markdown_table_rows(md)
    assert len(rows) == 2
    assert rows[0] == {"Col A": "Val 1", "Col B": "Val 2", "Col C": "Val 3"}
    assert rows[1] == {"Col A": "Val 4", "Col B": "Val 5", "Col C": "Val 6"}


def test_formulate_question_conformance():
    gap = ResearchGap(
        gap_id="GAP-BND-E001",
        gap_code="GAP-BND",
        target_concept="DuckDB",
        category="Entity Boundary",
        description="Lacks boundary",
        source_reference="Entities.md E001",
        workflow_centrality=5,
        evidence_severity=4,
        verification_difficulty=1,
    )
    q = formulate_question_from_gap(gap, 1)

    assert q.rq_id == "RQ-001"
    assert "DuckDB" in q.title
    assert len(q.core_question) > 20
    assert len(q.in_scope) > 10
    assert len(q.out_of_scope) > 10
    assert len(q.intended_use) > 10
    assert len(q.min_evidence_class) > 5
    assert len(q.falsifier) > 20


def test_build_research_agenda_markdown():
    gap = ResearchGap(
        gap_id="G1",
        gap_code="GAP-BND",
        target_concept="DuckDB",
        category="Entity",
        description="Lacks boundary",
        source_reference="Entities.md",
        workflow_centrality=5,
        evidence_severity=4,
        verification_difficulty=1,
    )
    q = formulate_question_from_gap(gap, 1)
    md = build_research_agenda_markdown([q])

    assert "# Follow-Up Research Agenda" in md
    assert "DuckDB" in md
    assert "Priority Ranking Table" in md
    assert "Falsification & Resolution Criteria" in md


def test_run_formulation_e2e(tmp_path):
    stage2_dir = tmp_path / "Stage 2"
    stage2_dir.mkdir()
    (stage2_dir / "Entities.md").write_text(
        """| Entity ID | Canonical name | Type | Boundary (what it is not) |
| --- | --- | --- | --- |
| E001 | DuckDB | Software | [boundary not stated in source] |
""",
        encoding="utf-8",
    )
    (stage2_dir / "ExtractionLog.md").write_text(
        """| Log ID | Step | Stage 1 source | Decision type | Description | Resolution |
| --- | --- | --- | --- | --- | --- |
| L001 | Step 2 | Doc.md | omission | Multiple URLs found: https://a.org · https://b.org | Kept primary |
""",
        encoding="utf-8",
    )

    out_dir = tmp_path / "FollowUps"
    db_path = tmp_path / "non_existent.duckdb"

    ret = run_formulation(stage2_dir, db_path, out_dir)
    assert ret == 0
    agenda = out_dir / "ResearchAgenda.md"
    assert agenda.is_file()
    content = agenda.read_text(encoding="utf-8")
    assert "DuckDB" in content
    assert "https://a.org" in content
