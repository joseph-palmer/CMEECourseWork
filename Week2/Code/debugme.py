#!/usr/bin/env python3
"""Example of how to debug using pdb"""
__appname__ = "debugme.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Oct-2018"

## imports ##
import sys

def createabug(x):
    """createabug - an example function with a bug.

    :param x: int
    """
    y = x**4
    z = 1 
    y = y/z
    return y

createabug(25)
