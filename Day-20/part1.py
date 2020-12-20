from os import rename
import sys
sys.path.append("..")
from common import *

def parse(data):
    lines = data.split("\n")
    tiles = {}
    tile = None
    buff = []
    for i in range(len(lines)):
        curr = lines[i]
        if len(curr) < 1: 
            tiles[tile] = buff
            tile = None
            buff = []
        elif sw(curr,"Tile"):
            tile = int(curr.split(" ")[1][:-1])
        else:
            buff.append(curr)
    tiles[tile] = buff
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
p(borders)

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
p(matches)

val = 1
for m in matches:
    if len(matches[m]) == 2:
        print(m)
        val *= m
print("Value:",val)