#!/usr/bin/env python3
"""Data exploration using mle fitting of sum of exponentials."""
__appname__  = "sumexp.py"
__author__   = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__  = "0.0.2"
__date__     = "07-2019"

import numpy as np
from scipy.optimize import minimize
import pandas as pd
import matplotlib.pyplot as plt
import config

def inverse_cdf(data):
    # create CCDF of given data for plotting
    sorted_data = -np.sort(-data)
    prob = np.arange(0, len(data), 1) / len(data)
    return pd.DataFrame({"SortedData":sorted_data, "Probability":prob})

def sample_sumexp(*args):
    # sample from a sum of exponentials with given rates and pweights
    rts, pwts, n = args
    rts = np.array([1/i for i in np.sort(rts)])
    pwts = np.array(np.sort(pwts))
    selection = np.random.choice(a = rts,
                                 p = pwts,
                                 size = n)
    sse = np.zeros(shape=(n, 1))
    for i in range(len(selection)):
        sse[i] = np.random.exponential(selection[i], 1)
    return sse

def sumexp_single(psi, _lambda, x):
    # single exponential function
    # alternative psi * _lambda * np.exp(-_lambda * (x - min(x)))
    return psi * _lambda * np.exp(-_lambda * x)

def sumexp_eq(psi, x):
    # combined sumexp - rates fixed in global variable
    eq_vector = np.zeros((len(config.FIXED_RATES), len(x)))
    for i in range(len(psi)):
        eq_vector[i] = sumexp_single(psi[i], config.FIXED_RATES[i], x)
    eq_vector[-1] = sumexp_single(1-sum(psi), config.FIXED_RATES[-1], x)
    return sum(eq_vector)

def sumexp_ll(psi, x):
    # return negative loglikelihood value
    return (-1)* sum(np.log(sumexp_eq(psi, x)))

def sumexp_jac(psi, x):
    # jacobian function (for the gradiant)
    fun = sumexp_eq(psi, x)
    jac_eq = np.zeros((len(psi), 1))
    numerator_2 = config.FIXED_RATES[-1] * np.exp(-config.FIXED_RATES[-1] * x)
    denominator = sumexp_eq(psi, x)
    for i in range(len(jac_eq)):
        numerator_1 = config.FIXED_RATES[i] * np.exp(-config.FIXED_RATES[i] * x)
        jac_eq[i] = -sum((numerator_1 - numerator_2) / denominator)
    return jac_eq

def minimize_model(startest, data):
    data = np.reshape(data, len(data))
    # run model through scipy.optimize.minimize   
    # define bounds so that 0<=pi<=1
    bounds = (((0., 1.),) * (len(startest)))
    # define constraints so that 0 <= sum(psi) <= 1
    const = ({"type" : "ineq",
              "fun"  : lambda psi: 1.0-sum(psi)})
    # load in args and kwargs
    m_args = (sumexp_ll, startest, data)
    m_kwargs = {"method" : "SLSQP",
                "jac"    : sumexp_jac,
                "bounds" : bounds,
                "constraints" : const,
                "options" : {}}
    # minimize model
    model = minimize(*m_args, **m_kwargs)
    return model

def spec_fig(x, y):
    plt.bar(x, y, 0.1)
    plt.xlabel("Rate")
    plt.ylabel("P weight")
    plt.show()
    return 0