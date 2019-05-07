#!/usr/bin/env python3
"""Container for MLE functions of common  distributions pdf"""
__appname__ = "PdfFunctions.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import sys
import pandas as pd
import numpy as np
import scipy as sp
from scipy.optimize import minimize

### Distribution CDFs ###
def ExponentialDist(params, x):
    rate = params[0]
    eq = 1 - np.exp(-rate * x)
    return 1 - eq

def NormalDist(params, x):
    mu = params[0]
    sigma = params[1]
    eq = 1 / 2 * (1 + sp.special.erf(x - mu / sigma * np.sqrt(2)))
    return 1 - eq

def LognormalDist(params, x):
    mu = params[0]
    sigma = params[1]
    eq = 1 / 2 + 1 / 2 * sp.special.erf(np.log(x) - mu / np.sqrt(2 * sigma))
    return 1 - eq

def GammaDist(params, x):
    alpha = params[0]
    beta = params[1]
    eq = 1 / sp.special.gamma(alpha) * sp.special.gammainc(alpha, beta * x)
    return 1 - eq

### Log-likelihood functions for distributions ###
def LLExponential(rate, x):
    eq = -(len(x) * np.log(rate) - rate * np.sum(x))
    return eq

def LLLognormal(params, x):
    mu = params[0]
    sigma = params[1]**2
    eq = - (len(x) / 2 * np.log(2 * np.pi * sigma) - 
            (np.sum([(np.log(x_) - mu)**2 for x_ in x]) / 2 * sigma) - 
            np.sum(np.log(x)))
    return eq

def LLNormal(params, x):
    mu = params[0]
    sigma = params[1]**2
    eq = -(len(x) / 2.0 * np.log(2 * np.pi) - len(x) / 2.0 * np.log(sigma) - 
            1 / (2 * sigma) * sum([(x_ - mu)**2 for x_ in x]))
    return eq

def LLGamma(params, x):
    alpha = params[0]
    beta = params[1]
    ex = -(len(x) * alpha * np.log(beta) - 
            len(x) * np.log(sp.special.gamma(alpha)) + 
            (alpha - 1) * np.sum(np.log(x)) - 
            beta * np.sum(x))
    return ex

def ModelData(f, init_est, data):
    model = minimize(f, init_est, data, method = "l-bfgs-b")
    return(model)

### Testing functions ###
def TestFunction(f):
    # get data size
    n = 10000
    # starting paramater estimates
    params = [1.1, 1.1]
    # Actual paramater values into distribution sampling
    input_params = [4.8, 1.8]

    # Sample data from each distribution
    if f.__name__ == "LLExponential":
        data = np.random.exponential(1 / input_params[0],
                                     n)
        params = [0.1]

    elif f.__name__ == "LLLognormal":
        data = np.random.lognormal(input_params[0],
                                   1 / input_params[1],
                                   n)
    elif f.__name__ == "LLNormal":
        data = np.random.normal(input_params[0],
                                input_params[1],
                                n)
    elif f.__name__ == "LLGamma":
        data = np.random.gamma(input_params[0],
                                1 / input_params[1],
                                n)
    else:
        return 1

    # optimize the model
    model = minimize(f, params, data, method = "l-bfgs-b")
    print(1/np.mean(data))
    if model.success is True:
        print("Model '{}' had no erors: Actual params = {},"
              " simulated params = {}".format(f.__name__,
                                              input_params,
                                              model.x))
    else:
        print("Model {} terminated with error:\n{}".format(model))
    return 0

def TestEachFunction():
    modellist = [LLLognormal,
                 LLExponential,
                 LLNormal,
                 LLGamma]
    success = 0
    for i in modellist:
        success = TestFunction(i)
        print(success)
    if success == 0:
        print("ALL MODELS RAN SUCCESSFULLY")
    else:
        print("ONE OR MORE MODELS FAILED!")
    return 0

### Data wrangling functions ###
def InverseCDF(data):
    sorted_data = -np.sort(-data)
    prob = np.arange(0, len(data), 1) / len(data)
    return pd.DataFrame({"SortedData":sorted_data, "Probability":prob})

def ModelMap(f):
    modeldict = {LLExponential : ExponentialDist,
                 LLNormal      : NormalDist,
                 LLLognormal   : LognormalDist,
                 LLGamma       : GammaDist}
    return modeldict[f]

def MLEPredictor(data, f, starting_params): 
    # get inverse cdf of data
    ivdata = InverseCDF(data)

    # run the model
    model = ModelData(f,
                      starting_params,
                      data)

    # get predicted data 
    lengths = np.linspace(max(data),min(data), num=len(data))
    prediction = np.array(ModelMap(f)(model.x, lengths))

    # load into dataframe to return
    df = pd.DataFrame({"SortedData" : ivdata["SortedData"],
                       "Probability" : ivdata["Probability"],
                       "Lengths" : lengths,
                       "Prediction" : prediction})
    return (model, df)

def main():
    TestEachFunction()


if __name__ == "__main__":
    main()
