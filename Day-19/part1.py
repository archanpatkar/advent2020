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

# Bruteforce!
# def flatap(l,prefix=""):
#     poss = []
#     if isinstance(prefix,str):
#         poss.append("{}".format(prefix))
#     else: poss = [*prefix]
#     for ch in l:
#         temp = []
#         if isinstance(ch,list):
#             for p in poss:
#                 temp.extend(flatap(ch,p))
#         elif isinstance(ch,tuple):
#             for p in poss:
#                 for c in ch:
#                     temp.extend(flatap(c,p))
#         else: 
#             for p in poss:
#                 p += ch
#                 temp.append(p)
#         poss = temp
#     return poss

# rmap = {}
# def find(start,rules):
#     if start in rules:
#         if start in rmap:
#             return rmap[start]
#         rs = rules[start]
#         final = []
#         for r in rs:
#             if isinstance(r,str):
#                 rmap[start] = r
#                 return r
#             elif isinstance(r,list):
#                 final.extend(flatap([find(sr,rules) for sr in r]))
#         rmap[start] = (*final,)
#         return rmap[start]
#     return []

# ops = find(0,data[0])

# count = 0
# for msg in data[1]:
#     print(msg)
#     if msg in ops:
#         count += 1
# print("final count:",count)

def match(stri,r,rules):
    rule = rules[r]
    for option in rule:
        if isinstance(option,str):
            if stri[0] == option: return stri[1:]
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
                if isinstance(curr,bool): return curr
                elif len(curr) == 0: return True
                stri = curr
                break
    if r == 0: return False
    return stri

count = 0
for msg in data[1]:
    if match(msg,0,data[0]):
        count += 1
print("final count:",count)