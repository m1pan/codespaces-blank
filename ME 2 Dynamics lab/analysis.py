from itertools import islice
import numpy as np
import matplotlib.pyplot as plt


#read in damped data
def readfile(file):
    damped1 = []
with open('X2sv00006.txt') as f:
    for line in islice(f,9,None):
        damped1.append([float(line.split(' ')[0]),float(line.split(' ')[-1])])

damped1 = []
with open('X2sv00006.txt') as f:
    for line in islice(f,9,None):
        damped1.append([float(line.split(' ')[0]),float(line.split(' ')[-1])])

damped2 = []
with open('X2sv00007.txt') as f:
    for line in islice(f,9,None):
        damped2.append([float(line.split(' ')[0]),float(line.split(' ')[-1])])


damped3 = []
with open('X2sv00008.txt') as f:
    for line in islice(f,9,None):
        damped3.append([float(line.split(' ')[0]),float(line.split(' ')[-1])])

damped4 = []
with open('X2sv00009.txt') as f:
    for line in islice(f,9,None):
        damped4.append([float(line.split(' ')[0]),float(line.split(' ')[-1])])

damp = np.array([damped1, damped2, damped3, damped4])

for j in range(0,4):
    plt.plot([i[0] for i in damp[j]], [i[1] for i in damp[j]])
    plt.xlabel("Time / s")
    plt.ylabel("Acceleration / ms^-2")
    plt.xticks(np.arange(0, 16+0.5, 0.5))
    plt.yticks(np.arange(-16,17,1))
    plt.show()
