import sys
flags = [83, 77, 147, 163]
while True:
    line = sys.stdin.readline()
    if line:
        fields = line.split('\t')
        if int(fields[1]) not in flags:
            print(line),
    else:
        break
        



