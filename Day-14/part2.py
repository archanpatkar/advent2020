from os import O_APPEND
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

def comb(base,d,start):
    done = [start]
    q = []
    for k in d[start]:
        var = list(base)
        var[start] = k
        q.append(var)
    for o in d:
        if not o in done:
            next = []
            while len(q) != 0:
                e = q.pop(0)
                for k in d[o]:
                    var = list(e)
                    var[o] = k
                    next.append("".join(var))
            q = next
            done.append(o)
    return q

def addrMask(value,mask):
    nw = []
    total = {}
    for b in range(len(mask)):
        bit = mask[b]
        if(bit == "X"):
            total[b] = ["0","1"]
            nw.append("_")
        elif(bit == "1"): nw.append(bit)
        else: nw.append(value[b])
    return list(map(lambda n: int(n,base=2),comb(nw,total,list(total.keys())[0])))

nc = []
m = 0
while m < len(data):
    i = 1
    while m+i < len(data) and data[m+i][0] != "mask":
        mem = data[m+i]
        ad = addrMask(binary(mem[1]).rjust(36,"0"),data[m][1])
        nc.append((mem[0],ad,mem[2]))
        i += 1
    m += i

memory = {}
for up in nc:
    for addr in up[1]:
        memory[addr] = up[2]
p(memory)

sum = 0
for cell in memory:
    sum += memory[cell]
print(sum)