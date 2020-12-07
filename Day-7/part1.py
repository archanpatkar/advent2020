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
    graph[n[0][:-4].strip()] = [e.split(" ",1)[1][:-4].strip() for e in n[1]]
p(graph)
graph["other"] = []

def rec_count(graph,node,visited=[]):
    p = []
    for n in graph:
        for b in graph[n]:
            if(b == node):
                p.append(n)
                break
    for n in p:
        if not (n in visited):
            rec_count(graph,n,visited)
            visited.append(n)
    return visited

o = rec_count(graph,"shiny gold")
print(len(o))
o.append("shiny gold")

# VIZ
ng = {}
for p in o:
    ng[p] = [n for n in graph[p] if n in o]
drawGraph("part1",ng)