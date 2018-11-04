#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Autocalculates the correlation between temperatures over successive years.

# clear environment
rm(list=ls())

# load in the data
datapath <- "../Data/KeyWestAnnualMeanTemprature.RData" 
load(datapath)

# get the data split on time series
t1 = ats[1:99,2]
t2 = ats[2:100,2]

a = cor(t1, t2)

# function to randomply sample the data and return the corelation
GetCor <- function(x, y){
  sample1 = sample(x, length(x))
  sample2 = sample(y, length(y))
  correl = cor(sample1, sample2)
  return(correl)
}

# run the function using lapply to vectorize
cors = sapply(1:10000,function(i) GetCor(t1, t2))

# make a density plot of the cors, placing a line at the obsserved coreleation.
pdf("../Results/KeyWestAnualMeanTemperaturePlot.pdf")
plot(density(cors), main = "")
abline(v = a, col = "red")
dev.off()

# calculate what proportion of corelations are greater than the observed.
length(cors[cors>a])/length(cors)
length(cors[cors>a])

# another way to generate the above.
1- length(cors[cors< a])/length(cors)

