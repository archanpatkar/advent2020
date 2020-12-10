import sys
sys.path.append("..")
from common import *

def parse(data):
    return int(data)

data = [0] + fnl(parse);

data.sort()
data.append(data[-1]+3)
p(data);


graph = {}
for n in data:
    nodes = []
    for m in data:
        if n+1 == m: nodes.append(m)
        elif n+2 == m: nodes.append(m)
        elif n+3 == m: nodes.append(m)
    graph[n] = nodes
p(graph)
drawDGraph("numbers",graph,lambda n:str(n),format="svg",shape="circle",color="lightgrey")

def count(n,graph,visited={}):
    next = graph[n]
    if(len(next) == 0): return 1
    cc = 0
    for poss in next:
        if not poss in visited:
            visited[poss] = count(poss,graph)
            cc += visited[poss]
        else: cc += visited[poss]
    return cc

print(count(0,graph))