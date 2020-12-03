from pprint import pprint
from functools import *

def p(str):
    pprint(str,indent=4)

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

iden = lambda x: x

def aoci(func=iden):
    return func(open("input.txt","r").read());

def fnl(func=iden):
    return [func(l) for l in aoci(lambda data: data.split("\n"))]