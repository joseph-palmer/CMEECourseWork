#!/usr/bin/env python3
"""Python version of vectorize1.R"""
__appname__ = "vectorize1.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Oct-2018"

## imports ##
import sys
import numpy as np
import time

def SumAllElements(M):
    Dimensions = M.shape
    total = 0
    for i in range(0,Dimensions[0]):
        for j in range(0,Dimensions[-1]):
            total = total + M[i, j]
    return total


# create random matrix
M = np.random.rand(1000, 1000)

# time the looping function
start = time.time()       
SumAllElements(M)
end = time.time()
elapsed = end - start
print("Python SumAllElements function: {}".format(elapsed))

# time the vectorized sum function.
start = time.time()
M.sum()
end = time.time()
elapsed2 = end - start
print("Python sum vectorised function: {}".format(elapsed2))
