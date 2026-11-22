
import pandas as pd

# Create bank clients DataFrame
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

# Select clients with more than 4 years
experienced_clients = bank_client_df[
    bank_client_df["Years with bank"] > 4
]

print("\nExperienced Clients:")
print(experienced_clients)

# Delete a column
modified_df = bank_client_df.drop(
    columns=["Bank client ID"]
)

print("\nDataFrame without Client ID:")
print(modified_df)

# MINI CHALLENGE 8
# Select clients with a minimum net worth of $5000

high_networth_df = bank_client_df[
    bank_client_df["Net worth [$]"] >= 5000
]

print("\nHigh Net Worth Clients:")
print(high_networth_df)

# Calculate combined net worth
total_networth = high_networth_df[
    "Net worth [$]"
].sum()

print("\nCombined Net Worth:")
print(total_networth)
