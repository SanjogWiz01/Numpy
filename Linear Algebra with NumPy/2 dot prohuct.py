
import numpy as np

# 1D array
vector_a = np.array([[1, 4], [5, 6]])
vector_b = np.array([[2, 4], [5, 2]])

product = np.dot(vector_a, vector_b)
print("Dot Product  : \n", product)

product = np.dot(vector_b, vector_a)
print("\nDot Product  : \n", product)

""" 
Code 2 : as normal matrix multiplication
"""