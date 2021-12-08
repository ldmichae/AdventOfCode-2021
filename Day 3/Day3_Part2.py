# %%
from collections import Counter
from itertools import groupby

readings = []
with open('day3-data.txt', 'r') as file:
    lines = file.readlines();    
    [readings.append(i.split('\n')[0]) for i in lines]

def multi_mode(lst):
    # group most_common output by frequency
    freqs = groupby(Counter(lst).most_common(), lambda x:x[1])
    # pick off the first group (highest frequency)
    res = [val for val,count in next(freqs)[1]]
    return res

def oxygen_rating_calculator(digit):
    oxygen_split_lst = [x[digit] for x in oxygen_lst]
    most_common = multi_mode(oxygen_split_lst)
    if len(most_common) == 1:
        return int(most_common[0])
    else:
        return int(max(most_common))

def carbon_rating_calculator(digit):
    carbon_split_lst = [x[digit] for x in carbon_diox_lst]
    most_common = multi_mode(carbon_split_lst)
    if len(most_common) == 1:
        return abs(int(most_common[0])-1)
    else:
        return int(min(most_common))

def filter_lst(lst, digit, value):
    res = [i for i in lst if i[digit] == str(value)]
    return res
    
# %%
oxygen_lst = readings.copy()
oxygen = ''

for x in range(len(readings[0])):
    if len(oxygen_lst) > 1 :
        oxy_val = oxygen_rating_calculator(x)
        print(oxy_val)
        oxy_filt = filter_lst(oxygen_lst, x, oxy_val)
        oxygen_lst = oxy_filt
        print(oxygen_lst)
    else:
        pass

carbon_diox_lst = readings.copy()
carbon = ''

for y in range(len(readings[0])):
    if len(carbon_diox_lst) > 1:
        carbon_val = carbon_rating_calculator(y)
        print(carbon_val)
        carbon_filt = filter_lst(carbon_diox_lst, y, carbon_val)
        carbon_diox_lst = carbon_filt
        print(carbon_diox_lst)
    else:
        pass        
oxygen = int(oxygen_lst[0],2)
carbon = int(carbon_diox_lst[0],2)

print(f'Oxygen: {oxygen}, Carbon: {carbon}')

print(f'Result: {oxygen * carbon}')


# %%
test_values = [
'00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010'
]


# %%
