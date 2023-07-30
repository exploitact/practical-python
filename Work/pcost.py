# pcost.py
#
# Exercise 1.27

import csv


def portfolio_cost(file_name):

    total_shares = []
    share_prices = []

    with open(file_name, "rt") as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            try:
                price = float(row["price"])
                share_prices.append(price)
                shares = int(row["shares"])
                total_shares.append(shares)
            except ValueError as e:
                print(f"Error processing row: , {e}")
                continue

    total_cost = []
    for i in range(0, len(total_shares)):
        total_cost.append(total_shares[i] * share_prices[i])

    return sum(total_cost)


file_name = "Data/portfolio.csv"
cost = portfolio_cost(file_name)
print("Total cost:", cost)


# Read each file line by line
# Sort each line by it's list and excluding the first line
# Get the shares and price number and multipe it. 