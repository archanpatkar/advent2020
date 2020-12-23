import sys
sys.path.append("..")
from common import *

input = [int(c) for c in "219347865"]
p(input)

temp = list(input)
temp.sort()
min = temp[0]
max = temp[-1]
input.extend(range(max+1,1000000+1))
ncups = len(input)
max = input[-1]

def process(n):
    l = {}
    l[n[0]] = n[1]
    for i in range(1,len(n)-1):
        l[n[i]] = n[i+1]
    l[n[-1]] = n[0]
    return l

l = process(input)

def next3(n):
    i = 0
    curr = n
    p = []
    while i < 3:
        p.append(l[curr])
        curr = l[curr]
        i += 1
    return p

# Better than prev. solution 
curr = input[0]
for m in range(10000000):
    des = curr-1
    picked = next3(curr)
    while des in picked or des < min or des > max:
        des = des - 1
        if des < min: des = max
    l[curr] = l[picked[-1]]
    l[picked[-1]] = l[des]
    l[des] = picked[0]
    curr = l[curr]

print("Answer:",l[1]*l[l[1]])