"""Tests for src/viz_core.py — the shared notebook visualization library.

Each test seeds a temp DuckDB database from schemas/stage2.sql with a small,
deterministic fixture and points ``viz_core`` at it by monkeypatching the
module-level ``DEFAULT_DB_PATH`` (mirroring the monkeypatch-ROOT convention
used by the citation/ingest tests in AGENTS.md).
"""
from __future__ import annotations

from pathlib import Path

import duckdb
import pandas as pd
import pytest

import src.viz_core as viz

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas" / "stage2.sql"


def _seed_db(path: Path) -> None:
    con = duckdb.connect(str(path))
    con.execute(SCHEMA.read_text(encoding="utf-8"))
    con.execute(
        "INSERT INTO stage2_document VALUES "
        "('doc_d1','research/raw/Stage 2/Extraction 2/Claims.md','sha','2026-01-01'),"
        "('doc_d2','research/raw/Stage 2/Extraction 2/Entities.md','sha2','2026-01-01'),"
        "('doc_d3','research/raw/Stage 2/Extraction 2/Metrics.md','sha3','2026-01-01'),"
        "('doc_d4','research/raw/Stage 2/Extraction 2/Sources.md','sha4','2026-01-01'),"
        "('doc_d5','research/raw/Stage 2/Extraction 2/Predicates.md','sha5','2026-01-01'),"
        "('doc_d6','research/raw/Stage 2/Extraction 2/ExtractionLog.md','sha6','2026-01-01')"
    )
    con.execute(
        "INSERT INTO entity VALUES "
        "('e_c1','C001','Matter','Standard','C001 boundary',TRUE,'stage1','Core idea','high','doc_d1'),"
        "('e_c2','C002','Thread','Technology (low-power IP mesh network)','b2',TRUE,'stage1','Core idea','high','doc_d1'),"
        "('e_other','X99','Other','Device','b',TRUE,'s','Device Types & Feature Consistency','medium','doc_d1')"
    )
    con.execute(
        "INSERT INTO source_mirror VALUES "
        "('s_S1','S1','Matter 1.4','https://csa.example/matter','CSA','Primary','2024-05-01','doc_d4'),"
        "('s_S10','S10','Internal S10','https://internal.example/s10','Internal','Secondary','2025-01-01','doc_d4')"
    )
    con.execute(
        "INSERT INTO metric VALUES "
        "('m_m1','M001','Matter version','1.6','version','',TRUE,'documented fact','high','S1;S34','stage1','Core idea','doc_d3'),"
        "('m_m2','M002','Versions referenced','1.4, 1.4.2, 1.5, 1.6','version','',TRUE,'documented fact','high','S1','stage1','Core idea','doc_d3'),"
        "('m_m3','M003','Samsung device types','58','count','scope',TRUE,'reported signal','medium','S10','stage1','Device Types & Feature Consistency','doc_d3')"
    )
    con.execute(
        "INSERT INTO stage2_claim VALUES "
        "('cl_C001','C001','Matter is the app-layer standard.','documented fact','high',"
        "'[falsifier not stated]',TRUE,'W3','S1','stage1','Core idea','doc_d1'),"
        "('cl_C002','C002','Thread complements Wi-Fi.','documented fact','high',"
        "'A falsifier text',TRUE,'W3','S10;S2','stage1','Core idea','doc_d1'),"
        "('cl_C003','C003','Empty refs claim.','documented fact','high',"
        "'[falsifier not stated]',TRUE,'W3','','stage1','Core idea','doc_d1'),"
        "('cl_C999','C999','Support periods are short.','reported signal','medium',"
        "'[falsifier not stated]',TRUE,'W9','S18','stage1','The practical gap','doc_d1')"
    )
    con.execute(
        "INSERT INTO predicate VALUES "
        "('p1','implemented_by','Standard','Ecosystem implementation','Matter -> ecosystem','Matter example','stage1','doc_d5'),"
        "('p2','complements','Technology (mesh network)','Technology (transport)','Thread -> IP','Thread complements','stage1','doc_d5'),"
        "('p3','no_match','Quantum','Quantum','q','unrelated','stage1','doc_d5')"
    )
    con.execute(
        "INSERT INTO workflow_stage VALUES "
        "('ws_W3','W3','Six-Lens Category Synthesis','i','a','o','q','r','t','e','high','doc_d5')"
    )
    con.execute(
        "INSERT INTO extraction_decision VALUES "
        "('d1','L001','Step 1','research/raw/Stage 2/Extraction 2/Claims.md','label_resolution','Core idea decision','resolved','doc_d6')"
    )
    con.commit()
    con.close()


