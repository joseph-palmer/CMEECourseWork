#!/usr/bin/env python3
"""Cummulative Density Functions for mletols"""
__appname__ = "cdf.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import numpy as np
import scipy as sp

def ExponentialDist(params, x):
    """ExponentialDist - CDF function for exponential distribution

    :param params: paramters required (rate).
    :param x: data.
    """
    rate = params[0]
    eq = 1 - np.exp(-rate * x)
    return 1 - eq

def NormalDist(params, x):
    """NormalDis - CDF function for the normal distributiont.

    :param params: paramaters required (meam and standard deviation).
    :param x: data.
    """
    mu = params[0]
    sigma = params[1]
    eq = 1 / 2 * (1 + sp.special.erf((x - mu) / (sigma * np.sqrt(2))))
    return 1 - eq

def LognormalDist(params, x):
    """LognormalDist - CDF function for the log-normal distribution.

    :param params: paramaters required (mean and standard deviation).
    :param x: data.
    """
    mu = params[0]
    sigma = params[1]
    eq = ((1 / 2) + (1 / 2) * sp.special.erf((np.log(x) - mu) / 
          np.sqrt(2 * sigma)))
    return 1 - eq

def GammaDist(params, x):
    """GammaDist - CDF function for the gamma distribution.

    :param params: paramaters required (alpha and beta).
    :param x: data.
    """
    k = params[0]
    theta = params[1]
    eq = (sp.special.gammainc(k, x / theta))
    return 1 - eq

def SumExp_2r(params, x):
    """SumExp_2p - CDF for 2 rate sum of exponentials.

    :param params: paramaters required (rate 1 and 2, probability 1).
    :param x: data.
    """
    r1 = params[0]
    r2 = params[1]
    p1 = params[2]
    eq = (p1 - 1) * np.exp(-r2 * x) - p1 * np.exp(-r1 * x) + 1
    return 1 - eq

def SumExp_3r(params, x):
    r1 = params[0]
    r2 = params[1]
    r3 = params[2]
    p1 = params[3]
    p2 = params[4]
    eq = ((p2 + p1 - 1) * np.exp(-r3 * x) - 
          p2 * np.exp(-r2 * x) -
          p1 * np.exp(-r1 * x) + 1)
    return 1 - eq

def SumExp(params, x, rval):
    rates = params[:rval]
    probs = params[rval:]
    df = np.column_stack((rates[:-1], probs))
    e1 = "({}-1)".format("+".join([str(i) for i in reversed(probs)]))
    e2 = "np.exp(-{}*x)".format(rates[-1])
    e3 = ["({}*np.exp(-{}*x))".format(i[1], i[0]) for i in reversed(df)]
    e4 = "({}*{}-{})+1".format(e1, e2, "-".join(e3))
    return 1 - eval(e4)
