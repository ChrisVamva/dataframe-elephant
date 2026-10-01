# Quarto Research Notes

## Overview
Quarto (quarto.org) is a publishing system that executes notebooks (Jupyter, Python, R, Julia) and renders to multiple output formats. Key differences from Jupyter:
- Not a notebook runtime; uses Jupyter kernels for execution
- Input: `.qmd` (Quarto Markdown) or `.ipynb` files
- Output: HTML, PDF, DOCX, RevealJS, websites, books, blogs
- Embedding in existing repos: additive (doesn't replace Jupyter)

## Porting Considerations

### Plotly → Quarto
- Uses Jupyter kernel → Plotly renders identically
- HTML output preserves Plotly interactivity
- PDF output: static images (kaleido)
- No translation needed; same figures

### ipywidgets → Quarto
- In HTML output: ipywidgets work if `widgets` extension enabled
- In static outputs (PDF): widgets become static (frozen at execution time)
- Shiny for Python can add reactivity to published HTML

### DuckDB → Quarto
- Uses Jupyter kernel → DuckDB connection identical
- No changes needed for data loading

### Environment/Reproducibility
- Uses same Python environment as Jupyter
- Dependency locking: same `requirements.txt`
- Quarto itself version-pinned: `quarto --version`
- Can use `renv`/`conda`/`venv` for full reproducibility

### Deployment
- Static site generation (GitHub Pages, Netlify, Vercel)
- Quarto websites/books/blogs for narrative outputs
- Can embed in existing documentation
- PDF/LaTeX output for formal reports

## Resources
- Quarto docs: https://quarto.org/docs/
- Quarto Jupyter integration: https://quarto.org/docs/jupyter/
- Publishing: https://quarto.org/docs/publishing/
- Shiny for Python: https://shiny.posit.co/py/

## Next Steps
1. Install Quarto CLI
2. Convert 1-2 notebooks to `.qmd` with `quarto convert`
3. Test HTML + PDF output quality
4. Test widget interactivity in HTML output
5. Document workflow for team

## Blockers Tracking
See `comparison/blockers.md`