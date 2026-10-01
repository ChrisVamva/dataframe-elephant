# Jupyter Research Notes (Baseline)

## Overview
Jupyter is the original Python notebook platform. All current notebooks in this repo are Jupyter-based.

## Porting Strategy
- Jupyter serves as baseline for all platforms
- All other platforms will be compared against Jupyter capabilities
- Known limitations tracked in blockers

## Current Environment
- Kernel: Python (pip packages from requirements.txt)
- Environment: `.venv` in repo root
- Widget system: ipywidgets (separate package)
- Static export: nbconvert to HTML
- Reactive: Limited to widgets callbacks

## Comparison Baseline Expectations
Plotly: ✓ Native, good quality
ipywidgets: ✓ Native, but callback-based
DuckDB: ✓ Native (duckdb package)
Reproducibility: ✓ (conda env export)
Authoring: ✓ (Git-friendly with nbstripout)
Deployment: ✓ (JupyterHub, MyBinder, cloud)

## Resource Inventory
- `notebooks/1/` and `notebooks/2/` – source notebooks (15 total)
- `src/viz_core.py` – shared visualization library
- `scripts/build_visualization_notebooks.py` – generator
- `scripts/wave2_notebook_specs.py` – wave 2 specs
- `data/` – DuckDB database files
- `requirements.txt` – Python dependencies

## Next Steps
1. Select 3 representative notebooks (simple, medium, complex)
2. Establish baseline performance metrics
3. Begin porting process to Observable
4. Document time/accuracy for each conversion

## Blockers Tracking
See `comparison/blockers.md`