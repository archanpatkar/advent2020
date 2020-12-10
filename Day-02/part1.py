import sys
import math
sys.path.append("..")
from common import barchart, scatterplot, piechart
from pprint import pprint
data = open("input.txt","r").read();
def handle(input):
    temp = input.split(":");
    password = temp[1].strip();
    temp = temp[0].split(" ")
    letter = temp[1]
    temp = temp[0].split("-")
    return ([int(n) for n in temp],letter,password)

data = [handle(r) for r in data.split("\n")]
pprint(data,indent=4)

def freq(str):
    l = {}
    for c in str: 
        if c in l: l[c] += 1
        else: l[c] = 1
    return l

il = []
nl = []
cl = []
i = 0
for passw in data:
    letters = freq(passw[2])
    n = letters.get(passw[1])
    if n and n >= passw[0][0] and n <= passw[0][1]: 
        cl.append(passw[1])
        nl.append(n)
        il.append(i)
        i += 1

print(i)
# scatterplot(nl,il,"Part1a")
# barchart(cl,nl,"Part1b")
piechart([i,len(data)-i],"Part1",["Valid","Invalid"],"%10.4f cent.")