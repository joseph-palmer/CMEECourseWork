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
#import mlemodel
import warnings
warnings.filterwarnings("error")

# import data into pandas dataframe
path = "../Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

rural_dist.to_csv(path = "../Data/test_distances.csv", index = False)

exit()

# run exponential model on the data to get base line
start = [1.1]
bounds = ((0, np.inf),)
basemod = mlemodel.runmle(data = rural_dist,
                          startest = start,
                          bounds = bounds,
                          method = "exponential")
model = basemod.ModelData()
basell = model.fun
pred = basemod.MLEPredict(model)
#fig = basemod.PredictFig(pred, ci = False)

# start paramater space exploration
bestll = {}
counter = 0
c = 0
while len(bestll.keys()) < 100:
    repeat = True
    while repeat:
        length = 3
        rates = [i for i in np.random.uniform(0.0, 10.0, length)] # [0.1] * length
        param = [i for i in np.random.uniform(0, 1, length - 1)]
        # catch to stop starting values violating main constraint
        # without this the code will fail with nan values
        while sum(param) > 1:
            param = [i / length for i in np.random.uniform(0, 1, length - 1)]
        start = [rates, param]
        # 0, 1 p value bounds stop function improving on exponential
        # and maintain function behaviour as a likelihood function
        bounds = (((None, None),) * length) + (((0, 1),) * (length - 1))
        mod = mlemodel.runmle(data = rural_dist,
                              startest = start,
                              bounds = bounds,
                              method = "sumexp")
        try:
            model = mod.ModelDataSE()
            repeat = False
        except RuntimeWarning:
            print("rates out of bounds")
    print(model)
    pred = mod.MLEPredict(model)
    pred["diff2"] = (pred["Probability"] - pred["Prediction"])**2
    r2 = pred["diff2"].sum()
    print(r2)
    fig = mod.PredictFig(pred, ci = False)
    fig.show()
    if model.fun < basell:
        counter += 1
        bestll[counter] = [model, rates + param]
        print("###############################")


# check dictionary
bestmodel = bestll[[i for i in bestll.keys()][0]][0]
write_str = "R2, LL, ORate_1, ORate_2, ORate_3, OP_1, OP_2, SRate_1, SRate_2, SRate_3, SP_1, SP_2\n"
for key in bestll:
    pred = mod.MLEPredict(bestll[key][0])
    fig = mod.PredictFig(pred, ci = False)
    pred["diff2"] = (pred["Probability"] - pred["Prediction"])**2
    r2 = pred["diff2"].sum()
    write_str = write_str + "{},{},{},{}\n".format(r2,
                               bestll[key][0].fun,
                               ",".join([str(i) for i in bestll[key][0].x]),
                               ",".join([str(i) for i in bestll[key][1]]))

exit()
savepath = "../Data/SSAnalysis.csv"
with open(savepath, "w") as writer:
    writer.write(write_str)

print("finished, output saved to {}".format(savepath))
