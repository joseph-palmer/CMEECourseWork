#!/usr/bin/env python3
"""Timing a python function"""
__appname__ = "timeitme.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import timeit
from profileme import my_squares as my_squares_loops
from profileme2 import my_squares as my_squares_lc
from profileme import my_join as my_join_join
from profileme2 import my_join as my_join

# loops vs. list comprehensions: which is faster?
iters = 1000000
#%timeit my_squares_loops(iters)
#%timeit my_squares_lc(iters)

# loops vs. the join method for strings: which is faster?
mystring = "my string"
#%timeit my_join_join(iters, mystring)
#%timeit my_join(iters, mystring)
