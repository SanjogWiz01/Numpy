"""15 - Modern random number generation for DS/ML experiments."""
import numpy as np

rng = np.random.default_rng(42)

print("uniform:", rng.random(5))
print("integers:", rng.integers(1, 101, size=10))
print("normal:", rng.normal(loc=50, scale=10, size=5))
print("choice:", rng.choice(["A", "B", "C"], size=10, p=[0.5, 0.3, 0.2]))

data = np.arange(10)
rng.shuffle(data)
print("shuffled:", data)
