data = open("input.txt","r").read();
data = [int(row) for row in data.split("\n")];
print(data);
sums = [(n1,n2) for n1 in data for n2 in data if(n1 != n2 and (n1+n2 == 2020))]
print(sums);
print([t[0]*t[1] for t in sums]);