#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Describing distributions.

# clear environment
rm(list=ls())

# Load required packages # 

# read in the sparrow data
d<-read.table("../LectureMaterial/HandOutsandData_18/SparrowSize.txt", header=TRUE) 	
str(d)

# have a look
head(d)
names(d)

# check distribution
hist(d$Tarsus)

# get some basic stats
mean(d$Tarsus, na.rm = TRUE)
median(d$Tarsus, na.rm = TRUE) 	

# some others, g
par(mfrow = c(2, 2))
hist(d$Tarsus, breaks = 3, col = "grey")
hist(d$Tarsus, breaks = 10, col = "grey")
hist(d$Tarsus, breaks = 30, col = "grey")
hist(d$Tarsus, breaks = 100, col = "grey")


# have a look at the mode
require(modeest)
mlv(d$Tarsus)

# handle missing values
d2<-subset(d, d$Tarsus!="NA") 	
length(d$Tarsus)

# look at mode
mlv(d2$Tarsus)

# get range and variance for spread
range(d$Tarsus, na.rm = TRUE)
var(d$Tarsus, na.rm = TRUE)

# Equation for variance
sum((d2$Tarsus - mean(d2$Tarsus))^2)/(length(d2$Tarsus) - 1)

# bill length
mean(d$Bill, na.rm = TRUE)
svar(d$Bill, na.rm = TRUE)
sd(d$Bill, na.rm = TRUE)

# body mass
mean(d$Mass, na.rm = TRUE)
var(d$Mass, na.rm = TRUE)
sd(d$Mass, na.rm = TRUE)

# wing length
mean(d$Wing, na.rm = TRUE)
var(d$Wing, na.rm = TRUE)
sd(d$Wing, na.rm = TRUE)

# to get z transformed data, devide	the	deviation	from	the	mean	by	the	standard	deviation
zTarsus <- (d2$Tarsus - mean(d2$Tarsus))/sd(d2$Tarsus)
var(zTarsus)
sd(zTarsus)
hist(zTarsus)

# we can make any normal distribution using r
set.seed(123)
znormal <- rnorm(1e+06)
hist(znormal, breaks = 100)
summary(znormal)
# gives	the	2.5%	and	97.5%	quantiles	from	the	corresponding	
# probability	distribution.	Both	bracket	95%	of	all	values	in	the	distribution.	And	pnorm	gets	
# us	the	corresponding	probabilities.	
qnorm(c(0.025, 0.975))
pnorm(.Last.value)

# density
par(mfrow = c(1, 2)) 	
hist(znormal, breaks = 100) 	
abline(v = qnorm(c(0.25, 0.5, 0.75)), lwd = 2) 	
abline(v = qnorm(c(0.025, 0.975)), lwd = 2, lty = "dashed") 	
plot(density(znormal)) 	
abline(v = qnorm(c(0.25, 0.5, 0.75)), col = "gray") 	
abline(v = qnorm(c(0.025, 0.975)), lty = "dotted", col = "black") 	
abline(h = 0, lwd = 3, col = "blue") 	
text(2, 0.3, "1.96", col = "red", adj = 0) 	
text(-2, 0.3, "-1.96", col = "red", adj = 1) 	
boxplot(d$Tarsus~d$Sex.1, col = c("red", "blue"), ylab="Tarsus length (mm)")

