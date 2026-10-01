# Research Agenda: Visualization Notebook Portability — Jupyter vs. Observable vs. Marimo vs. Quarto

## Research Question

Can the wave 1/2 notebooks (`notebooks/1/`, `notebooks/2/`) be losslessly ported to other reactive notebook platforms (Observable, Marimo, Quarto)?

## Scope

### In Scope
- Transpilation of 3 representative notebooks from this repo to each platform
- Runtime parity: Plotly → native chart rendering on each platform
- Interactivity preservation: ipywidgets → platform equivalents
- Reproducibility: environment capture and dependency locking per platform
- Authoring ergonomics for the research team

### Out of Scope
- Full corpus of 13 notebooks (3-5 representative samples only)
- Performance benchmarking (runtime, memory)
- Security/review of external platforms

## Representative Notebook Selection Criteria

Select 3 notebooks that exercise the most diverse features:
1. **Simple**: Single Plotly figure + data fetch (e.g., `00_index.ipynb`)
2. **Medium**: Multiple chart types + interactive widgets (e.g., `01_matter_version_timeline.ipynb`)
3. **Complex**: Multi-panel dashboard with provenance rendering (e.g., `03_offline_failure_and_cloud_dependency.ipynb`)

## Evaluation Matrix

| Dimension | Metric | Jupyter | Observable | Marimo | Quarto |
|-----------|--------|---------|------------|--------|--------|
| Runtime parity | Native chart rendering | baseline | TBD | TBD | TBD |
| Interactivity | Widget equivalent support | baseline | TBD | TBD | TBD |
| Reproducibility | Environment capture quality | baseline | TBD | TBD | TBD |
| Authoring ergonomics | Team usability score | baseline | TBD | TBD | TBD |
| Deployment | Static HTML / server / cloud | baseline | TBD | TBD | TBD |
| Version control | Git-friendly workflow | baseline | TBD | TBD | TBD |

## Deliverables

1. **Porting Guide**: Step-by-step instructions for each platform
2. **Platform Recommendation**: Evidence-backed decision with tradeoffs
3. **Updated AGENTS.md**: Any changes to repo conventions based on findings

## References

- Existing: `NEW_Brainstorming.md` item #8 (original research idea)
- `src/viz_core.py` (shared viz library)
- `scripts/build_visualization_notebooks.py` (generator)
- `scripts/wave2_notebook_specs.py` (wave 2 specs)