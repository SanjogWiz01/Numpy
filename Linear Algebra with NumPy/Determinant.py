import numpy as np
matrix = np.array([[1, 2],
                   [3, 2]])

# Calculate the determinant
determinant = np.linalg.det(matrix)

print("Determinant:", determinant)
'''
import numpy as np

A = np.array([[50, 29], [30, 44]])
sign, logdet = np.linalg.slogdet(A)
res = sign * np.exp(logdet)

print(res)'''