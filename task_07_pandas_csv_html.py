
import pandas as pd

# Create sample customer data
customers_df = pd.DataFrame({
    "First Name": ["Joseph", "Noah", "Nina"],
    "Last Name": ["Patton", "Moran", "Keller"],
    "Email": [
        "daafeja@boh.jm",
        "guutodi@bigwoc.kw",
        "azikez@gahew.mr"
    ],
    "Postal Code": [
        "M6U 5U7", "K2D 4M9", "S1T 4E6"
    ],
    "Net Worth": [2629.13, 8626.96, 9072.02]
})

# Export to CSV
customers_df.to_csv("customers.csv", index=False)

# Read CSV file
bank_df = pd.read_csv("customers.csv")

print("CSV Data:")
print(bank_df)

# Display first rows
print("\nFirst two rows:")
print(bank_df.head(2))

# Read HTML tables from a website
url = "https://www.ssa.gov/oact/progdata/nra.html"

try:
    html_tables = pd.read_html(url)

    print("\nNumber of HTML tables:")
    print(len(html_tables))

    print("\nFirst HTML table:")
    print(html_tables[0])

except Exception as error:
    print("\nUnable to import HTML data:")
    print(error)

# MINI CHALLENGE 7
# Import US retirement age data

try:
    retirement_age_df = pd.read_html(url)

    print("\nUS Retirement Age Data:")
    print(retirement_age_df[0])

except Exception as error:
    print("\nRetirement data could not be loaded:")
    print(error)
