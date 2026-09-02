"""
=============================================================
 NUMPY BASICS - ESSENTIAL FOR AI/ML
=============================================================
 Repository: ai-ml-learning
 GitHub: https://github.com/haroongetscoding/ai-ml-learning
 
 NumPy is the foundation of numerical computing in Python.
 Almost every AI/ML library depends on NumPy.
=============================================================
"""

import numpy as np

print("=" * 60)
print(" NUMPY BASICS - AI/ML ESSENTIAL")
print("=" * 60)


# ============================================================
# SECTION 1: CREATING ARRAYS
# ============================================================

print("\n--- SECTION 1: CREATING ARRAYS ---\n")

# From list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr1}")
print(f"Type: {type(arr1)}")
print(f"Shape: {arr1.shape}")
print(f"Data type: {arr1.dtype}")

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D Array:\n{arr2d}")
print(f"Shape: {arr2d.shape}")

# Special arrays
zeros = np.zeros((3, 4))
print(f"\nZeros (3x4):\n{zeros}")

ones = np.ones((2, 3))
print(f"\nOnes (2x3):\n{ones}")

eye = np.eye(4)
print(f"\nIdentity (4x4):\n{eye}")

full = np.full((3, 3), 7)
print(f"\nFull of 7s:\n{full}")

# Random arrays
random_arr = np.random.rand(5)
print(f"\nRandom (0-1): {random_arr}")

random_int = np.random.randint(1, 100, size=(3, 3))
print(f"\nRandom Integers:\n{random_int}")

# Arange and linspace
.arange = np.arange(0, 20, 2)
print(f"\narange(0, 20, 2): {arange}")

linspace = np.linspace(0, 1, 5)
print(f"linspace(0, 1, 5): {linspace}")


# ============================================================
# SECTION 2: ARRAY OPERATIONS
# ============================================================

print("\n--- SECTION 2: ARRAY OPERATIONS ---\n")

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Element-wise operations
print(f"a + b = {a + b}")
print(f"a * 2 = {a * 2}")
print(f"a ** 2 = {a ** 2}")
print(f"a / 2 = {a / 2}")

# Mathematical functions
print(f"\nsqrt(a) = {np.sqrt(a)}")
print(f"sin(a) = {np.sin(a)}")
print(f"exp(a) = {np.exp(a)}")
print(f"log(a) = {np.log(a)}")

# Aggregation
print(f"\nsum: {np.sum(a)}")
print(f"mean: {np.mean(a)}")
print(f"std: {np.std(a):.2f}")
print(f"min: {np.min(a)}")
print(f"max: {np.max(a)}")
print(f"median: {np.median(a)}")


# ============================================================
# SECTION 3: INDEXING & SLICING
# ============================================================

print("\n--- SECTION 3: INDEXING & SLICING ---\n")

arr = np.array([10, 20, 30, 40, 50, 60])

# Indexing
print(f"First element: {arr[0]}")
print(f"Last element: {arr[-1]}")
print(f"Middle element: {arr[2]}")

# Slicing
print(f"First 3: {arr[:3]}")
print(f"Last 3: {arr[3:]}")
print(f"Middle: {arr[1:4]}")
print(f"Every 2nd: {arr[::2]}")
print(f"Reversed: {arr[::-1]}")

# 2D indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{arr2d}")
print(f"Element [0,1]: {arr2d[0, 1]}")
print(f"Row 0: {arr2d[0, :]}")
print(f"Column 1: {arr2d[:, 1]}")
print(f"Sub-array:\n{arr2d[0:2, 1:3]}")


# ============================================================
# SECTION 4: RESHAPING & TRANSPOSING
# ============================================================

print("\n--- SECTION 4: RESHAPING & TRANSPOSING ---\n")

arr = np.arange(12)
print(f"Original: {arr}")
print(f"Shape: {arr.shape}")

# Reshape
reshaped = arr.reshape(3, 4)
print(f"\nReshaped (3x4):\n{reshaped}")

reshaped2 = arr.reshape(4, 3)
print(f"\nReshaped (4x3):\n{reshaped2}")

# Flatten
flattened = reshaped.flatten()
print(f"\nFlattened: {flattened}")

# Transpose
transposed = reshaped.T
print(f"\nTransposed:\n{transposed}")

# Resize
resized = np.resize(arr, (2, 6))
print(f"\nResized (2x6):\n{resized}")


# ============================================================
# SECTION 5: BOOLEAN INDEXING & FILTERING
# ============================================================

print("\n--- SECTION 5: BOOLEAN INDEXING ---\n")

arr = np.array([1, 5, 10, 15, 20, 25, 30])

# Boolean conditions
mask = arr > 10
print(f"Array: {arr}")
print(f"Mask (>10): {mask}")
print(f"Filtered: {arr[mask]}")

# Multiple conditions
filtered = arr[(arr > 5) & (arr < 25)]
print(f"Between 5 and 25: {filtered}")

# Where
result = np.where(arr > 15, arr * 2, arr)
print(f"Where > 15, double: {result}")

# Find indices
indices = np.where(arr > 15)[0]
print(f"Indices > 15: {indices}")


