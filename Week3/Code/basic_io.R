#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: A simple script to illustrate R input output.

# clear environment
rm(list=ls())

# Load required packages #

# Read in the data in csv format with headers
MyData <- read.csv("../Data/trees.csv", header = TRUE)

# Write the data to the result directory.
write.csv(MyData, "../Results/MyData.csv")

# Append to the results file
write.table(MyData[1,], file = "../Results/MyData.csv", append = TRUE)

# write the row names
write.csv(MyData, "../Results/MyData.csv", row.names = TRUE)

# ignore the column names
write.table(MyData, "../Results/MyData.csv", col.names = FALSE)
