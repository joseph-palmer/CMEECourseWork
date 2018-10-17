#!/usr/bin/env python3
"""A boilerplate script in python"""

__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

## constants ##



# functions ##
def main(argv):
    """main - The main entry point of the program - 
    contains code to be executed.

    :param argv: command line arguments.
    """
    print("This is a boilerplate")
    return 0


if __name__ == "__main__":
    "Makes sure the 'main' function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)
