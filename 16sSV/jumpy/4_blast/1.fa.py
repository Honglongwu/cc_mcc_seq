import sys
inFile = open(sys.argv[1])
for line in inFile:
    line = line.strip()
    fields = line.split()
    if fields:
        if fields[0].find(':') != -1:
            seq1 = fields[0]
            fs = seq1.split(':')
            if sys.argv[1].split('.')[0] in ['CHC10A']:
                if fs[7] == '1':
                    seq2 = ':'.join(fs[0:7]+['2']+fs[8:])
                elif fs[7] == '2':
                    seq2 = ':'.join(fs[0:7]+['1']+fs[8:])
            print(seq1)
            print(seq2)


inFile.close()
