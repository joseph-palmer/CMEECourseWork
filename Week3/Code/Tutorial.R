#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Another tutorial for R based on the jupyter notebook

# clear environment
rm(list=ls())

# Load required packages #

a <- 4
a # display it
a_squared <- a * a
sqrt(a_squared)
v <- c(1, 2, 3, 4) # Build a vector

is.vector(v) # is it a vector? (yes)
mean(v) # mean
var(v) # variance
median(v) # medial
sum(v) # sum all the elements
prod(v + 1) # multiply
length(v)

# variable names and tabbing
wing.width.cm <- 1.2 # using dot notation
wing.length.cm <- c(4.7, 5.2, 4.8) # c means concatonate
x <- (1 + (2 * 3))
2 + (2*3)

# variable types
v <- TRUE
class(v)
v <- 3.2
class(v)
v <- 2L
class(v)
v <- "A string"
class(v)
b <- NA
is.na(b)
b <- 0/0
b
is.nan(b)
b <- 5/0
b
is.nan(b)
is.infinite(b)
is.finite(0/0)

# type conversions and special values.
as.integer(3.1)
as.numeric(4)
as.roman(155)
as.character(155)
as.logical(5)
as.logical(0)
1E4
1e4
5e-2
1e4^2
1 / 3 / 1e8

# Data types and structures (see notes as already covered)
v1 <- c(0.02, 0.5, 1)
v2 <- c("a", "bc", "def", "ghij")
v3 <- c(TRUE, TRUE, FALSE)
v1;v2;v3

# R vectors can only store data of a single type, which is why 1 is put as 1.0 (a float)

# Matrices and arrays - a 2 dimensional vector and an array can store date in more than 2 dimentions
mat1 <- matrix(1:25, 5, 5)
mat1 <- matrix(1:25, 5, 5, byrow = TRUE)
mat1
dim(mat1) # get the size of the matrix

# to make an array of 2 5X5 matrices containing integers 1--50.
arr1 <- array(1:50, c(5, 5, 2))
arr1[,,1]
arr1[,,2]

# Matracies and arrays have to be part of a homogenous type and R will convert those that arnt. so be aware.

# Vectorization






