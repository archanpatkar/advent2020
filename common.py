from pprint import pprint

def p(str):
    pprint(str,indent=4)

def freq(str):
    l = {}
    for c in str: 
        if c in l: l[c] += 1
        else: l[c] = 1
    return l

def aoci(func=lambda x: x):
    return func(open("input.txt","r").read());

def fnl(func=lambda x:x):
    return [func(l) for l in aoci(lambda data: data.split("\n"))]