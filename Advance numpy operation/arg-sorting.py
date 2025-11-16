import numpy as np
# Create a 1D array
arr1 = np.array([10, 2, 30, 4, 50])
print("Original Array:", arr1)
print("Sorted Array:", np.argsort(arr1))  # [1 3 0 2 4] (indices of the sorted array)