inFile=open('gene_fdr_0.1')

ouFile=open('sum_snp.exome_combined.sorted.pass012.new_mcc_heat','w')

dict1=dict()
for line in inFile :
    line=line.strip()
    gene=line.split('\t')[0]

    inFile1=open('sum_snp.exome_combined.sorted.pass012.new_mcc')

    for line in inFile1 :
        line=line.strip()
        fields=line.split('\t')
        if fields[1] == gene :
            ouFile.write(line+'\n')


    inFile1.close()


inFile.close()
