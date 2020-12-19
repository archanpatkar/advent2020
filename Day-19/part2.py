import sys
sys.path.append("..")
from common import *

def parse(data):
    data = data.split("\n")
    rules = {}
    messages = []
    c = 0
    for i in data:
        if len(i) < 1:
            break
        i = i.split(":")
        sb = i[1].split("|")
        sr = []
        for op in sb:
            op = op.strip()
            if op[0] == '"': 
                sr.append(op[1:-1])
            else: 
                sr.append([int(n) for n in op.split(" ") if len(n) > 0])
        rules[int(i[0])] = (*sr,)
        c += 1
    for i in range(c+1,len(data)):
        messages.append(data[i])
    return (rules,messages)

data = aoci(parse);
p(data);

def handleZero(stri,rules):
    curr = stri
    temp = None
    i = 0
    j = 0
    while True:
        temp = match(curr,42,rules)
        if temp == curr: break
        else: curr = temp
        i += 1
    if curr == stri: return False
    while True:
        temp = match(curr,31,rules)
        if temp == curr: break
        else: curr = temp
        j += 1
    if isinstance(curr,bool) or len(curr) == 0:
        if i and j and i-j >= 1: return True
    return False

def match(stri,r,rules):
    if isinstance(stri,bool): return stri
    rule = rules[r]
    if r == 0: return handleZero(stri,rules)
    for option in rule:
        if isinstance(option,str):
            if stri[0] == option:
                return stri[1:]
        else:
            i = 0
            curr = stri
            temp = None
            for sq in option:
                temp = match(curr,sq,rules)
                if temp == curr: break
                else: curr = temp
                i += 1
            if i == len(option): 
                if isinstance(curr,bool):
                    return curr
                elif len(curr) == 0:
                    return True
                stri = curr
                break
    return stri

count = 0
for msg in data[1]:
    if match(msg,0,data[0]): count += 1
print("final count:",count)