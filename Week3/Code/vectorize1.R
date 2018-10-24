#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: An example of vectorizing and loops with a speed comparison

# clear environment
rm(list=ls())

# Load required packages #


rm(list=ls())

M <- matrix(runif(1000000),1000,1000)

SumAllElements <- function(M){
  Dimensions <- dim(M)
  Tot <- 0
  for (i in 1:Dimensions[1]){
    for (j in 1:Dimensions[2]){
      Tot <- Tot + M[i,j]
    }
  }
  return (Tot)
}

# Get execution time for loop
start_time <- Sys.time()
a = SumAllElements(M)
end_time <- Sys.time()
cat(paste("R SumAllElements function:", end_time - start_time, "\n"))

# Get execution time for vectorised
start_time <- Sys.time()
a = sum(M)
end_time <- Sys.time()
cat(paste("R vectorised sum function:", end_time - start_time, "\n"))




## This on my computer takes about 1 sec
#print("R SumAllElements function:")
#print(system.time(SumAllElements(M)))
## While this takes about 0.01 sec
#print("R vectorised sum function:")
#print(system.time(sum(M)))
