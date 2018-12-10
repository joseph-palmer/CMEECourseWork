#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: November 2018
# Desc: Fits distributions to bee foragine distances.

# clear environment
rm(list=ls())

# Load required packages #
require(fitdistrplus)

# load in the distance data
data = read.csv("../Data/Distances.csv")
distance = data$Distance_km
zsl_dist = data$Distance_km[data$Location == "ZSL"]
rot_dist = data$Distance_km[data$Location == "ROT"]


# fit distributions via Maximum Liklihood to the data
fit_methods = c("norm", "gamma", "weibull")
print("--- Full Distance Data ---")
for (i in fit_methods){
  # fit the model to all the data
  modelfit = fitdist(distance, i, method = "mle")
  print("value: ActualData")
  print(summary(modelfit))
}


# fit distrubutions to random subsets of the data
print("-- Fit to random subsets --")
random_variables = c(59, 187, 310, 209, 277, 14, 133)
set.seed(21)
for (i in random_variables){
  rsample = sample(distance, i)
  for (ii in fit_methods){
    modelfit_random = fitdist(rsample, ii, method = "mle")
    print(paste("Random subset value:", i))
    print(summary(modelfit_random))
  }
}


# take a random value from the distribution and get the valus up to it
#section = sample(min(distance):max(distance), 1)
#subsection = distance[distance < section]
#plot(density(subsection))

#descdist(distance, discrete=FALSE, boot=500) # what does this do?

#plot(modelfit)


# 
# gamma_MLE = fitdist(distance, "gamma", method = "mle")
# norm_MLE = fitdist(distance, "norm", method = "mle")
# weibull_MLE = fitdist(distance, "weibull", method = "mle")
# 
# # get summaries
# summary(norm_MLE)
# summary(gamma_MLE)
# summary(weibull_MLE)
# 
# # Get distributions for plotting
# distance_optimized_gamma = rgamma(length(distance), shape = 1.430485, rate = 1.357784)
# distance_optimized_norm = rnorm(length(distance), 1.0535957, 0.8019474)
# distance_optimized_weibull = rweibull(length(distance), shape = 1.288731, scale = 1.135072)
# distance_optimized_uniform = runif(length(distance))
# 
# # plot distribution fits
# plot(density(distance))
# lines(density(distance_optimized_gamma), col = "red")
# lines(density(distance_optimized_norm), col = "green")
# lines(density(distance_optimized_weibull), col = "blue")
# 
# # compare AIC scores
# gamma_mle_aic = gamma_MLE$aic
# norm_mle_aic = norm_MLE$aic
# weibull_mle_aic = weibull_MLE$aic
# 
# print(paste(gamma_mle_aic, norm_mle_aic, weibull_mle_aic))
# 
# 
# # do it on subsets of the data
# sample_distance = sample(distance, 200)
# 
# gamma_MLE = fitdist(rot_dist, "gamma", method = "mle")
# norm_MLE = fitdist(rot_dist, "norm", method = "mle")
# weibull_MLE = fitdist(rot_dist, "weibull", method = "mle")
# 
# gamma_MLE$aic
# norm_MLE$aic
# weibull_MLE$aic




