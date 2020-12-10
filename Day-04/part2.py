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

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

def year(f,s,e):
    return len(f) == 4 and int(f) >= s and int(f) <= e

def height(f):
    if f.endswith("cm"):
        n = int(f.split("cm")[0])
        if n >= 150 and n <= 193: return True
    elif f.endswith("in"):
        n = int(f[:2])
        if n >= 59 and n <= 76: return True
    return False;

def haircolor(c):
    if c.startswith("#"):
        flag = False
        for ch in c[1:]:
            if ch in ["0","1","2","3","4","5","6","7","8","9"] or ch in ["a","b","c","d","e","f"]:
                flag = True
            else: flag = False
        return flag
    return False

def pid(c):
    if len(c) == 9:
        flag = False
        for ch in c:
            if ch in ["0","1","2","3","4","5","6","7","8","9"]:
                flag = True
            else: flag = False
        return flag
    return False

keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
valid = 0
wocid1 = 0
wocid2 = 0
for passp in data:
    if len(passp.keys()) == 8 or (len(passp.keys()) == 7 and not("cid" in passp)):
        if not("cid" in passp): wocid1 += 1
        if year(passp["byr"],1920,2002) and year(passp["iyr"],2010,2020) and year(passp["eyr"],2020,2030) and height(passp["hgt"]) and haircolor(passp["hcl"]) and (passp["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and pid(passp["pid"]):
            if not("cid" in passp): wocid2 += 1
            valid += 1
print(valid)
piechart([valid-wocid1,wocid2,(wocid1-wocid2),len(data)-valid],"Part2",["Valid Passports","Without CID Valid","Without CID Invalid","Invalid Passports"],"%10.4f cent.")