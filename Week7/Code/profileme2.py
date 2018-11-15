#!/usr/bin/env python3
"""More efficient profiling in python"""
__appname__ = "profileme2.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys

def my_squares(iters):
    """my_squares - Makes a list of squared values of range itters.

    :param iters: int
    """
    out = [i ** 2 for i in range(iters)]
    return out

def my_join(iters, string):
    """my_join - Make a string of string repeated iters number of times

    :param iters: int
    :param string: str
    """
    out = ''
    for i in range(iters):
        out += ", " + string
    return out

def run_my_funcs(x,y):
    """run_my_funcs - Runs the functions my_squares and my_join

    :param x: int
    :param y: str
    """
    print(x,y)
    my_squares(x)
    my_join(x,y)
    return 0

run_my_funcs(10000000,"My string")
