import sys
sys.path.append("..")
from common import *

def parse(data):
    lines = data.split("\n")
    items = []
    for l in lines:
        u,a = l.split("(")
        i = tuple(u.strip().split(" "))
        items.append((i,tuple(e.strip() for e in a[8:-1].split(","))))
    return items

data = aoci(parse);
p(data);

inc = {}
all = {}
for food in data:
    for i in food[0]:
        if not inc.get(i):
            inc[i] = {
                "count":0,
                "aller": {}
            }
        inc[i]["count"] += 1
        for a in food[1]:
            if not all.get(a):
                all[a] = {}
            if not all[a].get(i):
                all[a][i] = 0
            if not inc[i]["aller"].get(a):
                inc[i]["aller"][a] = 0
            inc[i]["aller"][a] += 1
            all[a][i] += 1
p(inc)
p(all)

assign = {}
for a in all:
    l = list(all[a].items())
    l.sort(key=lambda x: x[1],reverse=True)
    for i in l:
        if not i[0] in assign:
            assign[i[0]] = a
            break
p(assign)

total = 0
for i in inc:
    if not i in assign:
        total += inc[i]["count"]
print("total:",total)