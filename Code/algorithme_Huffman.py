# -*- coding: utf-8 -*-
"""
@author: Salim
email: salim.ouarab@ouotlook.com
"""

import numpy as np

chaine = "abracadabrada"  # chaine de caractère à tester 

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

# Tri des deux premieres colonnes 
table = table[table[:,1].argsort()[::-1]]  # tri descendant 


# Récupération des indices
"""
Stockage des indices des nombres sommés dans un tableau pour attribuer les digites.
Chaque deux colones représente une sommation
"""

# tableau des indices 
tab_indices = np.zeros((1,2), dtype = int)
saut = 2   # le saut dans le tableau des indices  
indice_zero = 0    
col_en_cours = 1  #  colonne de début 
donne = 0
p=0

while donne != 1:
    
    # Tri à partir de la 2eme colonne
    if col_en_cours > 1:
        p=2                  
        while p>=1:
           p=0
           for jj in range(len(table)-1):
               # tri des nombres d'occurrence
               if table[jj,col_en_cours] < table[jj+1,col_en_cours]:
                       aux = table[jj,col_en_cours]
                       table[jj,col_en_cours]=table[jj+1,col_en_cours]
                       table[jj+1,col_en_cours] = aux
                       
                       # tri des indices 
                       tmp1 = tab_indices[jj,saut-2]
                       tab_indices[jj,saut-2] = tab_indices[jj+1,saut-2]
                       tab_indices[jj+1,saut-2]=tmp1
                       
                       tmp2 = tab_indices[jj,saut-1]
                       tab_indices[jj,saut-1] = tab_indices[jj+1,saut-1]
                       tab_indices[jj+1,saut-1]=tmp2
                       p+=1
 
    
    for ii in range(len(table)):  
         if table[ii, col_en_cours] == 0:
             indice_zero = ii
             break
         else:
             if col_en_cours == 1 and ii > 0 :
                 # Indices pour les deux colonnes 
                 tab_indices = np.r_[tab_indices,[[0,0]]]
                 tab_indices[ii,col_en_cours-1] = ii
                 tab_indices[ii,col_en_cours]  =  ii  
                                 
    table = np.append(table,np.zeros((len(table),1),dtype=int), axis=1)
    #indices pour les colonnes suivantes 
    tab_indices = np.append(tab_indices,np.zeros((len(tab_indices),2),dtype=int), axis=1)
    for k in range(len(tab_indices)):
        tab_indices[k,saut] = k
        tab_indices[k,saut+1] = k
   
    table[:,col_en_cours+1] = table[:,col_en_cours]
    table[indice_zero-1,col_en_cours + 1] = 0
    # sommation des deux nombres 
    table[indice_zero-2,col_en_cours+1] = table[indice_zero-1,col_en_cours]+table[indice_zero-2,col_en_cours]   
    

    if indice_zero <=2:
        donne = 1
    else:
        
        table[indice_zero-1,col_en_cours + 1] = 0
        table[indice_zero-2,col_en_cours+1] = table[indice_zero-1,col_en_cours]+table[indice_zero-2,col_en_cours]
        
        tab_indices[indice_zero-2,saut] = indice_zero - 2
        tab_indices[indice_zero-2,saut+1] = indice_zero - 1      
      
                    
        if indice_zero == 2:
            donne = 1
        else:
            saut+=2
            col_en_cours = col_en_cours + 1






