from PyPlot.PyPlotClass import *
def gene_heatmap(inF,sampleNameList,ouF,figsize=0,rowList=[]):
    D = dict()
    inFile = open(inF)
    row = -1
    for line in inFile:
        row+=1
        line = line.strip()
        fields =line.split('\t')
        for item in fields[1:]:
            D.setdefault(item,[0]*20)
            D[item][row]+=1
    inFile.close()

    LD = []
    geneList = []
    for key in D :
        LD.append(D[key])
        geneList.append(key)
    
    pp=PyPlot(ouF)
    pp.heatmap(LD,col=False,xLabel=sampleNameList,yLabel=geneList,xLabelVertical=True,grid=True)

gene_heatmap('1.sv.stat.gene.symbol', ['ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','ICC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A','CHC10A'],'juppy.gene.heatmap.pdf')
gene_heatmap('1.sv.stat.exon.symbol', ['ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A','ICC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A','CHC10A'],'juppy.exon.heatmap.pdf')


