#!/usr/bin/env Rscript
# Author: Joseph Palmer <Joseph.Palmer18@imperial.ac.uk>
# Date: October 2018
# Desc: calculates tree height given angle and distance from base of tree

# clear environment
rm(list=ls())

# Load required packages #

# Header.
########################################################################
#                               Functions
########################################################################
# define function TreeHeight.R
# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
# height = distance * tan(radians)
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
# OUTPUT
# The heights of the tree, same units as "distance"
TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  print(paste("Tree height is:", height))
  
  return (height)
}

# Test TreeHeight
TreeHeight(37, 40)

###########################################################################
#                             Script
###########################################################################

# Read in trees.csv
trees_path = "../Data/trees.csv"
trees <- read.csv(trees_path, header = TRUE)

# make a new column in trees with the value of the output of the TreeHeight function.
trees$Tree.Height.m <- TreeHeight(trees$Angle.degrees, trees$Distance.m)

print(head(trees))









