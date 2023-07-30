# pcost.py
#
# Exercise 1.27

import csv


total_shares = []
share_prices = []

with open('Data/portfolio.csv', 'rt') as f:
    csv_reader = csv.DictReader(f)
        
    for row in csv_reader:
        price = float(row['price'])
        share_prices.append(price)
        shares = int(row['shares'])
        total_shares.append(shares)
    
total_cost = []
for i in range(0, len(total_shares)):
    total_cost.append(total_shares[i] * share_prices[i])
 

print ("Total cost", sum(total_cost))



# Read each file line by line
# Sort each line by it's list and excluding the first line
# Get the shares and price number and multipe it. 