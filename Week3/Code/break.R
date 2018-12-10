#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: December 2018
# Desc: How to break out of loops in R.

# clear environment
rm(list=ls())

# Load required packages #

i <- 0 #Initialize i
while(i < Inf) {
  if (i == 20) {
    break 
  } # Break out of the while loop! 
  else { 
    cat("i equals " , i , " \n")
    i <- i + 1 # Update i
  }
}