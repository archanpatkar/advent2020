import sys
sys.path.append("..")
from common import scatter3d

data = open("input.txt","r").read();
data = [int(row) for row in data.split("\n")];
print(data);
sums = [(n1,n2,n3) for n1 in data for n2 in data for n3 in data if(n1 != n2 != n3 and (n1+n2+n3 == 2020))]
print(sums);
print([t[0]*t[1]*t[2] for t in sums]);
x,y,z = zip(*sums)
scatter3d(x,y,z,"Part2")