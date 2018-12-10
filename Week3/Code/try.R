#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Run a simulation that involves sampling from a population

# clear environment
rm(list=ls())

# Load required packages #

x <- rnorm(50) # generate your population
doit <- function(x){
  x <- sample(x, replace = TRUE)
  if(length(unique(x)) > 30) { # only take mean in sample was sufficient
    print(paste("Mean of this sample was: ", as.character(mean(x))))
  } else {
    stop("Couldn't calculate mean: too few unique points!")
  }
}

# run 100 iterations using vectorization.
result <-lapply(1:100, function(i) try(doit(x)))

# or use a for loop
result <- vector("list", 100) # Initializa
for(i in 1:100){
  result[[i]] <- try(doit(x))
}

result
