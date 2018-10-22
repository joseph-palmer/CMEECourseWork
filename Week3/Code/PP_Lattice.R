# script that draws and saves three lattice graphs by feeding interaction type.

# clear environment
rm(list=ls())

# set data path
datapath = "../Data/EcolArchives-E089-51-D1.csv"

# load the data
MyDF <- read.csv(datapath)
head(MyDF)

# get the lattace package in
library(lattice)

# convert units to g....

# latice for predator mass
densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF, xlab = "Predator mass (Kg)")

# lattice for prey mass
densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data=MyDF, xlab = "Prey mass (Kg)")

# lattice for predator mass / prey mass ratio.
densityplot(~log(Predator.mass/Prey.mass) | Type.of.feeding.interaction, data=MyDF, xlab = "Predator mass (Kg) / Prey mass (Kg)")

# basic stats
mean(MyDF$Predator.mass)

MyDF %>%
  group_by(Type.of.feeding.interaction) %>% 
    summarise(
      Predator.mass.mean = mean(Predator.mass),
      Predator.median.mass = median(Predator.mass),
      Prey.mass.mean = mean(Prey.mass),
      Prey.mass.median = median(Prey.mass),
      Predator.Prey.Size.Ratio = mean(Prey.mass/Predator.mass)
    )
