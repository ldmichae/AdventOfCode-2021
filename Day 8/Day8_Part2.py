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
with open('day8-test-data.txt', 'r') as file:
    lines = file.readlines();   
    for line in lines:
        signal_init.append(line.split('|')[0].split(' ')) 
        outputs_init.append(line.split('|')[1].split(' '))

signals = []
for lst in signal_init:
    tlst = []
    for item in lst:
        if item != '':
            tlst.append(item.split('\n')[0])
        else:
            pass
    signals.append(tlst)

outputs = []
for lst in outputs_init:
    tlst = []
    for item in lst:
        if item != '':
            tlst.append(item.split('\n')[0])
        else:
            pass
    outputs.append(tlst)

# %%
uq_lengths = {k:len(v) for k,v in key.items() if len(v) in [2,4,3,7]}
uq_words = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
[uq_words[length].append(word) for length in uq_lengths.keys() for word in signals[0] if len(word) == uq_lengths[length]]
# %%
