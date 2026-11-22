
import numpy as np

# Generate 20 random numbers between 0 and 1
random_numbers = np.random.rand(20)

print("Random numbers:")
print(random_numbers)

# Generate a 3x3 random matrix
random_matrix = np.random.rand(3, 3)

print("\nRandom matrix:")
print(random_matrix)

# Generate one random integer
random_integer = np.random.randint(1, 100)

print("\nRandom integer:")
print(random_integer)

# Generate 15 random integers
random_integers = np.random.randint(1, 100, 15)

print("\nRandom integers:")
print(random_integers)

# Generate numbers from 1 to 49
sequence = np.arange(1, 50)

print("\nNumber sequence:")
print(sequence)

# Create a 7x7 identity matrix
identity_matrix = np.eye(7)

print("\nIdentity matrix:")
print(identity_matrix)

# Create a matrix of ones
ones_matrix = np.ones((7, 7))

print("\nMatrix of ones:")
print(ones_matrix)

# Create an array of zeros
zeros_array = np.zeros(8)

print("\nArray of zeros:")
print(zeros_array)

# MINI CHALLENGE 2
# Generate 10 random integers between 0 and x

x = int(input("\nEnter a positive integer: "))

if x > 0:
    challenge_array = np.random.randint(0, x + 1, 10)
    print("\nMini Challenge 2:")
    print(challenge_array)
else:
    print("Please enter a positive integer.")
