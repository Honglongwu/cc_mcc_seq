import sys
import re


hits = 2
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
        'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
        'chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']

identity = 95
size = 90
if sys.argv[1].find('ICC4A') != -1:
    size = 60

D = {}
def blat():
    #inFile = open(sys.argv[1] + '.blat')
    inFile = open('test')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        if float(fields[2]) >= identity and float(fields[3]) >= size:
            D.setdefault(fields[0], [])
            D[fields[0]].append(line)

    inFile.close()

blat()


inFile = open(sys.argv[1])
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    line3 = inFile.readline().strip()
    line4 = inFile.readline().strip()

    if line1:
        k1 = line1.lstrip('>')
        k2 = line3.lstrip('>')

        if k1 in D and k2 in D:
            if len(D[k1]) == 1 and len(D[k2]) == 1:
                print(D[k1][0])
                print(line2)
                print(D[k2][0])
                print(line4)

    else:
        break



inFile.close()

