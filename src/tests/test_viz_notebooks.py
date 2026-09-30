"""Headless execution tests for the notebooks in ``notebooks/<wave>/``.

These notebooks are the deliverable of the visualization work, so the gate is
the same as the export gate: build them from
``scripts/build_visualization_notebooks.py``, execute every one against
``data/smarthome.duckdb`` in a real Jupyter kernel, and fail on any error
output. Also asserts three things about provenance that a hand edit could
otherwise break:

* the notebooks on disk match the generator cell for cell, so a hand edit
  cannot silently diverge from the claim ids the generator declares;
* every claim id a spec declares exists in the database;
* every ``M###`` id mentioned anywhere in a notebook (code or prose) exists in
  the metric table.

Run just these:
    .\\.venv\\Scripts\\python.exe -m pytest src/tests/test_viz_notebooks.py -q
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import nbformat
import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import build_visualization_notebooks as builder  # noqa: E402

WAVES = builder.WAVES
CASES = [
    (wave, spec["name"], spec)
    for wave in WAVES
    for spec in builder.wave_specs(wave)
]
CASE_IDS = [f"wave{wave}-{name}" for wave, name, _spec in CASES]

HEADINGS = [
    "## Provenance",
    "## Primary evidence",
    "## Supporting context",
    "## Uncertainty and gaps",
    "## Reproducibility",
]

# Local ids as they appear in the corpus: M001 for metrics.
METRIC_ID_RE = re.compile(r"\bM\d{3}\b")


def _notebook_path(wave: str, name: str) -> Path:
    return builder.notebook_dir(wave) / f"{name}.ipynb"


def _requires_database() -> None:
    if not (ROOT / "data" / "smarthome.duckdb").exists():
        pytest.skip("data/smarthome.duckdb not present; run the Extraction 2 import")


def _existing_local_ids(table: str, ids: list[str]) -> set[str]:
    import viz_core as viz

    if not ids:
        return set()
    con = viz.connect_db()
    try:
        return {
            row[0] for row in con.execute(
                f"SELECT local_id FROM {table} WHERE local_id IN "
                f"({','.join('?' * len(ids))})", sorted(ids)
            ).fetchall()
        }
    finally:
        con.close()



@pytest.mark.parametrize("wave", WAVES)
def test_notebook_dir_exists(wave: str) -> None:
    directory = builder.notebook_dir(wave)
    assert directory.is_dir(), directory


@pytest.mark.parametrize("wave,name,spec", CASES, ids=CASE_IDS)
def test_notebook_is_on_disk(wave: str, name: str, spec: dict) -> None:
    path = _notebook_path(wave, name)
    assert path.exists(), f"missing {path.name}; run scripts/build_visualization_notebooks.py"
    nb = nbformat.read(str(path), as_version=4)
    nbformat.validate(nb)
    assert nb.cells, f"{name} has no cells"


@pytest.mark.parametrize("wave,name,spec", CASES, ids=CASE_IDS)
def test_notebook_matches_generator(wave: str, name: str, spec: dict) -> None:
    """Committed notebooks must equal the generator output (--check gate)."""
    expected = nbformat.writes(
        builder.stamp_cell_ids(builder.build_notebook(**spec), name)
    )
    actual = _notebook_path(wave, name).read_text(encoding="utf-8")
    assert actual == expected, (
        f"notebooks/{wave}/{name}.ipynb differs from "
        "scripts/build_visualization_notebooks.py; regenerate instead of "
        "editing the notebook by hand"
    )


@pytest.mark.parametrize("wave,name,spec", CASES, ids=CASE_IDS)
def test_notebook_structure(wave: str, name: str, spec: dict) -> None:
    """Every notebook carries the shared evidence contract, in order."""
    nb = nbformat.read(str(_notebook_path(wave, name)), as_version=4)
    headings = [
        "".join(cell.source) for cell in nb.cells
        if cell.cell_type == "markdown" and "".join(cell.source).startswith("## ")
    ]
    assert headings == HEADINGS, f"{name} headings: {headings}"


@pytest.mark.parametrize("wave,name,spec", CASES, ids=CASE_IDS)
def test_notebook_executes_headless(wave: str, name: str, spec: dict) -> None:
    _requires_database()
    import nbclient  # noqa: F401  (import asserts the execution stack is installed)
    from nbclient import NotebookClient

    path = _notebook_path(wave, name)
    nb = nbformat.read(str(path), as_version=4)
    client = NotebookClient(
        nb,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
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


@pytest.mark.parametrize("wave", WAVES)
def test_generator_check_mode_passes_per_wave(wave: str) -> None:
    assert builder.main(["--check", "--wave", wave]) == 0


@pytest.mark.parametrize("wave", WAVES)
def test_generator_declares_known_claims(wave: str) -> None:
    """Every claim id the notebooks read must exist in the real database."""
    _requires_database()
    declared = {cid for spec in builder.wave_specs(wave) for cid in spec["claim_ids"]}
    assert declared, f"no claim ids declared for wave {wave}"
    assert _existing_local_ids("stage2_claim", sorted(declared)) == declared, (
        f"wave {wave} unknown claim ids: "
        f"{sorted(declared - _existing_local_ids('stage2_claim', sorted(declared)))}"
    )


@pytest.mark.parametrize("wave,name,spec", CASES, ids=CASE_IDS)
def test_referenced_metric_ids_exist(wave: str, name: str, spec: dict) -> None:
    """Every ``M###`` mentioned in a notebook must exist in the metric table.

    The generator declares claim ids, but metric ids live inside the code and
    prose of each spec, where a typo would otherwise only surface as an empty
    dataframe at run time.
    """
    _requires_database()
    nb = nbformat.read(str(_notebook_path(wave, name)), as_version=4)
    referenced = set(METRIC_ID_RE.findall(
        "\n".join(cell.source for cell in nb.cells)
    ))
    if not referenced:
        pytest.skip(f"{name} references no metric ids")
    found = _existing_local_ids("metric", sorted(referenced))
    assert found == referenced, (
        f"{name}: unknown metric ids {sorted(referenced - found)}"
    )
