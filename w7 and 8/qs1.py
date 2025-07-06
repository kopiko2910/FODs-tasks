import numpy as np


arr = np.array([1, 2, 3, 4, 5])

print("Original array:", arr)


array_sum = np.sum(arr)
print("\na) Sum of elements:", array_sum)


array_avg = np.mean(arr)
print("b) Average of elements:", array_avg)


array_max = np.max(arr)
array_min = np.min(arr)
print("c) Maximum value:", array_max)
print("   Minimum value:", array_min)

print("\nAdditional operations:")
print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)  
print("Square of array:", arr ** 2) 