# %%
import csv

readings = []
with open('day1-data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        readings.append(int(row[0]))
        
group_sums = []
for first, second, third in zip(readings, readings[1:], readings[2:]):
    temp_sum = first + second + third
    group_sums.append(temp_sum)
    

num_increases = 0
for previous, current in zip(group_sums, group_sums[1:]):
    if current > previous:
        num_increases += 1
    else:
        pass
print(num_increases)
