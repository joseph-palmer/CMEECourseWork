#!/usr/bin/env python3
"""Log-likelihood functions for mletools"""
__appname__ = "loglike.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import numpy as np
import scipy as sp

def LLExponential(rate, x):
    """LLExponential - Loglikelihood function for exponential.

    :param rate: - the rate paramater of the model.
    :param x: data.
    """
    rate = rate[0]
    eq = (len(x) * np.log(rate) - rate * np.sum(x))
    return -eq

def LLLognormal(params, x):
    """LLLognormal - Loglikelihood function for the lognormal.

    :param params: Paramaters of the model (mean and standard deviation).
    :param x: data.
    """
    mu = params[0]
    sigma = params[1]**2
    eq = (-(len(x) / 2) * np.log(2 * np.pi * sigma) -
        (np.sum([(np.log(x_) - mu)**2 for x_ in x]) / (2 * sigma)) -
        np.sum(np.log(x)))
    return -eq

def LLNormal(params, x):
    """LLNormal - Loglikelihood function for the normal distribution.

    :param params: paramaters of the model (mean standard deviation)..
    :param x: data.
    """
    mu = params[0]
    sigma = params[1]**2
    eq = (-len(x) / 2.0 * np.log(2 * np.pi) - 
           len(x) / 2.0 * np.log(sigma) - 
           1 / (2 * sigma) * np.sum([(x_ - mu)**2 for x_ in x]))
    return -eq

def LLGamma(params, x):
    """LLGamma - Loglikelihood function of the gamma distribution.

    :param params: paramaters required.
    :param x: data.
    """
    k = params[0]
    theta = params[1]
    eq = ((k - 1) * np.sum(np.log(x)) - 
          np.sum([x_ / theta for x_ in x]) -
          len(x) * k * np.log(theta) - 
          len(x) * np.log(sp.special.gamma(k)))
    return -eq

def LLSumExp_2r(params, x):
    r1 = params[0]
    r2 = params[1]
    p1 = params[2]
    eq = (len(x) * np.log((p1 * r1) * ((1 - p1) * r2)) - (r1**len(x) + r2**len(x)) * np.sum(x))
    return -eq

def LLSumExp_3r(params, x):
    r1 = params[0]
    r2 = params[1]
    r3 = params[2]
    p1 = params[3]
    p2 = params[4]
    if (p1 + p2) > 1:
        return 100000
    eq = (len(x) * np.log((p1 * r1) * (p2 * r2) * ((1 - p1 - p2) * r3)) -
         (r1 + r2 + r3) * np.sum(x))
    return -eq

def LLSumExp(params, x, rval):
    rates = params[:rval]
    probs = params[rval:]
    df = np.column_stack((rates[:-1], probs))
    if np.sum(probs) > 1:
        return 1000000
    e1 = "*".join(["({}*{})".format(i[0], i[1]) for i in df])
    e2 = "1-{}".format("-".join([str(i) for i in probs]))
    e3 = "({})*{}".format(e2, rates[-1])
    e4 = "{}*({})".format(e1, e3)
    e5 = "len(x)*np.log({})".format(e4)
    e6 = "{}-({})*np.sum(x)".format(e5, "+".join(["{}**len(x)".format(i) for i in rates]))
    eq = eval(e6)
    return -eq
