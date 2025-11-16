# Python Program illustrating
# numpy.vdot() method

import numpy as sa

# 1D array
vector_a = sa.array([[1, 4], [5, 6]])
vector_b = sa.array([[2, 4], [5, 2]])

product = sa.vdot(vector_a, vector_b)
print("Dot Product  : ", product)

product = sa.vdot(vector_b, vector_a)
print("\nDot Product  : ", product)

""" 
How Code 2 works : 
array is being flattened

1 * 2 + 4 * 4 + 5 * 5 + 6 * 2 = 55
"""