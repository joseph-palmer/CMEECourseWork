#!/usr/bin/env python3
"""Demonstration of the sys.argv module"""

__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))
