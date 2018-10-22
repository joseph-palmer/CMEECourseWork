#!/usr/bin/env python3
"""Python version of vectorise2.R"""
__appname__ = "vectorize2.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Oct-2018"

## imports ##
import sys
import numpy as np
import time
import math


def stochrickvect(p0 = np.random.uniform(.5,1.5,(1000)),r=1.2,K=1,sigma=0.2,numyears=100):
    # initialise  
    N = np.full([numyears, len(p0)], np.nan)
    N[0,] = p0
    for yr in range(1,numyears):
        N[yr,] = N[yr - 1,] * np.exp(r * (1 - N[yr - 1,] / K) + np.random.normal(0, sigma, len(p0)))
    return N



start = time.time()
stochrickvect()
end = time.time()

print("Python vectorized stochrickvect function: {}".format(end - start))
