import numpy as np
import time

def slow_square(x):
    return x * x

arr = np.arange(1_000_000)

start = time.time()
result1 = [slow_square(x) for x in arr]
print(f"Python loop: {time.time() - start:.4f}s")

start = time.time()
result2 = arr ** 2
print(f"NumPy vectorized: {time.time() - start:.4f}s")

vfunc = np.vectorize(lambda x: x ** 2 + 1)
start = time.time()
result3 = vfunc(arr)
print(f"np.vectorize: {time.time() - start:.4f}s")

print("\nResults match:", np.allclose(result2, result3))
