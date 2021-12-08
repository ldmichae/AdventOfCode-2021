## All credit to Fortee, I can't do recursive programming :(
# %%
import csv

readings = []
with open('day6-data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    readings = list(csvreader)[0]

fish_squad = [int(x) for x in readings]
days = 256

known_fish = {}

def spawn_fish(fish, bday):
    if (fish, bday) in known_fish:
        return known_fish[(fish, bday)]
    else:
        spawn_day = fish + bday + 1

        total = 1

        while spawn_day <= days:
            total += spawn_fish(8, spawn_day)
            spawn_day += 7
        
        known_fish[(fish, bday)] = total
        return total

grand_total = 0
for idx, fish in enumerate(fish_squad):
    print(idx, len(fish_squad))
    grand_total += spawn_fish(fish, 0)

print(grand_total)

# %%
