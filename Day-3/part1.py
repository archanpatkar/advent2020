import sys
sys.path.append("..")
from common import *

def parse(line):
    return line*100

data = fnl(parse);
p(data);

treecount = 0
x = 0
y = 0
while y < len(data) and x < len(data[0]):
    if data[y][x] == "#": treecount += 1
    x += 3
    y += 1
print(treecount)