#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: November 2018
# Desc: The R file for interpoting the HPC output
# clear environment
rm(list=ls())

# Load required packages #
sum_vect <- function(x, y) {
  # sums 2 vectors, makes them the same length by adding zeros to the smallest vector first
  len = max(c(length(x), length(y)))
  x = c(x, rep(0, len - length(x)))
  y = c(y, rep(0, len - length(y)))
  return(x + y)
}

# load the data (all files with extention .rda)
datafiles = list.files(pattern = "*.rda")

# work out what datafiles correspond to what size
size_500 = c()
size_1000 = c()
size_2500 = c()
for(i in datafiles) {
  load(i)
  switch(as.character(size),
           "500" = {size_500 = append(size_500, i)},
           "1000" = {size_1000 = append(size_1000, i)},
           "2500" = {size_2500  = append(size_2500, i)})
}

# set partition for the bar plots produced
par(mfrow=c(2,2), oma=c(0,0,2,0))

# loop through each size, then loop through each file of that size
# get the octaves average for each file, then sum these averages and take an average
# for each size, then plot these in a bar plot 
for (files in c(size_500, size_1000, size_2500)){
  simulation_octaves = c()
  for (i in files) {
    load(i)
    octaves_sum = c()
    burnin_endpoint = burn_in_generations / interval_oct + 2
    for (data in species_abundance_octaves[burnin_endpoint:length(species_abundance_octaves)]) {
      octaves_sum = sum_vect(octaves_sum, data)
    }
    avg_octaves = unlist(lapply(octaves_sum, function(n) n/(length(species_abundance_octaves) - burnin_endpoint)))
    simulation_octaves = sum_vect(simulation_octaves, avg_octaves)
  }
  avg_simulation_octaves = unlist(lapply(simulation_octaves, function(n) n/length(files)))
  barplot(avg_simulation_octaves,
          main = paste("Size =", size),
          xlab = "Octaves",
          ylab = "Average Species Abundance")
  title(paste("Species Richness", speciation_rate), outer = T)
}







