import sys
sys.path.append("..")
from common import *

data = [19,20,14,0,9,1]
last = [*data]

ru = {0:[]}
for i in range(len(last)):
    ru[last[i]] = [i+1]
p(ru)

for i in range(len(last),2020):
    uses = ru.get(last[-1])
    if uses != None and len(uses) > 1: 
        diff = uses[-1] - uses[-2]
        last.append(diff)
        t = ru.get(diff)
        if t != None:
            t.append(i+1)
        else: ru[diff] = [i+1]
    else:
        last.append(0)
        ru[0].append(i+1)
print(last[-1])