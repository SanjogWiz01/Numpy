"""21 - NumPy I/O: CSV/text and binary .npy/.npz."""
import numpy as np
from pathlib import Path

data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(exist_ok=True)

x = np.array([[1, 2], [3, 4]])
np.save(data_dir / "matrix.npy", x)
np.savez(data_dir / "arrays.npz", matrix=x, doubled=x * 2)

loaded = np.load(data_dir / "matrix.npy")
archive = np.load(data_dir / "arrays.npz")

print("loaded .npy:\n", loaded)
print("npz keys:", archive.files)
print("doubled:\n", archive["doubled"])
