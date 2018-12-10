#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: November 2018
# Desc: test for fitting models to the data

# clear environment
rm(list=ls())

# Load required packages #
require("minpack.lm")
require(fitdistrplus)

# load in the distance data
data = read.csv("../Data/Distances.csv")
distance = data$Distance_km
zsl_dist = data$Distance_km[data$Location == "ZSL"]
rot_dist = data$Distance_km[data$Location == "ROT"]

# normal function
GausianFunc <- function(r, a, b){
  return(((b - 1) / pi * (a**2)) * (1 + (r**2 / a**2))**-b )
}

# actual
res<-density(distance)
x_dis = res$x
y_dis = res$y
plot(x_dis, y_dis)

# normal
res2 <- density(rnorm(length(distance), mean(distance), sd(distance)))
x_norm = res2$x
y_norm = res2$y
lines(x_norm, y_norm, col="red")


# fit the distribution using non-linear least squares (nlls)
# wrap density values in dataframe
dats = data.frame(y_dis, x_dis)
datass = data.frame(y_norm, x_norm)

# fit the model
plot(density(data$Distance_km))
fit = nlsLM(datass$y_norm ~ GausianFunc(dats$x_dis, a, b), data=dats, start = list(a = .1, b = .1))#, lower = .1, upper = 10000)
summary(fit)
AIC(fit)
coef(fit)["a"]
coef(fit)["b"]
confint(fit)

Lengths <- seq(min(dats$x_dis),max(dats$x_dis),len=200)
PredictedFit <- GausianFunc(Lengths,coef(fit)["a"],coef(fit)["b"])
lines(Lengths, PredictedFit)


#GausianFunc(len = length(x_dis), mean = mean(x_dis), sd = sd(x_dis))
modelfit = fitdist(distance, "norm", method = "mle")

a = rnorm(length(distance), modelfit$estimate)
plot(density(distance))
lines(density(a), col = "red")
modelfit$aic

gammafit = fitdist(distance, "gamma", method = "mle")
b = rgamma(length(distance), gammafit$estimate)
lines(density(b), col = "blue")
gammafit$aic

weifit = fitdist(distance, "weibull", method = "mle")
c = rweibull(length(distance), weifit$estimate)
lines(density(c), col = "green")
weifit$aic

# test for power law
require(poweRlaw)

data_pl <- conpl$new(distance)
est <- estimate_xmin(data_pl)
data_pl$xmin <- est$xmin
data_pl$pars <- est$pars
bs <- bootstrap_p(data_pl)
bs$p

require(igraph)
a = power.law.fit(distance)
plot(density(a))

     