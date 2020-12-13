import sys
sys.path.append("..")
from common import *

def parse(data):
    lines = data.split("\n");
    return (int(lines[0]),list(map(lambda x: int(x),filter(lambda x: x != "x",lines[1].split(",")))))

data = aoci(parse);
p(data);

goal = data[0]
i = [0 for i in range(0,len(data[1]))]
for bus in range(len(data[1])):
    n = data[1][bus]
    while i[bus] < goal:
        i[bus] += n
print(goal)

for n in range(len(i)):
    print("-------")
    print(data[1][n])
    print(i[n])
    print(goal-i[n])
    print("ans:")
    print(data[1][n]*(i[n]-goal))