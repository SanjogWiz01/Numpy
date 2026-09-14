import numpy as np

a = np.arange(24).reshape(4, 3, 2)
print("3D array:\n", a)

idx = np.array([[0, 2], [1, 3]])
print("Advanced indexing (take):\n", a.take(idx, axis=0))

print("Put values:", np.put(a, [0, 5], [99, 88]))
print("After put:\n", a)
