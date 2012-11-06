import sys
D = dict()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.top','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0] not in D:
        D[fields[0]]=line
inFile.close()

d = D.items()
d.sort(cmp=lambda x,y:cmp(x[1].split('\t')[1],y[1].split('\t')[1]))

for item in d:
    ouFile.write(item[1]+'\n')


