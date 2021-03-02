# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename = 'Data/portfolio.csv', select = None):
    '''
    Parse a CSV file into a list of records
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a selector is gived, find indices
        if select:
        	indices = [headers.index(colname) for colname in select]
        	headers = select
        else:
        	indices = []


        #records2 = [{colname: row[index] for colname, index in zip(select,indices)} for row in rows]
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            
            if indices:
            	row = [row[index] for index in indices]
            	#record = {colname: row[index] for colname, index in zip(select,indices)}
            
            record = dict(zip(headers,row))
            records.append(record)

    return records