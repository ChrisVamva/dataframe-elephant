from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import duckdb
import pytest

import src.ingest_citations as ingest_citations
from src.ingest_citations import _document_metadata, build_database, normalize_url, parse_markdown_tables, stable_id


SCHEMA_PATH = Path(__file__).resolve().parents[2] / "schemas" / "citations.sql"


def test_normalize_url_removes_tracking_and_preserves_path() -> None:
    assert (
        normalize_url("HTTP://WWW.Example.com/download?utm_source=mail&b=2#section").rstrip("/")
        == "https://example.com/download?b=2"
    )
    assert normalize_url("docs.example.com") == "https://docs.example.com/"
    assert normalize_url("not a url") is None


def test_normalize_url_keeps_trailing_path_characters_and_strips_brackets() -> None:
    assert normalize_url("https://example.org/docs/download") == "https://example.org/docs/download"
    assert normalize_url("https://example.org/docs/x}") == "https://example.org/docs/x"
    assert normalize_url("https://example.org/docs/x]") == "https://example.org/docs/x"


def test_stable_ids_are_repeatable_and_kind_scoped() -> None:
    assert stable_id("src", "https://example.com/a") == stable_id("src", "https://example.com/a")
    assert stable_id("src", "https://example.com/a") != stable_id("doc", "https://example.com/a")


def test_markdown_table_parser_retains_escaped_pipes() -> None:
    tables = parse_markdown_tables(
        "## Sources\n\n| ID | Citation | Classification |\n|---|---|---|\n| S1 | A \\| B | Primary |\n"
    )
    assert len(tables) == 1
    assert tables[0].heading == "Sources"
    assert tables[0].rows[0] == ("S1", "A | B", "Primary")


