#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: March 2019
# Desc: Miniproject Model fitting code

########## clear environment ##########
rm(list=ls())

########## Load required packages ##########
cat("### Loading required packages ###\n\n")
require("minpack.lm")  
require("pracma")
require("reshape2")
require("ggplot2")
require("cowplot")
require("xtable")

########## Source Functions script ##########
source("Functions.R")

########## Import data ##########
cat("\n### Generating descritive statistics and running data comparison tests ###\n\n")
data = read.csv("../Data/Distances.csv")

# change location names
data$Location = ifelse(data$Location == "ROT", "Rural", "Urban")

# divide dataset into groups by location
data.rot = subset(data, data$Location == "Rural")
data.zsl = subset(data, data$Location == "Urban")

########## T-test and descriptive statistics ##########
# get descriptive stats
sumstat = length(data$Distance_Km)
sumstat = length(data.zsl$Distance_Km)
sumstat = length(data.rot$Distance_Km)
ttest = t.test(data.rot$Distance_Km, data.zsl$Distance_Km)

# test for difference in means
ttest.plot = ggplot(data = data, aes(x = Location, y = Distance_Km)) +
  geom_boxplot() +
  labs(y = "Foraging distance (Km)")

########## Model fitting ##########
# get CDFs
cat("\n### Fitting models ###\n\n")
zsl.cdf = CalculateInverseCDF(data.zsl$Distance_Km)
zsl.cdf["Location"] = "Urban"
rot.cdf = CalculateInverseCDF(data.rot$Distance_Km)
rot.cdf["Location"] = "Rural"
cdf = rbind(rot.cdf, zsl.cdf)

# fit models to get predictions
predicted.zsl = GetPredictions(zsl.cdf)
predicted.rot = GetPredictions(rot.cdf)
predicted.comb = rbind(predicted.zsl, predicted.rot)

# Get best AICScore for each model and dataset
model_stats = matrix(ncol = 8, nrow = length(unique(predicted.comb$AIC)))
c = 0
for (i in unique(predicted.comb$Location)){
  sub = subset(predicted.comb, predicted.comb$Location == i)
  for(j in unique(sub$Model)){
    c = c + 1
    model_stats[c,1] = i
    model_stats[c,2] = j
    model_stats[c,3] = unique(subset(sub, sub$Model == j)$Parameters)
    model_stats[c,4] = unique(subset(sub, sub$Model == j)$Starting_Values)
    model_stats[c,5] = unique(subset(sub, sub$Model == j)$SE)
    model_stats[c,6] = unique(subset(sub, sub$Model == j)$t)
    model_stats[c,7] = unique(subset(sub, sub$Model == j)$p_value)
    model_stats[c,8] = round(unique(subset(sub, sub$Model == j)$AIC), 0)
  }
}
model_stats = as.data.frame(model_stats)
colnames(model_stats) = c("Location", "Model", "Parameters", "Starting estimates", "Standard error",  "t", "$p$", "AICc")

# get AIC stats in table
model_stats.aic = AICTableRank(model_stats)

########## Sampling sensitivity Analysis ##########
cat("\n### Conducting sampling sensitivity analysis ###\n\n")
combined.zsl = BootstapModels(data.zsl)
combined.zsl["Location"] = "Urban"
combined.rot = BootstapModels(data.rot)
combined.rot["Location"] = "Rural"

# Rank bootstrapped data according to AICc at each sample size.
bootstrap_data = data.frame()
for (dataset in list(combined.rot, combined.zsl)){
  new = data.frame()
  for (i in unique(dataset$Iter)){
    sub = subset(dataset, dataset$Iter == i)
    sub.aic = AICTableRank(sub)
    new = rbind(new, sub.aic)
  }
  bootstrap_data = rbind(bootstrap_data, new)
}

########## Plotting ###########
# AIC plot
cat("\n### Producing Plots and tabels ###\n\n")
aic1.plot = ggplot(data = bootstrap_data, aes(x = Iter)) +
  geom_point(aes(x = Iter, y = AICc, colour = Model)) +
  geom_ribbon(aes(ymin = LowerCI, ymax = UpperCI, fill = Model), alpha = 0.2) +
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        legend.position = "bottom",
        axis.line = element_line(colour = "black"),
        legend.title = element_text(face="bold")) +
  xlab("Sample size") + ylab("AICc") +
  facet_grid(.~Location, scales = "free_x")

