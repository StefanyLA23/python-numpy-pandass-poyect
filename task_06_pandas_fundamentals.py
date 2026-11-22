
import pandas as pd

# Create a bank clients DataFrame
bank_client_df = pd.DataFrame({
    "Bank client ID": [111, 222, 333, 444],
    "Bank Client Name": [
        "Chanel", "Steve", "Mitch", "Ryan"
    ],
    "Net worth [$]": [3500, 29000, 10000, 2000],
    "Years with bank": [3, 4, 9, 5]
})

print("Bank Clients DataFrame:")
print(bank_client_df)

# Check the data type
print("\nData type:")
print(type(bank_client_df))

# Display first two rows
print("\nFirst two clients:")
print(bank_client_df.head(2))

# Display last row
print("\nLast client:")
print(bank_client_df.tail(1))

# MINI CHALLENGE 6
# Create a stock portfolio

portfolio_df = pd.DataFrame({
    "Stock Symbol": ["AAPL", "AMZN", "T"],
    "Price per Share [$]": [3500, 200, 40],
    "Number of Shares": [3, 4, 9]
})

# Calculate stock values
portfolio_df["Total Value"] = (
    portfolio_df["Price per Share [$]"]
    * portfolio_df["Number of Shares"]
)

print("\nStock Portfolio:")
print(portfolio_df)

# Calculate total portfolio value
total_portfolio = portfolio_df["Total Value"].sum()

print("\nTotal Portfolio Value:")
print(total_portfolio)
