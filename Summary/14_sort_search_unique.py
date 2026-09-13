"""14 - Sorting, searching, uniqueness, counting."""
import numpy as np

x = np.array([40, 10, 30, 10, 20, 40, 10])

print("sorted:", np.sort(x))
print("argsort:", np.argsort(x))
print("unique:", np.unique(x))
values, counts = np.unique(x, return_counts=True)
print("frequency table:", dict(zip(values, counts)))

print("searchsorted:", np.searchsorted(np.array([10, 20, 30, 40]), 25))
