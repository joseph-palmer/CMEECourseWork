#!/usr/bin/env python3
"""Command line program to simulate sumexp on hpc"""
__appname__ = "hpc_sumexp.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "May-2019"

## imports ##
import sys, os
import argparse
import numpy as np
import pandas as pd
import datetime
import modules
import pickle

# set argument parser
description = "Fit sum of exponentials using MLE for specific time"
parser = argparse.ArgumentParser(description = description)

# add arguments
parser.add_argument("path",
                    type = str,
                    help = "Path to file as csv. Data must be in a csv file "
                           "with a single column of values.")

parser.add_argument("-ratenum",
                    type = int,
                    default = 3,
                    help = "The number of rates in the sum of exponentials "
                           "equation. Default is 3. Cannot be lower than 2.")

parser.add_argument("-walltime",
                    type = int,
                    default = 10,
                    help = "The amount of time to run simulations for.")
# checks
args = parser.parse_args()
if args.ratenum < 2:
    parser.error("Number of rates in sumexp must be larger than 3.")

# get data from given path
data = np.genfromtxt(args.path, delimiter=',')

# set up simulation requirement
storage = {}
best_ll = -1000
elapsed = 0
start = datetime.datetime.now()
counter = 0
while elapsed < args.walltime:
    while True:
        # set starting values which meet constraints
        rates = [i for i in np.random.normal(np.mean(data), np.std(data), args.ratenum)] #[i for i in np.random.uniform(0, 10, args.ratenum)]
        while np.prod(rates) < 1:
            rates = [i for i in np.random.normal(np.mean(data), np.std(data), args.ratenum)] #[i for i in np.random.uniform(0, 10, args.ratenum)]
        probs = [2]
        while sum(probs) > 1:
            probs = [i / args.ratenum for i in np.random.uniform(0, 1, args.ratenum - 1)]
        params = [*rates, *probs]

        # try fitting model but except paramater related errors
        try:
            mod = modules.RunSumexp(data, args.ratenum, params)
            model = mod.model
            if model.success:
                if model.fun > 0:
                    break
        except RuntimeWarning:
            pass

    # store results in dictionary
    llvals.append(model.fun)
    if (-1) * model.fun > best_ll:
        counter += 1
        storage[counter] = mod
        best_ll = (-1) * model.fun

    # get updated time
    end = datetime.datetime.now()
    proc = end - start
    elapsed = proc.total_seconds()

# pickle the data for later use
with open("sumexp_storage.pickle", "wb") as p:
    pickle.dump(storage, p)
