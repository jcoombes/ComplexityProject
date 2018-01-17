"""
Implementation of the Oslo model.
"""

import numpy as np



size = 16 # System size, int
p = 0.5

slopes = np.zeros(size)
np.random.seed(0) #Makes the initial threshhold sloped predictable from run to run.
rands = np.random.rand(size)

thresh = np.array([1 if i <= p else 2 for i in rands])

print(thresh)

def drive():
    slopes[0] += 1

def relax(i):
    """
    Helper function to relax slopes
    i - int, which site do you want to relax?
    """
    i = int(i)
    print(i)
    if i == 0:
        slopes[i] -= 2
        slopes[i+1] += 1
    
    elif (size-1) > i > 0:
#        print("i is ", i)
        slopes[i-1] += 1
        slopes[i] -= 2
        slopes[i+1] += 1
    
    elif (size-1) == i:
        slopes[i-1] += 1
        slopes[i] -= 1
        
    else:
        raise(IndexError)
    
    thresh[i] = (1 if np.random.rand <= p else 2)

vrelax = np.vectorize(relax)

def relaxation(slopes, thresh):
    """
    Relax the slope until no slopes are greater than thresh.
    """
    while (slopes > thresh).any():
        mask = slopes > thresh
        print(slopes[mask])
        np.where(mask, vrelax(slopes), slopes)
        vrelax(slopes[mask])
        #for i in range(len(slopes)):
        #    if slopes[i] > thresh[i]:
        #        relax(i)
            
    print(slopes)