import sys
D = dict()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.top','w')
ouFile2 = open(sys.argv[1]+'.top2','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if int(fields[2])>95 and int(fields[3])>90:
        D.setdefault(fields[0], [])
        D[fields[0]].append(line)
inFile.close()

d = D.items()
d.sort(cmp=lambda x,y:cmp(x[1][0].split('\t')[1],y[1][0].split('\t')[1]))

for item in d:
    ouFile.write(item[1][0]+'\n')
    if len(item[1]) > 1:
        for x in item[1]:
            ouFile2.write(x+'\n')


