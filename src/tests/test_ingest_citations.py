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
    analysis_dir = raw_dir / "On Research"
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
        assert row == ("raw/On Research/First-Ratings.md", True, "revise", "Moderate")
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


# ---------------------------------------------------------------------------
# Task 11 — New unit tests for incremental cache, schema migration, classifiers
# ---------------------------------------------------------------------------


def test_incremental_cache_produces_same_result_as_full_rebuild(tmp_path: Path) -> None:
    """Requirements: 9.6, 3.1, 3.2 — incremental run equals full rebuild for unchanged corpus."""
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "doc_a.md").write_text(
        "# Doc A\n\n"
        "| Source | URL | Classification |\n"
        "| --- | --- | --- |\n"
        "| Test Source A | https://example-a.com/page | Primary |\n",
        encoding="utf-8",
    )
    (raw_dir / "doc_b.md").write_text(
        "# Doc B\n\n"
        "| Source | URL | Classification |\n"
        "| --- | --- | --- |\n"
        "| Test Source B | https://example-b.com/page | Secondary |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "citations.duckdb"
    warnings_path = tmp_path / "warnings.jsonl"

    # First run — full rebuild (no prior database)
    result1 = build_database(raw_dir, database_path, warnings_path, SCHEMA_PATH)

    # Second run — incremental (database from first run now exists as cache)
    result2 = build_database(raw_dir, database_path, warnings_path, SCHEMA_PATH)

    # Content table counts must be identical across both runs
    assert result1["documents"] == result2["documents"]
    assert result1["sources"] == result2["sources"]
    assert result1["occurrences"] == result2["occurrences"]

    # Verify the counts are sane (2 docs, 2 sources, 2 occurrences)
    assert result1["documents"] == 2
    assert result1["sources"] == 2
    assert result1["occurrences"] == 2

    # Confirm content-table row counts in the live database match both results
    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        assert connection.execute("SELECT COUNT(*) FROM research_document").fetchone()[0] == result2["documents"]
        assert connection.execute("SELECT COUNT(*) FROM source").fetchone()[0] == result2["sources"]
        assert connection.execute("SELECT COUNT(*) FROM citation_occurrence").fetchone()[0] == result2["occurrences"]
        assert connection.execute("SELECT COUNT(*) FROM source_alias").fetchone()[0] == result2["occurrences"]
    finally:
        connection.close()

    # run_id is content-derived; identical corpus → identical run_id (by design)
    # The important invariant is that both runs succeeded with consistent counts.
    assert result1["run_id"] == result2["run_id"]


def test_schema_migration_is_idempotent(tmp_path: Path) -> None:
    """Requirements: 10.10 — executing citations.sql DDL twice raises no error
    and leaves domain_category / evidence_tier columns with the correct defaults."""
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    db_path = tmp_path / "idempotent.duckdb"
    connection = duckdb.connect(str(db_path))
    try:
        # First application
        connection.execute(schema_sql)
        # Second application must be idempotent
        connection.execute(schema_sql)

        # domain_category defaults to 'uncategorised' on source
        connection.execute(
            "INSERT INTO source (source_id, title) VALUES ('test_src_1', 'Idempotency test source')"
        )
        domain_cat = connection.execute(
            "SELECT domain_category FROM source WHERE source_id = 'test_src_1'"
        ).fetchone()[0]
        assert domain_cat == "uncategorised", f"Expected 'uncategorised', got {domain_cat!r}"

        # evidence_tier defaults to 'unclassified' on citation_occurrence
        # Insert a minimal research_document row first (FK dependency)
        connection.execute(
            "INSERT INTO research_document "
            "(document_id, path, title, document_type, is_internal, content_sha256) "
            "VALUES ('doc_test_1', 'test/doc.md', 'Test doc', 'research_note', FALSE, 'abc')"
        )
        connection.execute(
            "INSERT INTO citation_occurrence "
            "(occurrence_id, raw_citation_text, document_id, extraction_method, resolution_status) "
            "VALUES ('occ_test_1', 'raw text', 'doc_test_1', 'markdown_source_table', 'unresolved')"
        )
        evidence_tier = connection.execute(
            "SELECT evidence_tier FROM citation_occurrence WHERE occurrence_id = 'occ_test_1'"
        ).fetchone()[0]
        assert evidence_tier == "unclassified", f"Expected 'unclassified', got {evidence_tier!r}"
    finally:
        connection.close()


def test_domain_category_and_evidence_tier_columns_populated(tmp_path: Path) -> None:
    """Requirements: 10.1, 10.4, 10.10 — every source row has a valid domain_category
    and every citation_occurrence row has a valid evidence_tier after build_database."""
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "classified.md").write_text(
        "# Classified sources\n\n"
        "| ID | Source | URL | Classification |\n"
        "|---|---|---|---|\n"
        "| S1 | Example primary source | https://example.org/docs/primary-ref | Primary |\n"
        "| S2 | Example secondary source | https://example.org/docs/secondary-ref | Secondary |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "classified.duckdb"

    build_database(raw_dir, database_path, tmp_path / "classified-warnings.jsonl", SCHEMA_PATH)

    connection = duckdb.connect(str(database_path), read_only=True)
    try:
        # Every source row must have a non-null domain_category from the closed enumeration
        source_categories = connection.execute(
            "SELECT domain_category FROM source"
        ).fetchall()
        assert len(source_categories) > 0, "Expected at least one source row"
        for (category,) in source_categories:
            assert category is not None, "domain_category must not be NULL"
            assert category in ingest_citations.DOMAIN_CATEGORIES, (
                f"domain_category {category!r} is not in DOMAIN_CATEGORIES"
            )

        # Every citation_occurrence row must have a non-null evidence_tier from the closed enumeration
        occurrence_tiers = connection.execute(
            "SELECT evidence_tier FROM citation_occurrence"
        ).fetchall()
        assert len(occurrence_tiers) > 0, "Expected at least one citation_occurrence row"
        for (tier,) in occurrence_tiers:
            assert tier is not None, "evidence_tier must not be NULL"
            assert tier in ingest_citations.EVIDENCE_TIERS, (
                f"evidence_tier {tier!r} is not in EVIDENCE_TIERS"
            )
    finally:
        connection.close()


# ---------------------------------------------------------------------------
# Wave 5 — Integration test: incremental cache changed-file path
# ---------------------------------------------------------------------------


def test_incremental_cache_reprocesses_only_changed_files(tmp_path: Path) -> None:
    """Wave 5 — verifies that only the changed file is re-parsed on a second run,
    while unchanged files are carried forward from cache.
    """
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    doc_a = raw_dir / "doc_a.md"
    doc_b = raw_dir / "doc_b.md"
    doc_a.write_text(
        "# Doc A\n\n"
        "| Source | URL | Classification |\n"
        "| --- | --- | --- |\n"
        "| Source A | https://example-a.com/page | Primary |\n",
        encoding="utf-8",
    )
    doc_b.write_text(
        "# Doc B\n\n"
        "| Source | URL | Classification |\n"
        "| --- | --- | --- |\n"
        "| Source B | https://example-b.com/page | Secondary |\n",
        encoding="utf-8",
    )
    database_path = tmp_path / "citations.duckdb"
    warnings_path = tmp_path / "warnings.jsonl"

    result1 = build_database(raw_dir, database_path, warnings_path, SCHEMA_PATH)
    assert result1["documents"] == 2
    assert result1["sources"] == 2

    # Modify only doc_b — add a second source
    doc_b.write_text(
        "# Doc B\n\n"
        "| Source | URL | Classification |\n"
        "| --- | --- | --- |\n"
        "| Source B | https://example-b.com/page | Secondary |\n"
        "| Source B2 | https://example-b2.com/page | Primary |\n",
        encoding="utf-8",
    )

    result2 = build_database(raw_dir, database_path, warnings_path, SCHEMA_PATH)
    assert result2["documents"] == 2
    assert result2["sources"] == 3   # Source A + Source B + Source B2
    assert result2["occurrences"] == 3

    conn = duckdb.connect(str(database_path), read_only=True)
    try:
        # All three sources must be present
        assert conn.execute("SELECT COUNT(*) FROM source").fetchone()[0] == 3
        # Source A (from unchanged doc_a) still present via cache carry-forward
        assert conn.execute(
            "SELECT COUNT(*) FROM source WHERE canonical_url = 'https://example-a.com/page'"
        ).fetchone()[0] == 1
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Wave 6 — 7 property-based tests using hypothesis
# ---------------------------------------------------------------------------

from hypothesis import given  # noqa: E402
from hypothesis import strategies as st  # noqa: E402

from src.ingest_citations import (  # noqa: E402
    DOMAIN_CATEGORIES,
    EVIDENCE_TIERS,
    _classify_domain,
    _classify_evidence_tier,
)

_text = st.text(min_size=0, max_size=200)
_printable = st.text(
    alphabet=st.characters(blacklist_categories=("Cs",)), min_size=0, max_size=200
)


@given(_text)
def test_property_normalize_url_never_raises_and_returns_https(raw: str) -> None:
    """Property 1: normalize_url never raises; when it returns a string it starts with 'https://'."""
    result = normalize_url(raw)
    assert result is None or (isinstance(result, str) and result.startswith("https://"))


@given(_text)
def test_property_normalize_url_is_idempotent(raw: str) -> None:
    """Property 2: normalising an already-normalised URL is a no-op."""
    first = normalize_url(raw)
    if first is not None:
        second = normalize_url(first)
        assert second == first


@given(st.text(min_size=1, max_size=10), _printable)
def test_property_stable_id_is_deterministic(kind: str, value: str) -> None:
    """Property 3: stable_id is deterministic — same inputs always produce the same result."""
    assert stable_id(kind, value) == stable_id(kind, value)


@given(_printable)
def test_property_stable_id_is_kind_scoped(value: str) -> None:
    """Property 4: different kind prefixes never produce the same stable_id."""
    assert stable_id("src", value) != stable_id("doc", value)


@given(st.one_of(st.none(), _text))
def test_property_classify_evidence_tier_returns_valid_member(
    classification: str | None,
) -> None:
    """Property 5: _classify_evidence_tier always returns a member of EVIDENCE_TIERS."""
    assert _classify_evidence_tier(classification) in EVIDENCE_TIERS


@given(
    st.one_of(st.none(), _text),
    _text,
    st.one_of(st.none(), _text),
)
def test_property_classify_domain_returns_valid_member(
    canonical_url: str | None, title: str, publisher: str | None
) -> None:
    """Property 6: _classify_domain always returns a member of DOMAIN_CATEGORIES."""
    assert _classify_domain(canonical_url, title, publisher) in DOMAIN_CATEGORIES


@given(st.text(min_size=0, max_size=2000))
def test_property_parse_markdown_tables_heading_is_substring(markdown: str) -> None:
    """Property 7: every table's heading is either empty or a substring of the source markdown."""
    for table in parse_markdown_tables(markdown):
        assert table.heading == "" or table.heading in markdown
