#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Demonstration of functions

# clear environment
rm(list=ls())

# Load required packages #

MyFunction <- function(Arg1, Arg2){
  # Statements involving Arg1 and Arg2:
  print(paste("Argument", as.character(Arg1), "is a", class(Arg1)))
  print(paste("Argument", as.character(Arg2), "is a", class(Arg2)))
  
  return(c(Arg1, Arg2))
}

MyFunction(1,2) # To test the function with ints
MyFunction("Riki", "Tiki") # to test the function with strings.