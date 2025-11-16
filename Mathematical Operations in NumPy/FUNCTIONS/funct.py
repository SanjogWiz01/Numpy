import numpy as np
def custom_func(x):
    return x**2 + 2*x + 1

a1 = np.array([1, 2, 3, 4])
result = custom_func(a1)
print(result)