    import csv

    def parse_csv(filename = 'Data/portfolio.csv', select = None, types = None):
        '''
        # Parse a CSV file into a list of records
        '''
        records = []
        with open(filename) as f:
            rows = csv.reader(f, delimiter =' ')


            # Read the file headers
            #headers = next(rows)

            # If a selector is gived, find indices to filter for
            #if select:
            #  indices = [headers.index(colname) for colname in select]
            #  headers = select
            #else:
            #  indices = []
            #records2 = [{colname: row[index] for colname, index in zip(select,indices)} for row in rows]
            for row in rows:
                if not row:    # Skip rows with no data
                    continue
               
                #if indices:
                #    row = (row[index] for index in indices)
                    #record = {colname: row[index] for colname, index in zip(select,indices)}

                if types:
                   print(f'Before {row} **************')

                   row = (types[0](row[0]), types[1](row[1]))

                   #row = func(val) for func,val in zip(types,row)
                   print(f'After {row} --------------')

                records.append(row)

        
        return records