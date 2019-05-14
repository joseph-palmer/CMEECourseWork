#!/usr/bin/env python3
"""Tester for new way of fitting model"""
__appname__ = "pipeline.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import sys
#sys.path.insert(0, "/home/joe/Documents/CMEE/mletools")
import numpy as np
from scipy.optimize import minimize
import pandas as pd


def InverseCDF(data):
    """InverseCDF: Create the inverse CDF of given data.
    SortedData is the data sorted descending. Probability is calculated
    as the probability of a value being greater than or equal to x."""
    sorted_data = -np.sort(-data)
    prob = np.arange(0, len(data), 1) / len(data)
    return pd.DataFrame({"SortedData":sorted_data, "Probability":prob})

# function to minimize
def sumexp(params, x, rval): 
    # extract rates and probabilieties from paramaters and align.
    rates = params[:rval]
    probs = params[rval:]
    df = np.column_stack((rates[:-1], probs))

    # format and evaluate equation.
    e1 = ["{p}*{r}*np.exp(-{r}*x)".format(p = i[1], r = i[0]) for i in df]
    e2 = "(1-{})".format("-".join([str(i) for i in probs]))
    e3 = "{e}*{r}*np.exp(-{r}*x)".format(e = e2, r = rates[-1])
    e4 = "np.log(np.prod({e1}+{e3}))".format(e1 = "+".join(e1), e3 = e3)
    print(params)
    print(-eval(e4))
    return -eval(e4)

# constraints function
def con(params, rval):
    probs = params[rval:]
    return sum(probs) - 1

####### testing area #######
# get some data
path = "../../Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]


data = InverseCDF(rural_dist)
data = data["SortedData"]

l = 3
rates = [0.1] * l
param = [0.1] * (l -1)
startest = [rates, param]

rates = startest[0]
probs = startest[1]
rval = len(rates)
start = np.array([rates + probs])

cons = ({"type":"eq", "fun": con, "args":[rval]})

# minimize
model = minimize(sumexp, start, args=(data, rval), constraints = cons)
print(model)













