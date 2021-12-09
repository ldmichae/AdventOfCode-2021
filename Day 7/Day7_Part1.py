# %%
import csv

readings = []
with open('day7-data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    readings = list(csvreader)[0]

readings = [int(i) for i in readings]  

test_input = [16,1,2,0,4,2,7,1,2,14]
# %%
res = {}
for i in range(0,max(readings)):
    running_total = 0
    for j in readings:
        running_total += abs(j - i)
    res[i] = running_total
# %%
