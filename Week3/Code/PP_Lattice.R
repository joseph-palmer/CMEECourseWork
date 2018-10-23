### script that draws and saves three lattice graphs by feeding interaction type.

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
pdf("../Results/Pred_Lattice.pdf")
densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF, xlab = "Predator mass (Kg)")
dev.off()

# lattice for prey mass
pdf("../Results/Prey_Lattice.pdf")
densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data=MyDF, xlab = "Prey mass (Kg)")
dev.off()

# lattice for predator mass / prey mass ratio.
pdf("../Results/SizeRatio_Lattice.pdf")
densityplot(~log(Predator.mass/Prey.mass) | Type.of.feeding.interaction, data=MyDF, xlab = "Predator mass (Kg) / Prey mass (Kg)")

# basic stats
mean(MyDF$Predator.mass)

# get csv called pp_results.csv
require(dplyr)

pp_results <- MyDF %>%
  group_by(Type.of.feeding.interaction) %>% 
    summarise(
      Predator.mass.mean = mean(Predator.mass),
      Predator.mass.median = median(Predator.mass),
      Prey.mass.mean = mean(Prey.mass),
      Prey.mass.median = median(Prey.mass),
      Predator.Prey.Size.Ratio = mean(Prey.mass/Predator.mass)
    )

pp_results
write.csv(pp_results, file = "../Results/PP_Results.csv")