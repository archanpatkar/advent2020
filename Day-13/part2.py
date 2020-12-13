import sys
sys.path.append("..")
from common import *

def parse(data):
    lines = data.split("\n");
    return list(map(lambda x: int(x) if x.isnumeric() else x,lines[1].split(",")))

data = aoci(parse);
p(data);

busids = []
offsets = []
t = 0
for n in data:
    if isinstance(n,int):
        busids.append(n)
        offsets.append(t)
    t += 1

print(busids)
print(offsets)

# Taken from rosetta code
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print([busids[i]-offsets[i] for i in range(len(offsets))])
print(chinese_remainder(busids,[busids[i]-offsets[i] for i in range(len(offsets))]))

# Bruteforce
# step = busids[0]
# print(step)
# i = 0
# print(i)
# while True:
#     flag = False
#     for n in range(len(busids)):
#         if (i+offsets[n]) % busids[n] == 0: flag = True
#         else: 
#             flag = False
#             break
#     if flag: break
#     i += step
# print(i)