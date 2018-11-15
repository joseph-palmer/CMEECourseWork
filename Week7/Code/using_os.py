#!/usr/bin/env python3
"""Practicle - using os problem 1"""
__appname__ = "using_os.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import re

# Use the subprocess.os module to get a list of files and  directories 
# in your ubuntu home directory 

# Hint: look in subprocess.os and/or subprocess.os.path and/or 
# subprocess.os.walk for helpful functions
import subprocess

#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:

# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithC = []

# Use a for loop to walk through the home directory.
for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir:
        b = re.match(r"^C", i)
        if b != None:
            FilesDirsStartingWithC.append(i)
    for i in files:
        c = re.match(r"^C", i)
        if c != None:
            FilesDirsStartingWithC.append(i)

#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'

# Type your code here:

# create a list to store the results
FilesDirsStartingWithCorC = []

# Use a for loop to walk through the home directory.
for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir:
        b = re.match(r"^[Cc]", i)
        if b != None:
            FilesDirsStartingWithCorC.append(i)
    for i in files:
        c = re.match(r"^[Cc]", i)
        if c != None:
            FilesDirsStartingWithCorC.append(i)

#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 

# Type your code here:

# create a list to store results
DirsStartingWithCorC = []

# Use a for loop to walk through the home directory.
for (dir, subdir, files) in subprocess.os.walk(home):
    for i in subdir:
        b = re.match(r"^[Cc]", i)
        if b != None:
            DirsStartingWithCorC.append(i)
print("Files and Dirs Starting with C: {}".format(len(FilesDirsStartingWithC)))
print("Files and Dirs Starting with C or c: {}".format(len(FilesDirsStartingWithCorC)))
print("Dirs Starting with C or c: {}".format(len(DirsStartingWithCorC)))
