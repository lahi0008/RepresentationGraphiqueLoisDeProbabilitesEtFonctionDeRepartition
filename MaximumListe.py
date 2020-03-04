# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:24:32 2020

@author: papico
"""

def maximumListe(L,left,right): 
    if left== right: 
        return L[left] 
    else:
        m = (left+right)//2 
        x = maximumListe(L,m+1,right) 
        y = maximumListe(L,left,m) 
        themax= x if (x > y) else y 
        return themax
print(maximumListe([5,17],0,1))