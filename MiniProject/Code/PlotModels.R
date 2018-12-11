#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: December 2018
# Desc: Plots the distributions and residuals of the fitted distributions.

# clear environment
rm(list=ls())

# Load required packages #
require(ggplot2)
require(reshape2)

# Functions #
ExtractData <- function(filedoc) {
  # extracts the data from specified csv and melts into long format
  df = read.csv(fileloc)
  
  # convert to long format
  df <- melt(data = df, 
                    id.vars = c("x", "y"), 
                    variable.name = "model", 
                    value.name = "distribution")
  return(df)
}

GetR2 <- function(df2, i) {
  # calculates r squared for a given distribution
  tmp = subset(df2, df2$model == i)
  ss_tot = sum(tmp$y - mean(tmp$y)**2)
  r_ss = sum(tmp$Residuals**2)
  r_squared = 1 - (r_ss / ss_tot)
  n = length(tmp$Residuals)
  AIC_score = n * log((2 * pi) / n) + n + 2 + n * log(r_ss) + 2 * 2
  # print(paste("AIC for", i, ":", AIC_score))
  return(round(r_squared, digits = 3))
}

PlotModels <- function(dataframe) {
  # plots the distribution for a given model
  distribution_plot = ggplot() +
    geom_point(aes(x = dataframe$x, y = dataframe$y), dataframe) +
    geom_line(aes(x = dataframe$x, y = dataframe$distribution, colour = dataframe$model)) +
    ylab("Distribution") +
    xlab("Distance (km)") +
    theme_bw() +
    theme(legend.title=element_blank(),
          panel.border = element_blank(),
          panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          axis.line = element_line(colour = "black"))
  return(distribution_plot)
}

PlotResiduals <- function(dataframe) {
  # Makes a facet plot of the residuals
  # change name for plots
  model_names <- c('LogNormal' = paste("Log normal, r squared =", GetR2(dataframe, "LogNormal")),
                   'X_2Dt' = paste("2Dt, r squared =", GetR2(dataframe, "X_2Dt")),
                   'InversePowerlaw' =  paste("Inverse powerlaw, r squared =", GetR2(dataframe, "InversePowerlaw")))
  
  # make residual plots
  residuals_plot = ggplot() +
    geom_point(aes(x = x, y = Residuals), dataframe) +
    facet_wrap(model~., labeller = as_labeller(model_names), ncol = 1) +
    geom_hline(yintercept = 0, colour = "blue") +
    ylab("Residuals") +
    xlab("Distance (km)") +
    theme_bw() +
    theme(legend.title=element_blank(),
          panel.border = element_blank(),
          panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(),
          strip.background =element_blank(), #(fill="white"),
          strip.text = element_text(colour = 'black', size = 12),
          axis.line = element_line(colour = "black"))
  
  return(residuals_plot)
}


# Main body #

# get a list of files to work with
csv_files = list.files(path = "../Results/", pattern = "*.csv")

# for each, file create the model plots.
for (files in csv_files) {
  # extract the file path and read it in
  fileloc = paste0("../Results/", files)
  data = ExtractData(filedoc)
  
  # Keep only best fitting distribtions
  #df2 = subset(df2, model == "X_2Dt" | model == "LogNormal" | model == "InversePowerlaw")
  
  # calculate residuals
  data$Residuals = data$y - data$distribution
  
  # get main plot
  dist_plot = PlotModels(data)
  
  # get residual plot
  resid_plot = PlotResiduals(data)
  
  # save the plots
  dist_plot_save_path = paste0("../Results/Plots/", gsub(".csv", paste0("_dist", ".pdf"), files))
  res_plot_save_path = paste0("../Results/Plots/", gsub(".csv", paste0("_res", ".pdf"), files))
  ggsave(dist_plot_save_path, dist_plot)
  ggsave(res_plot_save_path, resid_plot)
}


# # alternative distribution ggplot
# mainplot = ggplot() + 
#   geom_point(aes(df$x, df$y), df) +
#   ylab("Distribution") +
#   xlab("Distance (km)") +
#   theme_bw() +
#   theme(panel.border = element_blank(),
#         panel.grid.major = element_blank(),
#         panel.grid.minor = element_blank(),
#         axis.line = element_line(colour = "black"))
# 
# mainplot = mainplot +
#   geom_line(aes(df$x, df$X_2Dt, colour = "red"), df) +
#   geom_line(aes(df$x, df$Powerlaw_undefined, colour = "blue"), df) +
#   geom_line(aes(df$x, df$InversePowerlaw, colour = "green"), df) #+
# #  scale_color_discrete(name = "Y series", labels = c("Y2", "Y1", "Y3"))
