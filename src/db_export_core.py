"""Core exporter: read-only DuckDB -> timestamped CSV + Parquet bundles.

Per Rules and Regulations/Protocols/ExportDatabase.md (implements
Commander Deck/Plans/ExportPlan): the production databases (citations.duckdb, stage2.duckdb, smarthome.duckdb) are exported
into timestamped, gitignored bundles under data/exports/ via DuckDB's native
EXPORT DATABASE (restorable schema.sql + load.sql + table files), plus
read-only snapshots of each view's query results. Sources stay unchanged.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import duckdb

ROOT = Path(__file__).resolve().parents[1]

PRODUCTION_DATABASES: dict[str, dict[str, str]] = {
    "citations": {
        "database": "data/citations.duckdb",
        "schema": "schemas/citations.sql",
        "warnings": "data/citation_ingestion_warnings.jsonl",
        "run_table": "ingestion_run",
    },
    "stage2": {
        "database": "data/stage2.duckdb",
        "schema": "schemas/stage2.sql",
        "warnings": "data/stage2_ingestion_warnings.jsonl",
        "run_table": "stage2_run",
    },
    "smarthome": {
        "database": "data/smarthome.duckdb",
        "schema": "schemas/stage2.sql",
        "warnings": "data/smarthome_ingestion_warnings.jsonl",
        "run_table": "stage2_run",
    },
}

EXPORT_FORMATS = ("csv", "parquet")


class ExportError(RuntimeError):
    """Raised when inventory, export, or verification fails."""


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with open(path, "rb") as fh:
        while chunk := fh.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def _quote_path(path: Path) -> str:
    return "'" + path.as_posix().replace("'", "''") + "'"


def _quote_ident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def _scalar(con: duckdb.DuckDBPyConnection, sql: str) -> Any:
    """First column of the first row of an aggregate query.

    ``DuckDBPyConnection.fetchone()`` is typed ``Any | None``, so subscripting
    it directly trips Pylance (reportOptionalSubscript). Aggregate queries here
    always return exactly one row; an empty result means the schema/shape is not
    what we expect, so fail loudly instead of returning None.
    """
    row = con.execute(sql).fetchone()
    if row is None:
        raise ExportError(f"Query returned no rows: {sql}")
    return row[0]

@dataclass
class DatabaseInventory:
    name: str
    database_path: Path
    tables: list[str]
    views: list[str]
    view_definitions: dict[str, str]
    row_counts: dict[str, int]
    run_id: str | None
    warnings_path: Path | None
    warnings_count: int | None


def inventory_database(name: str, database_path: Path, warnings_path: Path | None = None) -> DatabaseInventory:
    """Read-only inventory: tables, views (+SQL), row counts, run id."""
    if not database_path.is_file():
        raise ExportError(f"Source database not found: {database_path}")
    con: duckdb.DuckDBPyConnection | None = None
    try:
        con = duckdb.connect(str(database_path), read_only=True)
        tables = [
            r[0]
            for r in con.execute(
                "SELECT table_name FROM information_schema.tables "
                "WHERE table_schema='main' AND table_type='BASE TABLE' ORDER BY 1"
            ).fetchall()
        ]
        view_rows = con.execute(
            "SELECT view_name, sql FROM duckdb_views() "
            "WHERE schema_name='main' AND NOT internal ORDER BY 1"
        ).fetchall()
        views = [r[0] for r in view_rows]
        view_definitions = {r[0]: r[1] for r in view_rows}
        row_counts: dict[str, int] = {}
        for table in tables:
            row_counts[table] = _scalar(
                con, f"SELECT COUNT(*) FROM {_quote_ident(table)}")
        for view in views:
            row_counts[f"view:{view}"] = _scalar(
                con, f"SELECT COUNT(*) FROM {_quote_ident(view)}")
        run_table = PRODUCTION_DATABASES.get(name, {}).get("run_table")
        run_id: str | None = None
        if run_table and run_table in tables:
            row = con.execute(f"SELECT run_id FROM {_quote_ident(run_table)} LIMIT 1").fetchone()
            run_id = row[0] if row else None
    finally:
        if con is not None:
            con.close()
    warnings_count: int | None = None
    if warnings_path is not None and warnings_path.is_file():
        warnings_count = sum(1 for _ in warnings_path.open("r", encoding="utf-8"))
    return DatabaseInventory(name, database_path, tables, views, view_definitions,
                             row_counts, run_id, warnings_path, warnings_count)


def export_database_bundle(inventory: DatabaseInventory, bundle_dir: Path, export_format: str) -> Path:
    """Run DuckDB native EXPORT DATABASE (restorable schema.sql + load.sql)."""
    if export_format not in EXPORT_FORMATS:
        raise ExportError(f"Unsupported format {export_format!r}")
    bundle_dir.mkdir(parents=True, exist_ok=True)
    con: duckdb.DuckDBPyConnection | None = None
    try:
        con = duckdb.connect(str(inventory.database_path), read_only=True)
        if export_format == "csv":
            con.execute(f"EXPORT DATABASE {_quote_path(bundle_dir)} (FORMAT CSV, HEADER true)")
        else:
            con.execute(f"EXPORT DATABASE {_quote_path(bundle_dir)} (FORMAT PARQUET)")
    finally:
        if con is not None:
            con.close()
    if not (bundle_dir / "schema.sql").is_file() or not (bundle_dir / "load.sql").is_file():
        raise ExportError(f"EXPORT DATABASE produced no schema/load SQL in {bundle_dir}")
    return bundle_dir


def export_view_snapshots(inventory: DatabaseInventory, snapshots_dir: Path,
                          formats: tuple[str, ...] = ("csv", "parquet")) -> list[Path]:
    """Export each view's current query results as labelled snapshots."""
    snapshots_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    if not inventory.views:
        return written
    con: duckdb.DuckDBPyConnection | None = None
    try:
        con = duckdb.connect(str(inventory.database_path), read_only=True)
        for view in inventory.views:
            for fmt in formats:
                dest = snapshots_dir / f"{view}.{'csv' if fmt == 'csv' else 'parquet'}"
                if fmt == "csv":
                    con.execute(f"COPY (SELECT * FROM {_quote_ident(view)}) "
                                f"TO {_quote_path(dest)} (HEADER, DELIMITER ',')")
                else:
                    con.execute(f"COPY (SELECT * FROM {_quote_ident(view)}) "
                                f"TO {_quote_path(dest)} (FORMAT PARQUET)")
                written.append(dest)
    finally:
        if con is not None:
            con.close()
    return written
