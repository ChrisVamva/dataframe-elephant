# Observable Research Notes

## Overview
Observable (observablehq.com) is a reactive, JavaScript/TypeScript notebook platform built on Observable Framework. Key differences from Jupyter:
- Reactive execution model (cells re-run on dependency change)
- Native JavaScript + TypeScript (not Python)
- Built-in plotting: Observable Plot, D3 integration
- Cloud-hosted with GitHub sync

## Porting Considerations

### Plotly → Observable
- Observable Plot is declarative grammar (like ggplot2/Altair)
- Plotly figures require translation; no direct port
- Strategy: Re-implement charts in Observable Plot or use iframe embedding

### ipywidgets → Observable
- Observable has `Inputs` namespace for reactive UI
- Dropdowns, sliders, checkboxes map directly
- Cross-cell reactivity is native (vs. widgets callback model)

### DuckDB → Observable
- Observable Framework supports DuckDB via WASM
- SQL cells available in Observable Framework
- Data loading patterns differ (file attachments, fetch, SQL)

### Environment/Reproducibility
- No Python environment; dependency management via npm
- Lockfiles: `package-lock.json`
- Version pinning for Observable Framework and plot libraries

### Deployment
- Observable Cloud (hosted)
- Observable Framework → static site (GitHub Pages, Netlify, Vercel)
- Framework notebooks are `.md`/`.js` files, git-friendly

## Resources
- Observable Framework docs: https://observablehq.com/framework/
- Observable Plot: https://observablehq.com/plot/
- DuckDB WASM: https://observablehq.com/@observablehq/duckdb
- Inputs: https://observablehq.com/@observablehq/inputs

## Next Steps
1. Set up Observable Framework locally
2. Port one simple notebook (index) to test data flow
3. Port one medium notebook for interactivity
4. Document blockers in `blockers.md`

## Blockers Tracking
See `comparison/blockers.md`