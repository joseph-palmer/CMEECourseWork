#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Basic R recap

# clear environment
rm(list=ls())

# Load required packages #

getwd() 	

# setwd("~/home/CMEE/CMEECourseWork/Week4/Code") 

2*2 +1
2*(2+1) 	
12/2^3 	
(12/2)^3 

x <- 5 	
x

y <- 2

x2 <- x^2
a <- x2 + x

y2 <- y^2
z2 <- x2 + y2

z <- sqrt(z2)
print(z)

3>2
3 >= 2
4<2

myNumericVector  <- c(1.3,2.5,1.9,3.4,5.6,1.4,3.1,2.9) 	

myCharacterVector  <- c("low","low","low","low","high","high","high","high") 	

myLogicalVector  <- c(TRUE,TRUE,FALSE,FALSE,TRUE,TRUE,FALSE,FALSE)


str(myNumericVector)
str(myLogicalVector) 	

myMixedVector  <- c(1,  TRUE,  FALSE,  3,  "help",  1.2,  TRUE,  "notwhatIplanned") 	

str(myMixedVector) 


install.packages("lme4") 	

library(lme4) 	

require(lme4) 	

sqrt(4);  4^0.5;  log(0);  log(1);  log(10);  log(Inf) 	

exp(1) 	

pi

rm(list=ls())


# read in data table
d<- read.table("../LectureMaterial/HandOutsandData_18/SparrowSize.txt",  header=TRUE)
str(d)