@pytest.fixture()
def db(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "smarthome_test.duckdb"
    _seed_db(path)
    monkeypatch.setattr(viz, "DEFAULT_DB_PATH", str(path))
    return path


def test_connect_db_uses_env_path(db: Path) -> None:
    con = viz.connect_db()
    assert con.execute("SELECT COUNT(*) FROM stage2_claim").fetchone()[0] == 4
    con.close()


def test_fetch_claim_returns_dict(db: Path) -> None:
    claim = viz.fetch_claim("C001")
    assert claim["local_id"] == "C001"
    assert claim["claim_type"] == "documented fact"
    assert claim["section"] == "Core idea"
    assert claim["source_refs"] == "S1"
    assert claim["falsifier_stated"] is True
    assert "claim_id" in claim and "document_id" in claim


def test_fetch_claim_missing_raises(db: Path) -> None:
    with pytest.raises(KeyError):
        viz.fetch_claim("ZZZ")


def test_fetch_claim_accepts_internal_id(db: Path) -> None:
    claim = viz.fetch_claim("cl_C001")
    assert claim["local_id"] == "C001"


def test_source_tokens_split() -> None:
    assert viz._source_tokens("S1;S34;S36") == ["S1", "S34", "S36"]
    assert viz._source_tokens("S1, S34") == ["S1", "S34"]
    assert viz._source_tokens("") == []
    assert viz._source_tokens(None) == []


def test_source_tokens_dedupes_not_required() -> None:
    assert viz._source_tokens("S1;S1") == ["S1", "S1"]


def test_fetch_metrics_section_and_source_linkage(db: Path) -> None:
    # C001 section='Core idea', source_refs='S1'
    m = viz.fetch_metrics_for_claim("C001")
    assert set(m["local_id"]) == {"M001", "M002"}  # both same section + share S1
    assert (m["linkage"] == "section").any()
    # M003 is a different section -> not included
    assert "M003" not in set(m["local_id"])


def test_fetch_metrics_source_fallback(db: Path) -> None:
    # C002 source_refs 'S10;S2', section 'Core idea' only has M001,M002 (S1).
    # M003 shares S10 -> must appear via source linkage.
    m = viz.fetch_metrics_for_claim("C002")
    assert "M003" in set(m["local_id"])
    assert m.loc[m["local_id"] == "M003", "linkage"].iloc[0] == "source"


def test_fetch_metrics_empty_when_no_match(db: Path) -> None:
    assert viz.fetch_metrics_for_claim("C999").empty  # different section, no source overlap


def test_fetch_entities_for_claim(db: Path) -> None:
    e = viz.fetch_entities_for_claim("C001")
    assert set(e["local_id"]) == {"C001", "C002"}
    assert (e["section"] == "Core idea").all()


def test_fetch_sources_for_claim(db: Path) -> None:
    s = viz.fetch_sources_for_claim("C002")  # S10;S2 -> S10 resolves, S2 does not
    assert set(s["local_id"]) == {"S10"}
    assert s["url"].iloc[0] == "https://internal.example/s10"


def test_fetch_sources_no_tokens_empty(db: Path) -> None:
    # C003 has an empty source_refs cell -> no token -> empty frame.
    s = viz.fetch_sources_for_claim("C003")
    assert s.empty
    # column shape is still defined
    assert {"source_id", "local_id", "title", "linkage"}.issubset(s.columns)


def test_fetch_sources_partial_resolution(db: Path) -> None:
    # C999 references S18 which is not seeded in source_mirror -> empty.
    s = viz.fetch_sources_for_claim("C999")
    assert s.empty


def test_fetch_predicates_type_overlap_and_example(db: Path) -> None:
    p = viz.fetch_predicates_for_entities(["C001", "C002"])
    # 'implemented_by' (Standard) and 'complements' (Technology) match by type word overlap
    assert "implemented_by" in set(p["predicate"])
    assert "no_match" not in set(p["predicate"])
    assert "type_overlap" in set(p["linkage"])


def test_fetch_extraction_log_for_claim(db: Path) -> None:
    log = viz.fetch_extraction_log_for_claim("C001")  # section 'Core idea'
    assert log["local_id"].iloc[0] == "L001"
    assert log["linkage"].iloc[0] == "text_match"


def test_fetch_extraction_log_falsifier_stated(db: Path) -> None:
    claim = viz.fetch_claim("C002")
    assert claim["falsifier_stated"] is True
    assert claim["falsifier"] == "A falsifier text"


def test_confidence_color() -> None:
    assert viz.confidence_color("high") == "#1a7f37"
    assert viz.confidence_color("medium") == "#b06000"
    assert viz.confidence_color("low") == "#b32637"
    assert viz.confidence_color(None) == "#757575"
    assert viz.confidence_color("bogus") == "#757575"


def test_evidence_class_marker() -> None:
    assert viz.evidence_class_marker("documented fact") == "DOC"
    assert viz.evidence_class_marker("reported signal") == "SIG"
    assert viz.evidence_class_marker("inference") == "INF"
    assert viz.evidence_class_marker("recommendation") == "REC"
    assert viz.evidence_class_marker("nope") == "??"


def test_claim_domain() -> None:
    assert viz.claim_domain("Core idea") == "Matter/Thread"
    assert viz.claim_domain("What Savings Are Measured Rather Than Claimed?") == "Energy"
    assert viz.claim_domain("The practical gap") == "Security"
    assert viz.claim_domain("1. AI Hubs (Local AI Brains)") == "Emerging"
    assert viz.claim_domain("Subscription fatigue") == "Business"
    assert viz.claim_domain("Semantic Scholar source block") == "Meta"
    assert viz.claim_domain("Safe Autonomy vs. Required Confirmation") == "AI/Voice"
    assert viz.claim_domain(None) is None


def test_fetch_all_claims_has_domain(db: Path) -> None:
    df = viz.fetch_all_claims()
    assert {"local_id", "claim_text", "domain", "evidence_marker",
            "falsifier", "falsifier_missing"}.issubset(df.columns)
    assert "C001" in set(df["local_id"])
    assert viz.claim_domain("Core idea") in set(df["domain"])
    # C001's falsifier cell is the placeholder even though falsifier_stated is TRUE
    assert df.set_index("local_id").loc["C001", "falsifier_missing"]
    assert not df.set_index("local_id").loc["C002", "falsifier_missing"]


def test_render_provenance_panel(db: Path) -> None:
    panel = viz.render_provenance_panel("C002")
    value = panel.value
    assert isinstance(value, str)
    assert "C002" in value
    assert "A falsifier text" in value
    assert "https://internal.example/s10" in value
    # confidence color is embedded
    assert viz.confidence_color("high") in value


def test_render_provenance_panel_missing_falsifier_flag(db: Path) -> None:
    panel = viz.render_provenance_panel("C999")
    assert "falsifier not stated" in panel.value


def test_metrics_by_id_preserves_requested_order(db: Path) -> None:
    df = viz.metrics_by_id(["M003", "M001"])
    assert list(df["local_id"]) == ["M003", "M001"]
    assert "scope_conditions" in df.columns


def test_metrics_by_id_skips_unknown_and_empty(db: Path) -> None:
    df = viz.metrics_by_id(["M001", "NOPE"])
    assert list(df["local_id"]) == ["M001"]
    assert viz.metrics_by_id([]).empty


def test_range_frame_bounds_and_raw(db: Path) -> None:
    df = viz.range_frame(["M001", "M003"])
    by_id = df.set_index("metric")
    assert by_id.loc["M001", "low"] == 1.6
    assert by_id.loc["M001", "high"] == 1.6
    assert by_id.loc["M003", "value"] == "58"
    assert by_id.loc["M003", "unit"] == "count"
    assert by_id.loc["M003", "source"] == "S10"


def test_range_frame_drops_unparsable(db: Path) -> None:
    con = duckdb.connect(str(db))
    con.execute(
        "INSERT INTO metric VALUES ('m_m9','M009','PSTI minimum period','none',"
        "'n/a','',TRUE,'documented fact','high','S10','stage1',"
        "'The practical gap','doc_d3')"
    )
    con.close()
    df = viz.range_frame(["M001", "M009"])
    # 'none' holds no number, so M009 is dropped and only M001 survives.
    assert list(df["metric"]) == ["M001"]


def test_fetch_claims_cluster_preserves_order(db: Path) -> None:
    df = viz.fetch_claims(["C002", "C001"])
    assert list(df["local_id"]) == ["C002", "C001"]
    assert {"domain", "evidence_marker", "falsifier_missing"}.issubset(df.columns)
    assert list(df["falsifier_missing"]) == [False, True]


def test_fetch_claims_unknown_id_raises(db: Path) -> None:
    with pytest.raises(KeyError):
        viz.fetch_claims(["C001", "NOPE"])


def test_section_metrics(db: Path) -> None:
    df = viz.section_metrics("Core idea")
    assert set(df["local_id"]) == {"M001", "M002"}
    assert viz.section_metrics("no such section").empty


def test_sources_for_claims_union(db: Path) -> None:
    df = viz.sources_for_claims(["C001", "C002"])
    assert set(df["local_id"]) == {"S1", "S10"}
    assert len(df) == len(df["local_id"].unique())
    assert viz.sources_for_claims(["C003"]).empty


def test_parse_numbers_and_ranges() -> None:
    assert viz.parse_numbers("3-5") == [3.0, 5.0]
    # patch components of a version string ("1.4.2") are not separate numbers
    assert viz.parse_numbers("1.4, 1.4.2, 1.5, 1.6") == [1.4, 1.4, 1.5, 1.6]
    assert viz.parse_numbers("760 (45%)") == [760.0, 45.0]
    assert viz.parse_numbers(None) == []
    assert viz.numeric_value("58") == 58.0
    assert viz.numeric_value("March 2026") == 2026.0
    assert viz.numeric_value(None) is None


def test_parse_numbers_handles_thousands_separators() -> None:
    # A comma between a digit and exactly three digits groups one number...
    assert viz.parse_numbers("3,750") == [3750.0]
    assert viz.range_value("3,750") == (3750.0, 3750.0)
    assert viz.range_value("50,000-100,000") == (50000.0, 100000.0)
    assert viz.parse_numbers("11,800 USD") == [11800.0]
    assert viz.parse_numbers("2,070 TOPS; 20,000") == [2070.0, 20000.0]
    # ...but a comma-separated list of short values stays a list.
    assert viz.parse_numbers("3, 4, 5") == [3.0, 4.0, 5.0]
    assert viz.parse_numbers("3, 4, 5") != viz.parse_numbers("34,5")


def test_parse_numbers_keeps_signs_but_not_identifier_hyphens() -> None:
    # A real negative keeps its sign.
    assert viz.parse_numbers("-3,824") == [-3824.0]
    # A hyphen after a letter is part of a model number, not a sign.
    assert viz.parse_numbers("HPWH CTA-2045 200-400") == [2045.0, 200.0, 400.0]
    assert all(n >= 0 for n in viz.parse_numbers("CTA-2045; CTA-2045-B"))


def test_range_value_refuses_to_invent_a_range() -> None:
    """Two unrelated numbers are two quantities, not the ends of a span."""
    assert viz.range_value("48 TB; 26 TOPS") == (None, None)
    assert viz.range_value("760 (45%)") == (None, None)
    assert viz.range_value("23% base; range 10-35%") == (None, None)
    assert viz.range_value("11,800 USD; 7.6 years") == (None, None)
    assert viz.range_value("none") == (None, None)
    # A single number is not a range but is still a usable bound.
    assert viz.range_value("7") == (7.0, 7.0)
    assert viz.range_value("3-5") == (3.0, 5.0)


def test_range_value_never_inverts_a_corpus_cell(db: Path) -> None:
    """No value cell may produce a low above its high."""
    con = duckdb.connect(str(db))
    con.execute(
        "INSERT INTO metric VALUES ('m_m10','M010','Compound cell',"
        "'48 TB; 26 TOPS','TB; TOPS','',TRUE,'documented fact','high','S1',"
        "'stage1','Core idea','doc_d3')"
    )
    cells = [row[0] for row in con.execute("SELECT value FROM metric").fetchall()]
    con.close()
    for cell in cells:
        low, high = viz.range_value(cell)
        assert not (low is not None and high is not None and low > high), cell


def test_claim_metrics_lookup_dedup(db: Path) -> None:
    df = viz.claim_metrics_lookup(["C001", "C002"])
    # M001 and M002 appear once each despite overlapping linkage
    assert len(df) == len(df["local_id"].unique())
    assert {"M001", "M002", "M003"}.issubset(set(df["local_id"]))


def test_connect_db_missing_path_raises(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(viz, "DEFAULT_DB_PATH", str(tmp_path / "does_not_exist.duckdb"))
    with pytest.raises(duckdb.Error):
        viz.connect_db()
