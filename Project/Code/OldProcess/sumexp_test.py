#!/usr/bin/env python3
"""Testing function for sum of exponentials"""
__appname__ = "sumexp_test.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import sys
import pandas as pd
import numpy as np
from mletools_V1 import cdf
from mletools_V1.mlemodel import runmle


# get command line options
if len(sys.argv) < 2:
    print("you can add arguments in you know!")
    name = "exponential"
else:
    name = sys.argv[1]

params = [4.8, 1.8]

print("Testing {} with actual parmaters of {}".format(name, params))
# import data into pandas dataframe
path = "../Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

# run models one by one
modellist = ["sumexp"]

# create some test data for tests
n = 1000
testdata = {"exponential" : np.random.exponential(1 / params[1], n),
            "normal"      : np.random.normal(params[0], params[1], n),
            "lognormal"   : np.random.lognormal(params[0], params[1], n),
            "gamma"       : np.random.gamma(params[0], params[1], n),
            "rural"       : rural_dist,
            "urban"       : urban_dist}

data = testdata[name]

for i in range(0, len(modellist)):
    l = 10
    rates = [0.1] * l
    param = [0.1] * (l -1)
    start = [rates, param]
    bounds = (((None, None),) * l) + (((0, 1),) * (l - 1))

    mod = runmle(data = data,
                 startest = start,
                 bounds = bounds,
                 method = modellist[i])

    model = mod.ModelDataSE()

    print("{f1}\n{f2: ^50}\n{f1}".format(f1 = "#" * 50, f2 = modellist[i]))    
    print(model)
    print(", ".join([str(i) for i in model.x]))
