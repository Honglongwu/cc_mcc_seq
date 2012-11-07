import sys

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1] + '.format', 'w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if len(fields) > 1 :
        if len(fields) == 13:
            ouFile.write(fields[1] + '\n')
            ouFile.write('\t'.join(fields[2:4] + fields[7:11])+'\n')
        else:
            ouFile.write(fields[9] + '\n')
            ouFile.write('\t'.join(fields[2:4] + fields[7:11])+'\n')



inFile.close()
ouFile.close()
