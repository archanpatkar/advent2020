import sys
sys.path.append("..")
from common import *

def parse(line):
    line = line.split("\n");
    passports = []
    buff = ""
    for l in line:
        if not len(l):
            passports.append(buff)
            buff = ""
        else:
            buff += " {}".format(l.strip())
    passports.append(buff)
    np = []
    for p in passports:
        kv = p.strip().split(" ");
        passp = {}
        for e in kv:
            temp = e.split(":")
            passp[temp[0]] = temp[1]
        np.append(passp)
    return np

data = aoci(parse);
p(data);

keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
valid = 0
wocid = 0
for passp in data:
    if len(passp.keys()) == 8 or (len(passp.keys()) == 7 and not("cid" in passp)):
        if not("cid" in passp): wocid += 1
        valid += 1
print(valid)
piechart([valid-wocid,wocid,len(data)-valid],"Part1",["Valid Passports","Without CID","Invalid Passports"],"%10.4f cent.")