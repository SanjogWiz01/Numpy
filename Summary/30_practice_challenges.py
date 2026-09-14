import numpy as np

arr = np.random.randint(0, 100, size=(5, 5))
print("Array:\n", arr)
print("\nMean of each column:", arr.mean(axis=0))
print("Std of each row:", arr.std(axis=1))
print("Flattened sorted:", np.sort(arr.ravel()))

matrix = np.eye(4)
matrix[1, 1] = 5
matrix[2, 2] = 10
print("\nDiagonal matrix:\n", matrix)
print("Trace:", np.trace(matrix))
print("Determinant:", round(np.linalg.det(matrix), 1))

coords = np.random.rand(100, 2)
dists = np.sqrt(((coords[:, np.newaxis] - coords[np.newaxis, :]) ** 2).sum(axis=2))
np.fill_diagonal(dists, np.inf)
print("\nMin pairwise distance:", dists.min())

data = np.random.randn(1000)
q25, median, q75 = np.percentile(data, [25, 50, 75])
print(f"\nQuartiles: Q1={q25:.2f}, Q2={median:.2f}, Q3={q75:.2f}")
print("IQR:", round(q75 - q25, 2))
