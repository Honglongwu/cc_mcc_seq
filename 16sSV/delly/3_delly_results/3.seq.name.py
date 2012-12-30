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


inFs=['/netshare1/home1/szzhongxin/proj1/fudan/1A/ha',
        'he']
D['HWI-ST507_75_5_1_2446_2230_0']='xxxxx'

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
                fds = readname.split(':')
                k = ':'.join(fds[0:7])
            elif readname.find('_')!=-1:
                fds = readname.split('_')
                k = '_'.join(fds[0:7])
            else:
                print(inF+'\t'+readname)
                exit
            if k in D:
                ouFile.write('>'+k+'\t'+D[k]+'\n')
                ouFile.write(line2.strip()+'\t'+inF+'\n')
                ouFile.write(line4.strip()+'\t'+inF+'\n')
        else:
            break

    inFile.close()

ouFile.close()


