import numpy as np
arr = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Array 1:", arr)
print("Array 2:", arr2)
sum_arr = arr + arr2
print("Sum of Arrays:", sum_arr)


a1 = np.array([1, 2, 3, 4])
result = a1 * 2
print(result)


a1 = np.array([10, 20, 30])
result = a1 > 15
print(result)


a1= np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
result = np.dot(a1, a2) 
print(result)