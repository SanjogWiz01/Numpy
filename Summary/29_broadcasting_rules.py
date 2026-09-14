import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print("Matrix + vector:\n", a + b)

x = np.array([1, 2, 3]).reshape(3, 1)
y = np.array([10, 20]).reshape(1, 2)
print("\nOuter add:\n", x + y)

print("\nScalar op:\n", a * 2 - 1)

m = np.array([[1], [2], [3]])
n = np.array([10, 20, 30, 40])
print("\nBroadcast (3,1) + (1,4):\n", m + n)

print("\nIncompatible shapes:")
try:
    np.ones((2, 3)) + np.ones((4,))
except ValueError as e:
    print(f"  Error: {e}")
