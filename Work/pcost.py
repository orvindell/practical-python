# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):

    with open('Data/'+ filename, 'rt') as f:
        total_cost = 0.0
        headers = next(f)

        for line in f:
            row = line.split(',')
            try:
                n_shares = int(row[1])
                share_price = float(row[2])
            except ValueError:
                print("Couldn't parse", line)
            total_cost += n_shares * share_price

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
