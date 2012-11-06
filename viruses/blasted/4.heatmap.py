from PyPlot.PyPlotClass import *
import sys
import math
def gene_heatmap(sampleNameList, ouF, figsize=0, rowList=[]):
    D = dict()
    for i,inF in enumerate(sampleNameList):
        inFile = open(inF + '.unmapped.sam.mapped.fa.fa.blasted.top.num')
        for line in inFile:
            line = line.strip()
            fields =line.split('\t')
            D.setdefault(fields[0],[0]*16)
            D[fields[0]][i] = int(math.log(int(fields[1])+1,2))

        inFile.close()

    for k in D :
        print(k)
        print(D[k])
        
    LD = []
    geneList = []
    for key in D :
        LD.append(D[key])
        geneList.append(key)
    print(LD)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True,figsize=figsize,colorTickets=True)

gene_heatmap(['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B','CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B'],'viruses.heatmap.pdf',figsize=(8,12))

