import sys
sys.path.append("..")
from common import *

def parse(data):
    return data

data = fnl(parse);
p(data);

neighbours = {}
def get_neighbours(x,y,z):
    ns = neighbours.get((x,y,z))
    if not ns:
        ns = [(int(n[0]),int(n[1]),int(n[2])) for n in all_poss_var("xyz",["x","y","z"], { 
                "x":[str(x),str(x+1),str(x-1)],
                "y":[str(y),str(y+1),str(y-1)],
                "z":[str(z),str(z+1),str(z-1)] 
        })]
        neighbours[cube] = ns
    return ns

cubes = {}
for y in range(len(data)):
    for x in range(len(data[y])):
        cubes[(x,y,0)] = data[y][x]
        cube = cubes[(x,y,0)]
        for neighbour in get_neighbours(x,y,0):
            if neighbour != cube and (not (neighbour in cubes)):
                cubes[neighbour] = "."
p(cubes)

next = {}
for i in range(6):
    print("Iteration:",i)
    for cube in cubes:
        ns = get_neighbours(*cube)
        state = cubes[cube]
        active = 0
        for neighbour in ns:
            if neighbour != cube:
                if cubes.get(neighbour) == "#":
                    active += 1
                if not (neighbour in cubes):
                    next[neighbour] = "."
        next[cube] = "."
        if state == "#" and (active == 2 or active == 3):
            next[cube] = "#"
        elif state == "." and active == 3:
            next[cube] = "#"   
        print("cube:",cube)
        print("state:",state)
        print("active:",active)
        print("next state:",next[cube])         
    cubes = next
    next = {}

count = 0
for c in cubes:
    if cubes[c] == "#":
        count += 1 
print("active cubes:",count)