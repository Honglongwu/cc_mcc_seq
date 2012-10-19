import numpy as np
def dist(xList,yList):
    s = 0
    for i in range(len(xList)):
        s += abs(xList[i] - yList[i])
    return s
        
def dp_dist(inF):
    ds = []
    for D in [0,3,5,10]:
        inFile = open(inF)
        dp = [[] for i in range(16)]
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            for i,item in enumerate(fields[-16:]):
                d = int(item.split(':')[2])
                if d <=D:
                    dp[i].append(0)
                else:
                    dp[i].append(1)
                        
        inFile.close()
        tmp = []
        for i in range(8):
            tmp.append(dist(dp[i],dp[i+8]))
        ds.append(tmp)
    return ds
    
    

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 

sample = ['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10']
line = ['dp>=0','dp>=3','dp>=5','dp>=10']

def plot(xList,ouFile):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(1,9),xList[0],range(1,9),xList[1],range(1,9),xList[2],range(1,9),xList[3])
    ax.set_xticks(range(10))
    ax.set_xticklabels(['']+sample+[''])
    ax.legend(line,loc='upper left',bbox_to_anchor=[0.96,0.98],prop={'size':6})

    plt.grid(True)
    plt.savefig(ouFile)

plot(dp_dist('sum_snv16s.exome_summary'), '1.depth.exome.dist.pdf')
plot(dp_dist('sum_snv16s.genome_summary'), '1.depth.genome.dist.pdf')

