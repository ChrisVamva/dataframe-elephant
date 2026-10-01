# Cross-Platform Comparison Matrix Template

## Notebook-by-Notebook Comparison

For each representative notebook, track portability across all four platforms.

### Notebook: [Name] (`notebooks/1/XX_*.ipynb`)

| Aspect | Jupyter (baseline) | Observable | Marimo | Quarto |
|--------|-------------------|------------|--------|--------|
| **Data Loading** | | | | |
| DuckDB connection | ✓ native | | | |
| Parquet/CSV reads | ✓ native | | | |
| **Visualization** | | | | |
| Plotly figures | ✓ native | | | |
| Altair charts | ✓ native | | | |
| Custom JS rendering | ✓ | | | |
| **Interactivity** | | | | |
| ipywidgets (dropdowns, sliders) | ✓ native | | | |
| Reactive state | ✓ (via widgets) | | | |
| Cross-cell reactivity | ✗ | | | |
| **Provenance Rendering** | | | | |
| `render_provenance_panel` | ✓ | | | |
| `render_evidence_cards` | ✓ | | | |
| **Reproducibility** | | | | |
| Environment capture | `pip freeze` / `conda env export` | | | |
| Dependency locking | `requirements.txt` | | | |
| **Authoring** | | | | |
| Cell editing | ✓ | | | |
| Version control | ✓ (nbstripout) | | | |
| Collaboration | ✗ | | | |
| **Deployment** | | | | |
| Static HTML export | ✓ (nbconvert) | | | |
| Server deployment | JupyterHub | | | |
| Cloud hosting | ✓ | | | |

### Notebook: [Name] (`notebooks/2/XX_*.ipynb`)

Same structure as above.

### Notebook: [Name] (`notebooks/2/XX_*.ipynb`)

Same structure as above.

## Aggregate Scoring

| Dimension | Weight | Observable | Marimo | Quarto |
|-----------|--------|------------|--------|--------|
| Runtime parity | 30% | | | |
| Interactivity preservation | 25% | | | |
| Reproducibility | 20% | | | |
| Authoring ergonomics | 15% | | | |
| Deployment flexibility | 10% | | | |
| **Weighted Score** | 100% | | | |

## Decision Thresholds

- **≥ 85%**: Adopt as primary platform
- **70–84%**: Adopt for specific use cases (e.g., sharing, dashboards)
- **< 70%**: Keep Jupyter; use platform only for specific outputs

## Notes

- Scores are subjective; calibrate with team on 3+ reviewers
- Document specific blockers per platform in `blockers.md`