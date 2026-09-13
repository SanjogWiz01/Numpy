"""12 - Descriptive statistics for data science."""
import numpy as np

x = np.array([10, 12, 15, 18, 20, 25, 30])

print("mean:", np.mean(x))
print("median:", np.median(x))
print("std:", np.std(x))
print("variance:", np.var(x))
print("min/max:", np.min(x), np.max(x))
print("range:", np.ptp(x))
print("percentiles:", np.percentile(x, [25, 50, 75]))
print("quantiles:", np.quantile(x, [0.25, 0.5, 0.75]))
