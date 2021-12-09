# %%
key = {0:['a','b','c','e','f','g'],
       1:['c','f'],
       2:['a','c','d','e','g'],
       3:['a','c','d','f','g'],
       4:['b','c','d','f'],
       5:['a','b','d','f','g'],
       6:['a','b','d','e','f','g'],
       7:['a','c','f'],
       8:['a','b','c','d','e','f','g'],
       9:['a','b','c','d','f','g']
       }

signal_init = []
outputs_init = []
with open('day8-data.txt', 'r') as file:
    lines = file.readlines();   
    for line in lines:
        signal_init.append(line.split('|')[0].split(' ')) 
        outputs_init.append(line.split('|')[1].split(' '))

signals = []
for lst in signal_init:
    for item in lst:
        if item != '':
            signals.append(item.split('\n')[0])
        else:
            pass

outputs = []
for lst in outputs_init:
    for item in lst:
        if item != '':
            outputs.append(item.split('\n')[0])
        else:
            pass

# %%
# [word for word in outputs if sorted(set(list(word))) == key[1]]
uq_lengths = [2,4,3,7]
uq_outputs = []
[uq_outputs.append(word) for word in outputs if len(word) in uq_lengths]
print(len(uq_outputs))
# %%
