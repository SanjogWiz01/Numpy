"""22 - Practical performance: vectorization and avoiding Python loops."""
import numpy as np
from time import perf_counter

n = 1_000_000
x = np.arange(n, dtype=np.float64)

t0 = perf_counter()
vectorized = x * 2 + 5
t1 = perf_counter()

print("vectorized first values:", vectorized[:5])
print("vectorized time:", t1 - t0, "seconds")

# Rule of thumb: use NumPy operations for numeric bulk work,
# but benchmark when performance matters.
