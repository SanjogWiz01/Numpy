"""01 - NumPy setup and first arrays."""
import numpy as np

print("NumPy version:", np.__version__)

a = np.array([10, 20, 30, 40])
print("array:", a)
print("type:", type(a))
print("dtype:", a.dtype)
print("shape:", a.shape)
print("ndim:", a.ndim)
print("size:", a.size)
print("itemsize:", a.itemsize)
