
import pandas as pd

# STEP 1: Create the first bank clients DataFrame
Bank_df_1 = pd.DataFrame({
    "Bank Client ID": [1, 2, 3, 4, 5],
    "First Name": [
        "Nancy", "Alex", "Shep", "Max", "Allen"
    ],
    "Last Name": [
        "Rob", "Ali", "George", "Mitch", "Steve"
    ]
})

print("First Bank Clients:")
print(Bank_df_1)

# STEP 2: Create the second bank clients DataFrame
Bank_df_2 = pd.DataFrame({
    "Bank Client ID": [6, 7, 8, 9, 10],
    "First Name": [
        "Bill", "Dina", "Sarah", "Heather", "Holly"
    ],
    "Last Name": [
        "Christian", "Mo", "Steve", "Bob", "Michelle"
    ]
})

print("\nSecond Bank Clients:")
print(Bank_df_2)

# STEP 3: Create the annual salary DataFrame
bank_df_salary = pd.DataFrame({
    "Bank Client ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
    "Annual Salary [$/year]": [
        25000, 35000, 45000, 48000, 49000,
        32000, 33000, 34000, 23000, 22000
    ]
})

print("\nAnnual Salary Data:")
print(bank_df_salary)

# STEP 4: Concatenate the two bank DataFrames
bank_df_all = pd.concat(
    [Bank_df_1, Bank_df_2],
    ignore_index=True
)

print("\nAll Bank Clients:")
print(bank_df_all)

# STEP 5: Merge bank clients with annual salaries
bank_df_all = pd.merge(
    bank_df_all,
    bank_df_salary,
    on="Bank Client ID"
)

print("\nClients with Annual Salaries:")
print(bank_df_all)

# STEP 6: Create a new bank client
new_client_df = pd.DataFrame({
    "Bank Client ID": [11],
    "First Name": ["Ry"],
    "Last Name": ["Aly"],
    "Annual Salary [$/year]": [1000]
})

print("\nNew Bank Client:")
print(new_client_df)

# STEP 7: Add the new client to the DataFrame
new_df = pd.concat(
    [bank_df_all, new_client_df],
    ignore_index=True
)

print("\nFinal Bank Database:")
print(new_df)

# STEP 8: Export final database to CSV
new_df.to_csv(
    "final_bank_database.csv",
    index=False
)

print("\nDatabase exported successfully!")
