#!/usr/bin/env python3
"""Description of this program or app
[can be over several lines]"""

__appname__ = "[application name here]"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

#########################
# FILE INPUT
#########################
# open a file for reading
f = open("../Sandbox/test.txt", "r")

# use 'implicit' for loop:
# if the object is a file, python will cycle over the lines
for line in f:
    print (line)

# close the file
f.close()

# same example, skip blank lines
f = open("../Sandbox/test.txt", "r")
for line in f:
    if len(line.strip()) > 0:
        print (line)

f.close()

########################
# FILE OUTPUT
########################
# Save the elements of a list to a file
list_to_save = range(100)

f = open("../Sandbox/testout.txt", "w")
for i in list_to_save:
    f.write(str(i) + "\n") ## add a new line

f.close()

########################
# STORING OBJECTS
########################
# To save an object (even complex) for later use
my_dictionary = {"a key" : 10, "another key" : 11}

import pickle

f = open("../Sandbox/testp.p", "wb") # note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()

## Load the data again
f = open("../Sandbox/testp.p", "rb")
another_dictionary = pickle.load(f)
f.close()

print (another_dictionary)
