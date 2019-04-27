#!/usr/bin/env python3
"""MLE test of Gamma distribution"""
__appname__ = "gamma.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import sys
import numpy as np
from scipy.optimize import minimize
from scipy.special import gamma

# sample from gamma distribution
n = 100000
alpha = 3
beta = 1/1.2

data = np.random.gamma(alpha, beta, n)

# make gamma function
def LLGamma(params, x):
    alpha = params[0]
    beta = params[1]
    ex1 = -(len(x) * alpha * np.log(beta) - len(x) * np.log(gamma(alpha)) + (alpha - 1) * np.sum(np.log(x)) - beta * np.sum(x))
    return ex1


params = [1.1, 1.1]
a = minimize(LLGamma, params, data, method = "l-bfgs-b")
print(a)
