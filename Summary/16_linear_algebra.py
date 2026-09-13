"""16 - Linear algebra used in ML."""
import numpy as np

A = np.array([[2., 1.],
              [1., 3.]])
b = np.array([5., 6.])

print("matrix multiplication:", A @ b)
print("determinant:", np.linalg.det(A))
print("inverse:\n", np.linalg.inv(A))
print("eigenvalues:", np.linalg.eigvals(A))

solution = np.linalg.solve(A, b)
print("solve Ax=b:", solution)

print("norm:", np.linalg.norm(b))
