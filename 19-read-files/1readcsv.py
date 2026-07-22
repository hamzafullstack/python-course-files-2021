#read csv file
from csv import reader # csv module
with open('small_data.csv', 'r') as my_file:
    csv_reader = reader(my_file)
    # lets check the type of csvreader
    #print(type(csv_reader))
    # ouhh hahha it is a iterator i can loop on it
    next(csv_reader)
    for row in csv_reader: # we can also convert it into list
        print(row)