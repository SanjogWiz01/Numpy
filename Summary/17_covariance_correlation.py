"""17 - Covariance and correlation."""
import numpy as np

hours = np.array([1, 2, 3, 4, 5, 6], dtype=float)
scores = np.array([52, 55, 61, 68, 72, 80], dtype=float)

cov = np.cov(hours, scores)
corr = np.corrcoef(hours, scores)

print("covariance matrix:\n", cov)
print("correlation matrix:\n", corr)
print("correlation coefficient:", corr[0, 1])
