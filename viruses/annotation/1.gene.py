import sys

interval = 500

inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19_refGene.txt')
G = []
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    G.append([fields[2],int(fields[4]),int(fields[5]),fields[12]])
inFile.close()

inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.gene', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split()
    if fields:
        if fields[0].find('chr') == 0:
            ouFile.write(line + '\t')
            pos = int(fields[1])
            p1 = pos - interval
            p2 = pos + interval
            for item in G:
                if item[1]< p1 <item[2] or item[1] < p2 < item[2]:
                    #ouFile.write(line + '\t' + item[3] + '\n')
                    ouFile.write(item[3] + '\t')
            ouFile.write('\n')
inFile.close()
ouFile.close()
