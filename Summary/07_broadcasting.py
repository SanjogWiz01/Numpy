"""07 - Broadcasting."""
import numpy as np

prices = np.array([[100, 200, 300],
                   [150, 250, 350]])

tax_rates = np.array([0.13, 0.10, 0.08])
final_prices = prices * (1 + tax_rates)

print(final_prices)

# Another common ML/data-science pattern: center each column.
X = np.array([[10., 20., 30.],
              [20., 30., 40.],
              [30., 40., 50.]])
column_mean = X.mean(axis=0)
print("centered:\n", X - column_mean)
