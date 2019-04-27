#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: April 2019
# Desc: R code to fit mle exponential

# clear environment
rm(list=ls())

# Load required packages #

# declare log-likelihood function
lnlike = function(x, a){
  n = length(x)
  return(1 - (n*log(a) - a * sum(x)))
}

# get data from xponential distribution and order
rate = 1.8
data = rexp(10000, rate)
data = sort(data, decreasing = T)

# create a probability ranking for the data for the plot
rank = seq(1, length(data), by=1) / length(data)

# show the plot with log rank to observe typical straight line of exponential
plot(data, log(rank))

# put the data together to check
data.frame(rank, data)

# create an estimate of possible parameter values
estimate = seq(0.1, 10, 0.1)

# get loglikelihood estimates for the data and estimates
mle = lnlike(data, estimate)

# put into a dataframe for viewing
mle2 = data.frame(estimate, mle)

# extract the numerical minimum value
maxmle = mle2$estimate[mle2$mle == min(mle2$mle)]

# plot the likelihood curve with a line of the numerical minimum
plot(estimate, mle, type = "l")
abline(v = maxmle, col = "red")

# weird thing here is that the analitical solution doesn't work!
# The numerical methods return the correct number of 1.8.
# This is the opposite to the python code where the numerical methods return wrong number
# but the analytical solution returns the correct number of 1.8.
# The really odd part is the analytical solution here returns the same number as the numerical methods in the python code. 0.56.
# What is going on here??????/
an_mle = 1/(sum(data) / length(data))

print(paste("Analytical method:", an_mle, "Numerical Method:", maxmle, "Actual Rate:", rate))

# OK. SOLVED THE PROBLEM - The problem was in the was R and python generated the exponential data. Their rate is 1 divided by the rate I was using. python needs you to do this,
# R automatically does it for you. Realising this the fix was to change the rate I am using in python to 1/rate. This solved the numerical solving problem. The problem with the 
# analytical clution was because I needed to do 1/the estimate. I have changed and updated the code.
# Next task is to extent the MLE code in python to the lognormal and others.
