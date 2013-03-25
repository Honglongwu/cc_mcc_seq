inFile = open('/fs01/szzhongxin/proj1/hansun/RNAseq/result.txt')
L = []
for line in inFile:
    line = line.strip()
    fields = line.split()
    L.append(fields)
inFile.close()

def sv(inF):
    inFile = open(inF)
    for line in inFile:

    inFile.close()

