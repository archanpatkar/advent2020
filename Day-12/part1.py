import sys
sys.path.append("..")
from common import *
from PIL import Image, ImageDraw

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

direc = {
    "N":0,
    "S":0,
    "E":0,
    "W":0,    
}

points = [point(1000,1000)]

curr = "E"
angle = 0
for comm in data:
    if comm[0] == "F":
        direc[curr] += comm[1]
    elif comm[0] in ["N","E","S","W"]:
        direc[comm[0]] += comm[1]
    elif comm[0] in ["R","L"]:
        angle = (angle-comm[1]) % 360 if comm[0] == "R" else (angle+comm[1]) % 360
        curr = ad[angle]
    points.append(point(direc["E"]-direc["W"],direc["N"]-direc["S"]))
print(direc)
print(manhdis(point(direc["E"],direc["N"]),point(direc["W"],direc["S"])))
print(points)

img = Image.new('RGB', (3000, 3000), color = "blue")
d = ImageDraw.Draw(img)
i = 0
prev = points[0]
for seat in points[1:]:  
    curr = (seat.x+1000,seat.y+1000)
    d.line([prev, curr], width=10, fill="black")
    prev = curr
    img.save('anim/{}.png'.format(i))
    i += 1