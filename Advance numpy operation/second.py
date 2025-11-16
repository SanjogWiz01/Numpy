import numpy as np
sanjog = np.array([[3, 2, 0, 1], [6, 5, 4, 8]])
print("Original array:\n", sanjog)
#sorting along rows
print("Sorted array along rows:\n", np.sort(sanjog, axis=1))
#sorting along columns
print("Sorted array along columns:\n", np.sort(sanjog, axis=0))