# Using Numpy Functions: NumPy provides convenient methods to create
# arrays initialized with specific values like zeros and ones:
import numpy as np

sanjog = np.zeros((2, 5)) # 5 rows, 3 columns this createas a zero matrix
a2_ones = np.ones((1, 1)) # this cereates a marix of ones
# Array with a range of values 
a3_range = np.arange(0, 10, 2)  # start, stop, step

print(sanjog)
print(a2_ones)
print(a3_range)