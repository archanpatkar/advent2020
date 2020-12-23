import sys
sys.path.append("..")
from common import *

input = [int(c) for c in "219347865"]
p(input)

temp = list(input)
temp.sort()
min = temp[0]
max = temp[-1]
ncups = len(input)

def next3(i):
    next = []
    for j in range(1,4): next.append(input[(i+j)%ncups])
    for j in range(1,4):
        input.pop((i+1)%len(input))
        if i+1 >= len(input):
            i = len(input)-1
    return next

def insert3(i,n):
    global input    
    input = input[:i+1%len(input)] + n + input[i+1%len(input):]

i = 0
for r in range(100):
    curr = input[i]
    des = curr-1
    picked = next3(i)
    while des in picked or not(des in input):
        des = des - 1
        if des < min: des = max
    pos = input.index(des)
    insert3(pos,picked)
    i = (input.index(curr) + 1) % ncups

p(input)

i = input.index(1)
print("Final State:","".join([str(n) for n in input[i+1:]+input[:i]]))