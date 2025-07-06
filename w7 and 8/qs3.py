import numpy as np


np.random.seed(42)  
random_array = np.random.randint(1, 100, 10) 

print("Original random array:")
print(random_array)


sorted_array = np.sort(random_array)
print("\nSorted array:")
print(sorted_array)


print("\nReshaping operations:")

matrix_2x5 = sorted_array.reshape(2, 5)
print("\n2x5 Matrix:")
print(matrix_2x5)


matrix_5x2 = sorted_array.reshape(5, 2)
print("\n5x2 Matrix:")
print(matrix_5x2)


matrix_1x10 = sorted_array.reshape(1, 10)
print("\n1x10 Matrix:")
print(matrix_1x10)


try:

    matrix_3x3 = sorted_array.reshape(3, 3)
except ValueError as e:
    print(f"\nAttempting invalid reshape (3x3): {e}")

flattened = matrix_5x2.flatten()
print("\nFlattened array (back to 1D):")
print(flattened)