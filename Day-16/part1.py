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
    return (conds,myticket,nearbytickets)

data = aoci(parse);
p(data[0]);

count = 0
error_rate = 0
for tic in data[2]:
    for val in tic:
        flag = False
        for field in data[0]:
            c = data[0][field]
            if bi(val,c[0][0],c[0][1]) or bi(val,c[1][0],c[1][1]):
                flag = True
        if not flag:
            count += 1
            error_rate += val
print(error_rate)
print(count)