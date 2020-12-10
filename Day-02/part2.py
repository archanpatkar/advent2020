import sys
import math
sys.path.append("..")
from common import piechart
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

def poscheck(tup):
    o1 = False
    o2 = False
    if len(passw[2]) >= passw[0][0] and len(passw[2]) >= passw[0][1]:
        o1 = passw[2][passw[0][0]-1] == passw[1] and not(passw[2][passw[0][1]-1] == passw[1])
        o2 = passw[2][passw[0][1]-1] == passw[1] and not(passw[2][passw[0][0]-1] == passw[1])
    return  o1 or o2

i = 0
for passw in data:
    if poscheck(passw): i+=1
print(i)
piechart([i,len(data)-i],"Part2",["Valid","Invalid"],"%10.4f cent.")