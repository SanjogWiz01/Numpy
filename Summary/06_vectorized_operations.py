"""06 - Vectorization: replace many simple Python loops."""
import numpy as np

sales = np.array([100, 150, 120, 180, 200])
discount = 0.10

after_discount = sales * (1 - discount)
print("after discount:", after_discount)
print("tax:", after_discount * 1.13)
print("sqrt:", np.sqrt(sales))
print("log1p:", np.log1p(sales))
