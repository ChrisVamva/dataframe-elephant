"""Repository health check: verify databases, schemas, and test suite status."""
import sys
import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def check_database(db_path: str, expected_tables: set[str]) -> bool:
    """Check that a database exists and contains the expected tables."""
    path = ROOT / db_path
    if not path.exists():
        print(f"FAIL: {db_path} not found")
        return False
    con = duckdb.connect(str(path), read_only=True)
    try:
        tables = {row[0] for row in con.execute(
            "SELECT table_name FROM information_schema.tables"
        ).fetchall()}
        missing = expected_tables - tables
        if missing:
            print(f"WARN: {db_path} missing tables: {missing}")
            return False
        print(f"OK: {db_path} has all expected tables")
        return True
    finally:
        con.close()

def main() -> bool:
    """Run all checks and return True only if every check passed."""
    results: list[bool] = []
    print("=== Repository Health Check ===\n")

    # Check databases (citations.duckdb uses the singular names defined in
    # schemas/citations.sql: claim, source, claim_source -- no metrics table).
    print("Databases:")
    results.append(check_database("data/citations.duckdb", {"claim", "source", "claim_source"}))
    results.append(check_database("data/smarthome.duckdb", {"stage2_claim", "metric", "entity"}))
    results.append(check_database("data/stage2.duckdb", {"stage2_claim"}))
    results.append(check_database("data/AutomationResearch.duckdb", {"stage2_claim"}))

    # Check schemas
    print("\nSchemas:")
    for schema in ["schemas/citations.sql", "schemas/stage2.sql"]:
        if (ROOT / schema).exists():
            print(f"OK: {schema}")
        else:
            print(f"FAIL: {schema} not found")
            results.append(False)

    # Check AGENTS.md
    print("\nDocumentation:")
    if (ROOT / "AGENTS.md").exists():
        print("OK: AGENTS.md")
    else:
        print("FAIL: AGENTS.md not found")
        results.append(False)

    print("\n=== Health Check Complete ===")
    return all(results)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
