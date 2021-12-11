# %%
import functools
key = {0:'abcefg',
       1:'cf',
       2:'acdeg',
       3:'acdfg',
       4:'bcdf',
       5:'abdfg',
       6:'abdefg',
       7:'acf',
       8:'abcdefg',
       9:'abcdfg'
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

total = 0
for signal in range(len(signals)):
    uq_lengths = {k:len(v) for k,v in key.items() if len(list(v)) in [2,4,3,7]}
    uq_words = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    [uq_words[length].extend(list(word)) for length in uq_lengths.keys() for word in signals[signal] if len(word) == uq_lengths[length]]

    knowns = {}

    missing = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0
    }

    for i in ['a','b','c','d','e','f','g']:
        for word in signals[signal]:
            if i not in word:
                missing[i] += 1


    knowns['a'] = list(set(uq_words[7]) - set(uq_words[1]))[0]
    knowns['b'] = [k for k, v in missing.items() if v == 4][0]

    search_for_c = [k for k, v in missing.items() if v == 2]
    search_for_c.remove(knowns['a'])
    knowns['c'] = search_for_c[0]

    knowns['e'] = [k for k, v in missing.items() if v == 6][0]
    knowns['f'] = [k for k, v in missing.items() if v == 1][0]

    knowns['d'] = [i for i in uq_words[4] if i not in knowns.values()][0]

    search_for_g = [k for k, v in missing.items() if v == 3]
    search_for_g.remove(knowns['d'])
    knowns['g'] = search_for_g[0]


    translator = dict(sorted({v:k for k,v in knowns.items()}.items()))
    rev_key = {v:k for k,v in key.items()}

    res = []
    for word in range(len(outputs[signal])):
        t = list(outputs[signal][word])
        n = ''.join(sorted([translator.get(item,item)  for item in t]))
        f = rev_key.get(n,n)
        res.append(str(f))
    total += int(''.join(res))
    # %%
