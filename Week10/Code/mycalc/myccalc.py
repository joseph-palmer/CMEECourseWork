#!/usr/bin/env python3
"""Shows how to call C code from python"""
__appname__ = "myccalc.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Dec-2018"

## imports ##
import os
import ctypes

# Load the C library into python - needs the full path for some reason!
so_filepath = "{}/libmycalc.so".format(os.getcwd())
ctypes.cdll.LoadLibrary(so_filepath)
myccalc = ctypes.CDLL(so_filepath)

# make a simpler name for the mycalc.add_floats
add_floats = myccalc.add_floats

# tell python what variables this function takes & returns
add_floats.argtypes = [ctypes.c_float, ctypes.c_float]
add_floats.restype = ctypes.c_float

# the function can now be used
x = 1.2
y = 3.3
a = add_floats(x, y)
print("The sum of %.1f and %.1f is %.1f" % (x, y, a))

# we can do the same for others
sf = myccalc.subtract_floats
sf.argtypes = [ctypes.c_float, ctypes.c_float]
sf.restype = ctypes.c_float
b = sf(y, x)
print("Subtracting %.1f from %.1f is %.1f" % (x, y, b))
