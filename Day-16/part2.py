from os import fdopen
import sys
sys.path.append("..")
from common import *

def parse(data):
    data = list(map(lambda s: s.strip(),filter(lambda s: len(s) > 1,data.split("\n"))))
    conds = {}
    for i in range(20):
        kv = data[i].split(":")
        cs = kv[1].split("or")
        conds[kv[0]] = ([int(v) for v in cs[0].split("-")],
        [int(v) for v in cs[1].split("-")])
    myticket = [int(n) for n in data[21].split(",")]
    nearbytickets = [[int(n) for n in data[l].split(",")] for l in range(23,len(data))]
    return (conds,[myticket]+nearbytickets)

data = aoci(parse);
p(data[0]);

fd = []
for i in range(len(data[1])):
    tic = data[1][i]
    t = {g:[] for g in range(len(tic))}
    all_valid = True
    for v in range(len(tic)):
        val = tic[v]
        flag = False
        for field in data[0]:
            c = data[0][field]
            if bi(val,c[0][0],c[0][1]) or bi(val,c[1][0],c[1][1]):
                flag = True
                t[v].append(field)
        if not flag:
            all_valid = False
            break
    if all_valid:
        fd.append(t)
# p(fd)

freqs = {k:[] for k in data[0]}
for i in range(len(list(data[0].keys()))):
    curr = {f:0 for f in data[0]}
    for r in fd:
        for f in r[i]:
            curr[f] += 1
    [freqs[cat].append(i) for cat in curr if curr[cat] == len(fd)]
p(freqs)

final = {}
elim = []
while len(elim) != 20:
    keys = list(freqs.keys())
    shortest = reduce(lambda acc,v: v if len(freqs[v]) < len(freqs[acc]) else acc,keys[1:],keys[0])
    n = list(filter(lambda x: not(x in elim),freqs[shortest]))[0]
    final[shortest] = n
    elim.append(n)
    freqs.pop(shortest)
p(final)

val = 1
for k in final:
    if sw(k,"departure"):
        val *= data[1][0][final[k]]
print("final:",val)