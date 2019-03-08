#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: March 2019
# Desc: Miniproject Model fitting functions

########## clear environment ##########
rm(list=ls())

########## Load required packages ##########
suppressMessages(require("minpack.lm"))
suppressMessages(require("pracma"))
suppressMessages(require("reshape2"))
suppressMessages(require("ggplot2"))
suppressMessages(require("cowplot"))
suppressMessages(require("xtable"))
suppressMessages(require("compiler"))

# setup compiler
enableJIT(3)

########## Model Functions ##########
LogNormal <- function(x, a, b) {
  ## calculates the cdf for a log normal distribution ##
  return(1-((1/2) + (1/2) * erf((log(x) - a) / sqrt(2 * b))))
}

LogNormal = cmpfun(LogNormal)

Weibull <- function(x, a, b) {
  ## calculates the cdf for a normal distribution ##
  return(1 - (1 - exp(-(x/a)^b)))
}

Weibull = cmpfun(Weibull)

half_normal <- function(x, a) {
  ## calculates the cdf for a half normal distribution ##
  return(1-(erf(x / (a * sqrt(2)))))
}

half_normal = cmpfun(half_normal)

exponential <- function(x, a){
  ## calculates the cdf for the exponential distribution ##
  return(1-(1 - exp(-a * x)))
}

AICc = function(m, k, n) {
  ## compute corrected AIC to consider sample size.
  # k = no. of parameters, n = sample size. ##
  return(AIC(m) + 2 * k * (k + 1) / (n - k - 1))
}

AICc = cmpfun(AICc)

########## model fitting functions ##########
Fit_half_norm = function(x) {
  ## Fits the half-normal function and returns the AICc score of the fit ##
  PowFit <- nlsLM(probability ~ half_normal(sorted_distance, a), data = x, start = list(a = sqrt(var(x$sorted_distance))))
  return(AICc(PowFit, 1, nrow(x)))
}

Fit_half_norm = cmpfun(Fit_half_norm)

Fit_exponential = function(x){
  ## Fits the exponential function and returns the AICc score of the fit ##
  PowFit <- nlsLM(probability ~ exponential(sorted_distance, a), data = x, start = list(a = 1/mean(x$sorted_distance)))
  return(AICc(PowFit, 1, nrow(x)))
}

Fit_exponential = cmpfun(Fit_exponential)

Fit_lognormal = function(x){
  ## Fits the lognormal function and returns the AICc score of the fit ##
  PowFit <- nlsLM(probability ~ LogNormal(sorted_distance, a, b), data = x, start = list(a = mean(x$sorted_distance), b = var(x$sorted_distance)))
  return(AICc(PowFit, 2, nrow(x)))
}

Fit_lognormal = cmpfun(Fit_lognormal)

Fit_Weibull = function(x){
  ## Fits the weibull function and returns the AICc score of the fit ##
  PowFit <- nlsLM(probability ~ Weibull(sorted_distance, a, b), data = x, start = list(a = mean(x$sorted_distance), b = var(x$sorted_distance)))
  return(AICc(PowFit, 2, nrow(x)))
}

Fit_Weibull = cmpfun(Fit_Weibull)

########## Analysis functions ##########
CalculateInverseCDF <- function(distance_data) {
  ## Calculate a cdf based on input data,
  # returning the sorted data and its probability ##
  sorted_distance = sort(distance_data)
  probability = seq(1, 0, length.out = length(sorted_distance))
  return(data.frame(sorted_distance, probability))
}

CalculateInverseCDF = cmpfun(CalculateInverseCDF)

GetMeanAIC = function(i, data.plot, data.aic, bootstrap_n) {
  ## Calculates the mean AIC value for a bootstrap pluss 95CI ##
  data.plot[i,1] = i
  data.plot[i,2] = mean(data.aic)
  data.plot[i,3] = mean(data.aic) + qnorm(0.975)*sd(data.aic)/sqrt(bootstrap_n)
  data.plot[i,4] = mean(data.aic) - qnorm(0.975)*sd(data.aic)/sqrt(bootstrap_n)
}

GetMeanAIC = cmpfun(GetMeanAIC)

