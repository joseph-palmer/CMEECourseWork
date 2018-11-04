#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: NLLS practicle - Allometry

# clear environment
rm(list=ls())

# Load required packages #
require(minpack.lm)
require(ggplot2)
require(repr)

# create a function to create a power law model.
powMod <- function(x, a, b) {
  return(a * x^b)
}

# read in the data and have a look
MyData <- read.csv("../Data/GenomeSize.csv")
head(MyData)

# subset the data and remove NAs
Data2Fit <- subset(MyData,Suborder == "Anisoptera")
Data2Fit <- Data2Fit[!is.na(Data2Fit$TotalLength),]

# plot it
ggplot(Data2Fit, aes(x = TotalLength, y = BodyWeight)) + geom_point()

# fit the model to the data using NLLS
PowFit <- nlsLM(BodyWeight ~ powMod(TotalLength, a, b), data = Data2Fit, start = list(a = .1, b = .1))
summary(PowFit)

# generate a vector of body lengths for plotting
Lengths <- seq(min(Data2Fit$TotalLength),max(Data2Fit$TotalLength),len=200)

# calculate the predicted line - need to extract the coefficient from the model fit object using the coef()command.
coef(PowFit)["a"]
coef(PowFit)["b"]

# make plot predictions
Predic2PlotPow <- powMod(Lengths,coef(PowFit)["a"],coef(PowFit)["b"])

# plot the data dn the predicted model lines
plot(Data2Fit$TotalLength, Data2Fit$BodyWeight)
ggplot(Data2Fit, aes(x = TotalLength, y = BodyWeight)) + geom_point()
lines(Lengths, Predic2PlotPow, col = 'blue', lwd = 2.5)

# We can claculate the confidence intervals on the estimated parameters as we would in OLS fitting used for Linear Models:
confint(PowFit)
