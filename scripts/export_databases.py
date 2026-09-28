"""CLI: export production DuckDBs into timestamped CSV + Parquet bundles.

Defaults: data/citations.duckdb + data/stage2.duckdb + data/smarthome.duckdb -> data/exports/export_<ts>/.
Sources are opened read-only and left unchanged; bundles carry EXPORT DATABASE
output plus read-only view snapshots, README, and manifest.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.db_export_core import export_all  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Export production DuckDBs (CSV + Parquet).")
    parser.add_argument("--export-root", type=Path, default=PROJECT_ROOT / "data" / "exports")
    parser.add_argument("--which", choices=("all", "citations", "stage2", "smarthome"), default="all")
    parser.add_argument("--formats", default="csv,parquet")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--no-verify", action="store_true")
    parser.add_argument("--timestamp", default=None)
    args = parser.parse_args()
    formats = tuple(f.strip() for f in args.formats.split(",") if f.strip())
    result = export_all(args.export_root, args.which, formats,
                        overwrite=args.overwrite, verify=not args.no_verify,
                        timestamp=args.timestamp)
    print(f"[SUCCESS] Export {result['run_dir']}: "
          f"{sorted(result['databases'])} formats={result['formats']} -> {result['run_dir']}")
    print(json.dumps({k: v for k, v in result.items() if k != "files"}, indent=2))


if __name__ == "__main__":
    main()
