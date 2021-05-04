# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:13:39 2021

@author: wimpo
"""
from operator import itemgetter
import matplotlib.pyplot as plt
def ploT():
    pp=[]  
    with open("temperature_sample_calibrate2.csv",'r') as file:
            tabLines=file.read().splitlines()
            tabLines.pop(0) #delete first line with i and t
            for element in tabLines:
                i=float(element.split(";")[0])
                t=float(element.split(";")[1])
                pp.append((i,t))
    tabSorted=sorted(pp,key=itemgetter(0))
    X=[item[0] for item in tabSorted]
    Y=[item[1] for item in tabSorted]
    plt.scatter(X,Y)