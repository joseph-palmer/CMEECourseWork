#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: Stats with sparrows 13, 14 and 15 practicle

# clear environment
rm(list=ls())

# Load required packages #

# load data
datapath = "../Data/SparrowSize.txt"
d <- read.table(datapath, header=T)

cov(d$Tarsus,d$Mass, use = "complete.obs")
cor(d$Tarsus,d$Mass, use = "complete.obs")
d$Tarsus <- d$Tarsus/10
cov(d$Tarsus,d$Mass, use = "complete.obs")
cor(d$Tarsus,d$Mass, use = "complete.obs")

# handout 13
d1 <- subset(d, d$Wing!="NA")
summary(d1$Wing)
hist(d1$Wing)

# make model using lm
model1 <- lm(Wing~Sex.1,data=d1)
summary(model1)
boxplot(d1$Wing~d1$Sex.1, ylab="Wing length (mm)")
anova(model1)
t.test(d1$Wing~d1$Sex.1, var.equal=TRUE)

# linear model with wing length as response and BirdID as a factor
require(dplyr)
tbl_df(d1)
glimpse(d1)

# get a correlation to demonstrate pipes
d$Mass  %>%  cor.test(d$Tarsus,  na.rm=TRUE)

d1 %>%
  group_by(BirdID)  %>%
  summarise(count=length(BirdID))

model3 <- lm(Wing~as.factor(BirdID), data=d1)
anova(model3)

m2 <- lm(d$Mass~as.factor(d$Year))
anova(m2)
summary(m2)

# practicle 13 #
d <- read.table(datapath, header=T)
d1<-subset(d,  d$Wing!="NA")
model3<-lm(Wing~as.factor(BirdID),  data=d1)
anova(model3)




