#!/usr/bin/env python3
"""Fitting distributions to honeybee foraging distance data using MLE"""
__appname__ = "analysis.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import pandas as pd
import numpy as np
from mletools import runmle
import matplotlib.pyplot as plt

# import data into pandas dataframe
path = "~/Documents/CMEE/CMEECourseWork/Miniproject/Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

# run models one by one
modellist = ["exponential", "normal", "lognormal", "gamma"]

# create initialised dataframe to store weighted AIC results in
aicdata = pd.DataFrame({"Model":modellist})
aicdata["LogLike"] = None
aicdata["ParamNumber"] = None
aicdata["AIC"] = None

# create some test data to work with
data = np.random.exponential(1 / 1.8, 10000)
#data = np.random.normal(4.8, 1.8, 1000)
#data = np.random.lognormal(4.8, 1 / 1.8, 1000)

# loop through models and minimize loglikelihood function
for i in range(0, len(modellist)):
    if modellist[i] == "exponential":
        start = [0.1]
    else:
        start = [0.1, 0.1]
    mod = runmle(data = data,
              startest = start, 
              method = modellist[i])
    model = mod.ModelData()

    # store results in dataframe
    ll = (-1) * mod.GetLogLike(model)
    aicdata.iloc[i, 1] = ll
    aicdata.iloc[i, 2] = len(model.x)
    aicdata.iloc[i, 3] = mod.AIC(model)
    print("{f1}\n{f2: ^50}\n{f1}".format(f1 = "#" * 50, f2 = modellist[i]))    
    print(model)

    # show figures

# calculate weighted AIC scores
aicdata.sort_values(by=["AIC"], inplace = True)
aicdata.reset_index(inplace = True)
aicdata["wAIC"] = np.exp(-0.5 * (aicdata["AIC"].astype(float) - 
                  aicdata["AIC"].min()))
print("{f1}\n{f2:^50s}\n{f1}".format(f1 = "#" * 50, f2 = "Weighted AIC Table"))
print(aicdata)
