import sys
upper = 1.5
down = 0.67
upper = 2
down = 0.5

inFile = open(sys.argv[1])
ouFile1 = open(sys.argv[1]+'.upper', 'w')
ouFile2 = open(sys.argv[1]+'.down', 'w')
ouFile3 = open(sys.argv[1]+'.upped_down', 'w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if (float(fields[3])+1)/(float(fields[2])+1) > upper:
        #ouFile1.write(line + '\n')
        #ouFile3.write(line + '\n')
        ouFile1.write(fields[0] + '\n')
        ouFile3.write(fields[0] + '\n')

    elif (float(fields[3])+1)/(float(fields[2])+1) < down:
        #ouFile2.write(line + '\n')
        #ouFile3.write(line + '\n')
        ouFile2.write(fields[0] + '\n')
        ouFile3.write(fields[0] + '\n')

ouFile1.close()
ouFile2.close()
ouFile3.close()
        

