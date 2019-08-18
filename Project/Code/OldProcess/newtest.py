#!/usr/bin/env python3
"""Latest test with new exponential equation."""
__appname__ = "newtest.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import sys
sys.path.insert(0, "/home/joe/Documents/CMEE/mletools")
import numpy as np
import pandas as pd
import modelmle

"""
The function is still returning high log-likelihoods with bad fits, but for 
the most part the fits are good. This means there must be something off with
the values being outside the bounds of the domain. Check with vincent, but
carry on for most part because worst comes to the wost we set bounds between
0 and 1 and its just an exponential.
"""

# import data into pandas dataframe
path = "../Data/Distances.csv"
data = pd.read_csv(path)

# subset the data by locations
rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

# run multiple models
model_dict = {"exponential" : [[1.1], ((None,None),)],
              "normal" : [[1, 1], ((None,None), (None, None))]}

models = modelmle.ClusterRun(rural_dist, model_dict)
print(models.go())



exit()
mod = modelmle.Runmle(rural_dist, [0.1], "exponential")
model = mod.minimize_model()
fig = mod.predict_fig(model)
fig.show()
print("## Simple exponential ##")
print(model)

sn = 100
size = 3

simdata = np.random.exponential(1.8, 1000)

sim = modelmle.SimulateSumExp(data = rural_dist, sim_number = sn, size = size)
result = sim.run()
aictable = sim.waic(result)
aictable = aictable.sort_values(["LogLikelihood"])
indexs = list(aictable.index.values)[-10:]
max_index = aictable["LogLikelihood"].idxmax()
for i in indexs:
    best_model = result[i][0]
    print(best_model.fun)
    print(best_model.x)
    print(sum(best_model.x[:2]))
    print(result[i][-1])
    fig = sim.predict_fig(best_model)
    fig.show()

best_model = result[max_index][0]
fig = sim.predict_fig(best_model)
