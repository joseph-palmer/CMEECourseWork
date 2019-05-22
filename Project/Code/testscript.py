#!/usr/bin/env python3
"""testing script for mletools"""
__appname__ = "testscript.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import sys
sys.path.insert(0, "/home/joe/Documents/CMEE/mletools")
import modules
import numpy as np
import pandas as pd

# import data into pandas dataframe
path = "../Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]


# test sumexp
nsim = 10000
n_p = 3
storage = {}
for i in range(nsim):
    while True:
        rates = [i for i in np.random.exponential(1.28, n_p)]
        probs = [2]
        while sum(probs) > 1:
            probs = [i / n_p for i in np.random.uniform(0, 1, n_p - 1)]
        params = [*rates, *probs]
        try:
            mod = modules.RunSumexp(rural_dist, n_p, params)
            model = mod.model
            if model.success:
                if model.fun > 0:
                    break
        except RuntimeWarning:
            pass
    storage[i] = mod

vals = np.array([i.model.fun for i in tuple(storage.values())])
best_model = storage[np.argmin(vals)]
print(best_model.model)
fig = best_model.figure()
fig.show()


# test regular functions
exit()
nsim = 10
simdict = {}
storage = {}
for i in range(nsim):
    while True:
        startest = [np.random.uniform(0.1, 10, 1)]
        mod = modules.Runmle(rural_dist, "exponential", startest)
        print(len(mod.modelmap[mod.method][1]))
        try:
            storage[i] = mod.go()
            break
        except RuntimeWarning:
            pass

vals = np.array([i.fun for i in tuple(storage.values())])
best_model = storage[np.argmin(vals)]
simdict["exponential"] = best_model

storage = {}
for i in range(nsim):
    while True:
        startest = np.random.uniform(0.1, 10, 2)
        mod = modules.Runmle(rural_dist, "lognormal", startest)
        try:
            storage[i] = mod.go()
            break
        except RuntimeWarning:
            pass
vals = np.array([i.fun for i in tuple(storage.values())])
best_model = storage[np.argmin(vals)]
simdict["lognormal"] = best_model

waic = modules.waic_table(simdict)
print(waic)
