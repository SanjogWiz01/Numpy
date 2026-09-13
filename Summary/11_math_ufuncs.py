"""11 - Universal functions and mathematical operations."""
import numpy as np

x = np.array([-4, -1, 0, 1, 4], dtype=float)

print("abs:", np.abs(x))
print("square:", np.square(x))
print("exp:", np.exp(x))
print("sqrt(abs):", np.sqrt(np.abs(x)))
print("sin:", np.sin(x))
print("maximum:", np.maximum(x, 1))
print("clip:", np.clip(x, -1, 1))
