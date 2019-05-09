#!/usr/bin/env python3
"""Main MLE model tool for mletools"""
__appname__ = "mlemodel.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mletools_V1 import cdf
from mletools_V1 import loglike

class runmle():
    """
    Class to run MLE analysis.
    These functions are used with other modules in the package to return 
    analysis based on MLE through minimization of given log-likelihood 
    functions.
    """

    def __init__(self, data, startest, method, bounds = None):
        """
        data     : The data to fit the model to.
        startest : starting estimates for the minimization.
        method   : The distribution to fit as a string.
        bounds   : Parameter bounds for minimize, default is no bounds."""
        self.data = data
        self.method = method
        self.startest = startest
        self.bound = bounds

    def ModelMap(self):
        """ModelMap: Contains dictionary to link MLE and cdf functions
        based on input string."""
        modeldict = {"exponential" : [loglike.LLExponential,
                                      cdf.ExponentialDist],
                      "normal"     : [loglike.LLNormal,
                                      cdf.NormalDist],
                      "lognormal"  : [loglike.LLLognormal,
                                      cdf.LognormalDist],
                      "gamma"      : [loglike.LLGamma,
                                      cdf.GammaDist],
                      "sumexp2"    : [loglike.LLSumExp_2r,
                                      cdf.SumExp_2r],
                      "sumexp3"    : [loglike.LLSumExp_3r,
                                      cdf.SumExp_3r],
                      "sumexp"     : [loglike.LLSumExp,
                                      cdf.SumExp]}
        if self.method not in list(modeldict.keys()):
            msg = "'{}' Not a listed method for analysis.".format(self.method)
            raise ValueError(msg)
        return modeldict[self.method]

    def InverseCDF(self):
        """InverseCDF: Create the inverse CDF of given data.
        SortedData is the data sorted descending. Probability is calculated
        as the probability of a value being greater than or equal to x."""
        sorted_data = -np.sort(-self.data)
        prob = np.arange(0, len(self.data), 1) / len(self.data)
        return pd.DataFrame({"SortedData":sorted_data, "Probability":prob})

    def ModelDataSE(self):
        rates = self.startest[0]
        probs = self.startest[1]
        self.rval = len(rates)
        start = np.array([rates + probs])
        model = minimize(self.ModelMap()[0],
                         start,
                         args=(self.data, self.rval),
                         method = "l-bfgs-b")
        return model

    def ModelData(self):
        """ModelData: Minimize the likelihood functions and return the
        minimisation object"""
        if self.bound is None: 
            model = minimize(self.ModelMap()[0],
                             self.startest,
                             self.data,
                             method = "l-bfgs-b")
        else:
            model = minimize(self.ModelMap()[0],
                             self.startest,
                             self.data,
                             bounds = self.bound,
                             method = "l-bfgs-b")
        return(model)

    def MLEPredict(self, model):
        """MLEPredict: Produce model predicted data to compare to actual data.
        The dataframe returned contains the sorted data, its cdf probability,
        dummy data for the model and its predictions.
        :param model: The model ran from function ModelData.
        """
        ivdata = self.InverseCDF()
        lengths = np.linspace(max(self.data),
                              min(self.data),
                              num = len(self.data))
        if self.method == "sumexp":
            prediction = np.array(self.ModelMap()[1](model.x, lengths, self.rval))
        else:
            prediction = np.array(self.ModelMap()[1](model.x, lengths))
        df = pd.DataFrame({"SortedData"  : ivdata["SortedData"],
                           "Probability" : ivdata["Probability"],
                           "Lengths"     : lengths,
                           "Prediction"  : prediction})
        return df

    def MLEPredictCI(self, cidict, df):
        """MLEPredictCI - Produce model predicted data based on upper and
        lower confidence intervals of paramaters. This adds to the dataframe
        returned from MLEPredict using the same methods.

        :param cidict: Dictionary of CIs from Getci2p_2.
        :param df: Dataframe from MLEPredict.
        """
        cina = np.array(list(cidict.values()))
        df["UpperCI"] = np.array(self.ModelMap()[1](cina[:,1], df["Lengths"]))
        df["LowerCI"] = np.array(self.ModelMap()[1](cina[:,2], df["Lengths"]))
        return df

    def PredictFig(self, df, ci = True):
        """PredictFig - Produces a plot Using the dataframe from MLEPredictCI.

        :param df: The dataframe from MLEPredictCI.
        """
        plt.figure()
        l1 = plt.plot(df["SortedData"],
                      df["Probability"],
                      label = "Actual")
        l2 = plt.plot(df["Lengths"],
                      df["Prediction"],
                      label = self.method)
        if ci:
            lci = plt.fill_between(df["Lengths"], 
                                   df["UpperCI"],
                                   df["LowerCI"],
                                   color = "grey",
                                   alpha = 0.5,
                                   label = "95% CI")
            plt.legend(handles = [l1[0], l2[0], lci])
        else:
            plt.legend(handles = [l1[0], l2[0]])
        plt.xlabel("Foraging distance (Km)")
        plt.ylabel("Probability")
        return plt

    def GetLogLike(self, model):
        """GetLogLike - Returns the loglikelihood for a given pramater value
        for the model. Negative is required for inversion.

        :param model: The model object from ModelData.
        """
        if self.method == "sumexp":
            return (-1) * self.ModelMap()[0](model.x, self.data, self.rval)
        return (-1) * self.ModelMap()[0](model.x, self.data)

    def Getci1p(self, model):
        """Getci1p - Calculates 95% CI for a single parmater log-likelihood
        function. Returns a dataframe of the paramater value, loglikelihood
        and normalised loglikelihood.

        :param model: The model object from ModelData.
        """

        # get a range of paramater estimates around optimised value.
        target = model.x[0]
        n = 10 * target
        upper = np.arange(target, n, 0.01)
        lower = np.arange(-n, target, 0.01)
        comb = np.sort(np.concatenate([upper, lower]))

        # get the associated likelihood for these paramaters
        comb_ll = [-self.ModelMap()[0]([x], self.data) for x in comb]

        # srote in dataframe
        df = pd.DataFrame({"Param":comb, "LL":comb_ll})

        # make a column of loglikelihood where the minimum is 0 and other
        # scores relate to this
        df["NLL"] = 1 - (df["LL"] / -model.fun)

        # get the paramater value closest to estimate - 1.96
        ci = df.iloc[df["NLL"][df["NLL"] > -1.97].index[-1],0]
        upper = model.x[0] + ci
        lower = model.x[0] - ci

        # cant have estimate bellow 0 so correct to 0
        if lower < 0:
            lower = 0
        cidict = {"p0":[model.x[0],
                        upper,
                        lower]}

        return(cidict)


    def Getci2p(self, model):
        """Getci2p - Gets 95% confidence intervals of paramaters based on
        models hessian matrix converted to variance covariance matrix.
        Returns a dictionary of the paramater (pi) : [actual paramater, 
        upper CI, lower CI].

        :param model: The model object from ModelData.
        """

        # extract variance covariance matrix from 
        # inverse hessian matrix from model
        hess = model.hess_inv.todense()
        varcovar = hess

        # extract diagonal elements as standard errors
        se = np.diagonal(varcovar)

        # calulcate and store in dictionary
        ci = {}
        for i in range(0, len(se)):
            ci["p{}".format(i)] = [model.x[i],
                                   model.x[i] + (1.96 * np.sqrt(se[i])),
                                   model.x[i] - (1.96 * np.sqrt(se[i]))]
        # sanity check
        cina = np.array(list(ci.values()))
        if not (cina[:,0] < cina[:,1]).all() & (cina[:,0] > cina[:,2]).all():
            msg = "Confidence intervals do not surround estimate"
            raise RuntimeError(msg)

        return ci

    def AIC(self, model):
        """AIC - Caluclates standard AIC score from minimized model output.

        :param model: The model from ModelData.
        """
        k = len(model.x)
        ll = self.GetLogLike(model)
        return -2 * ll + 2 * k
