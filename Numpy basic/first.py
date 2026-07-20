import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Create a 2D array s she eh
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Array of zeros
zeros = np.zeros((2, 3))
print("Zeros:\n", zeros)

# Array of ones
ones = np.ones((3, 2))
print("Ones:\n", ones)

# Array with a range of values
range_arr = np.arange(0, 10, 2)
print("Range Array:", range_arr)

# Reshape array
reshaped = arr2.reshape((3, 2))
print("Reshaped Array:\n", reshaped)

# Basic operations
sum_arr = arr1 + 10
print("Add 10 to arr1:", sum_arr)

mult_arr = arr1 * 2
print("Multiply arr1 by 2:", mult_arr)