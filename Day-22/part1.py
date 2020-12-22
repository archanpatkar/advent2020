import sys
sys.path.append("..")
from common import *

def parse(data):
    temp = data.split("\n")
    pls = []
    d = []
    for l in temp:
        nw = l.strip()
        if nw.isnumeric():
            d.append(int(nw))
        elif len(nw) == 0:
            pls.append(d)
            d = []
    pls.append(d)
    return [p for p in pls if len(p) != 0]

data = aoci(parse);
p(data);

rounds = 0
stacks = data
totallen = len(stacks[0]) + len(stacks[1])
while len(stacks[0]) > 0 and len(stacks[1]) > 0:
    one = stacks[0].pop(0)
    two = stacks[1].pop(0)
    if one > two: stacks[0].extend([one,two])
    else: stacks[1].extend([two,one])
    rounds += 1
p(stacks)

allnums = [*stacks[0],*stacks[1]]
score = 0
for j in range(len(allnums)):
    score += (allnums[j] * (totallen-j))
print("Score:",score)