# %%
data = []
with open('day10-data.txt', 'r') as file:
    lines = file.readlines();   
    for line in lines:
        data.append(list(line.strip('\n')))

scoring = {')':3,']':57,'}':1197,'>':25137}

pairs = {'}':'{',')':'(',']':'[','>':'<'}

unclosed = []
score = 0
for sample in data:
    for idx, char in enumerate(sample):
        if char in list(pairs.values()):
            unclosed.append(char)
        else:
            if pairs[char] != unclosed[-1]:
                score += scoring[char]
                break
            else:
                unclosed = unclosed[:-1]
# %%
