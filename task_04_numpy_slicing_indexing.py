
import numpy as np

# Create a NumPy array
array = np.array([3, 5, 6, 2, 8, 10, 20, 50])

print("Original array:")
print(array)

# Access the first element
print("\nFirst element:")
print(array[0])

# Select the first three elements
print("\nArray slicing:")
print(array[:3])

# Modify the first four elements
array[:4] = 7

print("\nModified array:")
print(array)

# Create a two-dimensional matrix
matrix = np.array([
    [6, 9, 7, 1],
    [6, 5, 5, 5],
    [6, 9, 1, 8],
    [8, 9, 3, 1]
])

print("\nOriginal matrix:")
print(matrix)

# Select the third row
print("\nThird row:")
print(matrix[2])

# Select a specific element
print("\nSelected element:")
print(matrix[0, 2])

# MINI CHALLENGE 4
# Replace the last row with zeros

X = np.array([
    [2, 30, 20, -2, -4],
    [3, 4, 40, -3, -2],
    [-3, 4, -6, 90, 10],
    [25, 45, 34, 22, 12],
    [13, 24, 22, 32, 37]
])

X[-1] = 0

print("\nMini Challenge 4:")
print(X)

