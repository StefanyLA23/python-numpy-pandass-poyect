
import numpy as np

# Create a NumPy matrix
matrix = np.array([
    [4, 4, 3, 9, 6],
    [9, 9, 8, 9, 2],
    [4, 2, 1, 3, 3],
    [8, 1, 1, 6, 3],
    [1, 3, 6, 8, 8]
])

print("Original matrix:")
print(matrix)

# Select elements greater than 7
greater_than_seven = matrix[matrix > 7]

print("\nElements greater than 7:")
print(greater_than_seven)

# Select odd numbers
odd_numbers = matrix[matrix % 2 == 1]

print("\nOdd numbers:")
print(odd_numbers)

# MINI CHALLENGE 5
# Replace negative numbers with 0
# Replace odd numbers with -2

X = np.array([
    [2, 30, 20, -2, -4],
    [3, 4, 40, -3, -2],
    [-3, 4, -6, 90, 10],
    [25, 45, 34, 22, 12],
    [13, 24, 22, 32, 37]
])

X[X < 0] = 0
X[X % 2 == 1] = -2

print("\nMini Challenge 5:")
print(X)
