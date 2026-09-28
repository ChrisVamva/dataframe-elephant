"""Headless execution tests for the notebooks in ``notebooks/``.

These notebooks are the deliverable of the visualization work, so the gate is
the same as the export gate: build them from
``scripts/build_visualization_notebooks.py``, execute every one against
``data/smarthome.duckdb`` in a real Jupyter kernel, and fail on any error
output. Also asserts the notebooks on disk match the generator, so a hand
edit cannot silently diverge from the claim ids the generator declares.

Run just these: .\\.venv\\Scripts\\python.exe -m pytest src/tests/test_viz_notebooks.py -q
"""
from __future__ import annotations

import sys
from pathlib import Path

import nbformat
import pytest

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK_DIR = ROOT / "notebooks"
sys.path.insert(0, str(ROOT / "scripts"))

import build_visualization_notebooks as builder  # noqa: E402

NOTEBOOK_NAMES = [spec["name"] for spec in builder.NOTEBOOK_SPECS]


def _requires_database() -> None:
    if not (ROOT / "data" / "smarthome.duckdb").exists():
        pytest.skip("data/smarthome.duckdb not present; run the Extraction 2 import")


def test_notebook_dir_exists() -> None:
    assert NOTEBOOK_DIR.is_dir(), NOTEBOOK_DIR


@pytest.mark.parametrize("name", NOTEBOOK_NAMES)
def test_notebook_is_on_disk(name: str) -> None:
    path = NOTEBOOK_DIR / f"{name}.ipynb"
    assert path.exists(), f"missing {path.name}; run scripts/build_visualization_notebooks.py"
    nb = nbformat.read(str(path), as_version=4)
    nbformat.validate(nb)
    assert nb.cells, f"{name} has no cells"


@pytest.mark.parametrize("name", NOTEBOOK_NAMES)
def test_notebook_matches_generator(name: str) -> None:
    """Committed notebooks must equal the generator output (--check gate)."""
    spec = next(s for s in builder.NOTEBOOK_SPECS if s["name"] == name)
    expected = nbformat.writes(
        builder._stamp_cell_ids(builder.build_notebook(**spec), name)
    )
    actual = (NOTEBOOK_DIR / f"{name}.ipynb").read_text(encoding="utf-8")
    assert actual == expected, (
        f"{name}.ipynb differs from scripts/build_visualization_notebooks.py; "
        "regenerate instead of editing the notebook by hand"
    )


@pytest.mark.parametrize("name", NOTEBOOK_NAMES)
def test_notebook_structure(name: str) -> None:
    """Every notebook carries the shared evidence contract, in order."""
    nb = nbformat.read(str(NOTEBOOK_DIR / f"{name}.ipynb"), as_version=4)
    headings = [
        "".join(cell.source) for cell in nb.cells
        if cell.cell_type == "markdown" and "".join(cell.source).startswith("## ")
    ]
    assert headings == [
        "## Provenance",
        "## Primary evidence",
        "## Supporting context",
        "## Uncertainty and gaps",
        "## Reproducibility",
    ], f"{name} headings: {headings}"


@pytest.mark.parametrize("name", NOTEBOOK_NAMES)
def test_notebook_executes_headless(name: str) -> None:
    _requires_database()
    import nbclient  # noqa: F401  (import asserts the execution stack is installed)
    from nbclient import NotebookClient

    path = NOTEBOOK_DIR / f"{name}.ipynb"
    nb = nbformat.read(str(path), as_version=4)
    client = NotebookClient(
        nb,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(NOTEBOOK_DIR)}},
        allow_errors=False,
    )
    executed = client.execute()
    assert executed.cells, f"{name} produced no executed cells"
    for cell in executed.cells:
        if cell.cell_type != "code":
            continue
        for output in cell.get("outputs", []):
            assert output.get("output_type") != "error", (
                f"{name} cell {cell.get('execution_count')} raised "
                f"{output.get('ename')}: {output.get('evalue')}"
            )
    # A notebook that ran but produced no figures is a silent failure.
    mime_types = {
        output.get("data", {}).get("application/vnd.plotly.v1+json") is not None
        for cell in executed.cells if cell.cell_type == "code"
        for output in cell.get("outputs", [])
    }
    assert any(mime_types), f"{name} produced no plotly figure output"


def test_generator_check_mode_passes() -> None:
    assert builder.main(["--check"]) == 0


def test_generator_declares_known_claims() -> None:
    """Every claim id the notebooks read must exist in the real database."""
    _requires_database()
    import viz_core as viz

    declared = {cid for spec in builder.NOTEBOOK_SPECS for cid in spec["claim_ids"]}
    assert declared, "no claim ids declared"
    con = viz.connect_db()
    try:
        found = {
            row[0] for row in con.execute(
                "SELECT local_id FROM stage2_claim WHERE local_id IN "
                f"({','.join('?' * len(declared))})", sorted(declared)
            ).fetchall()
        }
    finally:
        con.close()
    assert found == declared, f"unknown claim ids: {sorted(declared - found)}"
