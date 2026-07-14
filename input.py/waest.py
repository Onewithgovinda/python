num=[1,2,3,4,5]
print(num)
from collections import defaultdict # count letters - the messy normal-dict way 
counts = {}
for ch in "banana": 
    if ch in counts: counts [ch] += 1 
    else: counts[ch] = 1 
# the clean defaultdict way counts = defaultdict (int) for ch in "banana": counts[ch] += 1 print(dict(counts))

# missing keys start at 0

# {'b' : 1, 'a': 3, 'n'