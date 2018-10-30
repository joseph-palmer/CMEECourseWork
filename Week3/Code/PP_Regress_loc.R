#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: ggplot practicle extra credit - adding Location to the subset lm

# clear environment
rm(list=ls())

# Load required packages #
require(dplyr)
require(plyr)

# set data path
datapath = "../Data/EcolArchives-E089-51-D1.csv"

# load the data
MyDF <- read.csv(datapath)
head(MyDF)

# solve mass unit problem - convert those in mg to g.
MyDF <- MyDF %>% 
            rowwise() %>% 
                    mutate(Prey.mass = ifelse(Prey.mass.unit == "mg",
                                              Prey.mass / 1000,
                                              Prey.mass))

# use dlpyl to group by feeding type and predator lifestage to get lm.
grouped_lm <- dlply(MyDF,.(Type.of.feeding.interaction,
                           Predator.lifestage,
                           Location),
                    function(x) lm(Predator.mass~Prey.mass, data = x))

# extract stats from grouped_ml
out <- ldply(grouped_lm, function(x){
  intercept <- summary(x)$coefficients[1]
  slope <- summary(x)$coefficients[2]
  p_val <- summary(x)$coefficients[8]
  r2 <- summary(x)$r.squared
  data.frame(slope, intercept, r2, p_val)
})

# extract f-statistic
Fstat <- ldply(grouped_lm, function(x) summary(x)$fstatistic[1])
out <- merge(out, Fstat, by = c("Type.of.feeding.interaction",
                                "Predator.lifestage",
                                "Location"), all = T)

# rename columns
names(out)[8] <- "F.Statistic"
names(out)[7] <- "P.Value"

# write the results to a file (exclude the row names they are not needed)
results_path = "../Results/PP_Regress_loc_results.csv"
write.csv(out, results_path, row.names = F, quote = F)