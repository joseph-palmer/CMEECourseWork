#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Describing distributions

# clear environment
rm(list=ls())

# Load required packages #

# read in the sparrow data, subset for non na values
d <- read.table("../Data/SparrowSize.txt", header=TRUE) 	
d1 <- subset(d,  d$Tarsus!="NA")
d2 <- subset(d, d$Bill != "NA")

#descriptive stats
summary(d1)
var(d1)

# work out standard error
seTarsus <- sqrt(var(d1$Tarsus)/length(d1$Tarsus))
seBL <- sqrt(var(d2$Bill)/length(d2$Bill)) 	

# subset for 2001
d12001<- subset(d1,  d1$Year==2001) 	
seTarsus2001<-sqrt(var(d12001$Bill)/length(d12001$Bill))
seTarsus2001 
seWL2001<-sqrt(var(d12001$Wing)/length(d12001$Wing))
seWL2001


# another way of working out standard error
require("plotrix")
std.error(d1$Bill)

# 95% CI
mean(d2$Bill) + (1.96 * std.error(d2$Bill))


# t test
d1 <- subset(d, d$Year==2001)
t.test(d1$Tarsus, mu=18.5, na.rm=TRUE)

# testing if two means are different. Testing if the differenc is equal to testing for 0.
t.test(d1$Tarsus~d1$Sex, na.rm=TRUE)


# exercise 5
d1 <- subset(d, d$Year==2001)
Total_mean = mean(d$Wing, na.rm = TRUE)
t.test(d1$Wing, mu=Total_mean, na.rm=TRUE)
# No significant difference in wing length between 2001 and all data mean. 

t.test(d1$Wing~d1$Sex, na.rm=TRUE)
# Significant difference between male and female wing lengths in 2001.

t.test(d$Wing~d$Sex, na.rm=TRUE)
# significant difference between male and female wing lengths in full dataset.

t.test(d$Tarsus~d$Sex, na.rm=TRUE)


