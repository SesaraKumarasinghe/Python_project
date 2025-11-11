import csv
from tabulate import tabulate

with open("Places Dataset.csv", 'r',newline="",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)

header = data[0]
rows = data[1:]

table = tabulate(rows, headers=header, tablefmt='simple')

with open("data.txt", 'w') as f:
    f.write(table)
