import sys


D = {}
for inF in sys.argv[1:]:
    sample = inF.split('.')[1]
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D.setdefault(fields[0], {})
        D[fields[0]][sample] = 1
    inFile.close()

L = []
for k in D:
    L.append([D[k].get('ICC4',0),D[k].get('ICC5',0),D[k].get('ICC9',0),D[k].get('ICC10',0),
        D[k].get('CHC5',0),D[k].get('CHC6',0),D[k].get('CHC7',0),D[k].get('CHC10',0)])

print(L)

