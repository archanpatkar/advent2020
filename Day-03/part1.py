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
xl = []
yl = []
tl = []
while y < len(data) and x < len(data[0]):
    xl.append(x)
    yl.append(y)
    tl.append(treecount)
    if data[y][x] == "#": treecount += 1
    x += 3
    y += 1
print(treecount)
scatter3d(xl,yl,tl,"Part1","X","Y","Trees")