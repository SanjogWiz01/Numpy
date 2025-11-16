import numpy as np
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(np.add(a, b))   # [11 22 33]
print(np.subtract(b, a)) # [9 18 27]
print(np.multiply(a, b)) # [10 40 90]
print(np.divide(b, a))   # [10. 10. 10.]
print(np.sqrt(a))       # [1.         1.41421356 1.73205081]