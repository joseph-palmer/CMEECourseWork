#!/usr/bin/env python3
"""Class of MLE distribution analysis"""
__appname__ = "PdfClass.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import sys
import pandas as pd
import numpy as np
import scipy as sp
from scipy.optimize import minimize


class CDFFunctions(object):

    """Docstring for CDFFunctions. """

    def __init__(self):
        """TODO: to be defined1. """


class LLFunctions(CDFFunctions):

    """Docstring for LLFunctions. """

    def __init__(self):
        """TODO: to be defined1. """
        .__init__(self)

        
class PdfMLE(object):

    """Docstring for PdfMLE. """

    def __init__(self, data, startest, method):
        """TODO: to be defined1. """
        self.data = data
        self.method = method
        self.startest = startest

    ### PRIVATE FUNCTIONS ###
    # Distribution CDFs
    def __ExponentialDist(self, params, x):
        rate = params[0]
        eq = 1 - np.exp(-rate * x)
        return 1 - eq

    def __NormalDist(self, params, x):
        mu = params[0]
        sigma = params[1]
        eq = 1 / 2 * (1 + sp.special.erf(x - mu / sigma * np.sqrt(2)))
        return 1 - eq

    def __LognormalDist(self, params, x):
        mu = params[0]
        sigma = params[1]
        eq = 1 / 2 + 1 / 2 * sp.special.erf(np.log(x) - 
                mu / np.sqrt(2 * sigma))
        return 1 - eq

    def __GammaDist(self, params, x):
        alpha = params[0]
        beta = params[1]
        eq = 1 / sp.special.gamma(alpha) * sp.special.gammainc(alpha, beta * x)
        return 1 - eq

    # Log-likelihood functions for distributions
    def __LLExponential(self, rate, x):
        eq = -(len(x) * np.log(rate) - rate * np.sum(x))
        return eq

    def __LLLognormal(self, params, x):
        mu = params[0]
        sigma = params[1]**2
        eq = - (len(x) / 2 * np.log(2 * np.pi * sigma) - 
                (np.sum([(np.log(x_) - mu)**2 for x_ in x]) / 2 * sigma) - 
                np.sum(np.log(x)))
        return eq

    def __LLNormal(self, params, x):
        mu = params[0]
        sigma = params[1]**2
        eq = -(len(x) / 2.0 * np.log(2 * np.pi) - 
                len(x) / 2.0 * np.log(sigma) - 
                1 / (2 * sigma) * sum([(x_ - mu)**2 for x_ in x]))
        return eq

    def __LLGamma(self, params, x):
        alpha = params[0]
        beta = params[1]
        ex = -(len(x) * alpha * np.log(beta) - 
                len(x) * np.log(sp.special.gamma(alpha)) + 
                (alpha - 1) * np.sum(np.log(x)) - 
                beta * np.sum(x))
        return ex

    # Data wrangling functions
    def __InverseCDF(self):
        sorted_data = -np.sort(-self.data)
        prob = np.arange(0, len(self.data), 1) / len(self.data)
        return pd.DataFrame({"SortedData":sorted_data, "Probability":prob})

    def __ModelMap(self):
        modeldict = {"exponential" : [self.__LLExponential,
                                      self.__ExponentialDist],
                      "normal"     : [self.__LLNormal,
                                      self.__NormalDist],
                      "lognormal"  : [self.__LLLognormal,
                                      self.__LognormalDist],
                      "gamma"      : [self.__LLGamma,
                                      self.__GammaDist]}
        if self.method not in list(modeldict.keys()):
            msg = "'{}' Not a listed method for analysis.".format(self.method)
            raise ValueError(msg)
        return modeldict[self.method]

    ### Public Functions ###
    def ModelData(self):
        model = minimize(self.__ModelMap()[0],
                         self.startest,
                         self.data,
                         method = "l-bfgs-b")
        return(model)

    def MLEPredict(self, model):
        ivdata = self.__InverseCDF()
        lengths = np.linspace(max(self.data),
                               min(self.data),
                               num = len(self.data))
        prediction = np.array(self.ModelMap()[1](model.x, lengths))
        df = pd.DataFrame({"SortedData" : ivdata["SortedData"],
                       "Probability" : ivdata["Probability"],
                       "Lengths" : lengths,
                       "Prediction" : prediction})
        return df



if __name__ == "__main__":

    path = "~/Documents/CMEE/CMEECourseWork/Miniproject/Data/Distances.csv"
    data = pd.read_csv(path)

    # subset the data by locations
    rural_dist = data["Distance_Km"][data["Location"] == "ROT"]
    urban_dist = data["Distance_Km"][data["Location"] == "ZSL"]

    test = PdfMLE(data = rural_dist,
                  startest = [0.1, 0.1], 
                  method = "normal")
    model = test.ModelData()
    print(model)
