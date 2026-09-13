"""03 - Shape, dimensions, and axis thinking."""
import numpy as np

x = np.arange(24).reshape(4, 6)
print("x:\n", x)
print("shape:", x.shape, "ndim:", x.ndim, "size:", x.size)

print("sum all:", x.sum())
print("sum by columns (axis=0):", x.sum(axis=0))
print("sum by rows (axis=1):", x.sum(axis=1))
