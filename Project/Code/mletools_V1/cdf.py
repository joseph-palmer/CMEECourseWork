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

def WeibullDist(params, x):
    """WeibullDist - CDF function for the 2 paramater weibull
    distribution.
    TESTING REQUIRED
    :param params: paramaters required (scale and shape)
    :param x: data.
    """
    lam = params[0]
    k = params[1]
    eq = (1 - np.exp(-(x / lam)**k))
    return 1 - eq
