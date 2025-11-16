'''NumPy provides functions to create specific types of matrices.

np.eye(): Creates an identity matrix of specified size.
np.diag(): Constructs a diagonal array.
np.zeros_like(): Creates an array of zeros with the same shape and type as a given array.
np.ones_like(): Creates an array of ones with the same shape and type as a given array.'''
import numpy as np

identity_matrix = np.eye(3)
diagonal_array = np.diag([1, 2, 3])
zeros_like_array = np.zeros_like(diagonal_array)
ones_like_array = np.ones_like(diagonal_array)

print(identity_matrix)
print(diagonal_array)
print(zeros_like_array)
print(ones_like_array)



