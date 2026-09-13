"""02 - Practical array creation."""
import numpy as np

print("zeros:", np.zeros(5))
print("ones:", np.ones((2, 3)))
print("full:", np.full((2, 3), 7))
print("range:", np.arange(0, 20, 2))
print("linspace:", np.linspace(0, 1, 6))
print("identity:\n", np.eye(3))
print("from nested list:", np.array([[1, 2], [3, 4]]))
