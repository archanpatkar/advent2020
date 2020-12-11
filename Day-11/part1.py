import sys
sys.path.append("..")
from common import *

def parse(data):
    lines = data.split("\n")
    d = {}
    [d.update({point(x,y):lines[y][x]}) for y in range(len(lines)) for x in range(len(lines[y]))]
    return (d,lines)

data,ls = aoci(parse);
p(data)


iterations = 0 
consec = 0
last = -1
n = 0
while iterations < 5000 and consec < 10:
    if last == n:
        consec += 1
    last = n
    n = 0
    nd = {}
    for seat in data:
        occupied = -1
        if data[seat] != ".":
            adj = n8(seat)
            occupied = 0
            for p1 in adj:
                if(p1.x >= 0 and p1.y >= 0 and p1.x < len(ls[0]) and p1.y < len(ls)):
                    if data[p1] == "#":
                        occupied += 1
            print(occupied)
        if occupied == 0:
            nd[seat] = "#"
        elif occupied >= 4:
            nd[seat] = "L"
        else: nd[seat] = data[seat]
    for seat in nd: 
        if nd[seat] == "#": n += 1
    data = nd
    iterations += 1
print(n)