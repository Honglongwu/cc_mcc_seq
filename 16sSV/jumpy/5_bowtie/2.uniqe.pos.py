import sys
D = dict()
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.unique', 'w')

for n in range(95):
    line = inFile.readline()

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], [])
    D[fields[0]].append(line)
inFile.close()

for k in D:
    if len(D[k]) == 1 and D[k][0].split('\t')[1] != '4':
        ouFile.write(D[k][0] + '\n')

inFile.close()
ouFile.close()
