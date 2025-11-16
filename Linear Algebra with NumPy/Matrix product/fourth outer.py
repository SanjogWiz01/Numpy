import numpy as np

a = np.array([2, 6])
b = np.array([3, 10])
print("Vectors :")
print("a = ", a)
print("\nb = ", b)

print("\nOuter product of vectors a and b =")
print(np.outer(a, b))

print("------------------------------------")

x = np.array([[3, 6, 4], [9, 4, 6]])
y = np.array([[1, 15, 7], [3, 10, 8]])
print("\nMatrices :")
print("x =", x)
print("\ny =", y)

print("\nOuter product of matrices x and y =")
print(np.outer(x, y))