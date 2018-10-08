#!/usr/bin/env python3
""" Demonstration of global and local variables"""
__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

_a_global = 10

def a_function():
    _a_global = 5
    _a_local = 4
    print ("Inside the function the value is ", _a_global)
    print ("Inside a function the local is ", _a_local)

a_function()

print ("Outside the function, the value is ", _a_global)


## Now try this

_a_global = 10

def a_function():
    global _a_global
    _a_global = 5
    _a_local = 4
    print ("Inside the function, the value is ", _a_global)
    print ("Inside the function, the value is ", _a_local)
    return None

a_function()
print ("Outside the function, the value is", _a_global)
