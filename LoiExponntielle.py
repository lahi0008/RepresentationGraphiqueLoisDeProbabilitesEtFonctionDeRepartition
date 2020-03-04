# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:13:50 2020

@author: papico
"""

###Loi exponentielle
from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt
abs=np.linspace(0,8,200) 
plt.plot(abs,expon.pdf(abs,scale=1)) 
plt.plot(abs,expon.pdf(abs,scale=1/3)) 
plt.grid() 
plt.xlabel("abscisses")
plt.ylabel("ordonnees")
plt.savefig("Exponentielle.png")
plt.show()