import sys
sys.path.append("..")
from common import *

def parse(data):
    return (data[:1],int(data[1:]))

data = fnl(parse);
p(data);

ad = {
    0:"E",
    90:"N",
    180:"W",
    270:"S"
}

rd = {
    "E": 0,
    "N": 90,
    "W": 180,
    "S": 270
}

waypoint = {
    "N":1,
    "S":0,
    "E":10,
    "W":0, 
}

direc = {
    "N":0,
    "S":0,
    "E":0,
    "W":0,    
}

for comm in data:
    if comm[0] == "F":
        for k in waypoint: 
            direc[k] += (comm[1]*waypoint[k])
    elif comm[0] in ["N","E","S","W"]:
        waypoint[comm[0]] += comm[1]
    elif comm[0] in ["R","L"]:
        nw = {}
        for k in waypoint:
            angle = (rd[k]-comm[1]) % 360 if comm[0] == "R" else (rd[k]+comm[1]) % 360
            nw[ad[angle]] = waypoint[k]
        waypoint = nw

print(direc)
print(manhdis(point(direc["E"],direc["N"]),point(direc["W"],direc["S"])))