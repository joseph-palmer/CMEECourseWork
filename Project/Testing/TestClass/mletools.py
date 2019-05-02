#!/usr/bin/env python3
"""Class of MLE distribution analysis"""
__appname__ = "mletools.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Apr-2019"

## imports ##
import pandas as pd
import numpy as np
import scipy as sp
from scipy.optimize import minimize
import matplotlib.pyplot as plt


class CDFFunctions(object):
    """
    Collection of cummulative density functions.
    These functions all return the cdf of the given data and parameters.
    """

    def __init__(self):
        """No arguments required."""

    def __ExponentialDist(self, params, x):
        """__ExponentialDist - CDF function for exponential distribution

        :param params: paramters required (rate).
        :param x: data.
        """
        rate = params[0]
        eq = 1 - np.exp(-rate * x)
        return 1 - eq

    def __NormalDist(self, params, x):
        """__NormalDis - CDF function for the normal distributiont.

        :param params: paramaters required (meam and standard deviation).
        :param x: data.
        """
        mu = params[0]
        sigma = params[1]
        eq = 1 / 2 * (1 + sp.special.erf((x - mu) / (sigma * np.sqrt(2))))
        return 1 - eq

    def __LognormalDist(self, params, x):
        """__LognormalDist - CDF function for the log-normal distribution.

        :param params: paramaters required (mean and standard deviation).
        :param x: data.
        """
        mu = params[0]
        sigma = params[1]
        eq = (1 / 2) + (1 / 2) * sp.special.erf((np.log(x) - mu) / np.sqrt(2 * sigma))
        return 1 - eq

    def __GammaDist(self, params, x):
        """__GammaDist - CDF function for the gamma distribution.

        :param params: paramaters required (alpha and beta).
        :param x: data.
        """
        alpha = params[0]
        beta = params[1]
        eq = 1 / (sp.special.gamma(alpha)) * sp.special.gammainc(alpha,
                                                                 beta * x)
        return 1 - eq

class LLFunctions(object):

    """
    Collection of Log-Likelihood functions.
    These functions are the loglikelihood of specified distributions
    to be used with scipy.optimize.minimize for MLE estimation.
    Vectorised. Each function returns the negative loglikelihood in order for
    minimise to work.
    """

    def __init__(self):
        """No arguments required"""

    def __LLExponential(self, rate, x):
        """__LLExponential - Loglikelihood function for exponential.

        :param rate: - the rate paramater of the model.
        :param x: data.
        """
        rate = rate[0]
        eq = (len(x) * np.log(rate) - rate * np.sum(x))
        return -eq

    def __LLLognormal(self, params, x):
        """__LLLognormal - Loglikelihood function for the lognormal.

        :param params: Paramaters of the model (mean and standard deviation).
        :param x: data.
        """
        mu = params[0]
        sigma = params[1]**2
        eq = (len(x) / 2 * np.log(2 * np.pi * sigma) -
            (np.sum([(np.log(x_) - mu)**2 for x_ in x]) / 2 * sigma) -
            np.sum(np.log(x)))
        return -eq

    def __LLNormal(self, params, x):
        """__LLNormal - Loglikelihood function for the normal distribution.

        :param params: paramaters of the model (mean standard deviation)..
        :param x: data.
        """
        mu = params[0]
        sigma = params[1]**2
        eq = (-len(x) / 2.0 * np.log(2 * np.pi) - 
               len(x) / 2.0 * np.log(sigma) - 
               1 / (2 * sigma) * np.sum([(x_ - mu)**2 for x_ in x]))
        return -eq

    def __LLGamma(self, params, x):
        """__LLGamma - Loglikelihood function of the gamma distribution.

        :param params: paramaters required.
        :param x: data.
        """
        alpha = params[0]
        beta = params[1]
        eq = (len(x) * alpha * np.log(beta) - 
                len(x) * np.log(sp.special.gamma(alpha)) +
                (alpha - 1) * np.sum(np.log(x)) - 
                beta * np.sum(x))
        return -eq

class runmle(CDFFunctions, LLFunctions):

    """
    Class to run MLE analysis through.
    These functions are used with the inherited classes to return analysis
    based on MLE through minimization of given log-likelihood functions.
    """

    def __init__(self, data, startest, method):
        """Inheritance of CDF and log-likelihood functions.
        data     : The data to fit the model to.
        startest : starting estimates for the minimization.
        method   : The distribution to fit as a string."""
        self.data = data
        self.method = method
        self.startest = startest

    def __ModelMap(self):
        """__ModelMap: Contains dictionary to link MLE and cdf functions
        based on input string."""
        modeldict = {"exponential" : [self._LLFunctions__LLExponential,
                                      self._CDFFunctions__ExponentialDist],
                      "normal"     : [self._LLFunctions__LLNormal,
                                      self._CDFFunctions__NormalDist],
                      "lognormal"  : [self._LLFunctions__LLLognormal,
                                      self._CDFFunctions__LognormalDist],
                      "gamma"      : [self._LLFunctions__LLGamma,
                                      self._CDFFunctions__GammaDist]}
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

    def ModelData(self):
        """ModelData: Minimize the likelihood functions and return the
        minimisation object"""
        model = minimize(self.__ModelMap()[0],
                         self.startest,
                         self.data,
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
        prediction = np.array(self.__ModelMap()[1](model.x, lengths))
        df = pd.DataFrame({"SortedData" : ivdata["SortedData"],
                       "Probability" : ivdata["Probability"],
                       "Lengths" : lengths,
                       "Prediction" : prediction})
        return df

    def MLEPredictCI(self, cidict, df):
        """MLEPredictCI - Produce model predicted data based on upper and
        lower confidence intervals of paramaters. This adds to the dataframe
        returned from MLEPredict using the same methods.

        :param cidict: Dictionary of CIs from Getci2p_2.
        :param df: Dataframe from MLEPredict.
        """
        cina = np.array(list(cidict.values()))
        df["UpperCI"] = np.array(self.__ModelMap()[1](cina[:,1], df["Lengths"]))
        df["LowerCI"] = np.array(self.__ModelMap()[1](cina[:,2], df["Lengths"]))
        return df

    def PredictFig(self, df):
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
        lci = plt.fill_between(df["Lengths"], 
                               df["UpperCI"],
                               df["LowerCI"],
                               color = "grey",
                               alpha = 0.5,
                               label = "95% CI")
        plt.xlabel("Foraging distance (Km)")
        plt.ylabel("Probability")
        plt.legend(handles = [l1[0], l2[0], lci])
        return plt

    def GetLogLike(self, model):
        """GetLogLike - Returns the loglikelihood for a given pramater value
        for the model.

        :param model: The model object from ModelData.
        """
        return self.__ModelMap()[0](model.x, self.data)

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
        comb_ll = [-self.__ModelMap()[0]([x], self.data) for x in comb]

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
        loglike = (-1) * self.GetLogLike(model)
        return -2 * loglike + 2 * k

def main():
    """main - main function ran when code executed as a script."""
    print("Execution at runtime")


if __name__ == "__main__":
    main()
