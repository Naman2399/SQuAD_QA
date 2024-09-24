import numpy as np

# Create tuples with NumPy arrays
tuple1 = (np.array([1, 2, 3]), np.array([4, 5, 6]))
tuple2 = (np.array([7, 8, 9]), np.array([10, 11, 12]))

# Create an array of tuples with dtype=object
arr = np.array(tuple1, dtype=object)

# Accessing an element
print(arr.shape)  # Output: (array([1
