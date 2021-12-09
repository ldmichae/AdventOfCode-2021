# %%
import csv

readings = []
with open('day7-data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    readings = list(csvreader)[0]

readings = [int(i) for i in readings]  

test_input = [16,1,2,0,4,2,7,1,2,14]
# %%
