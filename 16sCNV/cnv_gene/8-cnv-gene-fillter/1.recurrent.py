import sys
inFile = open(sys.argv[1])
ouFile = open(sys.argv[1]+'.recurrent', 'w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    n1 = 0
    n2 = 0
    for item in fields[2:6]:
        if int(item)!=0:
            n1 += 1
    for item in fields[6:]:
        if int(item)!=0:
            n2 += 1

    if n1 > 1 and sum([int(x) for x in fields[2:6]]):
        ouFile.write(line+'\n')
    if n2 > 1 and sum([int(x) for x in fields[6:]]):
        ouFile.write(line+'\n')



inFile.close()
ouFile.close()
