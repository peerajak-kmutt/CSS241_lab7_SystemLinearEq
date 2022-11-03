import numpy as np

def GaussianSwapForwardElimination(A,b):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    Aans = A.copy()
    bans = b.copy()
    l = list(range(n))
    sl = np.abs(A).max(axis=1)

    #Your Code Here
    # End your code

    
    return Aans,bans,l

def GaussianSwapBacksubstitution(A,b,l):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    x = np.zeros(n,dtype=np.float64)
    #Your Code Here
    # End your code
    return x

def Problem2(A,b):
    Aselem,bselem,l = GaussianSwapForwardElimination(A,b)
    x = GaussianSwapBacksubstitution(Aselem,bselem,l)
    return x

