#!/usr/bin/env python3
"""A test script for finding MLE of lognormal"""
__appname__ = "lognormal.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.optimize as spo
import pandas as pd

# draw from lognormal distribution
n = 100
m = 12
sigma = 1/4.8 # IS THAT IT???? HAVE TO DIVIDE BY 1!!!!!
lndata = np.random.lognormal(m, sigma, n)
#print(lndata)

plt.hist(np.log(lndata))
#plt.show()

# sort values largest to smallest to create sequence rank
lndata = np.flip(np.sort(lndata))
rank = np.arange(1, len(lndata) + 1, 1) / len(lndata)

# plot the data
plt.plot(lndata, np.log(rank))
#plt.show()

# functions for likelihood estimation
def ln_loglike(params, x):
    """ln_loglike - Calculaties the log-likelihood estimate for a lognormal
    distribution.

    :param x: data.
    :param mu: mu paramater
    :param sigma: sigma paramater
    """
    mu = abs(params[0])
    sigma = abs(params[1])
    print("mu = {}, sigma = {}".format(mu, sigma))
    
    return( (-(len(x)/2) * np.log(2 * np.pi * sigma**2)) - sum(np.log(x) - ( (sum(np.log(x)**2)/(2 * sigma**2)) + (sum(np.log(x)*mu)/sigma**2) - ((len(x) * mu**2)/(2*sigma**2)) )) )


def LLLognorm(params, x):
    """ll_lognorm - Log-Likelihood function for lognormal distribution

    :param params: list or set of paramater values
    :param x: data to be evaluated
    """ 
    # extract mu and sigma from params
    mu = params[0]
    sigma = params[1]**2

    print("mu = {}, sigma = {}, x = {}".format(mu, sigma, x[0]))

    # return loglikelihood
    eq1 = - (len(x) / 2 * np.log(2 * np.pi * sigma) - (np.sum([(np.log(x_) - mu)**2 for x_ in x]) / 2 * sigma) - np.sum(np.log(x)))

    eq2 = -(len(x) / 2 * np.log(2 * np.pi * sigma) - np.sum([(np.log(x_) - mu)**2 for x_ in x]) / 2 * sigma - np.sum([np.log(x_) for x_ in x]))

    print("eq1 = {}, eq2 = {}".format(eq1, eq2))
    return eq1


# Optimise the function
pe = np.arange(1, len(lndata) + 1, 1)
pe2 = pe

params = [1.1, 1.1]
a = spo.minimize(LLLognorm, params, lndata, method = 'l-bfgs-b')
print(a)

exit()
# grid search optimization
param1 = np.arange(0.1, 10, 0.1)
param2 = param1
plens = len(param1) * len(param2)

res = pd.DataFrame(np.nan, index=[i for i in range(0, plens)], columns=['p1', "p2", "le"])

c = 0
for i in range(0, len(param1)):
    for j in range(0, len(param2)):
        res["p1"].iloc[c] = param1[i]
        res["p2"].iloc[c] = param2[j]
        res["le"].iloc[c] = LLLognorm([param1[i], param2[j]], lndata)
        c += 1

a = res[res["le"] == min(res["le"])]
b = res[(res["p1"] < 2) & (res["p1"] > 1)]
#print(b)
print(a)


from mpl_toolkits.mplot3d import Axes3D
ax = plt.axes(projection='3d')
ax.plot(res["p1"], res["p2"], res["le"])
plt.show()






