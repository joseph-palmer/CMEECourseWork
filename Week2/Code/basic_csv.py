#!/usr/bin/env python3
"""Read a file containing:
  'Species', Infraorder', Family', Distribution, 'Body mass male (Kg)"""

__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys
import csv

# Read a file containing:
# 'Species', Infraorder', Family', Distribution, 'Body mass male (Kg)
f = open("../Data/testcsv.csv", "r")

csvread = csv.reader(f)
temp = []
for row in csvread:
    temp.append(tuple(row))
    print (row)
    print("The species is", row[0])
f.close()

# write a file containing only species name and body mass
f = open("../Data/testcsv.csv", "r")
g = open("../Results/bodymass.csv", "w")

csvread = csv.reader(f)
csvwrite = csv.writer(g)
for row in csvread:
    print (row)
    csvwrite.writerow([row[0], row[4]])

# close files
f.close()
g.close()

# show info about where saved.
print("\nOutput saved in", g)
