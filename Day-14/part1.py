import sys
sys.path.append("..")
from common import *

def parse(data):
    tup = None
    if sw(data,"mask"):
        tup = data.split("=")
        tup = (tup[0].strip(), tup[1].strip())
    else:
        tup = data.split("=")
        temp = tup[0].split("[")
        tup = (temp[0].strip(),int(temp[1].strip()[0:-1]),int(tup[1]))
    return tup

data = fnl(parse);
p(data);

def binary(i):
    return "".join(bin(i).split("b"))

def valMask(value,mask):
    nw = []
    for b in range(len(mask)):
        bit = mask[b]
        if(bit != "X"):
            nw.append(bit)
        else:
            nw.append(value[b])
    return int("".join(nw),base=2)

nc = []
m = 0
while m < len(data):
    i = 1
    while m+i < len(data) and data[m+i][0] != "mask":
        mem = data[m+i]
        nw = valMask(binary(mem[2]).rjust(36,"0"),data[m][1])
        nc.append((mem[0],mem[1],nw))
        i += 1
    m += i

memory = {}
for up in nc:
    memory[up[1]] = up[2]
p(memory)

sum = 0
for cell in memory:
    sum += memory[cell]
print(sum)