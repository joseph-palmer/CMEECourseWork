#!/usr/bin/env python3
"""Python practicle - simple list comprehensions"""
__appname__ = "lc1.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Oct-2018"

## imports ##
import sys


birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# latin names
latin_names = [ln[0] for ln in birds]
common_names = [cn[1] for cn in birds]
mean_body_mass = [mbm[-1] for mbm in birds]

# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !). 
# set an empty list for each grouping
print (latin_names)
print (common_names)
print (mean_body_mass)

latin_names = []
common_names = []
mean_body_mass = []

# loop through the birds,
# append the positional elements to their respective lists
for bird in birds:
    latin_names.append(bird[0])
    common_names.append(bird[1])
    mean_body_mass.append(bird[-1])


print (latin_names)
print(common_names)
print(mean_body_mass)


# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS.
