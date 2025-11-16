import numpy as np

# Creating an example array
array = np.arange(6)

# Splitting the array into 2 equal parts along the first axis (axis=0)
result = np.split(array, 2)

print("Array:")
print(array)
print("\nResult after numpy.split():")
print(result)