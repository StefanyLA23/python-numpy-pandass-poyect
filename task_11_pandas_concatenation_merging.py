
import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"]
})

# Create the second DataFrame
df2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"]
})

# Create the third DataFrame
df3 = pd.DataFrame({
    "A": ["A8", "A9", "A10", "A11"],
    "B": ["B8", "B9", "B10", "B11"],
    "C": ["C8", "C9", "C10", "C11"],
    "D": ["D8", "D9", "D10", "D11"]
})

print("First DataFrame:")
print(df1)

print("\nSecond DataFrame:")
print(df2)

print("\nThird DataFrame:")
print(df3)

# Concatenate DataFrames vertically
combined_df = pd.concat(
    [df1, df2, df3],
    ignore_index=True
)

print("\nConcatenated DataFrame:")
print(combined_df)

# Merge example using a common ID
clients_df = pd.DataFrame({
    "Client ID": [1, 2, 3],
    "Client Name": ["Nancy", "Alex", "Ryan"]
})

salary_df = pd.DataFrame({
    "Client ID": [1, 2, 3],
    "Annual Salary": [25000, 35000, 45000]
})

merged_df = pd.merge(
    clients_df,
    salary_df,
    on="Client ID"
)

print("\nMerged DataFrame:")
print(merged_df)
