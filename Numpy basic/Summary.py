# File: array_creation.py
import numpy as np
arr = np.array([1, 2, 3, 4])
print("Array:", arr)

# File: array_datatypes.py
import numpy as np
arr = np.array([1, 2, 3], dtype='float32')
print("Array:", arr)
print("Datatype:", arr.dtype)

# File: array_dimensions.py
import numpy as np
arr_2d = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr_2d)
print("Dimensions:", arr_2d.ndim)

# File: array_shape.py
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", arr.shape)

# File: array_reshape.py
import numpy as np
arr = np.arange(8)
reshaped = arr.reshape(2, 4)
print("Reshaped array:\n", reshaped)

# File: indexing_slicing.py
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])
print("Slice 1-3:", arr[1:4])

# File: numpy_arange_linspace.py
import numpy as np
print("Arange:", np.arange(0, 10, 2))
print("Linspace:", np.linspace(0, 1, 5))

# File: basic_operations.py
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition:", a + b)
print("Multiplication:", a * b)

# File: matrix_multiplication.py
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix Multiplication:\n", A @ B)

# File: numpy_statistics.py
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Std Dev:", np.std(arr))

# File: random_numbers.py
import numpy as np
print("Random ints:", np.random.randint(1, 10, size=5))
print("Random floats:", np.random.rand(3))

# File: boolean_filtering.py
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
filtered = arr[arr > 25]
print("Filtered:", filtered)

# File: stacking_arrays.py
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Vertical:\n", np.vstack((a, b)))
print("Horizontal:", np.hstack((a, b)))

# File: reshape_flatten_ravel.py
import numpy as np
arr = np.array([[1, 2], [3, 4]])
print("Flatten:", arr.flatten())
print("Ravel:", arr.ravel())

# File: numpy_broadcasting.py
import numpy as np
arr = np.array([1, 2, 3])
print("Add 10:", arr + 10)