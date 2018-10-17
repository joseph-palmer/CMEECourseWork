#!/usr/bin/env python3
"""Description of how to use __name__ == __main__"""

__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

if __name__ == "__main__":
    print ("This program is being run by itself")
else:
    print ("I am being imported from another module")
