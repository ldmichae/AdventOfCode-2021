# %%
import csv

readings = []
with open('day6-data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    readings = list(csvreader)[0]

readings = [int(i) for i in readings]  

# %%
day = 0
target_days = 80
fish_squad = readings

while day < target_days:
    print(day)
    []
    for i in range(len(fish_squad)):
        fishy = fish_squad[i]
        if fishy >= 1:
            fish_squad[i] -= 1
        else:
            fish_squad[i] = 6
            fish_squad.append(8)
    day += 1
print(len(fish_squad))          

# %%
