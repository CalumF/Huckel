# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:31:20 2019

@author: Calum
"""

import numpy as np

nC = int(input("Enter number of carbon atoms: "))
con = input("""Enter connectivity of carbons (number carbons then commas between connected carbons, 
             space between branches ie for sp2 methylcyclopropane 1,2,3,4,5,1 1,5): """)
con = con.split(" ")
con = [i.split(",") for i in con]
con = [list(map(int, i)) for i in con]
print(con)
ham = np.zeros((nC,nC))
for lis in con:
    for i in range(0, len(lis) - 1):
        ham[int(lis[i]-1)][int(lis[i+1]-1)] = -1
        ham[int(lis[i+1]-1)][int(lis[i]-1)] = -1
print(ham)
eval, evec = np.linalg.eig(ham)
eval.sort()
print(eval)
for i in range(0,nC):
    print("E{0} = α + {1:3.2f}β".format(i,eval[i]))
degen = 0
for i in range(0, len(eval) - 1):
    if -0.0001 < eval[i] - eval[i + 1] < 0.0001:
        degen += 1
if degen == 1:
    print("There is {0} degenerate energy level".format(degen))
else: print("There are {0} degenerate energy levels".format(degen))
    
