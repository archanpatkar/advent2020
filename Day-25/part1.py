import sys
sys.path.append("..")
from common import *

def parse(data):
    return int(data)

data = fnl(parse);

key1 = data[0]
key2 = data[1]

def pow(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y

loop_size = None
i = 0
while True:
    if pow(7,i,20201227) == key1:
        loop_size = i
        break
    i += 1
print("Loop Size:",loop_size)

print("Encryption key:",pow(key2,loop_size,20201227))