D = {}
inFile = open('sum_snp.genome_summary.012')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        k = fields[]
        D.setdefault(k, [0]*29)
        D[k][0]=''
        D[k][1]=fields[-9]
        D[k][2]=fields[-8]
        D[k][3]=fields[-7]
        D[k][4]=fields[-6]
        D[k][5]=fields[-5]
        D[k][6]=fields[-4]
        D[k][7]=fields[-3]
        D[k][8]=fields[-2]
        D[k][9]=fields[-1]
        D[k][10]=fields[-10]

inFile.close()
