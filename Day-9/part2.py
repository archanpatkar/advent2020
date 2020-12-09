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

contiguous_set = None
for i in range(len(data)):
    j = 0
    sum = 0
    nlist = set()
    while(j < len(data) and sum < weakness):
        sum += data[i+j]
        nlist.add(data[i+j])
        j += 1
    if sum == weakness and len(nlist) >= 2:
        contiguous_set = nlist
        break
print(contiguous_set)
sorted = list(contiguous_set)
sorted.sort()
print(sorted[0]+sorted[-1])