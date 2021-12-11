# %%
import csv

readings = []
with open('day6-data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    readings = list(csvreader)[0]

fish_squad = [(int(x),0) for x in readings]
days = 10
# %%
# On which days will each fish spawn?
fish_to_process = fish_squad
fish_spawned = len(fish_squad)
while(len(fish_to_process) > 0):
    for fish in fish_squad:
        day = 0
        total = 1
        while day < days:
            if (day - fish[0] - fish[1]) % 7 == 0:
                total += 1
                fish_to_process.append((6, day))
            day += 1
        fish_spawned += total

# %%