def test_markdown_source_link_is_used_when_url_has_its_own_cell(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "linked-source.md").write_text(
        "# Linked source\n\n"
        "| ID | Source | Publisher / date | Claims supported |\n"
        "|---|---|---|---|\n"
        "| S1 | [Example documentation](https://example.org/docs/reference) | Example publisher | A fact. |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "linked.duckdb"

    result = build_database(raw_dir, database_path, tmp_path / "linked-warnings.jsonl", SCHEMA_PATH)

    assert result["sources"] == 1
    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        assert connection.execute("SELECT title, canonical_url FROM source").fetchone() == (
            "Example documentation",
            "https://example.org/docs/reference",
        )
        assert connection.execute(
            "SELECT resolution_status FROM citation_occurrence"
        ).fetchone()[0] == "resolved"
    finally:
        connection.close()


def test_structured_source_register_header_is_parsed(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "register.md").write_text(
        "# Register\n\n"
        "| ID | Source (title, publisher/author, date) | URL | Supports |\n"
        "|---|---|---|---|\n"
        '| S1 | "Example specification", Example Foundation, 2025-01-02 | https://example.org/spec/v1 | A documented fact. |\n',
        encoding="utf-8",
    )
    database_path = tmp_path / "register.duckdb"

    result = build_database(raw_dir, database_path, tmp_path / "register-warnings.jsonl", SCHEMA_PATH)

    assert result["sources"] == 1
    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        assert connection.execute(
            "SELECT title, publisher, publication_date FROM source"
        ).fetchone() == ("Example specification", "Example Foundation, 2025-01-02", date(2025, 1, 2))
        assert connection.execute(
            "SELECT resolution_status FROM citation_occurrence"
        ).fetchone()[0] == "resolved"
    finally:
        connection.close()


def test_ingestion_preserves_ambiguous_aliases_and_explicit_claim_links(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    document = raw_dir / "sample.md"
    document.write_text(
        "# Sample research\n\n"
        "**Accessed:** 2026-09-27\n\n"
        "## Sources\n\n"
        "| ID | Source | URL | Classification | Publication date |\n"
        "|---|---|---|---|---|\n"
        "| S1 | Example documentation | https://www.example.com/docs/reference?utm_source=x#top | Primary | 2025-01-02 |\n"
        "| S2 | Grouped references | alpha.example.com; beta.example.org | Mixed | |\n"
        "| S3 | Example homepage | https://example.com/ | Secondary | |\n\n"
        "## Claims\n\n"
        "| Claim | Claim type | Confidence | Sources | Relationship | Locator | Quote | Workflow stage | Falsifier |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
        "| Testable assertion | documented fact | low | S1 | supports | section 4 | Exact source span | Research | Contrary primary record |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "citations.duckdb"
    warnings_path = tmp_path / "warnings.jsonl"

    first = build_database(raw_dir, database_path, warnings_path, SCHEMA_PATH)
    second = build_database(raw_dir, database_path, warnings_path, SCHEMA_PATH)

    assert first == second
    assert first["documents"] == 1
    assert first["sources"] == 2
    assert first["occurrences"] == 3
    assert first["claims"] == 1
    assert first["claim_source_mappings"] == 1

    connection = duckdb.connect(str(database_path))
    try:
        assert connection.execute(
            "SELECT COUNT(*) FROM source WHERE canonical_url = 'https://example.com/'"
        ).fetchone()[0] == 1
        occurrence_rows = connection.execute(
            "SELECT local_label, resolution_status, source_id FROM citation_occurrence ORDER BY local_label"
        ).fetchall()
        assert occurrence_rows[0][1] == "resolved"
        assert occurrence_rows[1][1] == "ambiguous"
        assert occurrence_rows[1][2] is None
        assert connection.execute(
            "SELECT evidence_quote, evidence_locator FROM claim_source"
        ).fetchone() == ("Exact source span", "section 4")
        assert connection.execute(
            "SELECT research_reason FROM next_research_candidates"
        ).fetchone()[0] == "low confidence"
        with pytest.raises(duckdb.ConstraintException):
            connection.execute(
                "INSERT INTO source (source_id, title, evidence_class) VALUES ('invalid', 'Invalid', 'mixed')"
            )
    finally:
        connection.close()

    warning_rows = [json.loads(line) for line in warnings_path.read_text(encoding="utf-8").splitlines()]
    assert any(row["warning_type"] == "duplicate_candidate" for row in warning_rows)


def test_internal_ratings_do_not_inflate_external_recurrence_or_claims(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    source_table = (
        "| ID | Source | URL | Classification |\n"
        "|---|---|---|---|\n"
        "| S1 | Example specification | https://example.org/spec/v1 | Primary |\n"
    )
    (raw_dir / "brief.md").write_text("# Research brief\n\n" + source_table, encoding="utf-8")
    (raw_dir / "First-Ratings.md").write_text(
        "# First ratings\n\n"
        + source_table
        + "\n| Claim | Claim type | Confidence | Sources |\n"
        + "|---|---|---|---|\n"
        + "| Evaluation-only assertion | inference | low | S1 |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "ratings.duckdb"

    result = build_database(raw_dir, database_path, tmp_path / "ratings-warnings.jsonl", SCHEMA_PATH)

    assert result["documents"] == 2
    assert result["occurrences"] == 2
    assert result["claims"] == 0
    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        assert connection.execute(
            "SELECT distinct_documents, total_occurrences FROM source_recurrence"
        ).fetchone() == (1, 1)
        assert connection.execute(
            "SELECT is_internal FROM research_document WHERE path LIKE '%First-Ratings.md'"
        ).fetchone()[0] is True
    finally:
        connection.close()


def test_document_metadata_parses_bold_evaluation_fields(tmp_path: Path) -> None:
    markdown_path = tmp_path / "brief.md"
    markdown = (
        "# Brief\n\n"
        "**Decision:** **Revise.**\n"
        "**Evaluation date:** 2026-09-27\n"
        "**Quality rating:** **Moderate**\n"
    )
    markdown_path.write_text(markdown, encoding="utf-8")

    metadata = _document_metadata(markdown_path, "brief.md", markdown)

    assert metadata["evaluation_date"] == date(2026, 9, 27)
    assert metadata["evaluation_decision"] == "revise"
    assert metadata["quality_rating"] == "Moderate"


def test_source_status_and_directness_stay_unset_when_not_recorded(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "statusless.md").write_text(
        "# Statusless\n\n"
        "| ID | Source | URL | Classification |\n"
        "|---|---|---|---|\n"
        "| S1 | Example docs | https://example.org/docs/x | Primary |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "statusless.duckdb"

    build_database(raw_dir, database_path, tmp_path / "statusless-warnings.jsonl", SCHEMA_PATH)

    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        assert connection.execute("SELECT directness, status FROM source").fetchone() == (None, None)
    finally:
        connection.close()


def test_first_ratings_file_is_ingested_as_internal_evaluation(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "brief.md").write_text("# Brief\n\n| ID | Source | URL | Classification |\n|---|---|---|---|\n| S1 | Example docs | https://example.org/docs/x | Primary |\n", encoding="utf-8")
    analysis_dir = tmp_path / "analysis" / "On Research"
    analysis_dir.mkdir(parents=True)
    (analysis_dir / "First-Ratings.md").write_text(
        "# First Ratings\n\n**Decision:** **Revise.**\n**Evaluation date:** 2026-09-27\n**Quality rating:** **Moderate**\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(ingest_citations, "ROOT", tmp_path)

    database_path = tmp_path / "ratings.duckdb"
    build_database(raw_dir, database_path, tmp_path / "ratings-warnings.jsonl", SCHEMA_PATH)

    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        row = connection.execute(
            "SELECT path, is_internal, evaluation_decision, quality_rating FROM research_document WHERE path LIKE '%First-Ratings.md'"
        ).fetchone()
        assert row == ("analysis/On Research/First-Ratings.md", True, "revise", "Moderate")
    finally:
        connection.close()


def test_unmapped_classification_warns_even_when_url_resolves(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "mixed.md").write_text(
        "# Mixed classification\n\n"
        "| ID | Source | URL | Classification |\n"
        "|---|---|---|---|\n"
        "| S1 | Example docs | https://example.org/docs/x | Mixed |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "mixed.duckdb"
    warnings_path = tmp_path / "mixed-warnings.jsonl"

    build_database(raw_dir, database_path, warnings_path, SCHEMA_PATH)

    warning_rows = [json.loads(line) for line in warnings_path.read_text(encoding="utf-8").splitlines()]
    assert any(row["warning_type"] == "weak_source_classification" for row in warning_rows)
    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        assert connection.execute("SELECT evidence_class FROM source").fetchone()[0] is None
    finally:
        connection.close()


def test_duplicate_claim_rows_merge_when_text_type_and_confidence_match(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "claims.md").write_text(
        "# Claims\n\n"
        "| ID | Source | URL | Classification |\n"
        "|---|---|---|---|\n"
        "| S1 | Example source | https://example.org/source | Primary |\n"
        "| S2 | Example source two | https://example.org/source-two | Secondary |\n"
        "\n"
        "| Claim | Claim type | Confidence | Sources | Relationship |\n"
        "|---|---|---|---|---|\n"
        "| The tool is fast | documented fact | high | S1 | supports |\n"
        "| the tool is FAST | documented fact | high | S2 | supports |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "duplicate_claims.duckdb"

    result = build_database(raw_dir, database_path, tmp_path / "duplicate_claims_warnings.jsonl", SCHEMA_PATH)

    assert result["claims"] == 1
    assert result["claim_source_mappings"] == 2
    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        assert connection.execute("SELECT COUNT(*) FROM claim").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM claim_source").fetchone()[0] == 2
        assert connection.execute(
            "SELECT warning_type FROM ingestion_warning WHERE warning_type = 'duplicate_claim'"
        ).fetchone()[0] == "duplicate_claim"
    finally:
        connection.close()


def test_build_database_rollback_preserves_existing_snapshot(tmp_path: Path) -> None:
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    good_document = raw_dir / "good.md"
    good_document.write_text(
        "# Good\n\n"
        "| ID | Source | URL | Classification |\n"
        "|---|---|---|---|\n"
        "| S1 | Example source | https://example.org/source | Primary |\n"
        "\n"
        "| Claim | Claim type | Confidence | Sources | Relationship |\n"
        "|---|---|---|---|---|\n"
        "| A valid fact | documented fact | high | S1 | supports |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "db.duckdb"
    warnings_path = tmp_path / "warnings.jsonl"

    good_result = build_database(raw_dir, database_path, warnings_path, SCHEMA_PATH)
    assert good_result["claims"] == 1

    broken_schema = tmp_path / "broken.sql"
    broken_schema.write_text("CREATE TABLE broken (", encoding="utf-8")

    with pytest.raises(Exception):
        build_database(raw_dir, database_path, warnings_path, broken_schema)

    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        assert connection.execute("SELECT COUNT(*) FROM claim").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM source").fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM research_document").fetchone()[0] == 1
    finally:
        connection.close()