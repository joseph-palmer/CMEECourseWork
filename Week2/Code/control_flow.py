#!/usr/bin/env python3
"""More function examples and calling them in name==main"""

__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

## constants ##



# functions ##

def even_or_odd(x=0): # if not specified, x should take value 0.
    """even_or_odd - Find whether x is even of odd.

    :param x: int
    """
    if x % 2 == 0: #The conditional if
        return "%d is Even!" % x
    return "%d is Odd!" % x

def largest_divisor_five(x=120):
    """largest_divisor_five - Find which is the largest deviser of x 
    among 2,3,4,5

    :param x: int
    """
    largest = 0
    if x % 5 == 0:
        largest = 5
    elif x % 4 == 0: #means "else, if"
        largest = 4
    elif x % 3 == 0:
        largest = 3
    elif x % 2 == 0:
        largest = 2
    else: # When all other (if, elif) conditions are not met
        return "No divisor found for %d!" % x # Each function can return a value or a variable.
    return "The largest divisor of %d is %d" % (x, largest)

def is_prime(x=70):
    """is_prime - Find whether an integer is a prime.

    :param x: int
    """
    for i in range(2, x): #  "range" returns a sequence of integers
        if x % i == 0:
          print("%d is not a prime: %d is a divisor" % (x, i)) #Print formatted text "%d %s %f %e" % (20,"30",0.0003,0.00003)

          return False
    print ("%d is a prime!" % x)
    return True 

def find_all_primes(x=22):
    """find_all_primes - find all primes up to x

    :param x: int
    """
    allprimes = []
    for i in range(2, x + 1):
      if is_prime(i):
        allprimes.append(i)
    print("There are %d primes between 2 and %d" % (len(allprimes), x))
    return allprimes


def main(argv):
    """main - Main entry point of the program.

    :param argv: command line arguments.
    """
    """Main entry point of the program"""
    print (even_or_odd(22))
    print (even_or_odd(33))
    print(largest_divisor_five(120))
    print (largest_divisor_five(121))
    print(is_prime(60))
    print(is_prime(59))
    print(find_all_primes(100))
    return 0


if __name__ == "__main__":
    "Makes sure the 'main' function is called from the command line"""
    status = main(sys.argv)
    sys.exit(status)
