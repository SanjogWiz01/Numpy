# NumPy — Junior Data Scientist (80/20)

This folder is a practical NumPy curriculum for a Junior Data Scientist. It follows an **80/20 / Pareto approach**: prioritize the NumPy operations that repeatedly appear in data cleaning, exploratory analysis, statistics, feature engineering, and machine learning.

## Files

1. setup and ndarray fundamentals
2. array creation
3. shape, dimensions, axis
4. indexing and slicing
5. dtypes and casting
6. vectorized operations
7. broadcasting
8. boolean masking and `where`
9. fancy indexing
10. reshape/transpose/stacking
11. ufuncs and math
12. descriptive statistics
13. NaN and infinity handling
14. sorting/searching/unique/counting
15. random sampling
16. linear algebra
17. covariance/correlation
18. views vs copies
19. structured arrays
20. datetime
21. NumPy file I/O
22. performance/vectorization
23. junior data-science workflow
24. NumPy patterns used in ML
25. capstone data-cleaning workflow

## Recommended learning order

**Tier 1 — must master:** 01–14  
**Tier 2 — highly useful for DS/ML:** 15–18, 22–24  
**Tier 3 — useful/advanced:** 19–21, 25

## Core 20% to memorize

- `np.array`, `zeros`, `ones`, `arange`, `linspace`
- `.shape`, `.ndim`, `.size`, `.dtype`
- indexing, slicing, boolean masks
- `reshape`, `.T`, `ravel`
- vectorized arithmetic and ufuncs
- broadcasting
- `sum`, `mean`, `median`, `std`, `var`, `min`, `max`, `percentile`
- `isnan`, `isfinite`, `nanmean`, `nanmedian`
- `where`, `unique`, `argsort`
- `default_rng`
- `@`, `np.linalg.solve`, `norm`
- views vs copies
- NumPy as the numerical foundation beneath pandas and much of the Python ML ecosystem

## Junior Data Scientist outcome

After completing this folder, you should be able to manipulate numerical datasets efficiently, filter and clean arrays, compute descriptive statistics, prepare feature matrices, perform basic linear algebra, generate reproducible samples, understand broadcasting and memory views, and recognize the NumPy patterns used inside ML workflows.

The examples target current NumPy 2.x concepts and use the modern `np.random.default_rng()` API.
