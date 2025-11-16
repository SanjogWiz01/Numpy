import numpy as np
'''
NumPy provides functions to create arrays filled with random numbers.

np.random.rand(): Creates an array of specified shape and 
fills it with random values sampled from a uniform distribution over [0, 1).
np.random.randn(): Creates an array of specified shape and
fills it with random values sampled from a standard normal distribution.
np.random.randint(): Creates an array of specified 
shape and fills it with random integers within a given range.
'''
sanjog=np.random.rand(3,3)
poudel=np.random.randn(2,3)
data=np.random.randint(3,4)
print(sanjog)
print(poudel)
print(data)