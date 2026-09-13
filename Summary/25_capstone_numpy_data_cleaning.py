"""25 - Capstone: clean and summarize a small dataset with NumPy."""
import numpy as np

# Columns: age, income, score
raw = np.array([
    [20, 25000, 65],
    [22, 32000, 72],
    [19, np.nan, 58],
    [35, 55000, 91],
    [28, 48000, 85],
    [41, 70000, 95],
], dtype=float)

print("Original:\n", raw)

# Median imputation for the income column.
income = raw[:, 1]
median_income = np.nanmedian(income)
income[np.isnan(income)] = median_income
raw[:, 1] = income

# Remove impossible rows if any.
valid = (
    (raw[:, 0] >= 18) &
    (raw[:, 1] > 0) &
    (raw[:, 2] >= 0) &
    (raw[:, 2] <= 100)
)
clean = raw[valid]

print("Clean:\n", clean)
print("Means:", clean.mean(axis=0))
print("Median:", np.median(clean, axis=0))
print("75th percentile:", np.percentile(clean, 75, axis=0))

# Standardize numeric columns for an ML-ready matrix.
mu = clean.mean(axis=0)
sigma = clean.std(axis=0)
scaled = (clean - mu) / sigma
print("Scaled:\n", scaled)
