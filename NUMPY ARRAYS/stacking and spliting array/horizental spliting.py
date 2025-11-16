import numpy as np

# Creating an example 2D array
array = np.array([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]])

# Horizontal splitting into 2 subarrays along axis=1
result = np.hsplit(array, 2)

print("2D Array:")
print(array)
print("\nResult after numpy.hsplit():")
print(result)