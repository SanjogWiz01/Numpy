import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

print("Split into 3:", np.split(a, 3))

b = np.arange(16).reshape(4, 4)
print("\nHsplit:\n", np.hsplit(b, 2))
print("Vsplit:\n", np.vsplit(b, 2))

c = np.array([1, 2, 3])
print("\nTile:", np.tile(c, 3))
print("Repeat:", np.repeat(c, 2))

d = np.array([[1], [2], [3]])
e = np.array([10, 20, 30])
print("\nColumn stack:\n", np.column_stack((d, e)))
print("Row stack:\n", np.row_stack((d.flatten(), e)))
