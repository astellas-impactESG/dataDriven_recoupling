# Replication Package for "Data-Driven Re-Coupling: An Embedded Case Study of Astellas Pharma's Journey to Substantive Legitimacy"

**Authors:** Daisuke Kato, Takehiro Metoki, Keigo Tanabe, Yohsuke Hagiwara, Shintaro Omuro, Shingo Iino  
**Affiliations:** Astellas Pharma Inc. (Sustainability; Digital X); Waseda University, Graduate School of Accountancy

---

## Overview

This repository contains the replication code for the macro-level quantitative analysis reported in the paper. The analysis identifies non-financial indicators (NFIs) statistically and causally linked to market capitalization using a panel dataset of 1,694 TSE Prime Market firms (2013–2023).

The empirical pipeline consists of three stages:

1. **SHAP-based contribution analysis** — XGBoost model with hyperparameter tuning and out-of-sample SHAP values (Step 1 of the paper)
2. **ICE simulation** — Individual Conditional Expectation curves anchored to Astellas' 2023 profile (Step 2 of the paper)
3. **Fixed-effects causal analysis** — Two-way fixed effects panel regression with industry-clustered standard errors (Step 1 of the paper)

---

## Repository Structure

```
.
├── README.md
├── LICENSE
├── requirements.txt          # Python dependencies
├── requirements_R.txt        # R dependencies
├── code/
│   ├── 1_shap_analysis.py    # XGBoost + SHAP (contribution & predictive analysis)
│   ├── 2_ice_simulation.py   # ICE curve simulation for a focal firm
│   └── 3_fixed_effects.R     # Fixed-effects panel regression + AME estimation
└── data/
    └── README_data.md        # Data documentation (see Data Availability)
```

---

## Data Availability

The empirical analysis uses the **TERRAST** dataset (Tokyo Stock Exchange Prime Market, 2013–2023), a proprietary ESG data platform that aggregates publicly available corporate disclosures via AI and big data technologies.

**The raw data cannot be redistributed** due to the data provider's terms of service. Researchers wishing to replicate the analysis should contact TERRAST directly to obtain access.

To run the code, place the licensed dataset in the data folder.

---

## Software Requirements

### Python (scripts 1–2)

Tested on Python 3.13.12. Install dependencies:

```bash
pip install -r requirements.txt
```

| Package | Version |
|---|---|
| matplotlib | 3.10.8 |
| matplotlib-inline | 0.2.1 |
| numpy | 2.3.5 |
| pandas | 3.0.0 |
| scikit-learn | 1.8.0 |
| shap | 0.50.0 |
| xgboost | 3.2.0 |

### R (script 3)

Tested on R 4.4.2. See `requirements_R.txt` for the full dependency list. Install dependencies manually:

```r
install.packages(c("tidyverse", "conflicted", "fixest", "marginaleffects"))
```

| Package | Version |
|---|---|
| conflicted | 1.2.0 |
| fixest | 0.12.1 |
| marginaleffects | 0.28.0 |
| tidyverse | 2.0.0 |

---

## How to Reproduce

Run scripts in order from the `code/` directory. Each script expects the data file at `../data/toshoPrime_2013-2023_en.csv` relative to the script location.

### Step 1: SHAP Contribution Analysis

```bash
cd code
python 1_shap_analysis.py
```

**Output:** `results/shap_summary.png` — reproduces **Figure 2** in the paper.

### Step 2: ICE Simulation

```bash
python 2_ice_simulation.py
```

**Output:** `figure/ice/Pct Female Managers.png` — reproduces **Figure 7** in the paper.

To generate ICE curves for other variables, change `VARIABLE` and `VARIABLE_LAB` at the top of the script.

### Step 3: Fixed-Effects Regression

```r
# In R, from the project root
source("code/3_fixed_effects.R")
```

**Output:** Coefficient bar chart — reproduces **Figure 3** in the paper.

Before running, set `vec_X` (human capital indicators) and `vec_G` (governance indicators) to match the column names in your licensed dataset, and set the `datagrid` argument for `totalAssets` to the appropriate firm-level value.

---

## Correspondence

For questions about this replication package, please open a GitHub Issue.  
For questions about the paper itself, please contact the corresponding authors via SSRN.

---

## License

This replication code is released under the **Apache License 2.0**. See [`LICENSE`](LICENSE) for details.

The TERRAST dataset is proprietary and is **not** covered by this license.
