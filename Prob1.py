import numpy as np

def GaussianForwardElimination(A,b): #A,b are numpy array of size (n,n) and n for equation Ax=b
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    Aans = A.copy()
    bans = b.copy()

    #Your Code Here
    #End Your code
    
    return Aans,bans

def GaussianBacksubstitution(A,b):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    x = np.zeros(n,dtype=np.float64)
    
    #Your Code Here
    #End Your code
    
    return x

def Problem1(A,b): 
    Aelem, belem = GaussianForwardElimination(A,b)
    x = GaussianBacksubstitution(Aelem,belem)
    return x
