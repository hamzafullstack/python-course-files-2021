from csv import DictReader
# ordered dict
with open('small_data.csv','r') as file_one:
    csv_reader = DictReader(file_one)
    for rows in csv_reader:
        # print(rows)
        print(rows['name'])
# dictreader is better than reader