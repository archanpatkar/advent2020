import sys
sys.path.append("..")
from common import *

opsm = {
    "+": lambda *v: sum(v),
    "*": lambda *v: mult(v)
}

def toks(str):
    tokens = []
    for ch in str:
        if ch.isnumeric(): tokens.append(int(ch))
        else: tokens.append(ch)
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
    while len(toks) > 0 and toks[0] in opsm:
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
    return expr(toks("".join(data.split(" "))))

data = fnl(parse);
p(data);

print(sum([eval(l) for l in data]))