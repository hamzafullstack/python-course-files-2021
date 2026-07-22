from csv import writer
with open('data.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    # methods==> writerow, writerows
    csv_writer.writerow(['Name', 'Country'])
    csv_writer.writerow(['Ali Haider', 'PAKISTAN'])
    csv_writer.writerow(['Ishu Rahal', 'INDIA'])
    csv_writer.writerow(['Boril Boyanov', 'BULGARIA'])

#csv_writer.writerows([['Name', 'Country'],['Ali Haider', 'PAKISTAN'],['Ishu Rahal', 'INDIA'],['Boril Boyanov', 'BULGARIA']])