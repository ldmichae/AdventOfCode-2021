# %%
import statistics

data = []
with open('day10-data.txt', 'r') as file:
    lines = file.readlines();   
    for line in lines:
        data.append(list(line.strip('\n')))

scoring = {')':1,']':2,'}':3,'>':4}

pairs = {'}':'{',')':'(',']':'[','>':'<'}
rev_pairs = {v:k for k,v in pairs.items()}

scores = []
for sample in data:
    score = 0
    unclosed = []
    error = False
    for idx, char in enumerate(sample):
        if char in list(pairs.values()):
            unclosed.append(char)
        else:
            if pairs[char] != unclosed[-1]:
                score += scoring[char]
                error = True
            else:
                unclosed = unclosed[:-1]
    if error:
        pass
    else:
        completion_extension = unclosed[::-1]
        for i in completion_extension:
            score = (score * 5) + scoring[rev_pairs[i]]
        scores.append(score)

result = statistics.median(scores)