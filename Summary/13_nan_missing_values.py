"""13 - NaN/inf handling in real datasets."""
import numpy as np

x = np.array([10., 20., np.nan, 40., np.inf, 60.])

print("isnan:", np.isnan(x))
print("isfinite:", np.isfinite(x))
print("nanmean:", np.nanmean(x))
print("nanmedian:", np.nanmedian(x))
print("nanstd:", np.nanstd(x))

clean = x[np.isfinite(x)]
print("finite values:", clean)
