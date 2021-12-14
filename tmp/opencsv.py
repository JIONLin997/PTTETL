import csv

p = 0
n = 0
x = 0

with open('Pmamilovdatababycarrier.csv', newline='', encoding='utf-8') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        print("'" + row['PN'])
        if '+' in row['PN']:
            p += 1
        elif '-' in row['PN']:
            n += 1
        elif 'x' in row['PN']:
            x += 1

print(p,n,x)














