#!/usr/bin/env python3
"""Python practicles - More compex list comprehension"""
__appname__ = "lc2.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Oct-2018"

## imports ##
import sys




# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )

# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
greater_than_100 = ([x for x in rainfall if x[-1] > 100])

# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 
less_than_50 = ([x for x in rainfall if x[-1] < 50])

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

# set empty lists to contain the
greater_than_100 = []
less_than_50 = []

# loop through the rainfall list
# if rainfall is greater than 100 or less than 50 put in their respective lists
for x in rainfall:
    if x[-1] > 100:
        greater_than_100.append(x)
    elif x[-1] < 50:
        less_than_50


# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
