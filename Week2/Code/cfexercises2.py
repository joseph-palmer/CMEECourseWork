#!/usr/bin/env python3
"""Description of this program or app
[can be over several lines]"""

__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

def foo1(x):
    return x ** 0.5

def foo2(x, y):
    if x > y:
        return x
    return y

def foo3(x, y, z):
    if x < y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]


def foo4(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo5(x):
    if x == 1:
        return 1
    return x * foo5(x-1)


foo5(10)

def main(argv):
    print (foo1(12))
    print (foo2(10, 11))
    print (foo2(15, 13))
    print (foo3(10, 11, 12))
    print (foo3(12, 11, 10))
    print (foo4(15))
    print (foo5(1))
    print (foo5(2))
    return 0
if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)






