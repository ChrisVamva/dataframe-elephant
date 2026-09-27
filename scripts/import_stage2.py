"""CLI: import research/raw/Stage 2/ into a typed DuckDB database.

Implements Protocols/FromStagetoDatabases.md (Option A: dedicated database,
default data/stage2.duckdb; citations.duckdb is never touched).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.stage2_import_core import Stage2ImportError, build_stage2_database  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Import Stage 2 extraction files into DuckDB.")
    parser.add_argument("--stage2-dir", type=Path,
                        default=PROJECT_ROOT / "research" / "raw" / "Stage 2")
    parser.add_argument("--database", type=Path,
                        default=PROJECT_ROOT / "data" / "stage2.duckdb")
    parser.add_argument("--warnings", type=Path,
                        default=PROJECT_ROOT / "data" / "stage2_ingestion_warnings.jsonl")
    parser.add_argument("--schema", type=Path,
                        default=PROJECT_ROOT / "schemas" / "stage2.sql")
    args = parser.parse_args()
    try:
        result = build_stage2_database(args.stage2_dir, args.database, args.warnings, args.schema)
    except Stage2ImportError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)
    print(f"[SUCCESS] Stage 2 import: {result['entities']} entities, {result['metrics']} metrics, "
          f"{result['claims']} claims, {result['decisions']} decisions, "
          f"{result['warnings']} warnings -> {result['database_path']}")


if __name__ == "__main__":
    main()
