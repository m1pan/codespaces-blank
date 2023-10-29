from itertools import islice
import numpy as np
import matplotlib.pyplot as plt

# number of readings
GAP = 4096

# function to read in damped data
def readfile(file):
    """reads file and inputs data into a nested list"""
    tmp = []
    with open(file,'r') as f:
        for line in islice(f,9,None):
            tmp.append([float(line.split(' ')[0]),float(line.split(' ')[-1])])
    return tmp

damp = np.empty((4,4096,2))

# read in damped data
for i in range(0,4):
    tmp = readfile(f'X2sv0000{i+6}.txt')
    for j in range(0,GAP):
        damp[i,j,0] = tmp[j][0]
        damp[i,j,1] = tmp[j][1]

#plotting the graphs
# for j in range(0,1):
#     plt.plot([i[0] for i in damp[j]], [i[1] for i in damp[j]])
#     plt.xlabel("Time / s")
#     plt.ylabel("Acceleration / ms^-2")
#     plt.xticks(np.arange(0, 16+0.5, 0.5))
#     plt.yticks(np.arange(-16,17,1))
#     plt.show()

# find natural frequency
# collect peaks and troughs
def peak(dataArray,j):
    '''takes in a np array of dataand dataset number and gives a list of peaks'''
    
    peaks = []
    for i in range(1,GAP):
        if dataArray[j-1,i,1] > dataArray[j-1,i-1,1] and dataArray[j-1,i,1] > dataArray[j-1,i+1,1]:
            peaks.append([dataArray[j-1,i,0],dataArray[j-1,i,1]])
    return peaks

def troughs(dataArray,j):
    '''takes in a np array of dataand dataset number and gives a list of troughs'''
    
    troughs = []
    for i in range(1,GAP):
        if dataArray[j-1,i,1] < dataArray[j-1,i-1,1] and dataArray[j-1,i,1] < dataArray[j-1,i+1,1]:
            troughs.append([dataArray[j-1,i,0],dataArray[j-1,i,1]])
    return troughs
