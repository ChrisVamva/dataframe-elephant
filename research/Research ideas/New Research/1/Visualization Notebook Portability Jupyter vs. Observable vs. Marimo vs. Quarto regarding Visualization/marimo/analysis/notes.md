# Marimo Research Notes

## Overview
Marimo (marimo.io) is a reactive, Python-based notebook platform built in Rust. Key differences from Jupyter:
- Compiled to WebAssembly (Rust) for runtime performance
- Reactive reactivity: changes in one cell auto-re-run dependent cells
- Python UI widgets via `marimo.ui` (replaces ipywidgets)
- Built for production deployment (single-file `.py` format)

## Porting Considerations

### Plotly → Marimo
- Plotly via `marimo` integrates directly with Plotly.js
- Better performance than Jupyter's Plotly
- Reactive reactivity may cause auto-re-runs; need careful dependency tracking

### ipywidgets → Marimo
- Marimo has native `marimo.ui` widgets (buttons, sliders, text inputs)
- Reactive by default: select dropdown → auto-updates downstream cells
- No separate widget callbacks; declarative UI/state binding

### DuckDB → Marimo
- Marimo supports Python packages; DuckDB available via pip
- WASM version may have performance implications
- Environment setup requires additional dependencies (duckdb-wasm)

### Environment/Reproducibility
- Single `.py` file captures notebook
- Dependency management: `requirements.txt` still used
- Version pinning critical for reproducible builds
- Lockfile format: `poetry.lock` or `requirements.txt.lock`

### Deployment
- Single `.py` file for easy sharing
- Git-friendly (pure Python)
- Can export to static HTML, run via server, or cloud hosting
- Docker support built-in

## Resources
- Marimo docs: https://docs.marimo.io/
- Marimo UI: https://docs.marimo.io/api/ui/
- Marimo export: https://docs.marimo.io/api/export/

## Next Steps
1. Install Marimo locally
2. Port one simple notebook to test reactive reactivity
3. Port one medium notebook with UI widgets
4. Document auto-re-run behaviors and workarounds

## Blockers Tracking
See `comparison/blockers.md`