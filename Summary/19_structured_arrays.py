"""19 - Structured arrays: useful for compact typed records."""
import numpy as np

dtype = np.dtype([
    ("name", "U20"),
    ("age", "i4"),
    ("score", "f8")
])

students = np.array([
    ("Sita", 20, 82.5),
    ("Ram", 21, 91.0),
    ("Hari", 19, 76.5)
], dtype=dtype)

print(students)
print("names:", students["name"])
print("scores:", students["score"])
print("top score:", students["score"].max())
