#!/usr/bin/env python3
"""Test script for MLE of half normal distribution"""
__appname__ = "halfnorm.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import sys
import numpy as np
import scipy as sp
from scipy.optimize import minimize

# sample from half normal distribution
# first create a half normal pdf
data = np.genfromtxt('halfnorm.csv', delimiter=',')
data = np.delete(data, 0)

# create a loglikelihood function
def LLHalfnorm(params, x):
    mu = params[0]
    sigma = params[1]**2
    eq1 = -(len(x) / 2 * np.log(2 * np.pi * sigma) - np.sum([((x_ - mu)**2 / 2 * sigma) for x_ in x]) + np.sum(np.log([1 + np.exp(-(2 * mu * x_) / sigma) for x_ in x])))
    return eq1


params = [1.1, 1.1]
a = minimize(LLHalfnorm, params, data, method = "l-bfgs-b")
print(a)
