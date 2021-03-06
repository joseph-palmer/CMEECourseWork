#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: applying the same function to rows/colums of a matrix

# clear environment
rm(list=ls())

# Load required packages #

###This is a test

## Build a random matrix
M <- matrix(rnorm(100), 10, 10)

## Take the mean of each row (the 1 means columns, 2 would mean columns.)
RowMeans <- apply(M, 1, mean)
print (RowMeans)

## The variance
RowVars <- apply(M, 1, var)
print (RowVars)

## By column
ColMeans <- apply(M, 2, mean)
print (ColMeans)
