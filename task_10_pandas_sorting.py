
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

# Sort by years with bank
sorted_df = bank_client_df.sort_values(
    by="Years with bank"
)

print("\nSorted DataFrame:")
print(sorted_df)

# Verify the original DataFrame
print("\nOriginal DataFrame remains unchanged:")
print(bank_client_df)

# Sort and save changes in the original DataFrame
bank_client_df.sort_values(
    by="Years with bank",
    inplace=True
)

print("\nUpdated DataFrame:")
print(bank_client_df)

# Sort in descending order
descending_df = bank_client_df.sort_values(
    by="Years with bank",
    ascending=False
)

print("\nDescending Order:")
print(descending_df)
