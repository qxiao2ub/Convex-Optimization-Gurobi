#pandas is for using reading functions
import pandas as pd

#numpy for n-dimensional array obj
import numpy as np

#read cijt-cost from csv
#cijt-i,j,t all from 0-1, total 8 numbers, value range [1,100]
cijt = pd.read_csv('cijt.csv',header=None)

cijt = cijt.values.tolist()

print('cijt: ', cijt)

print(cijt[1][4])

#read pijt-penalty of not satisfying demand from csv
#pijt-i,j,t all from 0-1, total 8 numbers, value range [1,10]
pijt = pd.read_csv('pijt.csv',header=None)

pijt = pijt.values.tolist()

print('pijt: ', pijt)

#read hit-inventory cost from csv
#hit-i,t all from 0-1, value range [1,10]
hit = pd.read_csv('hit.csv',header=None)

hit = hit.values.tolist()

print('hit: ', hit)

#read dijt-demand from csv
#dijt-i,j,t all from 0-1, value range [1,100]
dijt = pd.read_csv('dijt.csv',header=None)

dijt = dijt.values.tolist()

print('dijt: ', dijt)

#read alpha_ijtaot-possible to reach in time t from csv
#alpha_ijtaot-i,j,tao,t, value binary
alpha_ijtaot = pd.read_csv('alpha-ijtaot.csv',header=None)

alpha_ijtaot = alpha_ijtaot.values.tolist()

print('alpha_ijtaot: ', alpha_ijtaot)


#python calls Gurobi
#from docplex.mp.model import Model
from gurobipy import *
mdl = Model(name='Zhiheng Linear')

x = mdl.addVar(vtype=GRB.CONTINUOUS, name="x")

#define 3 types decision variables: Uijt, Xijt, Vit
Uijt=[]

for i in range(0,2):
    for j in range(0,2):
        for t in range(0,2):
            Uijt.append (mdl.addVar(vtype=GRB.CONTINUOUS, name= 'Uijt'))


for v in mdl.getVars():
    print('%s ' % (v.varName))
    
print("\n")



