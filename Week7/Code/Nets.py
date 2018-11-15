#!/usr/bin/env python3
"""Practicle to convert script writen in R to python to visualise a network"""
__appname__ = "Nets.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import scipy as sc
import pandas as pd

# set paths to data
edgespath = "../Data/QMEE_Net_Mat_edges.csv"
nodespath = "../Data/QMEE_Net_Mat_nodes.csv"

# load the data into pandas dataframes
nodes = pd.read_csv(nodespath, index_col = "id")
edges = pd.read_csv(edgespath)

print(nodes)
print(edges)
