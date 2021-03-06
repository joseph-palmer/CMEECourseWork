#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: data wrangling with dpylr and tidyr

# clear environment
rm(list=ls())

# Load required packages #

# clear environment
rm(list=ls())

# Imports
require(dplyr)
require(tidyr)

############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F)) 

# header = true because we do have metadata headers
MyMetaData <- read.csv("../Data/PoundHillMetaData.csv",header = T, sep=";", stringsAsFactors = F)

############# Inspect the dataset ###############
# use tbl_df instead of head()
tbl_df(MyData)
dim(MyData)
#use glimpse instead of str()
glimpse(MyData)
fix(MyData) #you can also do this
fix(MyMetaData)

############# Transpose ###############
# To get those species into columns and treatments into rows 
MyData <- t(MyData) 
tbl_df(MyData)

############# Replace species absences with zeros ###############
MyData[MyData == ""] = 0

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!
colnames(TempData) <- MyData[1,] # assign column names from original data

############# Convert from wide to long format  ###############
# use gather piped into mutate to get the long format.
MyWrangledData <- TempData %>% gather(., Species, Count, -Cultivation, -Block, -Plot, -Quadrat) %>% mutate(Cultivation = as.factor(Cultivation),
                                                                                                           Block = as.factor(Block),
                                                                                                           Plot = as.factor(Plot),
                                                                                                           Quadrat = as.factor(Quadrat),
                                                                                                           Species = as.factor(Species),
                                                                                                           Count = as.numeric(Count))


head(MyWrangledData)

############# Start exploring the data (extend the script below)!  ###############

hist(MyWrangledData$Count)

hist(log(MyWrangledData$Count))

boxplot(MyWrangledData$Count ~ MyWrangledData$Cultivation)

plot(MyWrangledData$Count ~ MyWrangledData$Cultivation)




