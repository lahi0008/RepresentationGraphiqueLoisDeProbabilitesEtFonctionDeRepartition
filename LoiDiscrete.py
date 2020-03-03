# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:23:29 2020

@author: papico
"""

###Représentation d’un échantillon de loi discrète

import numpy as np 
import scipy.stats as sps 
import matplotlib.pyplot as plt
n, p, N = 20, 0.3, int(1e4) 
B = np.random.binomial(n, p, N) 
m= sps.binom.pmf(np.arange(n+1), n, p) 
plt.hist(B,bins=n+1,normed=1,range=(-.5,n+.5),\
         color="white",label="loi empirique")
plt.stem(np.arange(n+1),m,"r",label="loi theorique")
plt.xlabel("abscisses")
plt.ylabel("ordonnees")
plt.legend()