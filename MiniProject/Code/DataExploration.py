#!/usr/bin/env python3
"""Data exploration script for MiniProject"""
__appname__ = "DataExploration.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import os
import re
import subprocess
import MiniprojectFunctions as mpf
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
plt.style.use('ggplot')

# load the data into pandas dataframes
regex = r"(ROT2.csv).+?(ZSL2.csv)"
csv_files = list(re.findall(regex, "  ".join(os.listdir("../Data")))[0])
csv_data = [pd.read_csv("../Data/{}".format(x)) for x in csv_files]
data = pd.concat(csv_data)

# remane columns headings and set data types
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

# view tha data with a summary
summary_data = ("\n----- Data -----\n"
                "{}Columns: {}"
                "\n----- Summary -----\n"
                "{}\nVariance: {}".format(data.head(),
                                          ", ".join(list(data.columns)),
                                          data.Distance_km.describe(),
                                          data.Distance_km.var()))
print(summary_data)

# save the ouput to a csv file
print("\nRunning 'FitDistributions.R' ---")
data.to_csv("../Data/Distances.csv", index = False)

# call rscript to fit the optimized models
rout = mpf.RunScript("Rscript", "FitDistributions.R")
rout = rout.replace("\n", "").replace("\t", "")

# extract the model values outputed by FitDistributions.R
regex = r"value:\s(\w+).+?'\s(\w+).+?Std.\sError\w+\s(.+?)\s.+?\s([0-9].[0-9]+).+?AIC:\s+(.+?)\s"
model_stats = re.findall(regex, rout)
runs = set([x[0] for x in model_stats])

# create a dictionary to store the model selection output
model_stats_dict = {"DataType" : [],
                    "Distribution" : [],
                    "AIC" : [],
                    "AICDifferance" : [],
                    "Param1" : [],
                    "Param2" : []}

# loop through each model run and get the distribution with lowest aic
for i in runs:
    aic_scores = sorted([float(x[-1]) for x in model_stats if x[0] == i])
    aic_difference = aic_scores[1] - aic_scores[0]
    distribution = "".join([x[1] for x in model_stats if str(aic_scores[0]) == x[-1]])
    param1 = float([x[2] for x in model_stats if str(aic_scores[0]) == x[-1]][0])
    param2 = float([x[3] for x in model_stats if str(aic_scores[0]) == x[-1]][0])
    model_stats_dict["AIC"].append(aic_scores[0])
    model_stats_dict["Distribution"].append(distribution)
    model_stats_dict["DataType"].append(i)
    model_stats_dict["AICDifferance"].append(aic_difference)
    model_stats_dict["Param1"].append(param1)
    model_stats_dict["Param2"].append(param2)

    
# convert dictionary to pandas df for display
model_stats_df = pd.DataFrame.from_dict(model_stats_dict)

# show model stats
print("Output summary of 'FitDistributions.R' ---\n")
print(model_stats_df)

# make some plots of the distributions
sns.distplot(data.Distance_km, hist = True)

param1 = model_stats_df["Param1"][model_stats_df["DataType"] == "ActualData"]
param2 = model_stats_df["Param2"][model_stats_df["DataType"] == "ActualData"]
normdist = sp.random.weibull(param1, len(data.Distance_km))

sns.distplot(normdist, hist = True)
plt.show()



#plt.show()

sys.exit()
# my own generator
# extract the distribution x, y values
x, y = sns.distplot(data.Distance_km).get_lines()[0].get_data()
plt.clf()
plt.plot(x, y, "o")

def fit_straight_line(x, m, b):
    return m * x + b

p, cov = sp.optimize.curve_fit(fit_straight_line, x, y)

t = sp.array([min(x), max(x)])
plt.plot(t, p[0] * t + p[-1])
plt.show()


# fit normal to data
def normal_fit(x, mean, sigma):
    return sp.stats.norm.pdf(x, mean, sigma)

p, cov = sp.optimize.curve_fit(normal_fit, x, y)
plt.plot(x, y, "o")
plt.plot(x, normal_fit(x, p[0], p[1]), "-")
plt.show()

print("***")
print(sp.optimize.curve_fit(normal_fit, x, y))
print("***")


