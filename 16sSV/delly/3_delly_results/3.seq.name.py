inFile = open('16sSV.read.name')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split()
    for item in fields[1:]:
        if item.find(':')!=-1:
            fds = item.split(':')
            k = ':'.join(fds[0:7])
        elif item.find('_')!=-1:
            fds = item.split('_')
            k = '_'.join(fds[0:7])
        else:
            print('key error')
            exit
        D.setdefault(k, [])
        D[k].append(fields[0])
inFile.close()

for k in D:
    D[k]='\t'.join(D[k])

#for k in D:
#    print(k)
#    print(D[k])


inFs=['ha',
        'he']
D['HWI-ST507:84:D05YWACXX:1:1101:1449:2165']='xxxxx'

ouFile = open('16sSV.read.name.paired','w')

for inF in inFs:
    inFile = open(inF)
    while True:
        line1 = inFile.readline()
        line2 = inFile.readline()
        line3 = inFile.readline()
        line4 = inFile.readline()
        if line1:
            readname = line1.strip('@\n')
            if readname.find(':')!=-1:
                fds = item.split(':')
                k = ':'.join(fds[0:7])
            elif readname.find('_')!=-1:
                fds = item.split('_')
                k = '_'.join(fds[0:7])
            else:
                print(inF+'\t'+readname)
                exit
            if k in D:
                ouFile.write('>'+k+'\t'+D[k]+'\n')
                ouFile.write(line2)
                ouFile.write(line4)
        else:
            break

    inFile.close()

ouFile.close()


