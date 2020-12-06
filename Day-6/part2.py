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
for sec in data:
    for k in sec[0]:
        if k != " " and sec[0][k] == sec[1]:
            n += 1
print(n)