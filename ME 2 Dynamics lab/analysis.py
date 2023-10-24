import numpy as np
import csv as c
from itertools import islice


#read in damped data
damped1 = []
with open('X2sv00006.txt') as f:
    for line in islice(f,10,None):
        damped1.append((float(line.split(' ')[0]),float(line.split(' ')[-1])))

damped2 = []
with open('X2sv00007.txt') as f:
    for line in islice(f,10,None):
        damped2.append((float(line.split(' ')[0]),float(line.split(' ')[-1])))

damped3 = []
with open('X2sv00008.txt') as f:
    for line in islice(f,10,None):
        damped3.append((float(line.split(' ')[0]),float(line.split(' ')[-1])))

damped4 = []
with open('X2sv00009.txt') as f:
    for line in islice(f,10,None):
        damped4.append((float(line.split(' ')[0]),float(line.split(' ')[-1])))
        