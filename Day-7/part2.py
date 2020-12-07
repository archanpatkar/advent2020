import sys
import math
sys.path.append("..")
from common import *

def parse(data):
    d = data[:-1].split("contain")
    return (d[0].strip(),[c.strip() for c in d[1].split(",")])

data = fnl(parse);
graph = {}
for n in data:
    graph[n[0][:-4].strip()] = [(e.split(" ",1)[0],e.split(" ",1)[1][:-4].strip()) for e in n[1]]
p(graph)

def n_count(graph,node,cache={}):
    i = 0
    for n in graph[node]:
        if(n[1] != "other"): 
            t = 0
            if n[1] in cache: t = cache[n[1]]
            else: 
                t = n_count(graph,n[1],cache)
                cache[n[1]] = t
            nt = int(n[0])
            i += nt + (nt*t)
    return i

o = n_count(graph,"shiny gold")
print(o)
