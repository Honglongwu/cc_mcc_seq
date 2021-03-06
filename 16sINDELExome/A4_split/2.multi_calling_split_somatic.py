import re
Q = 20
D = 30
def multi_calling_split(iFile,samplePosList,sampleNameList) :
    for i,item in enumerate(samplePosList) :
        inFile=open(iFile)
        ouFile=open(sampleNameList[i],'w')
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            if int(fields[item].split(':')[-1])>=Q and int(fields[item+8].split(':')[-1])>=Q \
                    and int(fields[item].split(':')[-2])>=D and int(fields[item+8].split(':')[-2])>=D:
                gene=fields[1]
                gene=re.split(r'[,;(]',gene)[0]
                if fields[item].find('0/1')==0 and fields[item+8].find('0/0')==0:
                    ouFile.write('\t'.join([gene]+fields[21:26]+['1'])+'\n')
                if fields[item].find('1/1')==0 and fields[item+8].find('0/0')==0:
                    ouFile.write('\t'.join([gene]+fields[21:26]+['2'])+'\n')
        ouFile.close()
        inFile.close()


multi_calling_split('sum_snv16sExome.exome_summary.indel.overall.filter',range(-16,-8),['INDEL.exome.somatic.ICC4','INDEL.exome.somatic.ICC5','INDEL.exome.somatic.ICC9','INDEL.exome.somatic.ICC10','INDEL.exome.somatic.CHC5','INDEL.exome.somatic.CHC6','INDEL.exome.somatic.CHC7','INDEL.exome.somatic.CHC10'])

multi_calling_split('sum_snv16sExome.genome_summary.indel.overall.filter',range(-16,-8),['INDEL.genome.somatic.ICC4','INDEL.genome.somatic.ICC5','INDEL.genome.somatic.ICC9','INDEL.genome.somatic.ICC10','INDEL.genome.somatic.CHC5','INDEL.genome.somatic.CHC6','INDEL.genome.somatic.CHC7','INDEL.genome.somatic.CHC10'])
