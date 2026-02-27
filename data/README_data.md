# Data Documentation

## Source

**Dataset:** TERRAST (proprietary ESG data platform)  
**Coverage:** TSE Prime Market listed firms, 2013–2023  
**Observations:** 18,634 firm-year observations across 1,694 unique firms  
**Access:** Contact the TERRAST data provider directly. Raw data cannot be redistributed.

Place the licensed CSV file at:

```
data/toshoPrime_2013-2023_en.csv
```

---

## Variable Dictionary

### Identifiers

| Variable | Type | Description |
|---|---|---|
| `shokenCode` | int | Securities code (firm identifier) |
| `firmName` | str | Firm name (Japanese) |
| `year` | int | Fiscal year |
| `firm_fac` | category | Firm fixed-effect factor (same as shokenCode) |
| `industryCat` | int | Industry code (numeric) |
| `ind_DaiBunrui_en` | str | Industry classification (major category, English) |
| `ind_ChuBunrui_en` | str | Industry classification (sub-category, English) |
| `industryCat_en` | str | Industry label (English) |

### Dependent Variable

| Variable | Unit | Description |
|---|---|---|
| `mktCap` | million JPY | Market capitalization |
| `ln_mktCap` | log(million JPY) | Log-transformed market capitalization (used in regression) |
| `L1_ln_mktCap` | log(million JPY) | Lagged log market capitalization |

### Financial Controls

| Variable | Unit | Description |
|---|---|---|
| `totalAssets` | million JPY | Total assets |
| `n_employees` | persons | Number of employees |
| `gm_pct` | % | Gross profit margin |
| `annGrowthRate_pct` | % | Annual sales growth rate |
| `levRatio` | ratio | Leverage ratio (D/E) |
| `pbr` | ratio | Price-to-book ratio |
| `per` | ratio | Price-to-earnings ratio |
| `roe` | % | Return on equity |
| `ebitda` | million JPY | EBITDA |
| `roic` | % | Return on invested capital |
| `roa` | % | Return on assets |

### Human Capital Indicators (22 variables, selected examples)

| Variable | Unit | Description |
|---|---|---|
| `pct_femaleMger` | % | Percentage of female managers |
| `n_femaleMnger` | persons | Number of female managers (raw count; excluded from models) |
| `pct_mgmt` | % | Management position ratio (n_mgmtPosition / n_employees) |
| `n_mgmtPosition` | persons | Number of management positions |
| `employeeJobSatisfaction` | score | Employee job satisfaction score |
| `employeeEvalMgmt` | score | Employee evaluation of corporate management |

### Corporate Governance Indicators (24 variables, selected examples)

| Variable | Unit | Description |
|---|---|---|
| `avgRemunerationDirectors` | million JPY | Average remuneration paid to directors |
| `nDirectors` | persons | Number of directors on the board |
| `nNonExecDirectors` | persons | Number of non-executive directors |
| `avgAgeDirectors` | years | Average age of directors |

---

## Notes on Data Transformation

- `mktCap_1b` = `mktCap / 1000` (rescaled to billions JPY; used in ML scripts)
- `ln_mktCap` = `log(mktCap_1b)` (log-transformed; used in regression and SHAP script)
- `pct_mgmt` = `n_mgmtPosition / n_employees` (derived variable; computed in scripts)
- Financial ratios (`pbr`, `per`, `roe`, `ebitda`, `roic`, `roa`) are dropped from ML feature matrices to avoid leakage of market-derived information

---

## Excluded Variables

The following variables are dropped before model fitting (see `DROP_COLS` / `drop_cols` in the Python scripts):

`mktCap_1b`, `mktCap`, `ln_mktCap`, `L1_ln_mktCap`, `pbr`, `per`, `roe`, `ebitda`, `roic`, `roa`, `firm_fac`, `shokenCode`, `firmName`, `n_femaleMnger`, `industryCat`, `ind_DaiBunrui_en`, `ind_ChuBunrui_en`, `industryCat_en`
