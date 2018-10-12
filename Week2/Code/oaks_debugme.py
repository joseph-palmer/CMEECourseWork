#!/usr/bin/env python3
"""Finds the oaks from a csv file."""
__appname__ = "oaks_debugme.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Oct-2018"

## imports ##
import sys
import csv
import pdb
import doctest

#Define function - put debug stuff inside.
def is_an_oak(name):
    """is_an_oak - checks if name is an oak.

    :param name: Str
    """
    """ Returns True if name is starts with 'quercus'     
    >>> is_an_oak('Quercuss sylvatica')
    False
    >>> is_an_oak("Fagus sylvatica")
    False
    >>> is_an_oak("Quercus test")
    True
    """
    return name.lower().split(" ")[0] == "quercus"

def main(argv):
    """main - The main program.

    :param argv: command line arguments.
    """
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Results/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()
    for row in taxa:
        # stop the genus species row from printing but make sure it writes
        # to file.
        if row[0] == "Genus":
            csvwrite.writerow(row)
            continue
        print(row)
        print ("The genus is: ") 
        print(row[0])
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])

    doctest.testmod()

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)
