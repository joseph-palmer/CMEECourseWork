#!/usr/bin/env python3
"""Python notes on Networks"""
__appname__ = "networks.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import networkx as nx
import scipy as sc
import matplotlib.pyplot as p

def GenRdmAdjList(N = 2, C = 0.5):
    """GenRdmAdjList - Make a random adjacent C list.

    :param N: int
    :param C: int
    """
    Ids = range(N)
    ALst = []
    for i in Ids:
        if sc.random.uniform(0,1,1) < C:
            Lnk = sc.random.choice(Ids,2).tolist()
            if Lnk[0] != Lnk[1]: #avoid self (e.g., cannibalistic) loops
                ALst.append(Lnk)
    return ALst
#  using a uniform random distribution between [0,1] to generate a 
# connectance probability between each species pair.

# assign number of species and connectance
MaxN = 30
C = 0.75

#  generate an adjacency list representing a random food web
AdjL = sc.array(GenRdmAdjList(MaxN, C))
print(AdjL)
# The two columns of numbers correspond to the consumer and resource ids

Sps = sc.unique(AdjL) # get species ids, species node date
SizRan = ([-10,10]) # use log10 scale
Sizs = sc.random.uniform(SizRan[0],SizRan[1],MaxN)
print(Sizs)

# visualise the distribution generated
p.hist(Sizs) #log10 scale
p.hist(10 ** Sizs) #raw scale

# close all open plots
p.close('all')

#  use a circular configuration. For this, we need to calculate the 
# coordinates, easily done using networkx
pos = nx.circular_layout(Sps)

# generate a networkx graph object
G = nx.Graph()

# add the nodes and links (edges) to it.
G.add_nodes_from(Sps)
G.add_edges_from(tuple(AdjL)) # this function needs a tuple input

# Generate node sizes that are proportional to (log) body sizes
NodSizs= 1000 * (Sizs-min(Sizs))/(max(Sizs)-min(Sizs))

# draw the plot
nx.draw_networkx(G, pos, node_size = NodSizs)

# save the figure as pdf
fig1 = p.figure()
fig1.savefig("../Results/Plots/DrawFW.pdf")



