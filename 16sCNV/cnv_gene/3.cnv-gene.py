### python 3.cnv-gene.py varScan.CHC10.copynumber.called.depth 2

import sys

upper = float(sys.argv[2])
down = 1 / float(sys.argv[2])

inFile = open(sys.argv[1])
ouFile1 = open(sys.argv[1]+'_'+sys.argv[2]+'_upper_gene', 'w')
ouFile2 = open(sys.argv[1]+'_'+sys.argv[2]+'_down_gene', 'w')
ouFile3 = open(sys.argv[1]+'_'+sys.argv[2]+'_upped_down_gene', 'w')

D1= {}
D2= {}
D3= {}

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if (float(fields[3])+1)/(float(fields[2])+1) > upper:
        #ouFile1.write(line + '\n')
        #ouFile3.write(line + '\n')
        D1[fields[0]]=1
        D3[fields[0]]=1

    elif (float(fields[3])+1)/(float(fields[2])+1) < down:
        #ouFile2.write(line + '\n')
        #ouFile3.write(line + '\n')
        D2[fields[0]]=1
        D3[fields[0]]=1

for k in D1:
    ouFile1.write(k+'\n')
for k in D2:
    ouFile2.write(k+'\n')
for k in D3:
    ouFile3.write(k+'\n')



ouFile1.close()
ouFile2.close()
ouFile3.close()
        

