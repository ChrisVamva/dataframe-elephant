# Visualization Notebook Portability Research

This directory contains research on the portability of visualization notebooks across Jupyter, Observable, Marimo, and Quarto platforms, focusing on:

- **Core Problem**: Can the wave 1/2 notebooks (`notebooks/1/`, `notebooks/2/`) from this repo be losslessly ported to other reactive notebook platforms?
- **Evaluation Criteria**:
  - Runtime parity (Plotly → native charts)
  - Interactivity preservation (ipywidgets → platform equivalents)
  - Reproducibility (environment capture, dependency locking)
  - Authoring ergonomics for the research team

## Directory Structure

```
.
├── README.md                  ← This overview
├── jupyter/                   ← Jupyter notebook research
│   ├── notebooks/             ← Exported/transpiled Jupyter notebooks
│   └── analysis/              ← Portability analysis notes
├── observable/                ← Observable notebook research
│   ├── notebooks/             ← Observable notebook implementations
│   └── analysis/              ← Portability analysis notes
├── marimo/                    ← Marimo notebook research
│   ├── notebooks/             ← Marimo notebook implementations
│   └── analysis/              ← Portability analysis notes
├── quarto/                    ← Quarto notebook research
│   ├── notebooks/             ← Quarto notebook implementations
│   └── analysis/              ← Portability analysis notes
├── comparison/                ← Cross-platform comparison matrices
│   ├── runtime/
│   ├── interactivity/
│   ├── reproducibility/
│   └── authoring/
├── sources/                   ← Collected research sources
│   ├── academic/
│   ├── documentation/
│   └── tools/
└── research_agenda.md         ← Structured research plan (see template below)
```

## Research Approach

1. **Baseline**: Current notebooks in `notebooks/1/` and `notebooks/2/` (Jupyter-based)
2. **Porting**: Transpile 3-5 representative notebooks to each target platform
3. **Evaluation**: Systematic comparison using the criteria above
4. **Deliverable**: Porting guide + platform recommendation

## Related Research

This research builds upon:
- `notebooks/` directory - Generated visualization notebooks
- `viz_core.py` - Shared visualization library
- `build_visualization_notebooks.py` - Notebook generation pipeline
- Wave 2 notebook specs (`wave2_notebook_specs.py`)

Last updated: $(date)