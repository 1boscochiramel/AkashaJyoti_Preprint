# Applied Energy: Simulation-first decision framework

Simulation-first decision framework for fast-fill thermal throttling in adsorptive hydrogen storage with PCM buffering.

## Repository structure

```
.
├── notebooks/
│   ├── AE_Models.ipynb
│   ├── AE_Validation.ipynb
│   ├── AE_Sweeps.ipynb
│   └── AE_Figures_Tables.ipynb
├── src/
│   ├── __init__.py
│   ├── paths.py
├── scripts/
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── cache/
├── tests/
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── .editorconfig
```

## Setup (local)

Recommended Python version: 3.10+

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How outputs are handled

All generated outputs are saved to the `outputs/` directory:
- `outputs/figures`: Generated plots.
- `outputs/tables`: Generated data tables.
- `outputs/cache`: Intermediate results.

These directories are ignored by git (except for `.gitkeep` files) to ensure reproducibility and keep the repository clean.

## How to run notebooks

### Manual Execution
Open the notebooks in `notebooks/` using Jupyter Lab or Jupyter Notebook and run the cells. Each notebook initializes the environment and ensures paths are correct.

### Headless Execution
Headless execution will be added in Task 2.

### Colab Instructions (Optional)
To run in Google Colab:
1. Clone the repository:
   ```python
   !git clone <repo_url>
   ```
2. Navigate to the repository:
   ```python
   %cd <repo_name>
   ```
3. Open the desired notebook from `notebooks/` and run.

The project uses repo-relative paths managed by `src/paths.py` and is designed to work identically in local and Colab environments.

## Reproducibility policy

Deterministic seeds and CI smoke runs will be implemented in later tasks to ensure robust reproducibility.
