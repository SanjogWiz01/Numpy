"""20 - Dates and timedeltas."""
import numpy as np

dates = np.array(["2026-01-01", "2026-01-10", "2026-02-01"], dtype="datetime64[D]")
print("dates:", dates)
print("days between:", dates - dates[0])

start = np.datetime64("2026-01-01")
end = np.datetime64("2026-03-01")
print("duration:", end - start)
