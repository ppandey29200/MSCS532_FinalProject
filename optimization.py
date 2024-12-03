import numpy as np
import time

# 1. Eliminating Unnecessary Operations
def unoptimized_multiply(arr1, arr2):
    result = np.zeros(len(arr1))
    for i in range(len(arr1)):
        result[i] = arr1[i] * arr2[i]  # redundant computation
    return result

def optimized_multiply(arr1, arr2):
    return arr1 * arr2  # NumPy's vectorized operations

# 2. Reducing Loop Iterations
def unoptimized_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]  # loop traversal
    return total

def optimized_sum(arr):
    return np.sum(arr)

# Create random arrays for testing
arr1 = np.random.rand(10**7)
arr2 = np.random.rand(10**7)
arr = np.random.rand(10**7)

# Measure performance for Eliminating Unnecessary Operations
start_time = time.time()
unoptimized_multiply_result = unoptimized_multiply(arr1, arr2)
unoptimized_multiply_time = time.time() - start_time

start_time = time.time()
optimized_multiply_result = optimized_multiply(arr1, arr2)
optimized_multiply_time = time.time() - start_time

# Measure performance for Reducing Loop Iterations
start_time = time.time()
unoptimized_sum_result = unoptimized_sum(arr)
unoptimized_sum_time = time.time() - start_time

start_time = time.time()
optimized_sum_result = optimized_sum(arr)
optimized_sum_time = time.time() - start_time

# Print the results
print(f"Unoptimized Multiply Time (Redundant Operations): {unoptimized_multiply_time:.6f} seconds")
print(f"Optimized Multiply Time (Redundant Operations Removed): {optimized_multiply_time:.6f} seconds")

print(f"Unoptimized Sum Time (Multiple Traversals): {unoptimized_sum_time:.6f} seconds")
print(f"Optimized Sum Time (Single Traversal): {optimized_sum_time:.6f} seconds")
