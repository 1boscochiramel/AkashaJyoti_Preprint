# Manifest

This manifest describes the contents of the repository associated with the high‑altitude balloon (HAB) profiling case study.  Each file is listed with its path and a brief description of its purpose.

## Top‑level

| Path | Description |
|---|---|
| `README.md` | Overview of the repository structure, reproduction instructions, and data/code availability statements. |
| `MANIFEST.md` | This manifest. |
| `requirements.txt` | Python packages required to execute the notebook. |
| `CITATION.cff` | Citation metadata for the GitHub repository. |
| `.zenodo.json` | Metadata for the Zenodo archive (title, authors, description, and keywords). |

## `paper/`

| Path | Description |
|---|---|
| `paper/main.tex` | LaTeX manuscript describing the study.  Compiles in a blank Overleaf project. |
| `paper/figures/Fig01_su202_proxy_vs_alt.png` | Relative SU‑202 intensity proxy vs altitude. |
| `paper/figures/Fig02_qc_rejections.png` | Quality control rejections and retained bins. |
| `paper/figures/Fig06_sensor_sanity.png` | Sensor sanity diagnostics (proxy vs temperature/time). |
| `paper/figures/Fig09_saturation_floor_detection.png` | Saturation, floor and plateau detection. |
| `paper/figures/Fig10_tau_segment_consistency.png` | Segment‑consistency check for the optical depth proxy. |

## `notebooks/`

| Path | Description |
|---|---|
| `notebooks/EarthArXiv_final_clean2_run_2025-10-05.ipynb` | Jupyter notebook containing the analysis.  Generates the run summary and figures. |

## `reports/`

| Path | Description |
|---|---|
| `reports/eartharxiv_clean2_new_run_fixed.html` | Executed HTML report of the analysis notebook.  Records run settings and printed metrics. |

## `data/processed/`

| Path | Description |
|---|---|
| `data/processed/datalog_cleaned_with_altitude.csv` | Processed HAB dataset containing pressure, temperature, humidity, proxy intensity and altitude. |
| `data/processed/Satellite_data_extracted.csv` | Satellite aerosol data used for comparison (if applicable). |
| `data/processed/Satellite_data_extracted2.csv` | Additional satellite data (if applicable). |
| `data/processed/AOD_Stat.csv` | Pre‑computed statistics for satellite aerosol optical depth. |

## `docs/specs/`

| Path | Description |
|---|---|
| `docs/specs/SU-200-spec-sheet (3).pdf` | Manufacturer specification sheet for the SU‑200 radiometer. |
| `docs/specs/SU-202-205 (1).pdf` | Manufacturer manual/specification for the SU‑202/205 radiometers. |
| `docs/specs/TR SU200 SS 1252 (1).pdf` | Additional SU‑200 sensor documentation. |
| `docs/specs/BME280_Datasheet-1 (6).pdf` | Datasheet for the Bosch BME280 environmental sensor. |

### Optional files

If present, additional files (e.g., `SHA256SUMS.txt`) provide checksums for verifying file integrity.  These are not required for reproduction but can be useful for verification.