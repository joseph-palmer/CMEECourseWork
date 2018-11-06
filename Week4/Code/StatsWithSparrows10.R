#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Stats with sparrows 10 practicle

# clear environment
rm(list=ls())

# Load required packages #

# load data
datapath = "../Data/SparrowSize.txt"
d <- read.table(datapath, header=T)

# have a look
plot(d$Mass~d$Tarsus, ylab="Mass (g)",xlab="Tarsus (mm)", pch=19, cex=0.4)

# line equation: yi = b0i + b1Xi + ei
d$Mass[1]
length(d$Mass)

plot(d$Mass~d$Tarsus,  ylab="Mass  (g)",  xlab="Tarsus  (mm)",  pch=19,  cex=0.4,  
     ylim=c(-5,38),  xlim=c(0,22)) 

# remove missing values for analysis by lm
d1 <- subset(d, d$Mass!="NA")
d2 <- subset(d1, d1$Tarsus!="NA") 	
length(d2$Tarsus)

# calculate lm
model1 <-lm(Mass~Tarsus, data=d2)
summary(model1) 	

# have a look at the distribution of residuals
hist(model1$residuals)
head(model1$residuals)

# standardize
d2$z.Tarsus<-scale(d2$Tarsus)
model3<-lm(Mass~z.Tarsus, data=d2)
summary(model3)

# make plot with mark at 0
plot(d2$Mass~d2$z.Tarsus, pch=19, cex=0.4) 	
abline(v = 0, lty = "dotted") 	

head(d) 	

d$Sex<-as.numeric(d$Sex)
par(mfrow = c(1, 2))
plot(d$Wing ~ d$Sex.1, ylab="Wing(mm)")
plot(d$Wing ~ d$Sex, xlab="Sex", xlim=c(-?‐0.1,1.1), ylab="")
abline(lm(d$Wing ~ d$Sex), lwd = 2) 
text(0.15, 76, "intercept") 
text(0.9, 77.5, "slope", col = "red")

d4<-subset(d, d$Wing!="NA")
m4<-lm(Wing~Sex, data=d4)
t4<-t.test(d4$Wing~d4$Sex, var.equal=TRUE)
summary(m4)