# Corrected AIC plot
aic2.plot = ggplot(data = bootstrap_data, aes(x = Iter)) +
  geom_point(aes(x = Iter, y = abs(AICc) / Iter, colour = Model)) +
  geom_ribbon(aes(ymin = abs(LowerCI) / Iter, ymax = abs(UpperCI) / Iter, fill = Model), alpha = 0.2) +
  theme(panel.grid.major = element_blank(),
        axis.line = element_line(colour = "black"),
        legend.position = "bottom",
        legend.title = element_text(face="bold")) +
  xlab("Sample size") + ylab("AICc") +
  facet_grid(.~Location, scales = "free_x")

# plot pdfs
pdf = data
pdf.plot = ggplot(data = pdf, aes(x = Distance_Km, fill = "red")) +
  geom_density(alpha = 0.2) +
  theme(legend.position = "None") +
  xlab("Foraging distance (km)") +
  facet_grid(.~ Location)

# plot cdfs
cdf.plot = ggplot(data = cdf, aes(x = sorted_distance, y = probability, fill = "red")) +
  geom_area(alpha = 0.2) +
  geom_line() +
  theme(legend.position = "None") +
  xlab("Foraging distance (km)") +
  facet_grid(.~ Location, scales = "free_x")

# combine the plots
combined.plot = plot_grid(pdf.plot, cdf.plot, ncol = 1, nrow = 2, labels = c("A", "B"))

# possible alternative plot? ##################################################################### <---------------------------------------------------------
model_plot_alternative = ggplot(data = predicted.comb, aes(x = sorted_distance, y = probability)) +
  geom_line(size = 0.8) +
  geom_line(data = predicted.comb, aes(x = Lengths, y = Prediction), colour = "blue", linetype = "dashed") +
  facet_grid(Model ~ Location) +
  theme(legend.position = "None")

# divide dataframe into two for optimal plotting
predicted.comb.1 = subset(predicted.comb, Model == "Half-Normal" | Model == "Exponential")
predicted.comb.2 = subset(predicted.comb, Model == "Weibull" | Model == "Lognormal")

# make plot of exponential and half-normal
predicted.plot1 = ggplot(data = predicted.comb.1, aes(x = sorted_distance, y = probability)) +
  geom_point(size = 2, shape = 1) +
  geom_line(data = predicted.comb.1, aes(x = Lengths, y = Prediction, colour = Model), size = 1) +
  facet_grid(.~Location) +
  scale_color_manual(values = c("red", "blue")) +
  xlab("Foraging distance (km)") +
  theme(legend.position = "bottom")

# make plot of lognormal and normal
predicted.plot2 = ggplot(data = predicted.comb.2, aes(x = sorted_distance, y = probability)) +
  geom_point(size = 2, shape = 1) +
  geom_line(data = predicted.comb.2, aes(x = Lengths, y = Prediction, colour = Model), size = 1) +
  scale_color_manual(values = c("purple", "orange")) +
  facet_grid(.~Location) +
  xlab("Foraging Distance (km)") +
  theme(legend.position = "bottom")

# combine the plots
modelplot2 = plot_grid(predicted.plot1, predicted.plot2, ncol = 1, nrow = 2)

########### Save all plots and tables ##########
plotpath = "../Results/Plots/"
ggsave(paste0(plotpath, "ttest.pdf"), ttest.plot)
ggsave(paste0(plotpath, "model_pdf_cdf.pdf"), combined.plot)
ggsave(paste0(plotpath, "models.pdf"), modelplot2)
ggsave(paste0(plotpath, "models_hn_ex.pdf"), predicted.plot1)
ggsave(paste0(plotpath, "models_ln_n.pdf"), predicted.plot2)
ggsave(paste0(plotpath, "bootstrap_model_aic.pdf"), aic1.plot, scale=2)
ggsave(paste0(plotpath, "bootstrap_model_aic_corrected.pdf"), aic2.plot, scale=2)

# save tabele
model_stats.aic$Rank = NULL
model_stats.latex = xtable(model_stats.aic, type = "latex", caption = "Summary statistics for each model at each dataset")
print(model_stats.latex,
      caption.placement = "top",
      sanitize.text.function=function(x){x},
      size = "\\",
      include.rownames = FALSE,
      scalebox='0.75',
      file = "../Results/ModelAICc.tex")
