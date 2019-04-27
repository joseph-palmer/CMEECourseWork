#!/usr/bin/env python3
"""Test MLE of normal distribution"""
__appname__ = "normal.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# draw data from a normal distribution
n = 10000
mu = 3.6
sigma = 1.8
data = np.random.normal(mu, sigma, n)

plt.hist(data)
#plt.show()

def LLNormal(params, x):
    """LLNormal - return normal Log-Likelihood of data

    :param params: List / tuple of parameters
    :param x: the data to be used
    """ 
    mu = params[0]
    sigma = params[1]
    return -(n / 2.0 * np.log(2 * np.pi) - n / 2.0 * np.log(sigma**2) - 1 / (2 * sigma**2) * sum([(x_ - mu)**2 for x_ in x]))


# set parameter estimates
params = [0.1, 0.1]

# get MLE estimate
a = minimize(LLNormal, params, data, method = "l-bfgs-b")

print(a)
print("ANALYTICAL: mu = {}, sigma = {}".format(np.mean(data), np.std(data)))
