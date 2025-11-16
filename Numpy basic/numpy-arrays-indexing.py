import numpy as np
sanjog = np.array([[1, 2, 3], [4, 5, 6]])

print(sanjog[0]) #print first row
print(sanjog[1]) #print second row
print(sanjog[0, 1]) #print element at first row and second column
print(sanjog[1, 2]) #print element at second row and third column
print(sanjog[:, 1]) #print second column
print(sanjog[1, :]) #print second row
print(sanjog[0:2, 1:3]) #print sub-array from first two rows and last two columns
print(sanjog[0:1, 0:2]) #print sub-array from first row and first two columns
print(sanjog[0:2, 0:2]) #print sub-array from first two rows and first two columns
print(sanjog[1, 1:3]) #print elements from second row and last two columns
print(sanjog[0, 0:2]) #print elements from first row and first two columns
print(sanjog[0:2, 1]) #print elements from first two rows
print(sanjog[1, 0:2]) #print elements from second row and first two columns