BootstapModels = function(data){
  ## Fit models to the data over a number of bootstraps ##
  # set n number of equal chunks whose value represents the number of data points to sample
  sample_length = 17
  
  # set the number of bootstraps to perform
  bootstrap_n = 100
  
  # create equal chunks
  sample_range = unlist(lapply(1:sample_length, function(x) x*length(data$Distance_Km) / sample_length))
  
  # initialize matrix to store average AIC values at each sample range
  half_normal.plot = matrix(nrow = sample_length, ncol = 4)
  exponential.plot = matrix(nrow = sample_length, ncol = 4)
  lognormal.plot = matrix(nrow = sample_length, ncol = 4)
  normal.plot = matrix(nrow = sample_length, ncol = 4)
  
  # loop through the sample ranges and draw the range value number of elements from the data
  for(i in 1:sample_length){
    # get bootstrapped sample of AIC values from models fitted
    half_normal_aic = unlist(lapply(1:bootstrap_n, function(x) Fit_half_norm(CalculateInverseCDF(sample(data$Distance_Km, sample_range[i], replace = T)))))
    exponential_aic = unlist(lapply(1:bootstrap_n, function(x) Fit_exponential(CalculateInverseCDF(sample(data$Distance_Km, sample_range[i], replace = T)))))
    lognormal_aic = unlist(lapply(1:bootstrap_n, function(x) Fit_lognormal(CalculateInverseCDF(sample(data$Distance_Km, sample_range[i], replace = T)))))
    weibull_aic = unlist(lapply(1:bootstrap_n, function(x) Fit_Weibull(CalculateInverseCDF(sample(data$Distance_Km, sample_range[i], replace = T)))))
    
    # half normal
    half_normal.plot[i,1] = sample_range[i]
    half_normal.plot[i,2] = mean(half_normal_aic)
    half_normal.plot[i,3] = mean(half_normal_aic) + qnorm(0.975)*sd(half_normal_aic)/sqrt(bootstrap_n)
    half_normal.plot[i,4] = mean(half_normal_aic) - qnorm(0.975)*sd(half_normal_aic)/sqrt(bootstrap_n)
    
    # exponential
    exponential.plot[i,1] = sample_range[i]
    exponential.plot[i,2] = mean(exponential_aic)
    exponential.plot[i,3] = mean(exponential_aic) + qnorm(0.975)*sd(exponential_aic)/sqrt(bootstrap_n)
    exponential.plot[i,4] = mean(exponential_aic) - qnorm(0.975)*sd(exponential_aic)/sqrt(bootstrap_n)
    
    # lognormal
    lognormal.plot[i,1] = sample_range[i]
    lognormal.plot[i,2] = mean(lognormal_aic)
    lognormal.plot[i,3] = mean(lognormal_aic) + qnorm(0.975)*sd(lognormal_aic)/sqrt(bootstrap_n)
    lognormal.plot[i,4] = mean(lognormal_aic) - qnorm(0.975)*sd(lognormal_aic)/sqrt(bootstrap_n)
    
    # weibull
    normal.plot[i,1] = sample_range[i]
    normal.plot[i,2] = mean(weibull_aic)
    normal.plot[i,3] = mean(weibull_aic) + qnorm(0.975)*sd(weibull_aic)/sqrt(bootstrap_n)
    normal.plot[i,4] = mean(weibull_aic) - qnorm(0.975)*sd(weibull_aic)/sqrt(bootstrap_n)
  }
  
  # convert matrix to dataframes for use in ggplot, for each model
  half_normal.df = as.data.frame(half_normal.plot)
  exponential.df = as.data.frame(exponential.plot)
  lognormal.df = as.data.frame(lognormal.plot)
  normal.df = as.data.frame(normal.plot)
  colnames(half_normal.df) = c("Iter", "AICc", "LowerCI", "UpperCI")
  colnames(exponential.df) = c("Iter", "AICc", "LowerCI", "UpperCI")
  colnames(lognormal.df) = c("Iter", "AICc", "LowerCI", "UpperCI")
  colnames(normal.df) = c("Iter", "AICc", "LowerCI", "UpperCI")
  half_normal.df["Model"] = "Half-Normal"
  exponential.df["Model"] = "Exponential"
  lognormal.df["Model"] = "Lognormal"
  normal.df["Model"] = "Weibull"
  combined = rbind(half_normal.df, exponential.df, lognormal.df, normal.df)
  
  return(combined)
}

BootstapModels = cmpfun(BootstapModels)

