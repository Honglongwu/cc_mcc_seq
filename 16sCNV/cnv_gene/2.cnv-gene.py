### python 2.cnv-gene.py varScan.CHC10.copynumber.called.depth 2

import sys

upper = float(sys.argv[2])
down = 1 / float(sys.argv[2])

inFile = open(sys.argv[1])
ouFile1 = open(sys.argv[1]+'_'+sys.argv[2]+'_upper', 'w')
ouFile2 = open(sys.argv[1]+'_'+sys.argv[2]+'_down', 'w')
ouFile3 = open(sys.argv[1]+'_'+sys.argv[2]+'_upped_down', 'w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if (float(fields[3])+1)/(float(fields[2])+1) > upper:
        ouFile1.write(line + '\n')
        ouFile3.write(line + '\n')

    elif (float(fields[3])+1)/(float(fields[2])+1) < down:
        ouFile2.write(line + '\n')
        ouFile3.write(line + '\n')

ouFile1.close()
ouFile2.close()
ouFile3.close()
        

