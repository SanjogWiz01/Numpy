import numpy as np

a = np.array([3, 6])
b = np.array([9, 10])
print(np.cross(a, b))

print("------------------------------------")

x = np.array([[2, 6, 9], [2, 7, 3]])
y = np.array([[7, 5, 6], [3, 12, 3]])
print("\nCross product of matrices x and y =")
print(np.cross(x, y))