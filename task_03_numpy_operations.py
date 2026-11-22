
import numpy as np

# Create two NumPy arrays
array_1 = np.arange(1, 10)
array_2 = np.arange(1, 10)

print("First array:")
print(array_1)

print("\nSecond array:")
print(array_2)

# Add two arrays
addition = array_1 + array_2

print("\nArray addition:")
print(addition)

# Calculate squares
squared = array_1 ** 2

print("\nSquared elements:")
print(squared)

# Calculate square roots
square_roots = np.sqrt(array_1)

print("\nSquare roots:")
print(square_roots)

# Calculate exponential values
exponential = np.exp(array_1)

print("\nExponential values:")
print(exponential)

# MINI CHALLENGE 3
# Calculate the values using X and Y

X = np.array([5, 7, 20])
Y = np.array([9, 15, 4])

Z = np.sqrt(X**2 + Y**2)

print("\nMini Challenge 3:")
print(Z)
