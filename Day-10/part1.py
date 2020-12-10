import sys
sys.path.append("..")
from common import *

def parse(data):
    return int(data)

data = [0] + fnl(parse);

data.sort()
data.append(data[-1]+3)
p(data);

oj = 0
tj = 0
thj = 0
last = 0
for i in data:
    if i-1 == last:
        oj += 1
        last = i
    elif i-2 == last:
        tj += 1
        last = i
    elif i-3 == last:
        thj += 1
        last = i

print(oj) 
print(tj)
print(thj)
print(oj*thj)
print(len(data))