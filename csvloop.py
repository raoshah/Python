import csv

filename = "crypto.csv"
field = ['Name', 'Price']
rows = [['Bitcoin', '30000'],
    ['Etheream', '2000'],
    ['Solana', '30'],
    ['cosmos', '9']]

with open(filename, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)

with open(filename) as csvr:
    csvread = csv.reader(csvr)
    for coin in csvread:
        print(f"Name {coin[0]} Price {coin[1]} ")