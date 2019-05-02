#!/usr/bin/env python3
"""Main execution script for honeybee foraging distance MLE analysis"""
__appname__ = "waicstats.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import pandas as pd
import numpy as np
from mletools import runmle
import matplotlib.pyplot as plt

path = "~/Documents/CMEE/CMEECourseWork/Miniproject/Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

### run the models ###
# create list of models to run
modellist = ["exponential", "normal", "lognormal", "gamma"]

# create initialised dataframe to store weighted AIC results in
aicdata = pd.DataFrame({"Model":modellist})
aicdata["LogLike"] = None
aicdata["ParamNumber"] = None
aicdata["AIC"] = None

# loop through models and minimize loglikelihood function
for i in range(0, len(modellist)):
    if modellist[i] == "exponential":
        start = [0.1]
    else:
        start = [0.1, 0.1]
    mod = runmle(data = rural_dist,
              startest = start, 
              method = modellist[i])
    model = mod.ModelData()

    # store results in dataframe
    ll = -mod.GetLogLike(model)
    aicdata.iloc[i, 1] = ll
    aicdata.iloc[i, 2] = len(model.x)
    aicdata.iloc[i, 3] = mod.AIC(model)
    print(modellist[i])
    print(model.x)

# calculate weighted AIC scores
aicdata.sort_values(by=["AIC"], inplace = True)
aicdata.reset_index(inplace = True)
aicdata["wAIC"] = np.exp(-0.5 * (aicdata["AIC"].astype(float) - aicdata["AIC"].min()))

# display
print(aicdata)

# get 95% CI
mod = runmle(data = rural_dist, startest = [0.1], method = "exponential")
model = mod.ModelData()
pred = mod.MLEPredict(model)

# single paramater 95% CI
if len(model.x) == 1:
    target = mod.Getci1p(model)
else:
    target = mod.Getci2p(model)
pred2 = mod.MLEPredictCI(target, pred)
pred2plot = mod.PredictFig(pred2)


pred2plot.show()

exit()
# stats = mod.Getci1p_2(target)

print(model)

# multiple parameter CI
# hess_inv is the inverse of the hessian matrix (I think!)
cis = mod.Getci2p(model)
print(mod.Getci2p_2(cis))

# plotting confidence interval shadded areas.
pred2 = mod.MLEPredictCI(cis, pred)
pred2plot = mod.PredictFig(pred2)
pred2plot.show()
