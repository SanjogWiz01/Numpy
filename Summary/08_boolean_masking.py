"""08 - Boolean masks, where, and filtering."""
import numpy as np

ages = np.array([17, 21, 25, 16, 31, 19])
scores = np.array([45, 78, 91, 33, 88, 62])

adult = ages >= 18
print("adults:", ages[adult])
print("high scores:", scores[scores >= 70])

passed = np.where(scores >= 50, "Pass", "Fail")
print(passed)

print("indices >= 80:", np.where(scores >= 80)[0])
