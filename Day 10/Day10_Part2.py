# %%
data = []
with open('day10-data.txt', 'r') as file:
    lines = file.readlines();   
    for line in lines:
        data.append(list(line.strip('\n')))

scoring = {')':3,']':57,'}':1197,'>':25137}

pairs = {'}':'{',')':'(',']':'[','>':'<'}
rev_pairs = {v:k for k,v in pairs.items()}

unclosed = []
score = 0
for sample in data:
    for idx, char in enumerate(sample):
        # print("=========================================")
        # print("")
        # print(f"Unclosed: {unclosed}")
        # print(f"Analyzing {char}")
        if char in list(pairs.values()):
            # print(f"Adding {char} to unclosed")
            unclosed.append(char)
        else:
            if pairs[char] != unclosed[-1]:
                # print(''.join(test[:(idx + 1)]))
                # print(f"Error! Found '{char}' at index {idx}, expected '{rev_pairs[unclosed[-1]]}'")
                score += scoring[char]
                break
            else:
                # print(f"Removing {pairs[char]} from unclosed")
                unclosed = unclosed[:-1]

# %%

# %%
