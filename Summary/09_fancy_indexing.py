"""09 - Advanced/fancy indexing."""
import numpy as np

x = np.array([10, 20, 30, 40, 50])
indices = np.array([4, 0, 2])
print("selected:", x[indices])

matrix = np.arange(1, 17).reshape(4, 4)
rows = np.array([0, 1, 2, 3])
cols = np.array([3, 2, 1, 0])
print("diagonal-like selection:", matrix[rows, cols])
