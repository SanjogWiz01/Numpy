'''Syntax : array.reshape(shape)
Argument : It take tuple as argument, tuple is the new shape to be formed
Return : It returns numpy.ndarray
 '''
import numpy as np
# Note : We can also use np.reshape(array, shape) command to reshape the array
# Reshaping : 1-D to 2D
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Normal array'+ str(array))
n = array.size # size eof array
# N-D array N dimension
N = 2

# calculating s
s = n//N

# reshaping numpy array
# converting it to 2-D from 1-D array
reshaped1 = array.reshape((N, s))
print(reshaped1 )
reshaped2 = np.reshape(array, (2, 5))
print(reshaped2 )