# ============================================================
# SECTION 6: LINEAR ALGEBRA
# ============================================================

print("\n--- SECTION 6: LINEAR ALGEBRA ---\n")

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}")

# Dot product
C = np.dot(A, B)
print(f"\nA dot B:\n{C}")

# Alternative syntax
C2 = A @ B
print(f"\nA @ B:\n{C2}")

# Determinant
det = np.linalg.det(A)
print(f"\nDeterminant of A: {det:.2f}")

# Inverse
inv = np.linalg.inv(A)
print(f"\nInverse of A:\n{inv}")

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\nEigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

# Solving linear equations: 2x + 3y = 8, 3x + 4y = 11
coefficients = np.array([[2, 3], [3, 4]])
constants = np.array([8, 11])
solution = np.linalg.solve(coefficients, constants)
print(f"\nSolution: x={solution[0]:.2f}, y={solution[1]:.2f}")


# ============================================================
# SECTION 7: CONCATENATION & STACKING
# ============================================================

print("\n--- SECTION 7: CONCATENATION & STACKING ---\n")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Concatenate
c = np.concatenate([a, b])
print(f"Concatenated: {c}")

# Stack vertically
vstack = np.vstack([a, b])
print(f"\nVStack:\n{vstack}")

# Stack horizontally
hstack = np.hstack([a, b])
print(f"HStack: {hstack}")

# 2D arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(f"\nStack vertically:\n{np.vstack([arr1, arr2])}")
print(f"\nStack horizontally:\n{np.hstack([arr1, arr2])}")


# ============================================================
# SECTION 8: STATISTICS & DISTRIBUTIONS
# ============================================================

print("\n--- SECTION 8: STATISTICS & DISTRIBUTIONS ---\n")

data = np.random.randn(1000)  # Normal distribution

print(f"Mean: {np.mean(data):.4f}")
print(f"Median: {np.median(data):.4f}")
print(f"Std Dev: {np.std(data):.4f}")
print(f"Variance: {np.var(data):.4f}")
print(f"Percentile (25%): {np.percentile(data, 25):.4f}")
print(f"Percentile (75%): {np.percentile(data, 75):.4f}")

# Histogram
hist, bins = np.histogram(data, bins=10)
print(f"\nHistogram bins: {bins[:5]}...")
print(f"Histogram counts: {hist[:5]}...")


# ============================================================
# SECTION 9: PRACTICAL EXAMPLE - SIMPLE ML
# ============================================================

print("\n--- SECTION 9: PRACTICAL ML EXAMPLE ---\n")

# Generate synthetic data
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 data points
y = 2.5 * X + np.random.randn(100, 1) * 2  # Linear relationship + noise

print(f"Data points: {X.shape[0]}")
print(f"Features: {X.shape[1]}")

# Simple linear regression using NumPy
X_mean = np.mean(X)
y_mean = np.mean(y)

# Calculate slope (m) and intercept (b)
numerator = np.sum((X - X_mean) * (y - y_mean))
denominator = np.sum((X - X_mean) ** 2)
m = numerator / denominator
b = y_mean - m * X_mean

print(f"\nLinear Regression Model:")
print(f"Slope: {m:.4f}")
print(f"Intercept: {b:.4f}")
print(f"Formula: y = {m:.4f}x + {b:.4f}")

# R-squared
y_pred = m * X + b
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - y_mean) ** 2)
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared:.4f}")

# Predict
new_x = np.array([[5.0]])
prediction = m * new_x + b
print(f"\nPrediction for x=5: {prediction[0, 0]:.4f}")


# ============================================================
# SECTION 10: PERFORMANCE COMPARISON
# ============================================================

print("\n--- SECTION 10: PERFORMANCE ---\n")

import time

# Python list
size = 1000000
python_list = list(range(size))
numpy_array = np.arange(size)

# Addition
start = time.time()
result_list = [x + 1 for x in python_list]
list_time = time.time() - start

start = time.time()
result_array = numpy_array + 1
np_time = time.time() - start

print(f"Addition 1M elements:")
print(f"  Python list: {list_time:.4f}s")
print(f"  NumPy array: {np_time:.4f}s")
print(f"  Speedup: {list_time / np_time:.1f}x faster with NumPy!")

# Multiplication
start = time.time()
result_list = [x * 2 for x in python_list]
list_time = time.time() - start

start = time.time()
result_array = numpy_array * 2
np_time = time.time() - start

print(f"\nMultiplication 1M elements:")
print(f"  Python list: {list_time:.4f}s")
print(f"  NumPy array: {np_time:.4f}s")
print(f"  Speedup: {list_time / np_time:.1f}x faster with NumPy!")


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 60)
print(" NUMPY COMPLETE!")
print("=" * 60)
print("\n Key Takeaways:")
print("  1. Arrays are faster than lists")
print("  2. Vectorized operations avoid loops")
print("  3. Broadcasting allows operations on different shapes")
print("  4. Linear algebra is built-in")
print("  5. Essential for all ML libraries")
print("\n Next: Pandas for Data Analysis")
print("=" * 60)
