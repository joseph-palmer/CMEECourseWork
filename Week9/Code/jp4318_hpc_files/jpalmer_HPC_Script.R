#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: November 2018
# Desc: The R file for running on the HPC cluster

## clear environment and turn graphics off #
rm(list=ls())
graphics.off()

# Load Functions #

initialise_min <- function(size){
  # Generate an alternative initial state for the simulation of a certain size with minimum number of
  # possible species
  return(array(1, size))
}

species_abundance <- function(community) {
  # retuns species abundance for all species in the system
  vals = sort(table(community), decreasing = TRUE)
  return(as.numeric(vals))
}

octaves <- function(abundance) {
  # places the abundances of species into bis where bin = log 2 to power abundance.
  return(tabulate(floor(logb(abundance, base = 2) + 1)))
}

neutral_generation_speciation <- function(community, v){
  # simulate several neutral steps over a generation with speciation
  # (returns the state of the community after x number of generations)
  # complete generation = number of individuals in the community divided by 2
  generation_time = ceiling(length(community) / 2)
  for (i in 1:generation_time) {
    community = neutral_step_speciation(community, v)
  }
  return(community)
}

species_richness <- function(community){
  # measures the species richness of a system
  return(length(unique(community)))
}

choose_two <- function(x){
  # chooses a random number from uniform distribution between 1 and x
  # choose a second random number as above but not equal to the previous one
  # return the numbers as a vector of length 2 *check again
  y = sample(1:x, 2)
  return(c(y[1], y[2]))
}

neutral_step_speciation <- function(community, v) {
  # performs a neutral step but with a random speciaton event given as v.
  remove_replace =  choose_two(length(community))
  if (v <= runif(1)){
    community[remove_replace[1]] = community[remove_replace[2]]
  } else {
    community[remove_replace[1]] =  max(community) + 1
  }
  return(community)
}

cluster_run <- function(speciation_rate, size, wall_time, interval_rich, interval_oct, burn_in_generations, output_file_name) {
  # function to run simulations for a set amount of time, returning species richness at burn in and abundace throughout.
  # ste the community with minimal diversity
  # change wall time from miinutes to seconds
  wall_time = wall_time * 60
  community = initialise_min(size)
  # run neautral generations over a specified period of time (counter records how many simulations we have done)
  total_elapsed_time = 0
  counter = 0
  species_richness_burnin = c()
  species_abundance_octaves = c()
  start = as.numeric(proc.time()[3])
  while (total_elapsed_time < wall_time) {
    # start recording the time taken to run the simulations
    counter = counter + 1
    # run the simulation
    community = neutral_generation_speciation(community, speciation_rate)
    # record species abundance at set intervals
    if (counter %% interval_oct == 0) {
      ans = octaves(species_abundance(community))
      species_abundance_octaves = append(species_abundance_octaves, list(octaves(species_abundance(community))))
    }
    # record species richness up to burn in generations at set intervals
    if ((counter <= burn_in_generations) && (counter %% interval_rich == 0)) {
      species_richness_burnin = append(species_richness_burnin, species_richness(community), length(species_richness_burnin))
    }
    # add the time taken so far to the elapsed time the while loop evaluates
    end = as.numeric(proc.time()[3])
    total_elapsed_time = end - start
  }
  # save the simulation output to r data file
  save(species_richness_burnin,
       species_abundance_octaves,
       # time ran on simulation
       total_elapsed_time,
       # state f community at end of simulation
       community,
       # input parameters
       speciation_rate,
       size,
       wall_time,
       interval_rich,
       interval_oct,
       burn_in_generations,
       file = output_file_name)
  return(0)
}

# run code #
# set the iter number as the job number of the cluster
iter <- as.numeric(Sys.getenv("PBS_ARRAY_INDEX"))
runtime = 11.5 * 60

# if code not being run from cluster, iter = NA. set a random iter number
if (is.na(iter)) {
  iter <- sample(100, 1)
  runtime = 0.05
}

# set random number seed to garuntee simulations are not repeated
set.seed(iter)

# set different values for community size
val = (iter %% 4) + 1
J = switch(val,
           5000,
           500,
           1000,
           2500)

# create file name to sore in results
savename = paste0("JP4318_Neutral_Simulations_", iter, ".rda")

# run the cluster function
cluster_run(speciation_rate = 0.002125,
            size = J,
            wall_time = runtime,
            interval_rich = 1,
            interval_oct = (J / 10),
            burn_in_generations = (8 * J),
            output_file_name = savename)

