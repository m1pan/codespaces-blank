from itertools import islice
from math import fsum
import numpy as np
import matplotlib.pyplot as plt

# number of readings
GAP = 4096

# time interval between each reading, 16s recordings
interval = 1/256

# function to read in damped data
def readfile(file):
    """reads file and inputs data into a nested list"""
    tmp = []
    with open(file,'r') as f:
        for line in islice(f,9,None):
            tmp.append([float(line.split(' ')[0]),float(line.split(' ')[-1])])
    return tmp

# collect peaks and troughs
def peak(dataArray,j):
    '''takes in a np array of dataand dataset number and gives a list of peaks after 1.5s'''   
    tmp = []
    for i in range(int(1.5/interval),GAP-1):
        if dataArray[j-1,i,1] > dataArray[j-1,i-1,1] and dataArray[j-1,i,1] > dataArray[j-1,i+1,1]:
            tmp.append([dataArray[j-1,i,0],dataArray[j-1,i,1]])
    return tmp

def trough(dataArray,j):
    '''takes in a np array of dataand dataset number and gives a list of troughs after 1.5s'''  
    tmp = []
    for i in range(int(1.5/interval),GAP-1):
        if dataArray[j-1,i,1] < dataArray[j-1,i-1,1] and dataArray[j-1,i,1] < dataArray[j-1,i+1,1]:
            tmp.append([dataArray[j-1,i,0],dataArray[j-1,i,1]])
    return tmp

# initialise empty array for data
damp = np.empty((4,GAP,2))

# read in damped data
for i in range(0,4):
    tmp = readfile(f'X2sv0000{i+6}.txt')
    noise = [m[1] for m in tmp[:9]]
    offset = fsum(noise)/len(noise)
    for j in range(0,GAP):
        damp[i,j,0] = tmp[j][0]
        damp[i,j,1] = tmp[j][1]-offset

# find natural frequency
# make lists of peaks and troughs[test number][peak number][time or amplitude]
peaks=[]
troughs=[]
for i in range(1,5):
    peaks.append(peak(damp,i))
    troughs.append(trough(damp,i))

periods = [[],[],[],[]]
deltas = [[],[],[],[]]
for i in range(0,4):
    for j in range(len(peaks[i])-1):
        periods[i] += [peaks[i][j+1][0] - peaks[i][j][0]]
        deltas[i] += [np.log(peaks[i][j][1]/peaks[i][j+1][1])]
T = [fsum(m)/len(m) for m in periods]
delta = [fsum(n)/len(n) for n in deltas]
wd = [2*np.pi/t for t in T]
dampratio = [d/(2*np.pi) for d in delta]
wn = [wd[i]/np.sqrt(1-dampratio[i]**2) for i in range(4)]
print(delta,fsum(delta)/4)
print(dampratio,fsum(dampratio)/4)
print(wd,fsum(wd)/4)
print(wn,fsum(wn)/4)


# plotting the graphs
# for j in range(0,4):
#     plt.plot([i[0] for i in damp[j]], [i[1] for i in damp[j]])
#     plt.xlabel("Time / s")
#     plt.ylabel("Acceleration / ms^-2")
#     plt.xticks(np.arange(0, 16+0.5, 0.5))
#     plt.yticks(np.arange(-16,17,1))
#     plt.show()
