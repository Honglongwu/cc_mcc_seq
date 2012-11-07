import sys
inF = 'CHC10A.unmapped.fa'
inF2 = 'CHC10A.unmapped.sam.mapped.fa.fa.blasted.top'
inF3 = '../CHC10A.unmapped'

inFile = open(inF)
D = dict()
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        D.setdefault(head,[])
        D[head].append(seq)
    else:
        break
inFile.close()

inFile = open(inF3)
D2 = dict()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '>'+fields[0]
    D2.setdefault(k, [])
    D2[k].append(line)
inFile.close()

inFile = open(inF2)
ouFile = open(inF2 + '.seq1', 'w')
ouFile2 = open(inF2 + '.seq2', 'w')
ouFile3 = open(inF2 + '.seq3', 'w')

for line in inFile:
    line = line.strip()
    fields =line.split('\t')
    k = '>'+fields[0]
    if k in D:
        ouFile.write(k + '\n')
        ouFile.write(D[k] + '\n')
    else:
        ouFile3.write(k.strip('>') + '\n')

    fs = k.split(':')

    if fs[7] == '1':
        k2 = ':'.join(fs[0:7]+['2']+fs[8:])
    elif fs[7] == '2':
        k2 = ':'.join(fs[0:7]+['1']+fs[8:])

    if k2 in D:
        ouFile.write(k2 + '\n')
        ouFile.write(D[k2] + '\n')
    else:
        ouFile2.write(k + '\n')
        ouFile2.write(D[k] + '\t' + line + '\n')
        ouFile2.write(k2 + '\n')
        ouFile2.write(D2[k2] + '\n')

inFile.close()
ouFile.close()
ouFile2.close()
ouFile3.close()


