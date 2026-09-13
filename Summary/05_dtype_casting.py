"""05 - Data types and safe casting."""
import numpy as np

x = np.array([1, 2, 3], dtype=np.int32)
print(x, x.dtype)

y = x.astype(np.float64)
print(y, y.dtype)

z = np.array([1.2, 2.8, 3.9])
print("float -> int:", z.astype(np.int64))

print("dtype limits:", np.iinfo(np.int32).min, np.iinfo(np.int32).max)
