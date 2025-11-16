# Python code to demonstrate matrix operations 
# add(), subtract() and divide() 

# importing numpy for matrix operations 
import numpy 

# initializing matrices 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]]) 

# using add() to add matrices 
print ("The element wise addition of matrix is : ") 
print (numpy.add(x,y)) 

# using subtract() to subtract matrices 
print ("The element wise subtraction of matrix is : ") 
print (numpy.subtract(x,y)) 

# using divide() to divide matrices 
print ("The element wise division of matrix is : ") 
print (numpy.divide(x,y))
# using multiply() to multiply matrices element wise 
print ("The element wise multiplication of matrix is : ") 
print (numpy.multiply(x,y)) 

# using dot() to multiply matrices 
print ("The product of matrices is : ") 
print (numpy.dot(x,y))
print ("The element wise square root is : ") 
print (numpy.sqrt(x)) 

# using sum() to print summation of all elements of matrix 
print ("The summation of all matrix element is : ") 
print (numpy.sum(y)) 

# using sum(axis=0) print summation of each column of matrix 
print ("The column wise summation of all matrix is : ") 
print (numpy.sum(y,axis=0)) 

# using sum(axis=1) print summation of each row of matrix 
print ("The row wise summation of all matrix is : ") 
print (numpy.sum(y,axis=1)) 

# using "T" to transpose the matrix 
print ("The transpose of given matrix is : ") 
print (x.T) 

# using nested loops to demonstrate matrix operations
'''A = [[1,2],[4,5]] 
B = [[7,8],[9,10]] 
rows = len(A) 
cols = len(A[0]) 

# Element wise addition 
C = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
	for j in range(cols): 
		C[i][j] = A[i][j] + B[i][j] 
print("Addition of matrices: \n", C) 

# Element wise subtraction 
D = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
	for j in range(cols): 
		D[i][j] = A[i][j] - B[i][j] 
print("Subtraction of matrices: \n", D) 

# Element wise division 
E = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
	for j in range(cols): 
		E[i][j] = A[i][j] / B[i][j] 
print("Division of matrices: \n", E) ''' 
# import numpy as np 
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print("Original array:\n", a)