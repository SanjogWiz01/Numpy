"""04 - Indexing and slicing."""
import numpy as np

x = np.arange(1, 13).reshape(3, 4)
print(x)
print("single:", x[1, 2])
print("row:", x[1])
print("column:", x[:, 2])
print("submatrix:\n", x[:2, 1:3])
print("reverse columns:\n", x[:, ::-1])
