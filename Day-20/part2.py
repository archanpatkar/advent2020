import sys
sys.path.append("..")
from common import *

# Very bad awfully redundant ~SLOW~ code!
def parse(data):
    lines = data.split("\n")
    tiles = {}
    tile = None
    buff = []
    for i in range(len(lines)):
        curr = lines[i]
        if len(curr) < 1: 
            tiles[tile] = tuple(buff)
            tile = None
            buff = []
        elif sw(curr,"Tile"):
            tile = int(curr.split(" ")[1][:-1])
        else:
            buff.append(tuple(curr))
    tiles[tile] = tuple(buff)
    return tiles

data = aoci(parse);
p(data);

borders = {} 
for tile in data:
    left = []
    right = []
    for line in data[tile]:
        left.append(line[0])
        right.append(line[-1])
    borders[tile] = ((*left,),(*right,),tuple(data[tile][0]),tuple(data[tile][-1]))

def check(tile1,tile2):
    l = len(borders[tile1])
    for border1 in range(l):
        for border2 in range(l):
            b1 = borders[tile1][border1]
            b2 = borders[tile2][border2]
            if b1 == b2:
                return (border1,border2)
            if b1[::-1] == b2:
                return (border1,border2)
            if b1 == b2[::-1]:
                return (border1,border2)
            if b1[::-1] == b2[::-1]:
                return (border1,border2)

matches = {tile:[] for tile in borders}
for tile1 in borders:
    for tile2 in borders:
        if tile1 != tile2:
            pos = check(tile1,tile2)
            if pos:
                matches[tile1].append({
                    "pos": pos,
                    "tile1":tile1,
                    "tile2":tile2
                })

corners = []
for m in matches:
    if len(matches[m]) == 2:
        corners.append(m)

tilegraph = {}
for m in matches:
    if not tilegraph.get(m):
        tilegraph[m] = []
    for d in matches[m]:
        tilegraph[m].append(d["tile2"])

def flip(tile,w):
    if w == 0:
        return tile[::-1]
    elif w == 1:
        return tuple(l[::-1] for l in tile)
    return tile

def cwrotate(data):
    nt = [["" for c in r] for r in data]
    l = len(data[0])
    for i in range(len(data)):
        for j in range(l):
            nt[i][j] = data[l-j-1][i]
    return tuple((*l,) for l in nt)

def acwrotate(data):
    nt = [["" for c in r] for r in data]
    l = len(data[0])
    for i in range(len(data)):
        for j in range(l):
            nt[i][j] = data[j][l-i-1]
    return tuple((*l,) for l in nt)

def dgrid(data):
    buff = ""
    for l in data:
        buff += "{}\n".format("".join([str(i) for i in l]))
    print(buff)

def getall(tile):
    variations = set()
    curr1 = data[tile] if isinstance(tile,int) else tile
    curr2 = data[tile] if isinstance(tile,int) else tile
    variations.add(data[tile] if isinstance(tile,int) else tile)
    for i in range(3):
        curr1 = cwrotate(curr1)
        curr2 = acwrotate(curr2)
        variations.add(curr1)
        variations.add(curr2)
    curr1 = flip(data[tile] if isinstance(tile,int) else tile,0)
    curr2 = curr1
    variations.add(curr1)
    for i in range(3):
        curr1 = cwrotate(curr1)
        curr2 = acwrotate(curr2)
        variations.add(curr1)
        variations.add(curr2)
    curr1 = flip(data[tile] if isinstance(tile,int) else tile,1)
    curr2 = curr1
    variations.add(curr1)
    for i in range(3):
        curr1 = cwrotate(curr1)
        curr2 = acwrotate(curr2)
        variations.add(curr1)
        variations.add(curr2)
    return variations
    
all_vars = {tile:getall(tile) for tile in data}
poss = list(all_vars.keys())
gsize = int(sqrt(len(poss)))
print("grid size:",gsize)

def getborder(tile,data=data):
    curr = data[tile] if isinstance(tile,int) else tile
    left = []
    right = []
    for line in curr:
        left.append(line[0])
        right.append(line[-1])
    if isinstance(tile,int): return (data[tile][0],(*right,),data[tile][-1],(*left,))
    else: return (tile[0],(*right,),tile[-1],(*left,))

