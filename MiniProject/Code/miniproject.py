#!/usr/bin/env python3
"""use nnls to fit distributions to foraging data"""
__appname__ = "miniproject.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"


# To do list:
# 1. Make a nice table for all the stats from the model.
#    They are currently worked out in make_plots. This function is no longer
#    required due to ploting in R. Change the function so it simply calculates
#    the stats. It may even be worthwhile working on this in R. Try both,
#    see which one looks better.
# 2. Add doc strings to the data.

## imports ##
import warnings
import sys
import os
import re
import MiniprojectFunctions as mpf
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# set plot styles
plt.style.use("ggplot")

# Functions
def SampleData(inputdata, proportion):
    sp.random.seed(int(proportion * 100))
    portioned_dd = inputdata.sample(frac = proportion)
    portioned_dd.sort_index(inplace = True)
    return portioned_dd

def calculate_aic(paramaters, mle):
    return 2 * len(paramaters) - 2 * mle

def calculate_mle(func, x, p):
    if len(p) == 1:
        return sp.sum(sp.log(func(x, p[0]) + 1))
    elif len(p) == 2:
        return sp.sum(sp.log(func(x, p[0], p[1]) + 1))
    elif len(p) == 3:
        return sp.sum(sp.log(func(x, p[0], p[1], p[2]) + 1))
    else:
        sys.exit("Error: p has to many items. add this to the code!")
        return 0

def PlotResiduals(df):
    plt.plot(df.Observed, df.Residuals, "o")
    plt.axhline()
    # plt.show()
    return 0

def make_plots(func, x, y, p):
    plt.plot(x, y, "o")
    if len(p) == 1:
        plt.plot(x, func(x, p[0]), "-")
        df = pd.DataFrame({"Observed" : x,
                           "Estimated" : func(x, p[0])})
        df["Residuals"] = y - func(x, p[0])
        r_ss = sp.sum(df.Residuals**2)
        ss_tot = sp.sum((y - sp.mean(y))**2)
        r_squared = 1 - (r_ss / ss_tot)
    elif len(p) == 2:
        plt.plot(x, func(x, p[0], p[1]), "-")
        df = pd.DataFrame({"Observed" : x,
                           "Estimated" : func(x, p[0], p[1])})
        df["Residuals"] = y - func(x, p[0], p[1])
        r_ss = sp.sum(df.Residuals**2)
        ss_tot = sp.sum((y - sp.mean(y))**2)
        r_squared = 1 - (r_ss / ss_tot)
    elif len(p) == 3:
        plt.plot(x, func(x, p[0], p[2]), "-")
        df = pd.DataFrame({"Observed" : x,
                           "Estimated" : func(x, p[0], p[1], [2])})
        df["Residuals"] = y - func(x, p[0], p[1], p[2])
        r_ss = sp.sum(df.Residuals**2)
        ss_tot = sp.sum((y - sp.mean(y))**2)
        r_squared = 1 - (r_ss / ss_tot)  
    n = len(df.Observed)
    aic = n * sp.log((2 * sp.pi) / n) + n + 2 + n * sp.log(r_ss) + 2 * len(p)
    print([func.__name__, r_ss, ss_tot, r_squared, aic])
    plt.xlabel("Distance km")
    plt.ylabel("Density")
    plt.legend(["Distribution", func.__name__.replace("_", "")])
    #plt.show()
    PlotResiduals(df)
    return 0

def GetDistribution(df):    
    # Note: This generates a warning due to internal conditons in seaborn and is 
    # a package rather than user error allowing us to safely silence this warning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        x, y = sns.distplot(df.Distance_km.values).get_lines()[0].get_data()
        plt.clf()
    df = pd.DataFrame({"x":x, "y":y})
    distribution_data = df[df["x"] >= 0]
    return distribution_data

def OptimizeModel(df, model, x, y):
    p, c = sp.optimize.curve_fit(model, x, y, maxfev=100000, method='lm')
    make_plots(model, x, y, p)
    mle = calculate_mle(model, x, p)
    returnstats = {"Model"  : model.__name__,
                   "Params" : p,
                   "MLE"    : mle,
                   "AIC"    : calculate_aic(p, mle)}
    # save output to a global dataframe 
    if len(p) < 2:
        df[model.__name__] = model(x, p[0])
    else:
        df[model.__name__] = model(x, p[0], p[1])
    return returnstats

def NegativeExponential(r, a):
    return (1 / (2 * sp.pi * a**2)) * sp.exp(-(r / a))

