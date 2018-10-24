#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: map the Global Population Dynamics Database (GPDD).

# clear environment
rm(list=ls())

# Load required packages #

# clear mem
rm(list=ls())

# load required packages
library("maps")

# load the data
datapath = "../Data/GPDDFiltered.RData"
load(datapath)

# data is named - 
gpdd

# set the map
map(database = "world", fill = T)

# put the points on the map.
points(x = gpdd$long, y = gpdd$lat, pch = 21, bg = gpdd$common.name)


# Biases - The data is heavily biased towards western regions, specifically North America and Europe. The southern hemisphere shows only a single point in
# Southern Africa. This may introduce biases when inferring the state of biodiversity in the southern hemisphere and in the tropics, where biodiversity is
# much higher than in the regions recorded in this dataset.