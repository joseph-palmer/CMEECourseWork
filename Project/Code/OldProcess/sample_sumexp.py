#!/usr/bin/env python3
"""Samples from sum of exponential distribution"""
__appname__ = "sample_sumexp.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import sys
sys.path.insert(0, "/home/joe/Documents/CMEE/mletools") 
import mlemodel
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("error")

# inverse cdf of exponential
def InvExpCDF(params, x):
    rate = 1 / params[0]
    return (-1/rate) * np.log(x)

# testing function - inverse cdf of sumexp
def InvSumExpCDF(params, x):
    r1 = params[0]
    r2 = params[1]
    r3 = params[2]
    p1 = params[3]
    p2 = params[4]
    e1 = (p1 + np.exp(p2)) / (np.exp(r3) + r2 * p2 - np.exp(r3) * p2 + np.exp(r1) * x - np.exp(r3) * x)
    e2 = (p1 + np.exp(p2)) / (np.exp(r3) + r2 * p2 - np.exp(r3*p2) + np.exp(r1*x) - np.exp(r3*x))
    return e2

path = "../Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

# sample from uniform distribution to input into function
n = 1000
sample = np.random.uniform(0, 1, n)

r1 = 1
r2 = 2
r3 = 3
p1 = 0.2
p2 = 0.3
params = [r1, r2, r3, p1, p2]

newdata = InvSumExpCDF(params, sample)
#newdata = InvExpCDF([1/1.8], sample)
#newdata = rural_dist
#newdata = np.random.gamma(1.8, 4.8, 100)
#newdata = urban_dist

# run the model and generate plots

l = 10
repeat = True
while repeat:
    rates = [i for i in np.random.uniform(0.0, 10.0, l)] #[0.1] * l
    param = [i for i in np.random.uniform(0.0, 10.0, l - 1)]
    while sum(param) > 1:
        param = [i/l for i in np.random.uniform(0, 1, l - 1)]
    start = [rates, param]
    bounds = (((None, None),) * l) + (((0, 1),) * (l - 1))
    mod = mlemodel.runmle(data = newdata,
                          startest = start,
                          bounds = bounds,
                          method = "sumexp")
    try:
        model = mod.ModelDataSE()
        repeat = False
    except RuntimeWarning:
        print("Out of bound rates")
        repeat = True
pred = mod.MLEPredict(model)
#cis = mod.Getci2p(model)
#pred2 = mod.MLEPredictCI(cis, pred)
fig = mod.PredictFig(pred, ci = False)
print(model)
print(start)
fig.show()

