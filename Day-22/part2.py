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

def game(stacks):
    p = ({},{})
    while len(stacks[0]) > 0 and len(stacks[1]) > 0:
        if p[0].get((*stacks[0],)) or p[1].get((*stacks[1],)): 
            return (0,stacks[0])
        temp = ((*stacks[0],),(*stacks[1],))
        one = stacks[0].pop(0)
        two = stacks[1].pop(0)
        winner = 0 if one > two else 1
        if one <= len(stacks[0]) and two <= len(stacks[1]):
            winner = game([stacks[0][:one],stacks[1][:two]])[0]
        if not winner: stacks[0].extend([one,two])
        else: stacks[1].extend([two,one])
        p[0][temp[0]] = True
        p[1][temp[1]] = True
    winner = 0 if len(stacks[0]) > 0 else 1
    return (winner,stacks[winner])

out = game([[*data[0]],[*data[1]]])
p(out)

score = 0
for j in range(len(out[1])):
    score += (out[1][j] * (len(out[1])-j))
print("Score:",score)