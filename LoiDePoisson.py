# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:10:12 2020

@author: papico
"""
###Loi de poisson
import  numpy  as  np 
import matplotlib.pyplot as plt
s = np.random.poisson(5, 10000)
count ,  bins ,  ignored  =  plt . hist ( s ,  14 ,  density = True, label = "loi de Poisson" ) 
plt.legend()
plt.grid()
plt.xlabel("abscisses")
plt.ylabel("ordonnees") 
plt.show ()