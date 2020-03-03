# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:24:41 2020

@author: papico
"""

###Théorème (Loi des Grands Nombres, Kolmogorov, 1929)
import matplotlib.pyplot as plt 
import numpy as np 
n=int(1e3) 
S=np.cumsum(np.random.rand(n))/np.arange(1,n+1) 
plt.plot(range(1,n+1),S,"r",label="S_n") 
plt.plot((1,n),(.5,.5),"b−−",label="Esperance") 
plt.ylabel("S_n") 
plt.xlabel("n") 
plt.legend(loc="best") 
plt.title("LGN")