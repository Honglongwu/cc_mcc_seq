import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1].split('.txt')[0] + '.fa', 'w')
if sys.argv[1].find('ICC4A')==0:
    pass

else:
    for line in inFile:
        line = line.strip()
        fields = line.split()
        if fields:
            if fields[0].find(':') != -1:
                seq1 = fields[0]
                fs = seq1.split(':')
                if sys.argv[1].split('.')[0] in ['CHC10A','ICC10A','ICC9A']:
                    if fs[7] == '1':
                        seq2 = ':'.join(fs[0:7]+['2']+fs[8:])
                    elif fs[7] == '2':
                        seq2 = ':'.join(fs[0:7]+['1']+fs[8:])
                elif sys.argv[1].split('.')[0] in ['CHC5A','CHC6A','CHC7A','ICC5A',]:
                    if fs[7] == '1':
                        seq2 = ':'.join(fs[0:7]+['2']+fs[8:10]+'#2')
                    elif fs[7] == '2':
                        seq2 = ':'.join(fs[0:7]+['1']+fs[8:10]+'#1')
                elif sys.argv[1].split('.')[0].find('B') != -1:
                    seq =seq1
                    D.setdefault(seq, 0)
                    D[seq] += 1
                    seq1 = seq + ':' + str(D[seq])
                    seq2 = seq + ':' + str(D[seq])
            #elif fields[0].find('_') != -1:
            #    seq1 = fields[0]
            #    fs = seq1.split('_')
            #    if sys.argv[1].split('.')[0] in ['ICC4A']:
            #        if fs[7] == '1':
            #            seq2 = '_'.join(fs[0:8]+['2'])
            #        elif fs[7] == '2':
            #            seq2 = '_'.join(fs[0:8]+['1'])
    
                ouFile.write(seq1 + '\n')
                ouFile.write(seq2 + '\n')


inFile.close()
