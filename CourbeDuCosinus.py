# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:31:48 2020

@author: papico
"""

#courbe du cosinus
import matplotlib.pyplot as plt
import numpy as np
from math import pi,cos
plt.clf()

x=np.linspace(0,2*pi,1000)
y=[cos(t) for t in x]
plt.plot(x,y,label="cos(x)")
plt.title("courbe du cosinus")
plt.xlabel("abscisses")
plt.ylabel("ordonnees")
plt.savefig("image.png")
plt.show()