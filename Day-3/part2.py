import sys
sys.path.append("..")
from common import *

def parse(line):
    return line*100

data = fnl(parse);
p(data);

all_trees = []
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for sl in slopes:
    treecount = 0
    x = 0
    y = 0
    while y < len(data) and x < len(data[0]):
        if data[y][x] == "#": treecount += 1
        x += sl[0]
        y += sl[1]
    all_trees.append(treecount)

mult = 1
for t in all_trees:
    mult *= t
print(mult)