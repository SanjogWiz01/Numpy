
import numpy as np 
	
# 2D array 
arr = [[14, 17, 12, 33, 44], 
	[15, 6, 27, 8, 19], 
	[23, 2, 54, 1, 4,]] 

print("\nSum of arr : ", np.sum(arr)) 
print("Sum of arr(axis = 0) : ", np.sum(arr, axis = 0)) 
print("Sum of arr(axis = 1) : ", np.sum(arr, axis = 1))

print("\nSum of arr (keepdimension is True): \n",
	np.sum(arr, axis = 1, keepdims = True))
# for basic 
print("Sum of arr(uint8) : ", np.sum(arr, dtype = np.uint8)) 
print("Sum of arr(float32) : ", np.sum(arr, dtype = np.float32))

# for addition only
print("\nSum of arr : ", np.sum(arr)) 