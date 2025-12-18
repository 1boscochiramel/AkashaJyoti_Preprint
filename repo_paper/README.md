## Research Artifact for MDPI Atmosphere Submission

This repository contains all artefacts necessary to reproduce the results presented in our UTLS high‑altitude balloon case study.  The high‑altitude balloon (HAB) dataset is treated as the primary observation, and satellite products are used strictly as comparison data.  A detailed methods description and run‑summary are contained in the manuscript `paper/main.tex`.

### Contents

```
repo_paper/
├── paper/
│   ├── main.tex           # LaTeX manuscript (compiles in a blank Overleaf project)
│   └── figures/           # PNG figures referenced in the manuscript
├── notebooks/
│   └── EarthArXiv_final_clean2_run_2025-10-05.ipynb  # Canonical Jupyter notebook used to generate the HTML report
├── reports/
│   └── eartharxiv_clean2_new_run_fixed.html          # Executed HTML run report (evidence of all printed metrics)
├── data/
│   └── processed/
│       ├── datalog_cleaned_with_altitude.csv         # Primary HAB dataset (processed)
│       ├── Satellite_data_extracted.csv              # Satellite comparison data (used in notebook)
│       ├── Satellite_data_extracted2.csv             # Additional satellite comparison data (used in notebook)
│       └── AOD_Stat.csv                              # Summary statistics for satellite AOD (used in notebook)
└── docs/
    └── specs/                                        # Manufacturer documentation for sensors used in Table 1
        ├── SU-200-spec-sheet (3).pdf
        ├── SU-202-205 (1).pdf
        ├── BME280_Datasheet-1 (6).pdf
        └── TR SU200 SS 1252 (1).pdf
```

### How to reproduce

1. **Install dependencies** – create a new environment and install the packages listed in `requirements.txt` (or use the notebook’s own metadata if available).
2. **Execute the notebook** – open `notebooks/EarthArXiv_final_clean2_run_2025-10-05.ipynb` and run all cells to reproduce the HTML report.  The HTML report in `reports/` is provided for reference and verification.
3. **Compile the manuscript** – navigate to `paper/` and compile `main.tex` using any standard LaTeX engine.  The manuscript is intentionally written to compile without MDPI‑specific macros.
4. **Check data integrity** – optional: verify SHA256 checksums listed in `SHA256SUMS.txt` to ensure no file corruption occurred during transfer.

### Data & Code availability

All processed data, the executed HTML report, and the canonical Jupyter notebook are archived in this repository.  Satellite data are included for comparison only and originate from the sources listed in the methods section of the manuscript.  No proprietary software is required to reproduce the analysis.
