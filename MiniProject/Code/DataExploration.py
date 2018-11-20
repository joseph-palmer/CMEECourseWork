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
import scipy as sp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

## Functions ##
def Distance(origin, destination):
    """Distance - Get the distance in kilometers between two coordinates.

    :param origin: tuple of lat and long
    :param destination: tuple of lat and long
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = sp.radians(lat2-lat1)
    dlon = sp.radians(lon2-lon1)
    a = sp.sin(dlat/2) * sp.sin(dlat/2) + sp.cos(sp.radians(lat1)) \
        * sp.cos(sp.radians(lat2)) * sp.sin(dlon/2) * sp.sin(dlon/2)
    c = 2 * sp.arctan2(sp.sqrt(a), sp.sqrt(1-a))
    d = radius * c

    return d


# load the data into pandas dataframes
csv_files = re.findall(r"(\w+.csv)", "  ".join(os.listdir("../Data")))
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
data["Distance_km"] = Distance((data.Hive_Latitude,
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



sys.exit()

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
