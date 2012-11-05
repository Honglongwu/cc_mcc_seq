import sys

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.fa', 'w')
D = dict()
while True:
    head = inFile.readline()
    seq = inFile.readline()
    if head:
        D[seq] = head
    else:
        break
inFile.close()

for k in D:
    ouFile.write(D[k])
    ouFile.write(k)

ouFile.close()
