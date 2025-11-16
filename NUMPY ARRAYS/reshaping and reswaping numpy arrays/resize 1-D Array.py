
import numpy as np

# Making a random array
sanjog= np.array([1, 2, 3, 4, 5, 6])

# Reshape the array permanently
sanjog.resize(2, 3)

print(sanjog)
sanjog.resize(3,45) # remainig value will be replece by the zeroes

print(sanjog)