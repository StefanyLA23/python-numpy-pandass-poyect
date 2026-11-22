
import numpy as np

# Create a one-dimensional array
my_list = [50, 60, 80, 100, 200, 300, 500, 600]

my_array = np.array(my_list)

print("One-dimensional array:")
print(my_array)

# Check the data type
print("\nArray type:")
print(type(my_array))

# Create a multi-dimensional array
matrix = np.array([
    [2, 5, 8],
    [7, 3, 6]
])

print("\nMulti-dimensional array:")
print(matrix)

# MINI CHALLENGE 1
# Create a 2x4 NumPy array

challenge_matrix = np.array([
    [3, 7, 9, 3],
    [4, 3, 2, 2]
])

print("\nMini Challenge 1:")
print(challenge_matrix)

print("Matrix shape:", challenge_matrix.shape)
