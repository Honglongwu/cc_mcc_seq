from PyPlot.PyPlotClass import *

def dist(xList,yList):
    s = 0
    for i in range(len(xList)):
        s += abs(xList[i] - yList[i])
    return s
        
def dp_heatmap(inF,D):
    inFile = open(inF)
    dp = []
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        x = []
        y = []
        for item in fields[-16:]:
            d = int(item.split(':')[2])
            if D == 0:
                x.append(d)
            else:
                if d <=D:
                    x.append(0)
                else:
                    x.append(d)
                    
        for i in range(8):
            y.append(x[i])
            y.append(x[i+8])
        dp.append(y)
    inFile.close()
    return(dist(dp[i],dp[i+1]) [for i in range(8))])
    
dp_heatmap('sum_snv16s.exome_summary',0)
dp_heatmap('sum_snv16s.exome_summary',3)
dp_heatmap('sum_snv16s.exome_summary',5)
dp_heatmap('sum_snv16s.genome_summary',0)
dp_heatmap('sum_snv16s.genome_summary',3)
dp_heatmap('sum_snv16s.genome_summary',5)
