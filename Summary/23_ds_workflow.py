"""23 - Junior Data Scientist mini workflow using only NumPy."""
import numpy as np

rng = np.random.default_rng(7)

# Synthetic customer dataset: age, monthly_spend, visits
X = np.column_stack([
    rng.integers(18, 60, 100),
    rng.normal(3000, 800, 100),
    rng.integers(1, 20, 100)
]).astype(float)

# Basic quality checks
print("shape:", X.shape)
print("missing:", np.isnan(X).sum())
print("column means:", X.mean(axis=0))
print("column std:", X.std(axis=0))

# Standardization pattern used before many ML models.
mean = X.mean(axis=0)
std = X.std(axis=0)
X_scaled = (X - mean) / std

print("scaled mean:", X_scaled.mean(axis=0))
print("scaled std:", X_scaled.std(axis=0))
