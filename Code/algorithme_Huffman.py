# -*- coding: utf-8 -*-
"""
@author: Salim
email: salim.ouarab@ouotlook.com
"""

import numpy as np

chaine = "abracadabrada"  # chaine de caactère à tester 

table = np.zeros((1,2),dtype=int) # Table d'occurrence

for i in range(len(chaine)):
    for j in range(len(chaine)):
        if ord(chaine[i]) == table[j,0]:
            table[j,1]= table[j,1]+1
            break
        else:
            if table[j,0] == 0:
                table[j,0] = ord(chaine[i])
                table[j,1] = 1
                table = np.r_[table,[[0,0]]]
                break
 
table = table[table[:,1].argsort()[::-1]]  # tri descendant 

