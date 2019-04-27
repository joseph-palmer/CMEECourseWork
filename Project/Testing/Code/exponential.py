#!/usr/bin/env python3
"""A test script for finding MLE of exponential"""
__appname__ = "example.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import minimize

# draw from exponential distribution
n = 10000
rate = 1.8
exdata = np.random.exponential(1/rate, n)

# sort the values by size largest to smallest and create a sequence rank
exdata = np.sort(exdata)
exdata = np.flip(exdata)
rank = np.arange(1, len(exdata) + 1, 1) / len(exdata)

# plot the data to have a look
# an exponential will show a straght line (roughly)
plt.plot(exdata, np.log(rank))
plt.show()

# Function for likelihood estimation
def exp_loglike(a, x):
    """exp_loglike - Calculates the log-likelihood estimate for an
    exponential distribution. 

    :param x: data.
    :param a: Rate.
    """
    #print("value = {}".format(a[0]))
    a = abs(a)
    #print("length is {}".format(len(x)))

    return(-(len(x) * np.log(a) - a * np.sum(x)))


# set the parameter estimates
pe = np.arange(0.1, 10, 0.1)

# get MLE estimate
mle = exp_loglike(pe, exdata)

# analytical solve
print("ANALYTICAL SOLVE")
max_mle = 1/(np.sum(exdata) / len(exdata))

# log the mle to get the actual mle for the rate parameter
print("Max mle = {}".format(max_mle))

# use estimate to fit a model line
pred = np.random.exponential(abs(np.log(max_mle)), len(exdata))
pred = np.flip(np.sort(pred))

# get min value from plot
df = pd.DataFrame({"Param":pe, "MLE":mle})

# use optimizer
a = minimize(exp_loglike, 0.1, exdata, method = "l-bfgs-b")

print("NUMERICAL MLE")
mle_numeric = df["Param"][df["MLE"] == min(df["MLE"])].values
print(mle_numeric)

print(np.sum(exdata) / len(exdata))

print("MINIMIZE")
print(a)

# plot the mle curve
plt.plot(pe, mle)
plt.axvline(x = max_mle, color = "r")
plt.axvline(x = mle_numeric, color = "b")
plt.show()


