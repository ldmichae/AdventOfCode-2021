# %%
import csv

readings = []
with open('day2-data.csv', newline = '') as csvfile:
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        readings.append(row)
# %%
horizontal_position = 0
depth = 0

for direction, value in readings:
    if direction == 'forward':
        horizontal_position += int(value)
    elif direction == 'down':
        depth += int(value)
    elif direction == 'up':
        depth -= int(value)

print(f'Horizontal: {horizontal_position}, Depth: {depth}')
print(horizontal_position * depth)

# %%
## Test Data
readings = [
['forward', 5],
['down', 5],
['forward', 8],
['up', 3],
['down', 8],
['forward', 2],
]
