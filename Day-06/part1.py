import sys
import math
sys.path.append("..")
from common import *

def parse(data):
    data = periodic(data)
    return [(freq(l),len(l.split(" "))) for l in [l.strip() for l in data]]

data = aoci(parse);
p(data);

n = 0
persec = []
for sec in data:
    temp = n
    for k in sec[0]:
        if k != " ":
            n += 1
    persec.append((n-temp))
print(n)
barchart(range(len(data)),persec,"Part1")