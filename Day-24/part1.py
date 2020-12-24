import sys
sys.path.append("..")
from common import *

def parse(data):
    data = data.strip()
    temp = []
    prev = ""
    for ch in data:
        if (ch == "e" or ch == "w") and len(prev) == 0:
            temp.append(ch)
        elif ch == "e" or ch == "w" and len(prev):
            temp.append(prev+ch)
            prev = ""
        else:
            prev = ch
    return tuple(temp)

data = fnl(parse)
p(data)

# Three Axis
# e - w
# ne - sw
# nw - se

# Hexagonal Cordinate System based on -
# 1. https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0405/MARTIN/Hex.pdf
# 2. https://www.redblobgames.com/grids/hexagons/#:~:text=The%20cube%20coordinates%20are%20a,valid%20cube%20hex%20coordinate%20systems.
def getC(c):
    curr = [0,0,0]
    for d in c:
        if d == "e":
            curr[0] += 1
            curr[1] -= 1
        elif d == "w":
            curr[0] -= 1
            curr[1] += 1
        elif d == "ne":
            curr[0] += 1
            curr[2] -= 1
        elif d == "sw":
            curr[0] -= 1
            curr[2] += 1
        elif d == "nw":
            curr[1] += 1
            curr[2] -= 1
        elif d == "se":
            curr[1] -= 1
            curr[2] += 1
    return tuple(curr)

cords = [getC(c) for c in data]
color = defaultdict(lambda: False)
for c in cords: color[c] = not color[c]
count = sum([1 for c in color if color[c]])
print("Black Tiles:",count)