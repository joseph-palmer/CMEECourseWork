# Takes a file from command line and calculates tree heights.
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
  #print(paste("Tree height is:", height))
  
  return (height)
}

# Test TreeHeight
# TreeHeight(37, 40)

###########################################################################
#                             Script
###########################################################################
# Read in file from the command line. 
# trailing only gets just the arguments passed after the script! (s)
inpath = commandArgs(trailingOnly = TRUE)
if (length(inpath) <1){
  print("No file provided as input! Using ../Data/trees.csv as default.")
  inpath = "../Data/trees.csv"
} else if (length(inpath) >1){
  print(paste("Script takes only 1 command line argument,", length(inpath), "given. Using the first argument as the file.", inpath[1]))
  inpath = inpath[1]
} else {
  print(paste("Reading from", inpath, sep = " "))
}

# strip of the file path and extension to get just the filename.
input = unlist(strsplit(inpath, "/"))[-1][-1]
output = gsub(".csv", "", input)

# format the input name as part of the output path to save to.
outpath = paste0("../Results/", output, "_treeheights.csv")

# read in the command line argument.
trees <- read.csv(inpath, header = TRUE)

# make a new column in trees with the value of the output of the TreeHeight function.
print("Calculating Tree heights...")
trees$Tree.Height.m <- TreeHeight(trees$Angle.degrees, trees$Distance.m)

print(paste("Analysis complete. File saved as ", outpath, sep = ""))
write.csv(trees, outpath, col.names = TRUE, row.names = FALSE)