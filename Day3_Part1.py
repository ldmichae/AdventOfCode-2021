# %%
from statistics import mode

readings = []
with open('day3-data.txt', 'r') as file:
    lines = file.readlines();    
    [readings.append(i.split('\n')[0]) for i in lines]

def bit_flipper(input_val):
    return (abs(input_val - 1))

# %%
counts = {}
for j in readings:
    val = str(j)
    for i in range(len(val)):
        if i not in counts.keys():
            counts[i] = [int(val[i])]  
        else:
            counts[i].append(int(val[i]))
            
gamma_stats = {k:mode(v) for k,v in counts.items()}
epsilon_stats = {k:mode(list(map(bit_flipper, v))) for k,v in counts.items()}
gamma = "".join([str(i) for i in list(gamma_stats.values())])
epsilon = "".join([str(i) for i in list(epsilon_stats.values())])

gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon,2)

result = gamma_decimal * epsilon_decimal
print(result)


# %%
readings = [
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
