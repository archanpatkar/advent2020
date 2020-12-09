import sys
sys.path.append("..")
from common import *

def parse(data):
    return int(data)

data = fnl(parse);
p(data);

preamble = 25
i = preamble
weakness = -1
while i < len(data):
    last25sum = set()
    for j in data[i-preamble:i]:
        for k in data[i-preamble:i]:
            last25sum.add(j+k)
    if data[i] in last25sum:
        i += 1
        continue;
    weakness = data[i]
    break;
print(weakness)