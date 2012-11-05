import sys
D = dict()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.top','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[1],{})
    if fields[0] not in D[fields[1]]:
        D[fields[1]][fields[0]] = line
inFile.close()

d = D.items()
d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])), reverse=True)

for item in d : 
    for k in item[1]:
        ouFile.write(item[1][k]+'\n')
