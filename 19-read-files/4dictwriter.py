from csv import DictWriter
with open('add_data.csv', 'w') as f:
    csv_writer = DictWriter(f,fieldnames=['first_name','last_name','age'])
    csv_writer.writeheader()
    # writerow and writerows
    csv_writer.writerow({
        'first_name' : 'Hamza',
        'last_name' : 'Baloch',
        'age' : 21
    })

# writerows.....>
#csv_writer.writerows([
#  {}
#  {}
#  {}
# ])
# dict inside the list