# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 170,
    "MSFT": 420
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Number of stocks user wants to enter
n = int(input("Enter number of different stocks: "))

portfolio = []

for i in range(n):

    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment

        portfolio.append((stock, quantity, price, investment))

        print("Investment for", stock, "=", investment)

    else:
        print("Stock not available in the list.")

# Display portfolio
print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity, price, investment in portfolio:
    print(
        stock,
        "| Quantity:", quantity,
        "| Price:", price,
        "| Investment:", investment
    )

print("\nTotal Investment Value =", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: {price} | Investment: {investment}\n"
        )

    file.write(f"\nTotal Investment Value = {total_investment}")

print("\nPortfolio saved successfully in portfolio.txt")