#!/usr/bin/env python3
"""Current running script for package mletools"""
__appname__ = "pipeline.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import sys
sys.path.insert(0, "/home/joe/Documents/CMEE/mletools")
import numpy as np
import pandas as pd
import mlemodel

# import data into pandas dataframe
path = "../Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

# run exponential model on the data to get base line
start = [1.1]
bounds = ((0, np.inf),)
basemod = mlemodel.runmle(data = rural_dist,
                          startest = start,
                          bounds = bounds,
                          method = "exponential")
model = basemod.ModelData()
basell = model.fun

# start paramater space exploration
bestll = {}
counter = 0
c = 0
while len(bestll.keys()) < 10:
    length = 3
    rates = [0.1] * length
    param = [i for i in np.random.uniform(0, 1, length - 1)]
    start = [rates, param] 
    bounds = (((None, None),) * length) + (((None, None),) * (length - 1))
    mod = mlemodel.runmle(data = rural_dist,
                          startest = start,
                          bounds = bounds,
                          method = "sumexp")
    model = mod.ModelDataSE()
    if model.fun < basell:
        counter += 1
        print(mod.GetLogLike(model))
        bestll[counter] = model

# check dictionary
bestmodel = bestll[[i for i in bestll.keys()][0]]
for key in bestll:
    print(bestll[key])
    print(bestll[key].x)
    print(sum(bestll[key].x[-2:]))
    pred = mod.MLEPredict(bestll[key])
    fig = mod.PredictFig(pred, ci = False)
    fig.show()
