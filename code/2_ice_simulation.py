# =============================================================================
# Setup
# =============================================================================
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import HistGradientBoostingRegressor

# =============================================================================
# Load Data
# =============================================================================
# Tosho Prime firms, 2013-2023
df = pd.read_csv('[load data here]')

df['firm_fac']  = df['firm_fac'].astype('category')
df['mktCap_1b'] = df['mktCap'] / 1000          # Rescale: yen → billions
df['pct_mgmt']  = df['n_mgmtPosition'] / df['n_employees']

# =============================================================================
# Feature Matrix
# =============================================================================
DROP_COLS = [
    'mktCap_1b', 'mktCap', 'ln_mktCap', 'L1_ln_mktCap',
    'pbr', 'per', 'roe', 'ebitda', 'roic', 'roa',
    'firm_fac', 'shokenCode', 'firmName', 'n_femaleMnger',
    'industryCat', 'ind_DaiBunrui_en', 'ind_ChuBunrui_en', 'industryCat_en'
]

X = df.drop(columns=DROP_COLS)
y = df['mktCap_1b']

# =============================================================================
# Model
# =============================================================================
model = HistGradientBoostingRegressor(random_state=2024101, learning_rate=0.1)
model.fit(X, y)

# =============================================================================
# ICE Curve: pct_femaleMger
# =============================================================================
VARIABLE     = 'pct_femaleMger'
VARIABLE_LAB = 'Pct Female Managers'
FIGURE_DIR   = '../figure/ice'
N_POINTS     = 100

# Select reference sample: Astellas Pharma in 2023
index  = df[(df['firmName'] == 'アステラス製薬') & (df['year'] == 2023)].index
sample = X.loc[index]

# Vary target feature across its range
feature_values = np.linspace(0, 100, N_POINTS).reshape(-1, 1)
predictions    = np.zeros(N_POINTS)

for i in range(N_POINTS):
    input_data = sample.copy()
    input_data[VARIABLE] = feature_values[i]
    predictions[i] = model.predict(input_data)

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(feature_values, predictions, color='blue')
ax.set_title(f'ICE Curve — {VARIABLE_LAB}')
ax.set_xlabel(f'{VARIABLE_LAB} (%)')
ax.set_ylabel('Predicted Market Cap (Billions JPY)')
ax.grid(True)

os.makedirs(FIGURE_DIR, exist_ok=True)
fig.savefig(os.path.join(FIGURE_DIR, f'{VARIABLE_LAB}.png'), bbox_inches='tight')
plt.show()
