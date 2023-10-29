# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:30:45 2023

@author: mpmor
"""

import matplotlib.pyplot as plt
import seaborn
import numpy as np


def OpenFile(name):
    f = open(name)
    a = f.readlines()
    f.close()
    A = []
    for element in a:
        A += [element.strip()]
    A = A[11:]
    tf = []
    ta = []
    F = []
    a = []
    for i in range(1,len(A)):
        if abs(abs(float((A[i][-10:])))-abs(float(A[i-1][-10:])))>0.03:
            pass
        else:
            ta+=[float(A[i][0:20])]
            a+=[float(A[i][-10:])]
            
            
    for i in range(1,len(A)):
        if abs(abs(float((A[i][-27:-18])))-abs(float(A[i-1][-27:-18])))>0.2:
            pass
        else:
            tf+=[float(A[i][0:20])]
            F+=[float(A[i][-27:-18])]        
            
           
    return [tf,F,ta,a]

def Plot(name,title):
    
    tf = OpenFile(name)[0]
    F = OpenFile(name)[1]
    ta = OpenFile(name)[2]
    a = OpenFile(name)[3]
    
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Force (N)', color=color)
    ax1.set_xlim(1,2)
    ax1.set_title(title)
    ax1.plot(tf, F, color=color, linewidth = 0.5)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    
    color = 'tab:blue'
    ax2.set_ylabel('Acceleration (m/s^2)', color=color)  # we already handled the x-label with ax1
    ax2.plot(ta, a, color=color, linewidth = 0.5)
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    return fig
"""  
for i in range(1,12):
    Plot("F"+str(i)+".txt","Force and Acceleration against time at a frequency of Hz")
    plt.show()
 """
    
def BodePlot():
    f = [10,12,14,16,17,17.5,18,18.25,18.5,19,20]
    a = [23.6,46.3,81.3,182.6,418.4,705.9,2875.0,3192.3,1359.0,645.2,306.1]
    a = [x/1000 for x in a]
    p = [0,0,0,0,0,0,-0.81,-1.57,-3.14,-3.14,-3.14]
    print(a)
    
    fig, ax = plt.subplots(2,1,figsize = (6,6))
    ax[0].set_xlabel('Frequency (Hz)')
    ax[0].set_ylabel('Accelerance (m/s^2N)')
    ax[0].plot(f, a, linewidth = 1)
    ax[0].tick_params(axis='y')
    ax[0].set_ylim(0,3.500)
    ax[0].set_xlim(10,20)
    ax[1].set_xlabel('Excitation Frequency (Hz)')
    ax[1].set_ylabel('Phase Difference (rad)')
    ax[1].plot(f, p, linewidth = 1)
    ax[1].tick_params(axis='y')
    ax[1].set_ylim(-3.5,0.5)
    ax[1].set_xlim(10,20)
    seaborn.despine(ax=ax[0], offset=0)
    seaborn.despine(ax=ax[1], offset=0)
    ax[1].axhline(-1.571,color="k",linestyle = "dotted")
    ax[0].axvline(18.25,color="k",linestyle = "dotted",clip_on=False)
    ax[1].axvline(18.25,color="k",linestyle = "dotted",clip_on=False)
    
    
    
BodePlot()    
""" 
    fig,ax = plt.subplots(2,1,figsize = (8,10))
    
    ax[0].plot(np.arange(0,geometry["Length"],0.01),shear_force)
    ax[0].grid(True, which='both')
    ax[0].set_xlabel("Distance (m)")
    ax[0].set_ylabel("Shear Force (N)")
    ax[0].set_title("Shear Force Diagram")
    ax[1].plot(np.arange(0,geometry["Length"],0.01),bending_moment)
    ax[1].grid(True, which='both')
    ax[1].set_xlabel("Distance (m)")
    ax[1].set_ylabel("Bending Moment (Nm)")
    ax[1].set_title("Bending Moment Diagram")
    seaborn.despine(ax=ax[0], offset=0)
    seaborn.despine(ax=ax[1], offset=0)
"""


    