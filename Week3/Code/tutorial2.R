
# clear environment
rm(list=ls())

# load the data
datapath = "../Data/PoundHillData.csv"
metadatapath = "../Data/PoundHillMetaData.csv"
MyData <- as.matrix(read.csv(datapath, header = F, stringsAsFactors = F))
MyMetaData <- read.csv(metadatapath, header = T, sep = ";", stringsAsFactors = F)

# check the data class and have a look
class(MyData)
head(MyData)

# look at metadata
MyMetaData

# set the absent values as 0. can do for this, but not all datasets as it may not be true
MyData[MyData == ""] = 0

# data is in wide format, need to change to long format.
# transpose it
MyData <- t(MyData)
head(MyData)

# there are no columns names, the name are in the first line of the matrix
colnames(MyData)

# all data types in the matrix are strings as they can only hold one type, need to make it into a dataframe
TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F)
head(TempData)

# assign column names from original data, get dir of row names as not needed
colnames(TempData) <- MyData[1,]
rownames(TempData) <- NULL
head(TempData)

# 'melt' the data into long format (this groups the data into a count)
require(reshape2)
MyWrangledData <- melt(TempData, id=c("Cultivation", "Block", "Plot", "Quadrat"), variable.name = "Species", value.name = "Count")
head(MyWrangledData); tail(MyWrangledData)

# asign column types manually - make sure R is not assuming for you!
MyWrangledData[, "Cultivation"] <- as.factor(MyWrangledData[, "Cultivation"])
MyWrangledData[, "Block"] <- as.factor(MyWrangledData[, "Block"])
MyWrangledData[, "Plot"] <- as.factor(MyWrangledData[, "Plot"])
MyWrangledData[, "Quadrat"] <- as.factor(MyWrangledData[, "Quadrat"])
MyWrangledData[, "Count"] <- as.integer(MyWrangledData[, "Count"])
str(MyWrangledData)
MyWrangledData


# dplyr and tydr
require(dplyr)
dplyr::glimpse(MyWrangledData)
dplyr::filter(MyWrangledData, Count > 100)
dplyr::slice(MyWrangledData, 10:15)
