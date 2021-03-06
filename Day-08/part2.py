import sys
sys.path.append("..")
from common import *

def parse(data):
    data = data.split(" ")
    return (data[0],int(data[1]))

data = fnl(parse);

def machine(code,memory={"acc":0,"ip":0}):
    while memory["ip"] < len(code):
        ins = code[memory["ip"]]
        if(ins[0] == "acc"): memory["acc"] += ins[1]
        elif(ins[0] == "jmp"): 
            memory["ip"] += ins[1]
            continue;
        memory["ip"] += 1
    return memory

def trace(code,limit=1000000,memory={"acc":0,"ip":0}):
    i = 0
    trace = [0 for _ in range(len(code))]
    while memory["ip"] < len(code) and i < limit:
        ins = code[memory["ip"]]
        trace[memory["ip"]] += 1
        if(ins[0] == "acc"): 
            memory["acc"] += ins[1]
        elif(ins[0] == "jmp"): 
            memory["ip"] += ins[1]
            continue;
        memory["ip"] += 1
        i += 1
    return (i < limit,memory,trace)

swap = {
    "nop":"jmp",
    "jmp":"nop"
}

tdata = []
success = None
for i in range(len(data)):
    ins = data[i]
    if ins[0] in ["nop","jmp"]:
        print("changing {}".format(ins[0]))
        old = ins
        data[i] = (swap[ins[0]],ins[1])
        t = trace(data)
        tdata.append(t)
        print(t[1])
        if t[0]:
            success = i
            data[i] = old
            break
        else: 
            print("backtracking")
            data[i] = ins
print("{} instruction should change".format(success))
if success:
    print("from:")
    p(data[success])
    data[success] = (swap[data[success][0]],data[success][1])
    print("to:")
    p(data[success])
p(machine(data))