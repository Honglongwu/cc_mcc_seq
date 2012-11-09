import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.paired', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    h = fields[0].split(':')
inFile.close()
ouFile.close()