def _nullable_columns(con: duckdb.DuckDBPyConnection, table: str) -> set[str]:
    try:
        rows = con.execute(f"DESCRIBE {_quote_ident(table)}").fetchall()
        # DESCRIBE columns: column_name, column_type, null, key, default, extra
        return {r[0] for r in rows if str(r[2]).upper() == "YES"}
    except Exception:
        return set()


def verify_bundle(bundle_dir: Path, inventory: DatabaseInventory, tmp_dir: Path) -> dict[str, Any]:
    """IMPORT bundle into fresh temp DB; compare schema, counts, full contents, FKs."""
    tmp_dir.mkdir(parents=True, exist_ok=True)
    restored = tmp_dir / f"verify_{bundle_dir.name}.duckdb"
    if restored.exists():
        restored.unlink()
    is_csv = bundle_dir.name.endswith("_csv")
    con: duckdb.DuckDBPyConnection | None = None
    src: duckdb.DuckDBPyConnection | None = None
    try:
        con = duckdb.connect(str(restored))
        con.execute(f"IMPORT DATABASE {_quote_path(bundle_dir)}")
        restored_tables = {r[0] for r in con.execute(
            "SELECT table_name FROM information_schema.tables "
            "WHERE table_schema='main' AND table_type='BASE TABLE'").fetchall()}
        if set(inventory.tables) != restored_tables:
            raise ExportError(f"Schema mismatch in {bundle_dir.name}: "
                              f"missing={sorted(set(inventory.tables) - restored_tables)} "
                              f"extra={sorted(restored_tables - set(inventory.tables))}")
        src = duckdb.connect(str(inventory.database_path), read_only=True)
        for table in inventory.tables:
            cols = [d[0] for d in src.execute(
                f"SELECT * FROM {_quote_ident(table)} LIMIT 0").description]
            # CSV collapses '' to NULL only in nullable VARCHAR columns
            # (NOT NULL columns roundtrip '' faithfully via force_not_null).
            nullable = _nullable_columns(src, table) if is_csv else set()
            expected = src.execute(f"SELECT * FROM {_quote_ident(table)} ORDER BY ALL").fetchall()
            actual = con.execute(f"SELECT * FROM {_quote_ident(table)} ORDER BY ALL").fetchall()
            if is_csv and nullable:
                idx = [i for i, c in enumerate(cols) if c in nullable]
                expected = [tuple(None if (i in idx and v == "") else v
                                  for i, v in enumerate(row)) for row in expected]
            if expected != actual:
                raise ExportError(f"Content mismatch for {table} in {bundle_dir.name}: "
                                  f"expected {len(expected)} rows, restored {len(actual)} rows")
        for view in inventory.views:
            restored_count = _scalar(
                con, f"SELECT COUNT(*) FROM {_quote_ident(view)}")
            if restored_count != inventory.row_counts.get(f"view:{view}"):
                raise ExportError(f"View {view} count mismatch in {bundle_dir.name}")
        try:
            violations = con.execute("PRAGMA foreign_key_check").fetchall()
        except Exception:
            violations = []
        if violations:
            raise ExportError(f"Foreign-key violations in {bundle_dir.name}: {violations[:5]}")
    finally:
        if src is not None:
            src.close()
        if con is not None:
            con.close()
        if restored.exists():
            restored.unlink()
    return {"bundle": bundle_dir.name, "status": "VERIFIED_OK"}