def check1(b1,b2):
    return b1[1] == b2[3] and (not (b1[3] == b2[1]))

def check2(b1,b2):
    return b1[2] == b2[0] and (not (b1[0] == b2[2]))

topleft = None
right = None
down = None
for tile1 in corners:
    vars = all_vars[tile1]
    for v in vars:
        right = None
        down = None
        b1 = getborder(v)
        found = False
        for tile2 in tilegraph[tile1]:
            if tile1 != tile2:
                for v2 in all_vars[tile2]:
                    b2 = getborder(v2)
                    if check1(b1,b2): 
                        right = (tile2,v2)
                    elif check2(b1,b2): 
                        down = (tile2,v2)
                    if right != None and down != None and right[0] != down[0]:
                        found = True
                        break
            if found:
                break
        if found:
            topleft = (tile1,v)
            break

maingrid = [[None for j in range(gsize)] for i in range(gsize)]

maingrid[0][0] = topleft
maingrid[0][1] = right
maingrid[1][0] = down
used = set([topleft[0],right[0],down[0]])

last = maingrid[0][1]
for col in range(2,len(maingrid[0])):
    b1 = getborder(last[1])
    found = False
    for tile in tilegraph[last[0]]:
        if not(tile in used):
            vars = all_vars[tile]
            for v in vars:
                b2 = getborder(v)
                if check1(b1,b2):
                    maingrid[0][col] = (tile,v)
                    used.add(tile)
                    found = True
                    break
            if found: break
    last = maingrid[0][col]

for r in range(1,len(maingrid)):
    last = maingrid[r][0]
    if not last:
        t = getborder(maingrid[r-1][0][1])
        found = False
        for tile in poss:
            if not(tile in used):
                vars = all_vars[tile]
                for v in vars:
                    b2 = getborder(v)
                    if check2(t,b2):
                        maingrid[r][0] = (tile,v)
                        used.add(tile)
                        found = True
                        break
                if found: break
        last = maingrid[r][0]
    for col in range(1,len(maingrid[0])):
        b1 = getborder(last[1])
        found = False
        for tile in tilegraph[last[0]]:
            if not(tile in used):
                vars = all_vars[tile]
                for v in vars:
                    b2 = getborder(v)
                    t = getborder(maingrid[r-1][col][1])
                    if check1(b1,b2) and check2(t,b2):
                        maingrid[r][col] = (tile,v)
                        used.add(tile)
                        found = True
                        break
                if found: break
        last = maingrid[r][col]

print("GRID:")
p([[t[0] for t in r] for r in maingrid])

def merge(t1,t2): return tuple(t1[i]+t2[i] for i in range(len(t1)))
def process(t): return [r[1:-1] for r in t[1:-1]]

final = []
for r in maingrid:
    final.extend(reduce(lambda acc,v: merge(acc,process(v[1])),r[1:],process(r[0][1])))

all_final_images = getall(tuple(final))

monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")

nh = sum([sum([1 for ch in r if ch == "#"]) for r in final])
mnh = sum([sum([1 for ch in r if ch == "#"]) for r in monster])

def create_window(template=monster,mchar="#"):
    cords = {}
    for x in range(len(template)):
        for y in range(len(template[x])):
            if template[x][y] != " ":
                cords[(x,y)] = mchar if mchar else template[x][y]
    return (cords,len(template),len(template[0]))

monster_window = create_window()

def slide(data,window=monster_window): 
    cords,xl,yl = window
    ncount = 0
    pos = []
    for x in range(0,len(data)-xl):
        for y in range(0,len(data[x])-yl):
            flag = True
            for c in cords:
                if not (data[x+c[0]][y+c[1]] == cords[c]):
                    flag = False
                    break
            if flag:
                pos.append((x,y))
                ncount += 1
    return (ncount,pos)

orientation = None
start_pos = None
monsters = 0
for i in all_final_images:
    n,pos = slide(i)
    if n > 0:
        orientation = i
        start_pos = pos
        monsters = n
        break
print("Monsters:",monsters)
print("Answer:",nh-(monsters*mnh))