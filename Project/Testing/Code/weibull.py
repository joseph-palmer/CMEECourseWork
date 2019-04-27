#!/usr/bin/env python3
"""MLE of weibull distribution test"""
__appname__ = "weibull.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import sys
import numpy as np
from scipy.optimize import minimize

# sample from weibull distribution
n = 100
beta = 3
lam = 1
data = np.random.weibull(beta, n) # lam not passed but is 1. cant pass it!
data = np.genfromtxt("weibull.csv", delimiter=",")
data = np.delete(data, 0)


def LLWeibull(params, x):
    beta = params[0]
    lam = params[1]
    print(params)
    eq1 = -(len(x) * np.log(beta) - len(x) * np.log(lam) - np.sum([x_/lam for x_ in x])**beta + (beta - 1) * np.sum(np.log(x)))
    eq2 = -(len(x) * np.log(lam) - lam * len(x) * np.log(beta) + (lam - 1) * np.sum(np.log(x)) - np.sum([x_/ beta for x_ in x]))
    eq3 = -(len(x) * np.log(lam) + len(x) * np.log(beta) + (lam - 1) * np.sum(np.log(x)) - lam * np.sum([x_**beta for x_ in x]))
    eq4 = -(len(x) * np.log(beta) + len(x) * np.log(lam) + (beta - 1) * np.sum(np.log(x)) - beta * np.sum([x_**lam for x_ in x]))

    return eq3


# set params
params = [1.1, 1.1]

# get MLE estimate
a = minimize(LLWeibull, params, data, method = "l-bfgs-b")
print(a)
