from pprint import pprint
from functools import *

def p(str):
    pprint(str,indent=4)

def kvd(data,sep=" ",s=":"):
    kv = data.strip().split(sep);
    p = {}
    for e in kv:
        temp = e.split(s)
        p[temp[0]] = temp[1]
    return p

def kvl(data,sep=" ",s=":"):
    kv = data.strip().split(sep);
    p = []
    for e in kv:
        temp = e.split(s)
        p.append((temp[0],temp[1]))
    return p

def periodic(data,pd=lambda x:not len(x),sep="\n",app=" "):
    lines = data.split(sep);
    u = []
    buff = ""
    for l in lines:
        if pd(l):
            u.append(buff)
            buff = ""
        else:
            buff += "{}{}".format(app,l.strip())
    u.append(buff)
    return u

def freq(str):
    l = {}
    for c in str: 
        if c in l: l[c] += 1
        else: l[c] = 1
    return l

def a(list,index):
    if index < len(list): return list[index]
    print("beyond {} list boundary!".format(index))

def m(list,index):
    return list[index % len(index)]

def add(list):
    return reduce(lambda acc,v: acc+v,list,0)

def mult(list):
    return reduce(lambda acc,v: acc*v,list,1)

def ew(str,e):
    return str.endswith(e)

def sw(str,e):
    return str.startswith(e)

nums = ["0","1","2","3","4","5","6","7","8","9"]

def alpha(str,cutoff="z",start="a"):
    n = ord(str)
    return (n >= ord(start) and n <= ord(cutoff)) or (n >= ord(start.capitalize()) and n <= ord(cutoff.capitalize()))

def minl(l,n):
    return len(l) >= n

def maxl(l,n):
    return len(l) <= n

def el(l,n):
    return len(l) == n

def bi(v,s,e):
    return v >= s and v <= e;

def be(v,s,e):
    return v > s and v < e;

def bf(v,s,e):
    return v >= s and v < e;

def bs(v,s,e):
    return v > s and v <= e;

def forall(l,f):
    return reduce(lambda acc,v: acc and f(v),l,True)

def exists(l,f):
    return reduce(lambda acc,v: acc or f(v),l,False)

def intl(l,sep=","):
    if(isinstance(l,str)):
        return [int(v) for v in str.split(sep)]
    return [int(v) for v in l]

def flol(l,sep=","):
    if(isinstance(l,str)):
        return [float(v) for v in str.split(sep)]
    return [float(v) for v in l]

iden = lambda x: x

def aoci(func=iden):
    return func(open("input.txt","r").read());

def fnl(func=iden):
    return [func(l) for l in aoci(lambda data: data.split("\n"))]