pp = sp.stats.norm.fit(data.Distance_km)
plt.plot(x, y, "o")
plt.plot(x, normal_fit(x, pp[0], pp[-1]))
plt.show()
print("work?>")
print(sp.sum(sp.log(normal_fit(x, pp[0], pp[-1]))))


# now plot a gamma function
def gamma_fit(x, a):
    return sp.stats.gamma.pdf(x, a)

p, cov = sp.optimize.curve_fit(gamma_fit, x, y)
print(p)
plt.plot(x, y, "o")
plt.plot(x, gamma_fit(x, p[0]), "-")
plt.show()

# plot weivan distribution
def wei_fit(x, c):
    return sp.stats.weibull_min.pdf(x, c)
p, cov = sp.optimize.curve_fit(wei_fit, x, y)
print (p)
plt.plot(x, y, "o")
plt.plot(x, wei_fit(x, p[0]), "-")
plt.show()


sys.exit()

# we can see a straigth line doesnt fit very well, lets try normal.
mean = 0.0
var = 1.0
sigma = sp.sqrt(var)
x = sp.linspace(-4, 4, 80)
plt.plot(x, sp.stats.norm.pdf(x, mean, sigma))
plt.show()

n = 20
x = sp.linspace(-4, 4, n)
jitter_amp = .1
jitter = jitter_amp * (sp.random.random(n) - 0.5)
y = sp.stats.norm.pdf(x, mean, sigma) + jitter
plt.plot(x, y, "o")
plt.show()


def normal_fit(x, mean, sigma):
    return sp.stats.norm.pdf(x, mean, sigma)

p, cov = sp.optimize.curve_fit(normal_fit, x, y)
print(p)

plt.plot(x, y, "o")
plt.plot(x, normal_fit(x, p[0], p[1]), "-")
plt.show()


sys.exit()

# make a normal distrubution to plot against the data
normal_data = sp.stats.norm.rvs(data.Distance_km.mean(),
                                data.Distance_km.std(),
                                size = len(data.Distance_km))
sns.distplot(data.Distance_km, label = "Actual", hist = False)
sns.distplot(normal_data, label = "Normal", hist = False)
plt.legend()
plt.show()



# Fit normal model to the data
a = sp.optimize.nnls(sp.asmatrix(data.Distance_km.values).transpose(), normal_data)
print(a)

# make random data subsets for comparison.
randomNorm = sp.stats.norm.rvs(data.Distance_km.mean(),
                               data.Distance_km.std(),
                               size = 100)

# create list to append distributions to (reformat this as numpy array!)
normal_ss = []

# Compare distribution to 100 random samples
for i in range(100):
   sample = data.Distance_km.sample(100)
   a = sp.optimize.nnls(sp.asmatrix(sample.values).transpose(), randomNorm)
   normal_ss.append(a)

# extract the mean and stdev for the models?
print(sp.mean([i[0] for i in normal_ss]))



# make a plot of the distrubution of Distance
#sns.distplot(data.Distance_km)
#plt.show()



#sys.exit()

# make two plots based on location
#zsl_data = data[data["Location"] == "ZSL"]
#sns.distplot(zsl_data.Distance_km)
#plt.show()
#rot_data = data[data["Location"] == "ROT"]
#sns.distplot(rot_data.Distance_km)
#plt.show()

#data.Distance_km.plot(kind = "density")
#zsl_data.Distance_km.plot(kind = "density")
#rot_data.Distance_km.plot(kind = "density")
#plt.legend(["All", "ZSL", "ROT"])
#plt.xlabel("Distance (km)")
# plt.show() # why is ROT so much longer in both directions than the others?

# make some log plots for fun?
#data["log_Distance_km"] = sp.log(data.Distance_km)
#data.log_Distance_km = data.log_Distance_km.astype("float64")
#data.log_Distance_km.plot(kind = "density")
#plt.xlabel("log Distance (km)")
# plt.show()

sns.distplot(data.Distance_km, hist = False)
plt.show()

# start subsampling - take 10 samples and plot the results
for i in range(100):
    sample = data.Distance_km.sample(50)
    sns.distplot(sample, hist=False)

plt.show()
