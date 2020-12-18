import sys
sys.path.append("..")
from common import *

opsm = {
    "+": lambda *v: sum(v),
    "*": lambda *v: mult(v)
}

def toks(str):
    i = 0
    l = len(str)
    tokens = []
    while i < l:
        curr = str[i]
        if curr.isnumeric():
            buff = "" + curr
            i += 1
            if i < l: curr = str[i]
            while curr.isnumeric() and i < l:
                buff += curr
                i += 1
                curr = str[i]
            tokens.append(int(buff))
        else:
            tokens.append(curr)
            i += 1
    return tokens

def atom(toks):
    curr = toks.pop(0)
    if isinstance(curr,int):
        return curr
    elif curr == "(":
        e = expr(toks)
        toks.pop(0)
        return e
    
def expr(toks):
    left = atom(toks)
    if len(toks) > 0: 
        while len(toks) > 0 and (toks[0] == "+" or toks[0] == "*"):
            op = opsm[toks.pop(0)]
            left = [op,left,atom(toks)]
    return left

def eval(ast):
    op = ast[0]
    if isinstance(ast[1],list):
        ast[1] = eval(ast[1])
    if isinstance(ast[2],list):
        ast[2] = eval(ast[2])
    return op(ast[1],ast[2])

def parse(data):
    exp = "".join(data.split(" "))
    print(exp)
    return expr(toks(exp))

data = fnl(parse);
p(data);

print(sum([eval(l) for l in data]))