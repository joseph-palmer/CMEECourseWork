#!/usr/bin/env python3
"""Testing script for the mle module"""
__appname__ = "mletester.py"
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

"""
def LLSumExp(params, x, rval):
    rates = params[:rval]
    probs = params[rval:]
    df = np.column_stack((rates[:-1], probs))
    if np.sum(probs) > 1:
        return 1000000
    e1 = "*".join(["({}*{})".format(i[0], i[1]) for i in df])
    e2 = "1-{}".format("-".join([str(i) for i in probs]))
    e3 = "({})*{}".format(e2, rates[-1])
    e4 = "{}*({})".format(e1, e3)
    e5 = "len(x)*np.log({})".format(e4)
    e6 = "{}-{}".format(e5, "-".join(["{}**len(x)*np.sum(x)".format(i) for i in rates]))
    #print(e6)
    #eq = eval(e6)
    return e6


params = [1, 2, 3, 4, 0, 0, 0]
rval = 4
x = [1, 2, 3, 4]

ans = LLSumExp(params, x, rval)
print(ans)

exit()
"""

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
modellist = ["exponential", "sumexp2", "sumexp"]#, "normal", "lognormal", "gamma"]

# create initialised dataframe to store weighted AIC results in
aicdata = pd.DataFrame({"Model":modellist})
aicdata["LogLike"] = None
aicdata["ParamNumber"] = None
aicdata["AIC"] = None

# create some test data for tests
n = 1000
testdata = {"exponential" : np.random.exponential(1 / params[1], n),
            "normal"      : np.random.normal(params[0], params[1], n),
            "lognormal"   : np.random.lognormal(params[0], params[1], n),
            "gamma"       : np.random.gamma(params[0], params[1], n),
            "rural"       : rural_dist,
            "urban"       : urban_dist}

data = testdata[name]

# loop through models and minimize loglikelihood function
for i in range(0, len(modellist)):
    if modellist[i] == "exponential":
        start = [1.1]
        bounds = ((0, None),)
    elif modellist[i] == "sumexp3":
        start = [0.1, 0.1, 0.1, 0.1, 0.1]
        bounds = ((0, None),
                  (0, None),
                  (0, None),
                  (0, 1.0),
                  (0, 1.0))
    elif modellist[i] == "sumexp2":
        start = [0.1, 0.1, 0.1]
        bounds = ((0, None),
                  (0, None),
                  (0, None))
    elif modellist[i] == "sumexp":
        l = 3
        rates = [0.1] * l
        param = [0.0001] * (l -1)
        start = [rates, param]
        bounds = (((None, None),) * l) + (((None, None),) * (l - 1))
    else:
        start = [1.1, 1.1]
    mod = runmle(data = data,
              startest = start,
              bounds = bounds,
              method = modellist[i])
    if modellist[i] == "sumexp":
        model = mod.ModelDataSE()
    else:
        model = mod.ModelData()

    print("{f1}\n{f2: ^50}\n{f1}".format(f1 = "#" * 50, f2 = modellist[i]))    
    print(model)
    print(", ".join([str(i) for i in model.x]))

    # store results in dataframe
    ll = mod.GetLogLike(model)
    aicdata.iloc[i, 1] = ll
    aicdata.iloc[i, 2] = len(model.x)
    aicdata.iloc[i, 3] = mod.AIC(model)
    # show figures
    pred = mod.MLEPredict(model)
    #ci = mod.Getci2p(model)
    fig = mod.PredictFig(pred, ci = False)
    fig.show()

# calculate weighted AIC scores
aicdata.sort_values(by=["AIC"], inplace = True)
aicdata.reset_index(inplace = True)
aicdata["wAIC"] = np.exp(-0.5 * (aicdata["AIC"].astype(float) - 
                  aicdata["AIC"].min()))
print("{f1}\n{f2:^50s}\n{f1}".format(f1 = "#" * 50, f2 = "Weighted AIC Table"))
print(aicdata)
print("\n\nTested {} with actual parmaters of {}".format(name, params))
