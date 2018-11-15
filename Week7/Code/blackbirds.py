#!/usr/bin/env python3
"""Regex blackbirds practicle """
__appname__ = "blackbirds.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import re

# Read the file
with open("../Data/blackbirds.txt") as r:
    text = r.read()

# remove \t\n and put a space in:
text = text.replace('\t',' ').replace('\n',' ')

# note that there are "strange characters" (these are accents and
# non-ascii symbols) because we don't care for them, first transform
# to ASCII:
text = text.encode('ascii', 'ignore').decode()

# Now extend this script so that it captures the Kingdom, 
# Phylum and Species name for each species and prints it out to screen neatly.
# Hint: you may want to use re.findall(my_reg, text)...
# Keep in mind that there are multiple ways to skin this cat! 
# Your solution may involve multiple regular expression calls (easier!), or a single one (harder!)

# find the kingdom, phylum and speces and return the values into a tuple
regex = r"Kingdom\s(\w+).+?Phylum\s(\w+).+?Species\s(\w+\s\w+)"
match = re.findall(regex, text)

# make a header row for the display string
header = "Kingdom, Phylum, Species\n"

# make a display string extracting the data from text and adding to the header
# string
display_string = header + "\n".join([", ".join(i) for i in match])

# print the information
print("--- Output of blackbirds.py ---")
print(display_string)

# --- RE breakdown
# Kingdom\s(\w+) -> This asks for a match of Kingdom folowed by a space and
# then any alpha character (the pluss means to the end, so \w+ means get a word
# the () around it means return just this bit to the tuple.
# The other bits for phylum and species are along the same lines.