PredictFunc = function(Name, data){
  ## fit different models to the distributions ##
  Lengths = seq(min(data$sorted_distance), max(data$sorted_distance), len = nrow(data))
  if (Name == "Half-Normal") {
    param = sqrt(var(data$sorted_distance))
    PowFit <- nlsLM(probability ~ half_normal(sorted_distance, a),
                    data = data, start = list(a = param))
    Predic2Plot = half_normal(Lengths, coef(PowFit)["a"])
    a = coef(summary(PowFit))
    model_start = paste(round(coef(PowFit)["a"], 2))
    model_p_name = paste("$\\sigma$")
    model_se = paste(signif(a[1,2], 3))
    model_t = paste(signif(a[1,3], 3))
    model_p = paste(signif(a[1,4], 3))
  } else if(Name == "Lognormal") {
    param1 = mean(data$sorted_distance)
    param2 = var(data$sorted_distance)
    PowFit <- nlsLM(probability ~ LogNormal(sorted_distance, a, b),
                    data = data, start = list(a = param1, b = param2))
    Predic2Plot = LogNormal(Lengths, coef(PowFit)["a"], coef(PowFit)["b"])
    model_start = paste(round(coef(PowFit)["a"], 2), ",", round(coef(PowFit)["b"], 2))
    model_p_name = paste("$\\mu$\\\ $\\sigma$")
    a = coef(summary(PowFit))
    model_se = paste(signif(a[1,2], 3), ",", signif(a[2,2], 3))
    model_t = paste(signif(a[1,3], 3), ",", signif(a[2,3], 3))
    model_p = paste(signif(a[1,4], 3), ",", signif(a[2,4], 3))
  } else if(Name == "Exponential") {
    param = 1 / mean(data$sorted_distance)
    PowFit <- nlsLM(probability ~ exponential(sorted_distance, a),
                    data = data, start = list(a = param))
    Predic2Plot = exponential(Lengths, coef(PowFit)["a"])
    model_start = paste(signif(coef(PowFit)["a"], 3))
    model_p_name = paste("$\\lambda$")
    a = coef(summary(PowFit))
    model_se = paste(signif(a[1,2], 3))
    model_t = paste(signif(a[1,3], 3))
    model_p = paste(signif(a[1,4], 3))
  } else if(Name == "Weibull") {
    param1 = mean(data$sorted_distance)
    param2 = var(data$sorted_distance)
    PowFit <- nlsLM(probability ~ Weibull(sorted_distance, a, b),
                    data = data, start = list(a = param1, b = param2))
    Predic2Plot = Weibull(Lengths, coef(PowFit)["a"], coef(PowFit)["b"])
    model_start = paste(signif(coef(PowFit)["a"], 3), ",", signif(coef(PowFit)["b"], 3))
    model_p_name = paste("$\\lambda,\\ k$")
    a = coef(summary(PowFit))
    model_se = paste(signif(a[1,2], 3), ",", signif(a[2,2], 3))
    model_t = paste(signif(a[1,3], 3), ",", signif(a[2,3], 3))
    model_p = paste(signif(a[1,4], 3), ",", signif(a[2,4], 3))
  }
  predictions = data.frame(Lengths, Predic2Plot)
  predictions["Model"] = Name
  predictions["Parameters"] = model_p_name
  predictions["Starting_Values"] = model_start
  predictions["SE"] = model_se
  predictions["t"] = model_t
  predictions["p_value"] = model_p
  colnames(predictions)[2] = "Prediction"
  predictions$AIC = round(AICc(PowFit, 1, nrow(data)), 0)
  predictions = merge(data, predictions, by = 0)
  predictions = predictions[order(as.numeric(predictions$Row.names)),]
  rownames(predictions) = seq(length = nrow(predictions))
  predictions$Row.names = NULL
  return(predictions)
}

PredictFunc = cmpfun(PredictFunc)

GetPredictions = function(data){
  ## Get the predicted values from the fitted model 
  # set lengths (the x axis values to predict) ##
  # combine prediction data
  predictions.hn = PredictFunc("Half-Normal", data)
  predictions.ln = PredictFunc("Lognormal", data)
  predictions.ex = PredictFunc("Exponential", data)
  predictions.nm = PredictFunc("Weibull", data)
  predictions.all = rbind(predictions.hn, predictions.ln, predictions.ex, predictions.nm)
  return(predictions.all)
}

GetPredictions = cmpfun(GetPredictions)

AICTableRank = function(model_stats){
  # #Creates a sorted tabe of Models according to AIC value ##
  # Order dataframe according to AIC value and Location
  sorted_model_stats = data.frame()
  for (i in unique(model_stats$Location)){
    sub =  subset(model_stats, model_stats$Location == i)
    sub$AICc = as.numeric(as.character(sub$AICc))
    sorted_dat = sub[order(sub$AICc, sub$Model), ]
    sorted_model_stats = rbind(sorted_model_stats, sorted_dat)
  }
  
  # get ranking
  sorted_model_stats$Rank = rep(seq(0, length(unique(sorted_model_stats$Model)) - 1, 1), length(unique(sorted_model_stats$Location)))
  return(sorted_model_stats)
}

AICTableRank = cmpfun(AICTableRank)