def LogNormal(r, a, b):
    return (1 / ((2 * sp.pi)**(3 / 2)) * b * r**2) * sp.exp(-(sp.log(r / a)**2 / 2 * b**2)) 

def _2Dt(r, a, b):
    return ((b - 1) / sp.pi * (a**2)) * (1 + (r**2 / a**2))**-b

def InversePowerlaw(r, a, b):
    return (((b - 2) * (b - 1)) / 2 * sp.pi * a**2) * (1 + (r / a))**-b

def Logsech(r, a, b):
    return (1 / (sp.pi**2 * b * r**2)) / ((r / a)**(1 / b)) + ((r / a)**(-1 / b))

def Weibull(r, a, b):
    return ((b / (2 * sp.pi * a**2)) * r**(b - 2)) * sp.exp(-(r**b / a**b))

def Linear(r, a, b):
    a = 0
    return a * r + b

def Powerlaw_undefined(r, a, b):
    return (r / a)**-b

def InverseGaussian(r, a, b):  # Currently returning error - cheack with samraat
    return (sp.sqrt(b) / sp.sqrt(8 * sp.pi**3 * r**5)) * sp.exp(-(b * (r - a)**2 / 2 * a**2 * r))

def Gamma(r, a, b):
    return (1 / 2 * sp.pi * a**2 * sp.special.gamma(b)) * ((r / a)**b-2) * sp.exp(-(r / a))


# load the data into pandas dataframe
regex = r"(ROT2.csv).+?(ZSL2.csv)"
csv_files = list(re.findall(regex, " ".join(os.listdir("../Data")))[0])
csv_data = [pd.read_csv("../Data/{}".format(x)) for x in csv_files]
data = pd.concat(csv_data)

# rename column headings and set data types
data.rename(columns={"X" : "Destination_Latitude",
                     "Y" : "Destination_Longitude"},
                      inplace = True)
data.Destination_Latitude.astype("float64")
data.Destination_Longitude.astype("float64")
data.Date = pd.to_datetime(data.Date, format = "%d/%m/%Y")

# set hive locations (lat, long)
zsl_hive = (-0.151846577, 51.53391924)
rot_hive = (-0.377314803, 51.81004975)

# add hive locations to the data
data["Hive_Latitude"] = sp.where(data.Location == "ZSL",
                                 zsl_hive[0],
                                 rot_hive[0])
data["Hive_Longitude"] = sp.where(data.Location == "ZSL",
                                  zsl_hive[-1],
                                  rot_hive[-1])

# Calculate the distance in Km from hive to desitation
data["Distance_km"] = mpf.Distance((data.Hive_Latitude,
                                    data.Hive_Longitude),
                                   (data.Destination_Latitude,
                                    data.Destination_Longitude))

# Get distribution data
distribution_data = GetDistribution(data)

# Make a list of models to fit the data to
models_list = [Gamma,
               Powerlaw_undefined,
               NegativeExponential,
               LogNormal,
               _2Dt,
               InversePowerlaw,
               Weibull,
               Linear]

models_list = [LogNormal, _2Dt, InversePowerlaw]

# set empty dictionary to store model output results.
model_summary = {}

# run each model and store the model summary, add the model distributions to
# the original dataframe
for model in models_list:
    model_stat = OptimizeModel(distribution_data,
                               model,
                               distribution_data.x,
                               distribution_data.y)
    model_summary[model_stat["Model"]] = model_stat

# set dictionary to store model output results
subset_model_summary = {}

# run each model on the subset data and store model summary
# take random slices of the data at 3 distributed sizes
for ss in [.31, .62, .93]:
    print(ss)
    subset_model_summary = {}
    subsample = GetDistribution(SampleData(data, ss))
    for model in models_list:
        model_stat = OptimizeModel(subsample,
                                   model,
                                   subsample.x,
                                   subsample.y)
        subset_model_summary[model_stat["Model"]] = model_stat

    # save the distributions to a new dataframe
    saveloc = "../Results/ModelDistributions_{}.csv".format(ss)
    subsample.to_csv(saveloc, index = False)

# write the distributions to file
saveloc = "../Results/ModelDistributions.csv"
distribution_data.to_csv(saveloc, index = False)

# Display the data
model_summary_df = pd.DataFrame.from_dict(model_summary)
subset_summary_df = pd.DataFrame.from_dict(subset_model_summary)
print(model_summary_df)
print(subset_summary_df)
