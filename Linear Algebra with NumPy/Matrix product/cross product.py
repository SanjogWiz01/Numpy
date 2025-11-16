import numpy as np

# Example 2D arrays (each row is a vector)
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8, 9],
              [10, 11, 12]])

# Compute cross product row-wise
cross_prod = np.cross(a, b)

print("Cross product:\n", cross_prod) 