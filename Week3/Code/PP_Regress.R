#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: ggplot practicle for data visualisation

# clear environment
rm(list=ls())

# Load required packages #
require(ggplot2)

# set data path
datapath = "../Data/EcolArchives-E089-51-D1.csv"

# load the data
MyDF <- read.csv(datapath)
head(MyDF)

# make the plot
p <- qplot(Prey.mass,
      Predator.mass,
      facets = Type.of.feeding.interaction ~.,
      data = MyDF,
      log = "xy",
      xlab = "Prey Mass in grams",
      ylab = "Predator mass in grams",
      colour = Predator.lifestage)
q = p + stat_smooth(method = "lm", fullrange = TRUE) + geom_point(shape = 9) + theme_bw() + theme(legend.position="bottom")

# show the plot
q

summary(q)

# work out stats
for (i in unique(MyDF$Predator.lifestage)) {
  print(i)
}
model <- lm(Prey.mass~Predator.mass, MyDF)
summary(model)
