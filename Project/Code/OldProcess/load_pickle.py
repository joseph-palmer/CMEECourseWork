#!/usr/bin/env python3
"""Loads pickled simulation results and allows for interavtive viewing"""
__appname__ = "load_pickle.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import sys, os
import numpy as np
import argparse
import pickle

# set argument parser
description = "View sumexp pickle object."
parser = argparse.ArgumentParser(description = description)

# add arguments
parser.add_argument("pickle",
                    type = str,
                    help = "Path to pickle file.")

args = parser.parse_args()

with open(args.pickle, "rb") as p:
    storage = pickle.load(p)

def cycle_models(vals, n, storage):
    best = np.argsort(vals)[:n]
    c, i = (0, 0)
    while i < len(best):
        while True:
            best_model = storage[best[i]]
            display = ("{f1}\n{f2: ^50}\n{f1}\n"
                       "{m1}\n{f1}\n{f3: ^50}\n{f1}\n"
                       "1:\tFigure\n"
                       "2:\tStarting estimates\n"
                       "3:\tEquation\n\n"
                       "n: next, "
                       "b: back, "
                       "e: exit\n{f1}\n"
                       "".format(f1 = "-" * 50,
                                 m1 = best_model.model,
                                 f2 = "model {}/{}".format(c + 1, n),
                                 f3 = "Options"))
            options = {"e" : None,
                       "1" : None,
                       "2" : "\nStarting estimates given: {}".format(best_model.startest),
                       "3" : "\nEquation: {}\nParamaters: {}".format(*best_model.equation),
                       "n" : None,
                       "b" : None}

            tryagain = True
            print(display)
            while tryagain is True:
                selection = input("Input: ")
                if selection in list(options.keys()):
                    tryagain = False
                else:
                    print("{} is not a registered option. Only select from "
                          "the list provided.".format(selection))

            if selection == "e":
                return False
            elif selection == "1":
                best_model.figure().show()
            elif selection == "n":
                break
            elif selection == "b":
                if c > 0:
                    c -= 1
                    i -= 1
                    os.system("clear")
            else:
                print(options[selection])
                input("\npress any key to return: ")
            os.system("clear")
        c += 1
        i += 1
        os.system("clear")
    return True


# get the best values
vals = np.array([i.model.fun for i in tuple(storage.values())])
best_model = storage[np.argmin(vals)]

# show interactive display
loop = True
while loop is True:
    loop = cycle_models(vals, len(vals) - 1, storage)
