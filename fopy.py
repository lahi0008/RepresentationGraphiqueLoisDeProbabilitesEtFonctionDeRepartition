# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 01:10:55 2020
@author: Coumbiss
"""
#%%
#Loi Binomiale
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
n, p, N = 20, 0.3, int(1e4)
B = np.random.binomial(n, p, N)
f = sps.binom.pmf(np.arange(n+1), n, p)
plt.hist(B,bins=n+1,normed=1,range=(0.5,n+.5),color = "white",label="loi empirique")
plt.stem(np.arange(n+1),f,"r",label="loi theorique")
plt.legend()
plt.grid()
#%%
#Loi normale
import numpy as np
import matplotlib.pyplot as plt
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2)),
         linewidth=2, color='r', label ="loi normale")
plt.legend()
plt.grid()
plt.show()
#%%

#Loi exponentielle
import numpy as np 
import matplotlib.pyplot as plt  
in_array = [1, 1.2, 1.4, 1.6, 1.8, 2] 
out_array = np.exp(in_array)  
y = [1, 1.2, 1.4, 1.6, 1.8, 2] 
plt.plot(in_array, y, color = 'blue', marker = "*", label ="loi empirique")   
# red for numpy.exp() 
plt.plot(out_array, y, color = 'red', marker = "o", label ="fonction de densité") 
plt.title("loi exponentielle") 
plt.xlabel("X", color = "green") 
plt.ylabel("Y", color = "green") 
plt.legend()
plt.grid()
plt.show()   
#%%
#Loi de poisson
import  numpy  as  np 
import matplotlib.pyplot as plt
s = np.random.poisson(5, 10000)
count ,  bins ,  ignored  =  plt . hist ( s ,  14 ,  density = True, label = "loi de Poisson" ) 
plt.legend()
plt.grid()
plt.show ()
#%%
#loi uniforme
import numpy as np
import matplotlib.pyplot as plt
s = np.random.uniform(-1,0,1000)
count, bins, ignored = plt.hist(s, 15, normed=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r', label ="loi uniforme")
plt.legend()
plt.grid()
plt.show()
#%%