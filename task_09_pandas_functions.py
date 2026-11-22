
import pandas as pd

# Create a DataFrame
bank_client_df = pd.DataFrame({
    "Bank client ID": [111, 222, 333, 444],
    "Bank Client Name": [
        "Chanel", "Steve", "Mitch", "Ryan"
    ],
    "Net worth [$]": [3500, 29000, 10000, 2000],
    "Years with bank": [3, 4, 9, 5]
})

print("Original DataFrame:")
print(bank_client_df)

# Define a function to increase net worth by 20%
def increase_networth(balance):
    return balance * 1.20

# Apply the function
updated_networth = bank_client_df[
    "Net worth [$]"
].apply(increase_networth)

print("\nNet Worth Increased by 20%:")
print(updated_networth)

# Calculate the length of client names
name_length = bank_client_df[
    "Bank Client Name"
].apply(len)

print("\nClient Name Length:")
print(name_length)

# MINI CHALLENGE 9
# Triple net worth and add $200

def networth_update(balance):
    return balance * 3 + 200

# Apply the function
results = bank_client_df[
    "Net worth [$]"
].apply(networth_update)

print("\nUpdated Net Worth:")
print(results)

# Calculate updated total
total_networth = results.sum()

print("\nUpdated Combined Net Worth:")
print(total_networth)
