"""Tests for the read-only DuckDB exporter (Protocols/ExportDatabase.md)."""

from __future__ import annotations

import json
from pathlib import Path

import duckdb
import pytest

from src.db_export_core import (
    ExportError,
    export_all,
    export_database_bundle,
    export_view_snapshots,
    inventory_database,
    verify_bundle,
)


def _mini_db(path: Path) -> None:
    con = duckdb.connect(str(path))
    con.execute("CREATE TABLE parent(id VARCHAR PRIMARY KEY, label VARCHAR NOT NULL)")
    con.execute("CREATE TABLE child(id VARCHAR PRIMARY KEY, parent_id VARCHAR REFERENCES parent(id), "
                "note VARCHAR, created DATE, stamp TIMESTAMP)")
    con.execute("INSERT INTO parent VALUES ('p1', 'caf\u00e9 \u00fcn\u00efc\u00f6d\u00e9 \u6f22\u5b57'), ('p2', '')")
    con.execute("INSERT INTO child VALUES ('c1', 'p1', NULL, DATE '2026-01-02', TIMESTAMP '2026-01-02 03:04:05')")
    con.execute("INSERT INTO child VALUES ('c2', 'p2', '', DATE '2026-03-04', TIMESTAMP '2026-03-04 05:06:07')")
    con.execute("CREATE VIEW child_count AS SELECT parent_id, COUNT(*) AS n FROM child GROUP BY parent_id")
    con.execute("CREATE TABLE run_meta(run_id VARCHAR PRIMARY KEY)")
    con.execute("INSERT INTO run_meta VALUES ('run_abc')")
    con.close()


def test_inventory_lists_tables_views_counts(tmp_path: Path) -> None:
    db = tmp_path / "m.duckdb"
    _mini_db(db)
    inv = inventory_database("citations", db)
    assert "parent" in inv.tables and "child" in inv.tables
    assert "child_count" in inv.views
    assert "CREATE VIEW child_count" in inv.view_definitions["child_count"]
    assert inv.row_counts["parent"] == 2 and inv.row_counts["view:child_count"] == 2


def test_inventory_missing_db_raises(tmp_path: Path) -> None:
    with pytest.raises(ExportError, match="not found"):
        inventory_database("citations", tmp_path / "nope.duckdb")


def test_export_bundle_is_restorable_and_verify_ok(tmp_path: Path) -> None:
    db = tmp_path / "m.duckdb"
    _mini_db(db)
    inv = inventory_database("citations", db)
    for fmt in ("csv", "parquet"):
        bundle = tmp_path / f"b_{fmt}"
        export_database_bundle(inv, bundle, fmt)
        assert (bundle / "schema.sql").is_file() and (bundle / "load.sql").is_file()
        assert verify_bundle(bundle, inv, tmp_path / "vtmp")["status"] == "VERIFIED_OK"


def test_view_snapshots_labelled_and_readable(tmp_path: Path) -> None:
    db = tmp_path / "m.duckdb"
    _mini_db(db)
    inv = inventory_database("citations", db)
    written = export_view_snapshots(inv, tmp_path / "views")
    names = sorted(p.name for p in written)
    assert names == ["child_count.csv", "child_count.parquet"]
    con = duckdb.connect(str(db), read_only=True)
    try:
        expected = con.execute("SELECT * FROM child_count ORDER BY ALL").fetchall()
    finally:
        con.close()
    got = duckdb.connect().execute(
        f"SELECT * FROM read_csv('{tmp_path.as_posix()}/views/child_count.csv', header=true) ORDER BY ALL"
    ).fetchall()
    assert [tuple(str(v) for v in r) for r in got] == [tuple(str(v) for v in r) for r in expected]


def test_verify_detects_content_mismatch(tmp_path: Path) -> None:
    db = tmp_path / "m.duckdb"
    _mini_db(db)
    inv = inventory_database("citations", db)
    bundle = tmp_path / "b_parquet"
    export_database_bundle(inv, bundle, "parquet")
    csv_file = bundle / "parent.parquet"
    csv_file.write_bytes(b"corrupted")
    with pytest.raises(Exception):
        verify_bundle(bundle, inv, tmp_path / "vtmp")


def test_verify_detects_schema_mismatch(tmp_path: Path) -> None:
    db = tmp_path / "m.duckdb"
    _mini_db(db)
    inv = inventory_database("citations", db)
    bundle = tmp_path / "b_parquet"
    export_database_bundle(inv, bundle, "parquet")
    inv2 = inventory_database("citations", db)
    object.__setattr__(inv2, "tables", inv2.tables + ["ghost_table"])
    with pytest.raises(ExportError, match="Schema mismatch"):
        verify_bundle(bundle, inv2, tmp_path / "vtmp2")


def test_export_all_production_end_to_end(tmp_path: Path) -> None:
    out = export_all(tmp_path / "exports", which="all", formats=("csv", "parquet"),
                     overwrite=False, verify=True, timestamp="test-suite-probe")
    run_dir = Path(out["run_dir"])
    assert run_dir.is_dir()
    for name in ("citations", "stage2"):
        for fmt in ("csv", "parquet"):
            assert (run_dir / f"{name}_{fmt}" / "schema.sql").is_file()
        assert (run_dir / "views" / name).is_dir()
        assert (run_dir / f"{name}_warnings.jsonl").is_file()
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["verification"]
    assert all(v["status"] == "VERIFIED_OK" for v in manifest["verification"].values())
    assert manifest["databases"]["citations"]["row_counts"]["source"] >= 1
    assert {f["path"] for f in manifest["files"]} >= {"manifest.json", "README.md"}
    for db_name, entry in manifest["databases"].items():
        assert entry["source_unchanged"] is True and entry["view_definitions"]
    # tmp_path auto-cleans; no manual rmtree (keeps Windows file-lock safety).
