from itertools import islice
import numpy as np
import matplotlib.pyplot as plt

#number of readings
GAP = 4096

#read in damped data
def readfile(file):
    """reads file and inputs data into a nested list"""
    tmp = []
    with open(file,'r') as f:
        for line in islice(f,9,None):
            tmp.append([float(line.split(' ')[0]),float(line.split(' ')[-1])])
    return tmp

damp = np.empty((4,4096,2))


for i in range(0,4):
    tmp = readfile(f'X2sv0000{i+6}.txt')
    for j in range(0,GAP):
        damp[i,j,0] = tmp[j][0]
        damp[i,j,1] = tmp[j][1]


for j in range(0,4):
    plt.plot([i[0] for i in damp[j]], [i[1] for i in damp[j]])
    plt.xlabel("Time / s")
    plt.ylabel("Acceleration / ms^-2")
    plt.xticks(np.arange(0, 16+0.5, 0.5))
    plt.yticks(np.arange(-16,17,1))
