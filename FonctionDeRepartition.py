# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:28:48 2020

@author: papico
"""

###Pour la fonction de répartition :
import numpy as np 
import matplotlib.pyplot as plt
def repartuni(x): #fonction de répartition pour a=-1 et b=2 
    if x<-1: 
        return(0) 
    elif (-1<=x and x<=2): 
        return((x+1)/3) 
    else: return(1)
abs=np.linspace(-5,5,200) 
y=[repartuni(x) for x in abs] 
plt.grid() 
plt.plot(abs,y) 
plt.xlabel("abscisses")
plt.ylabel("ordonnees")
plt.show()
plt.savefig("FonctionRepartition.png")
