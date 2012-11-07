import sys
ouFile = open('human.viruses.target.fa', 'w')
interval = 1000

D1 = dict()
D2 = dict()

inFile = open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
for line in inFile:
    line = line.strip()
    if line.find('>chr') == 0:
        head = line.lstrip('>')
    else:
        D1[head] = line
inFile.close()

inFile = open('/netshare1/home1/people/hansun/Data/VirusesGenome/VirusesGenome.fasta.fa')
for line in inFile:
    line = line.strip()
    if line.find('>NC') == 0:
        fields = line.split()
        head = fields[0].lstrip('>')
    else:
        D2[head] = line
inFile.close()



inFile = open(sys.argv[1])
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if fields[0].find('chr') == 0:
        if int(fields[1]) - interval >= 0:
            start = int(fields[1]) - interval
        else:
            start = 0
        if int(fields[1]) + interval <= len(D1[fields[0]]):
            end = int(fields[1]) + interval
        else:
            end = len(D1[fields[0]])
        ouFile.write('>' + sys.argv[1].split('.')[0] + 
                ':' + fields[0] + ':' + str(start) + ':' + str(end) + '\n')
        ouFile.write(D1[fields[0]][start:end+1]+'\n')
    if fields[0].find('NC') == 0:
        s = min(int(fields[4]), int(fields[5]))
        e = max(int(fields[4]), int(fields[5]))
        if s - interval >= 0:
            start = s - interval
        else:
            start = 0
        if e + interval <= len(D2[fields[0]]):
            end = e + interval
        else:
            end = len(D2[fields[0]])
        ouFile.write('>' + sys.argv[1].split('.')[0] + 
                ':' + fields[0] + ':' + str(start) + ':' + str(end) + '\n')
        ouFile.write(D2[fields[0]][start:end+1]+'\n')

inFile.close()
ouFile.close()
