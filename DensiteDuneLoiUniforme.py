# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:26:48 2020

@author: papico
"""

###Pour représenter la densité d’une loi uniforme on peut faire :
import numpy as np 
import matplotlib.pyplot as plt
def densuni(x): #densité pour a=-1 et b=2 
    if (-1<=x and x<=2): 
        return(1/3) 
    else: 
        return(0)
abs=np.linspace(-5,5,200) 
y=[densuni(x) for x in abs] #à cause des inégalités dans densuni on construit les ordonnées à la main 
plt.grid() 
plt.plot(abs,y) 
plt.xlabel("abscisses")
plt.ylabel("ordonnees")
plt.show()