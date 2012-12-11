### py  2.viruse.pos.py *.format
import sys

D = {}
for inF in sys.argv[1:]:
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if fields[0].find('NC_')==0:
            D.setdefault(fields[0], [])
            D[fields[0]].append((int(fields[4])+ int(fields[5]))/2)
    inFile.close()

for k in D:
    print(k)
    print(sorted(D[k]))
