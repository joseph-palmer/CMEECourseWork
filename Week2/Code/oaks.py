#!/usr/bin/env python3
"""Description of this program or app
[can be over several lines]"""

__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

taxa = [ 'Quercus robur',
        'Fraxinus excelsior',
        'Pinus sylvestris',
        'Quercus cerris',
        'Quercus petraea']

def is_an_oak(name):
    return name.lower().startswith("quercus ")

## Using for loops
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species)
print(oaks_loops)

## using list comprehensions
oaks_lc = set([species for species in taxa if is_an_oak(species)])
print (oaks_lc)

## Get names in UPPER CASE using loop
oaks_loops = set()
for species in taxa:
    if is_an_oak(species):
        oaks_loops.add(species.upper())
print(oaks_loops)

## Get names in upper case using list comprehensions
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)])

