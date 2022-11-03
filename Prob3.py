import numpy as np

def triband(a,d,c,b):
    n = len(d)
    assert len(a) == len(c) == n-1
    assert len(b) == n
    
    x = np.zeros_like(b)
    
    #Your code here
    #End your code
    
    return x

def Problem3(a,d,c,b):
    return triband(a,d,c,b)