def export_all(export_root: Path, which: str = "all",
               formats: tuple[str, ...] = ("csv", "parquet"),
               overwrite: bool = False, verify: bool = True,
               timestamp: str | None = None) -> dict[str, Any]:
    """Export production databases into a unique timestamped run directory."""
    names = list(PRODUCTION_DATABASES) if which == "all" else [which]
    for name in names:
        if name not in PRODUCTION_DATABASES:
            raise ExportError(f"Unknown database {name!r}")
    for fmt in formats:
        if fmt not in EXPORT_FORMATS:
            raise ExportError(f"Unsupported format {fmt!r}")
    stamp = timestamp or _utc_timestamp()
    run_dir = export_root / f"export_{stamp}"
    if run_dir.exists() and any(run_dir.iterdir()) and not overwrite:
        raise ExportError(f"Refusing to overwrite non-empty {run_dir}")
    run_dir.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, Any] = {
        "export_time_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "duckdb_version": duckdb.__version__, "formats": list(formats),
        "run_dir": run_dir.name, "databases": {},
        "restore_instructions": ("Each <db>_<format>/ is an EXPORT DATABASE bundle "
            "(schema.sql + load.sql + table files). Restore: "
            "con = duckdb.connect('restored.duckdb'); "
            "con.execute(\"IMPORT DATABASE '<bundle_dir>'\"). "
            "views/<db>/ holds read-only view-result snapshots, not source tables. "
            "Fidelity caveat: CSV collapses '' to NULL in nullable columns; "
            "Parquet preserves NULL-vs-empty exactly."),
        "fidelity_caveat": "csv_empty_string_as_null_in_nullable_columns; parquet_exact",
    }
    verification: dict[str, Any] = {}
    for name in names:
        spec = PRODUCTION_DATABASES[name]
        db_path = ROOT / spec["database"]
        warn_path = ROOT / spec["warnings"]
        before_stat = db_path.stat() if db_path.exists() else None
        before_sha = _sha256_file(db_path) if db_path.is_file() else None
        inv = inventory_database(name, db_path, warn_path)
        entry: dict[str, Any] = {"source_database": db_path.as_posix(),
            "source_sha256": before_sha, "run_id": inv.run_id,
            "tables": inv.tables, "views": inv.views, "row_counts": inv.row_counts,
            "warnings_file": warn_path.as_posix() if warn_path.is_file() else None,
            "warnings_count": inv.warnings_count, "bundles": {},
            "view_definitions": inv.view_definitions}
        for fmt in formats:
            bundle_dir = run_dir / f"{name}_{fmt}"
            if bundle_dir.exists() and not overwrite:
                raise ExportError(f"Refusing to overwrite {bundle_dir}")
            export_database_bundle(inv, bundle_dir, fmt)
            entry["bundles"][fmt] = bundle_dir.relative_to(run_dir).as_posix()
            if verify:
                verification[f"{name}_{fmt}"] = verify_bundle(bundle_dir, inv, run_dir / "_verify_tmp")
        written = export_view_snapshots(inv, run_dir / "views" / name, formats)
        entry["view_snapshots"] = [p.relative_to(run_dir).as_posix() for p in written]
        if warn_path.is_file():
            shutil.copyfile(warn_path, run_dir / f"{name}_warnings.jsonl")
        if before_sha is not None and _sha256_file(db_path) != before_sha:
            raise ExportError(f"Source database {db_path} changed during export")
        if before_stat is not None and db_path.stat().st_mtime_ns != before_stat.st_mtime_ns:
            raise ExportError(f"Source database {db_path} mtime changed during export")
        entry["source_unchanged"] = True
        manifest["databases"][name] = entry
    manifest["files"] = [_file_record(p, run_dir) for p in sorted(run_dir.rglob("*")) if p.is_file()]
    manifest["verification"] = verification
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    lines = [f"# Database export {run_dir.name}", "",
        f"Exported at {manifest['export_time_utc']} with DuckDB {manifest['duckdb_version']}.", "",
        "The `*.duckdb` files remain the source of truth; this directory holds derived artifacts.", "",
        "## Layout", ""]
    for name in names:
        for fmt in formats:
            lines.append(f"- `{name}_{fmt}/` -- restorable EXPORT DATABASE bundle ({fmt}).")
        lines.append(f"- `views/{name}/` -- read-only snapshots of each view's query results.")
        lines.append(f"- `{name}_warnings.jsonl` -- companion ingestion warnings copy.")
    lines += ["- `manifest.json` -- inventory, row counts, checksums, restore instructions.", "",
        "## Restore", "", "```python", "import duckdb",
        "con = duckdb.connect('restored.duckdb')", "con.execute(\"IMPORT DATABASE 'citations_csv'\")",
        "```", "", "CSV opens in spreadsheets; Parquet preserves typed data. Excel is out of scope."]
    (run_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    manifest["files"] = [_file_record(p, run_dir) for p in sorted(run_dir.rglob("*")) if p.is_file()]
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    manifest["run_dir"] = str(run_dir)
    return manifest


def _file_record(path: Path, base: Path) -> dict[str, Any]:
    return {"path": path.relative_to(base).as_posix(),
            "size_bytes": path.stat().st_size, "sha256": _sha256_file(path)}
