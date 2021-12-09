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
        running_total += sum(range(0, 1 + max(i,j) - min(i,j)))
    res[i] = running_total
# %%
print(min(res.values()))