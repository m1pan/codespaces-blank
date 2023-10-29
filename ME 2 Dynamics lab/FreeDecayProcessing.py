# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:24:05 2023

@author: mpmor
"""
import matplotlib.pyplot as plt
import seaborn
import numpy as np


f = open("X2sv00006.txt")
a = f.readlines()
f.close()
A = []
for element in a:
    A += [element.strip()]
    

x = [0,]
y = [0,]
x_highs = [0,]
y_highs = [0,]
acceleration = A[9:]
for i in range(1,len(acceleration)):
    if abs(float((acceleration[i][-10:])))-abs(float(acceleration[i-1][-10:]))>0.5:
        pass
    else:
        x+=[float(acceleration[i][0:20])]
        y+=[float(acceleration[i][-10:])]
        try:
            if abs(y[-1])>abs(float(acceleration[i-1][-10:])) and abs(y[-1])>abs(float(acceleration[i+1][-10:])):
                x_highs += [x[-1]]
                y_highs +=[y[-1]]
        except:
            pass         
for i in range(0,len(x_highs)):
    try:
        
        if y_highs[i]>0 and y_highs[i+1]>0 or y_highs[i]<0 and y_highs[i+1]<0:
            if abs(y_highs[i])>abs(y_highs[i+1]):
                
                y_highs.pop(i+1)
                x_highs.pop(i+1)
            else:
                y_highs.pop(i)
                x_highs.pop(i)
    except:
        pass

def OverallGraph():
    plt.plot(x,y,linewidth=0.5)
    plt.ylim()
    plt.xlim(0,5)
    plt.xlabel("Time (s)")
    plt.ylabel("Aceleration (mm/s^2)")
    plt.axhline(0,color="k",linestyle = "dotted")
    seaborn.despine()
    plt.show()

def TruncatedGraph(x1,x2):
    plt.plot(x,y,linewidth=0.5)
    plt.ylim(-1.5,1.5)
    plt.xlim(x1,x2)
    plt.xlabel("Time (s)")
    plt.ylabel("Aceleration (mm/s^2)")
    plt.axhline(0,color="k",linestyle = "dotted")
    seaborn.despine()
    plt.show()
    
def TruncatedGraphHighs(x1,x2):
    plt.scatter(x_highs,y_highs,s=5)
    plt.ylim(-1.5,1.5)
    plt.xlim(x1,x2)
    plt.xlabel("Time (s)")
    plt.ylabel("Aceleration (mm/s^2)")
    plt.axhline(0,color="k",linestyle = "dotted")
    plt.title()
    seaborn.despine()
    plt.show()
    

print(y_highs[150:170])
steps = []
deltas = []
for i in range(0,len(x_highs[150:170])-1):
    steps+=[x_highs[150:170][i+1]-x_highs[150:170][i]]
    try:    
        deltas += [np.log(y_highs[150:170][i]/y_highs[150:170][i+2])]
    except:
        pass
T = 2 * sum(steps)/len(steps)
omega = 2*np.pi/T
delta = sum(deltas)/len(deltas)
dampingratio = delta/(2*np.pi)
print(dampingratio)
print(omega)
OverallGraph()
TruncatedGraph(2,3)
    
