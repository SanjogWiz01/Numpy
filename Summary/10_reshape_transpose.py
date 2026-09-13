"""10 - Reshape, flatten/ravel, transpose, and stacking."""
import numpy as np

x = np.arange(12)
m = x.reshape(3, 4)

print("reshape:\n", m)
print("transpose:\n", m.T)
print("ravel:", m.ravel())
print("flatten:", m.flatten())

a = np.array([[1, 2]])
b = np.array([[3, 4]])
print("vstack:\n", np.vstack([a, b]))
print("hstack:", np.hstack([a, b]))
print("concatenate:", np.concatenate([a, b], axis=1))
