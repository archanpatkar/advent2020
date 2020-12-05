import sys
import math
sys.path.append("..")
from common import *

def parse(data):
    return (data[0:7],data[7:])

data = fnl(parse);
p(data);

def decode(data,m="F",init=127):
    lower = 0
    upper = init
    last = True
    for ch in data:
        if ch == m: 
            last = True
            upper = (upper - (upper-lower+1)//2)
        else: 
            last = False
            lower = (upper - (upper-lower)//2)
    if last: return upper;
    return lower;

rc = []
ids = []
for seat in data:
    seat = (decode(seat[0]),decode(seat[1],"L",7))
    rc.append(seat)
    ids.append((seat[0]*8)+seat[1])
ids.sort()

i = 0
openseats = []
while i < (len(ids)-2):
    first = ids[i]
    second = ids[i+1]
    if ((first+1) == (second-1)):
        openseats.append(first+1);
        break;
    i += 1
print(openseats)