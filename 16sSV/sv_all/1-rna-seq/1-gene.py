inFile = open('potential_fusion.txt')
ouFile = open('potential_fusion.gene','w')
D = {}
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    line3 = inFile.readline()
    line4 = inFile.readline()
    line5 = inFile.readline()
    line6 = inFile.readline()
    if line1:
        fields = line5.split()
        D[fields[0]]=1
        D[fields[2]]=1

    else:
        break
inFile.close()


inFile = open('1.sv.stat.gene.symbol')
for line in inFile:
    line = line.strip()
    if line in D:
        ouFile.write(line + '\n')

inFile.close()
