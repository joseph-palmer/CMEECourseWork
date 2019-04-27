#!/usr/bin/env pyth on3
"""Fit MLE estimate to foraging distance data"""
__appname__ = "MLEFit.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PdfFunctions as Func
from scipy.stats import linregress


def main():
    # load the distance data into a pandas dataframe
    path = "~/Documents/CMEE/CMEECourseWork/Miniproject/Data/Distances.csv"
    data = pd.read_csv(path)

    # subset the data by locations
    rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
    urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

    # run exponential model and show loglikelihood score
    ex_rural_model = Func.MLEPredictor(rural_dist, Func.LLExponential, [0.1])
    ex_rural = ex_rural_model[1]
    print("Log likelihood for Exponential = {}".format(ex_rural_model[0].fun))

    # create plot with predicted model line
    plt.plot(ex_rural["SortedData"], ex_rural["Probability"])
    plt.plot(ex_rural["Lengths"], ex_rural["Prediction"])

    # run normal model and have a look
    nm_rural_model = Func.MLEPredictor(rural_dist, Func.LLNormal, [0.1, 0.1])
    nm_rural = nm_rural_model[1]

    print("Log likelihood for Normal = {}".format(nm_rural_model[0].fun))

    # create plot with predicted model line
    plt.plot(nm_rural["Lengths"], nm_rural["Prediction"])

    # run lognormal model
    ln_rural_model = Func.MLEPredictor(rural_dist, Func.LLLognormal, [0.1, 0.1])
    ln_rural = ln_rural_model[1]

    print("Log likelihood for LogNormal = {}".format(ln_rural_model[0].fun))

    # create plot with predicted model line
    plt.plot(ln_rural["Lengths"], ln_rural["Prediction"])

    # run gamma model
    gam_rural_model = Func.MLEPredictor(rural_dist, Func.LLGamma, [0.1, 0.1])
    gam_rural = gam_rural_model[1]

    print("Log likelihood for Gamma = {}".format(gam_rural_model[0].fun))

    # create plot with predicted model line
    plt.plot(gam_rural["Lengths"], gam_rural["Prediction"])

    # print all model summaries in full
    print(ex_rural_model[0])
    print(nm_rural_model[0])
    print(ln_rural_model[0])
    print(gam_rural_model[0])

    plt.show()

    # check the exponential in a log format as a straight line
    plt.plot(ex_rural["SortedData"], np.log(ex_rural["Probability"]))
    plt.plot(ex_rural["Lengths"], np.log(ex_rural["Prediction"]))

    # looks like the line isnt a good fit, try a linear regression on it.
    ex_rural.iloc[0, 1] = 0.00001
    lr = linregress(ex_rural["SortedData"].values, np.log(ex_rural["Probability"].values))
    # the linear regression here gives -1.6 ish, when used in the model as the
    # paramater estimate for exponential it is a worse fit. Check all this
    # with Vincent along with the full process

    plt.show()



if __name__ == "__main__":
    main()
