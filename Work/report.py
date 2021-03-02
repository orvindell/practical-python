# report.py
#
# Exercise 2.4
import sys
import csv



def read_portfolio(filename):
	portfolio = []

	with open(filename,'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			record = dict(zip(headers, row))

			stock = {
				'name' : record['name'],
				'shares': int(record['shares']),
				'price': float(record['price'])
			}

			portfolio.append(stock)

	return portfolio



def read_portfoliotuple(filename):
	portfolio = []

	with open(filename,'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			holding = (row[0], int(row[1]), float(row[2]))
			portfolio.append(holding)

	return portfolio


def read_portfoliodict(filename):
	portfolio = {}
	portfolio_list = []
	second_list = []

	with open(filename,'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:

			portfolio[headers[0]] = row[0]
			portfolio[headers[1]] = int(row[1])
			portfolio[headers[2]] = float(row[2])
			portfolio_list.append(portfolio.copy())

	return portfolio_list

def read_prices(filename):
	prices = {}

	with open(filename,'rt') as f: 
		rows = csv.reader(f)
		for row in rows:
			try:
				prices[row[0]] = float(row[1])
			except IndexError:
				print('Empty row')

	return prices

def make_report(portfolio, prices):
	price_report = []

	for s in portfolio:
		holding = (s['name'], s['shares'], prices[s['name']], prices[s['name']]-s['price'])
		price_report.append(holding)

	return price_report


def print_report(report):
	headers = ('Name', 'Shares', 'Price', 'Change')
	#space = ''
	#print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	#print(f'{space:->10s} {space:->10s} {space:->10s} {space:->10s} ')

	print('%10s %10s %10s %10s' % headers)
	print(('-' * 10 + ' ') * len(headers))
	for name,shares,price,diff in report:
		price = '$' + str(price)
		print(f'{name:>10s} {shares:>10d} {price:>10s} {diff:>10.2f}')

def portfolio_report(portfolio_filename = 'Data/portfolio.csv', prices_filename = 'Data/prices.csv'):
	portfolio = read_portfolio(portfolio_filename) #--- error + question
	new_prices = read_prices(prices_filename)
	report = make_report(portfolio,new_prices)

	print_report(report)

#portfolio = read_portfolio(filename)





#for s in portfolio:
#	value_before += s['shares']*s['price']
#	value_after += s['shares']*new_prices[s['name']]

#value_diff =  value_after - value_before

#print(f'Old value:{value_before:2.2f} New value:{value_after:2.2f} difference{value_diff:2.2f}')



