# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:21:46 2020

@author: papico
"""

####Histogramme d’un échantillon de loi continue
import numpy as np 
import scipy.stats as sps 
import matplotlib.pyplot as plt 
E = np.random.randn(int(1e5))#echantillon 
x = np.linspace(-4,4,1000) 
f_x = sps.norm.pdf(x) #Densite gaussienne 
plt.plot(x,f_x,"r",label="Theory") 
#Affichage histo: 
plt.hist(E,bins=50,normed=1,label="Data")
plt.xlabel("abscisses")
plt.ylabel("ordonnees") 
plt.legend(loc="best")