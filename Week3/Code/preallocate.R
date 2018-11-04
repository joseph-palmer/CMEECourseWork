#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: pre allocation in R - can be faster.

# clear environment
rm(list=ls())

# Load required packages #

testme <- function(){
 a <- 1
 for (i in 1:10) {
   a[i] = 10
 }
}

testme2 <- function(){
 a <- rep(NA, 10)
 for (i in 1:10){
   a[i] = 10
 }
}
 
# time the functions
 print(system.time(testme()))
 print(system.time(testme2()))

 