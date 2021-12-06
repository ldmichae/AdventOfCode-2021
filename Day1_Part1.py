import csv

readings = []
with open('day1-data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        readings.append(int(row[0]))
        
num_increases = 0
for previous, current in zip(readings, readings[1:]):
    if current > previous:
        num_increases += 1
    else:
        pass
print(num_increases)


