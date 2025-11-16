'''
NumPy ufuncs
NumPy provides familiar mathematical functions such as sin, cos, exp, etc.
These functions also operate elementwise on an array, producing an array as output.
Example:
'''
import numpy as np
sanjog=([0,np.pi/2,np.pi])
print(np.sin(sanjog)) # [0. 1. 0.]
print(np.cos(sanjog)) # [ 1.  0. -1.]
print(np.tan(sanjog)) # [ 0.  1. -0
# exponential values
a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))

# square root of array values
print ("Square root of array elements:", np.sqrt(a))
