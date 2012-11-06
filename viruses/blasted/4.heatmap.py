from PyPlot.PyPlotClass import *
import sys
#def gene_heatmap(sampleNameList,ouF,figsize=0,rowList=[]):
def gene_heatmap():
    D = dict()
    for i,inF in enumerate(sys.argv[1:]):
        inFile = open(inF)
        for line in inFile:
            line = line.strip()
            fields =line.split('\t')
            D.setdefault(fields[0],[0]*16)
            D[fields[0]][i] = int(fields[1])
        inFile.close()

    ouFile = open('xxx','w') 
    for k in D :
        ouFile.write(k + '\t' + '\t'.join([str(x) for x in D[k]])+'\n')
    '''
    LD = []
    geneList = []
    for key in D :
        LD.append(D[key])
        geneList.append(key)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=figsize)
    '''

#gene_heatmap(['ICC1A','ICC2A','ICC3A','ICC6A','ICC7A','ICC8A','CHC1A','CHC2A','CHC3A','CHC4A','CHC8A','CHC9A'],'sv.exon.heatmap.pdf',figsize=(8,12))

gene_heatmap()
