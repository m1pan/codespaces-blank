from itertools import islice
from math import fsum
import numpy as np
import matplotlib.pyplot as plt

# number of readings
GAP = 4096

# time INTERVAL between each reading, 2s recordings
INTERVAL = 1/2048

# function to read in damped data
def readfile(file):
    """reads file and inputs data into a nested list"""
    tmp = []
    with open(file,'r') as f:
        for line in islice(f,11,None):
            tmp.append([float(i) for i in line.split()])
    return tmp

# collect peaks and troughs
def peak(dataArray):
    '''takes in a list of dataand dataset number and gives a list of peaks after 1.5s'''  
    forcepeaks = []
    accelpeaks = []
    for i in range(int(1.5/INTERVAL),GAP-1):
        if dataArray[i][1] > dataArray[i-1][1] and dataArray[i][1] > dataArray[i+1][1]:
            forcepeaks.append([dataArray[i][0],dataArray[i][1]])
        elif dataArray[i][2] > dataArray[i-1][2] and dataArray[i][2] > dataArray[i+1][2]:
            accelpeaks.append([dataArray[i][0],dataArray[i][2]])
    return forcepeaks,accelpeaks

def trough(dataArray):
    '''same as peak but for trough'''
    forcetroughs = []
    acceltroughs = []
    for i in range(int(1.5/INTERVAL),GAP-1):
        if dataArray[i][1] < dataArray[i-1][1] and dataArray[i][1] < dataArray[i+1][1]:
            forcetroughs.append([dataArray[i][0],dataArray[i][1]])
        elif dataArray[i][2] < dataArray[i-1][2] and dataArray[i][2] < dataArray[i+1][2]:
            acceltroughs.append([dataArray[i][0],dataArray[i][2]])
    return forcetroughs,acceltroughs

# dictionary for data of different frequencies
freqs = [10,12,13,14,15,16,18,20,14.5]
data = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}
fpeaks = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}
ftroughs = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}
apeaks = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}
atroughs = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}

# read in all data and find peaks and troughs
for i in range(len(data)):
    data[freqs[i]] = readfile(f'Xxsv{(i+9):05}.txt')
    fpeaks[freqs[i]],apeaks[freqs[i]] = peak(data[freqs[i]])
    ftroughs[freqs[i]],atroughs[freqs[i]] = trough(data[freqs[i]])

Tf = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}
Ta = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}

# populating force and accel periods
for i in freqs:
    for j in range(len(fpeaks[i])-1):
        Tf[i]+=[fpeaks[i][j+1][0]-fpeaks[i][j][0]]
    for k in range(len(apeaks[i])-1):
        Ta[i]+=[apeaks[i][j+1][0]-apeaks[i][j][0]]

#phase shift
shifts = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}

for k,v in fpeaks.items():
    for i in range(len(v)-1):
        phi = 0
        if apeaks[k][i][0]>v[i][0]:
            phi = -360*((apeaks[k][i][0]-v[i][0])/(v[i+1][0]-v[i][0]))
        else:
            phi = -360*((apeaks[k][i+1][0]-v[i][0])/(v[i+1][0]-v[i][0]))
        shifts[k].append(phi)


phaseshift = {10:[], 12:[],13:[],14:[],15:[],16:[],18:[],20:[],14.5:[]}
for k,v in shifts.items():
    phaseshift[k] = fsum(v)/len(v)
print(phaseshift)




# fig, ax = plt.subplots(2,1)

# ax[0].plot([i[0] for i in data[10]],[i[1] for i in data[10]],color='b')
# ax[0].set_xlabel('Time / s')
# ax[0].set_ylabel('Force (N)')

# ax[1].plot([i[0] for i in data[10]], [i[2] for i in data[10]],color='r')
# ax[1].set_xlabel('Time / s')
# ax[1].set_ylabel('Acceleration / ms^-2')

# plt.show()
