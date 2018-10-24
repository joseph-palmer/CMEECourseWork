#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: ggplot practicle for data visualisation

# clear environment
rm(list=ls())

# Load required packages #

#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: 

# clear environment
rm(list=ls())

# Load required packages #

# clear workspace
rm(list=ls())

# load required packages
require(ggplot2)

# set data path
datapath = "../Data/EcolArchives-E089-51-D1.csv"

# load the data
MyDF <- read.csv(datapath)
head(MyDF)


p <- qplot(Prey.mass,
      Predator.mass,
      facets = Type.of.feeding.interaction ~.,
      data = MyDF,
      log = "xy",
      xlab = "Prey Mass in grams",
      ylab = "Predator mass in grams",
      colour = Predator.lifestage)
q = p + geom_smooth(method = "lm", fullrange = TRUE) + geom_point(shape = 9) + theme_bw() + theme(legend.position="bottom")
q

# ask francis
# smooth_vals = predict(lm(log(Predator.mass)~log(Prey.mass)), MyDF)


