import numpy as np


def Problem1(n): 
    onesk = np.ones((n,n))
    indx = #Your code here
    xyindx = tuple(zip(*indx))
    onesk[xyindx] = 0
    return onesk
