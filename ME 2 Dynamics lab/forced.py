from itertools import islice
from math import fsum
import numpy as np
import matplotlib.pyplot as plt

# number of readings
GAP = 4096

# time interval between each reading, 20s recordings
interval = 5/1024

# function to read in damped data
def readfile(file):
    """reads file and inputs data into a nested list"""
    tmp = []
    with open(file,'r') as f:
        for line in islice(f,11,None):
            tmp.append([float(i) for i in line.split()])
    return tmp

# collect peaks and troughs
def peak(dataArray,j):
    '''takes in a np array of dataand dataset number and gives a list of peaks after 1.5s'''
    
    peaks = []
    for i in range(int(1.5/interval),GAP-1):
        if dataArray[j-1,i,1] > dataArray[j-1,i-1,1] and dataArray[j-1,i,1] > dataArray[j-1,i+1,1]:
            peaks.append([dataArray[j-1,i,0],dataArray[j-1,i,1]])
    return peaks

def trough(dataArray,j):
    '''takes in a np array of dataand dataset number and gives a list of troughs after 1.5s'''
    
    troughs = []
    for i in range(int(1.5/interval),GAP-1):
        if dataArray[j-1,i,1] < dataArray[j-1,i-1,1] and dataArray[j-1,i,1] < dataArray[j-1,i+1,1]:
            troughs.append([dataArray[j-1,i,0],dataArray[j-1,i,1]])
    return troughs