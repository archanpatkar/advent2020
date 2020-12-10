import sys
sys.path.append("..")
from common import *

def parse(data):
    data = data.split(" ")
    return (data[0],int(data[1]))

data = fnl(parse);

def machine(code,memory={"acc":0,"ip":0}):
    done = []
    while memory["ip"] < len(code):
        if(memory["ip"] in done): break
        done.append(memory["ip"])
        ins = code[memory["ip"]]
        if(ins[0] == "acc"): memory["acc"] += ins[1]
        elif(ins[0] == "jmp"): 
            memory["ip"] += ins[1]
            continue;
        memory["ip"] += 1
    return memory

p(machine(data))