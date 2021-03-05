# report.py
#
# Exercise 2.4
from . import fileparse
from . import tableformat
from .stock import Stock
from .portfolio import Portfolio

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file,
                                        select=['name','shares','price'],
                                        types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return Portfolio(portfolio)


    '''
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
    '''


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

    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))

    '''
    prices = {}

    with open(filename,'rt') as f: 
       rows = csv.reader(f)
       for row in rows:
         try:
          prices[row[0]] = float(row[1])
         except IndexError:
          print('Empty row')

    return prices
    '''

def make_report(portfolio, prices):
    price_report = []

    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        holding = (s.name, s.shares, prices[s.name], change)
        price_report.append(holding)

    return price_report


def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    #space = ''
    #print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    #print(f'{space:->10s} {space:->10s} {space:->10s} {space:->10s} ')

    #print('%10s %10s %10s %10s' % headers)
    #print(('-' * 10 + ' ') * len(headers))

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name,shares,price,change in reportdata:
       rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
       formatter.row(rowdata)
       #price = '$' + str(price)
       #print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename = 'Data/portfolio.csv', prices_filename = 'Data/prices.csv', fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    #Read data files
    portfolio = read_portfolio(portfolio_filename) #--- error + question
    new_prices = read_prices(prices_filename)
    
    #Create report data
    report = make_report(portfolio,new_prices)

    #Print the report
    formatter = tableformat.create_formatter(fmt)
    print_report(report,formatter)

#portfolio = read_portfolio(filename)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)




#for s in portfolio:
#   value_before += s['shares']*s['price']
#   value_after += s['shares']*new_prices[s['name']]

#value_diff =  value_after - value_before

#print(f'Old value:{value_before:2.2f} New value:{value_after:2.2f} difference{value_diff:2.2f}')



