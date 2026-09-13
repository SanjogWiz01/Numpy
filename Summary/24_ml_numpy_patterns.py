"""24 - NumPy patterns that appear constantly in machine learning."""
import numpy as np

rng = np.random.default_rng(42)

# Feature matrix X: samples x features
X = rng.normal(size=(100, 4))
# Parameter vector w: features
w = np.array([0.5, -1.2, 2.0, 0.7])
b = 1.5

# Linear model prediction
y_hat = X @ w + b

# Mean squared error
y = y_hat + rng.normal(0, 0.5, size=100)
mse = np.mean((y - y_hat) ** 2)

print("X shape:", X.shape)
print("prediction shape:", y_hat.shape)
print("MSE:", mse)

# One-hot encoding pattern
labels = np.array([0, 2, 1, 2])
one_hot = np.eye(3)[labels]
print("one-hot:\n", one_hot)
