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
p(all)

k = list(all.keys())
filt = []
filt2 = []
assign = {}
while len(list(assign.keys())) != len(k):
    for a in k:
        if not a in filt2:
            l = list(filter(lambda v: not v[0] in filt,all[a].items()))
            l.sort(key=lambda x: x[1],reverse=True)
            if len(l) == 1 or l[0][1] > l[1][1]:
                assign[l[0][0]] = a
                filt.append(l[0][0])
                filt2.append(a)
p(assign)

aol = list(assign.items())
aol.sort(key=lambda x:x[1])
print(aol)
print("Dangerous:",",".join([a[0] for a in aol]))