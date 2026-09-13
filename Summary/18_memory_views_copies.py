"""18 - Copies vs views: important for performance and bugs."""
import numpy as np

x = np.arange(6)
view = x[1:4]
view[0] = 999
print("x changed by view:", x)

y = np.arange(6)
copy = y[1:4].copy()
copy[0] = 999
print("y unchanged by copy:", y)

print("shares memory:", np.shares_memory(y, copy))
