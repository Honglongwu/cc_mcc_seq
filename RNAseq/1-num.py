inFile = open('potential_fusion.txt')
D = {}
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    line3 = inFile.readline()
    line4 = inFile.readline()
    line5 = inFile.readline()
    line6 = inFile.readline()
    if line1:
        fields = line1.split()
        D.setdefault(fields[0], 0)
        D[fields[0]]+=1
    else:
        break
inFile.close()
for k in D:
    print(k)
    print(D[k])
'''

Data=[[D['ICC4A'],D['ICC5A'],D['ICC9A'],D['ICC10A'],D['CHC5A'],D['CHC6A'],D['CHC7A'],D['CHC10A']],[D['ICC4B'],D['ICC5B'],D['ICC9B'],D['ICC10B'],D['CHC5B'],D['CHC6B'],D['CHC7B'],D['CHC10B']]]


from PyPlot.PyPlotClass import *
pp=PyPlot('delly.number.pdf')
pp.multi_bar_vertical(Data,legTitle=['Tumor','Normal'],xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],legX=0.85, legY=0.98)
'''
