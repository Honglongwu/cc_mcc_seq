import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.unique', 'w')
for line in inFile:
    line = line.strip()
    fields  = line.split('\t')


inFile.close()
ouFile.close()
