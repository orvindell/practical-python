# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):

    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

    '''
    with open(filename, 'rt') as f:
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
    '''

def portfolio_costx(filename):

    with open(filename, 'rt') as f:
        total_cost = 0.0
        rows = csv.reader(f)
        headers = next(rows)

        for rowno,row in enumerate(rows,start=1):
            record = dict(zip(headers,row))
            try:
                n_shares = int(record['shares'])
                share_price = float(record['price'])
                total_cost += n_shares * share_price
            except ValueError:
                print(f'Couldnt parse rowno {rowno} line{row}')
            

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_costx(filename)
print('Total cost:', cost)
