#!/usr/bin/env python3
"""Practicle - Lotka-Volterra model problem."""
__appname__ = "LV1.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import scipy as sc
import scipy.stats
import scipy.integrate as intergrate
import matplotlib.pylab as p

def dCR_dt(pops, t=0):
    """dCR_dt: A function to return the growth rate of consumer and
    resource population at any given time step.
    :param pops: list
    :param t: int
    """
    R = pops[0]
    C = pops[1]
    # add K into equation
    dRdt = r * R * (1-(R/K)) - a * R * C
    dCdt = -z * C + e * a * R * C
    return sc.array([dRdt, dCdt])

# assign some parameter values from command line, if none given use defaults.
try:
    r = float(sys.argv[1])
    a = float(sys.argv[2])
    z = float(sys.argv[3])
    e = float(sys.argv[4])
except (IndexError, ValueError):
    print("4 float arguments are required. Using default")
    r = 1.
    a = 0.1
    z = 1.5
    e = 0.75

# manually set carrying capacity (K)
K = 50

# define the time vector
t = sc.linspace(0, 60, 1000)

# set the inital conditions for the two populations
R0 = 10
C0 = 5
RC0 = sc.array([R0,C0])

# now, numerically integrate this system forwards from these conditions
pops, infodict = intergrate.odeint(dCR_dt, RC0, t, full_output = True)

# plot it
f1 = p.figure()
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')

# add the parameter values to the plot. Currently in the plot but for
# multiple plots as part of a pipeline this should be substituted for
# something outside the plot grid.
p.text(6, 15,"r = {}, a = {}, z = {}, e = {}, K = {}".format(r, a, z, e, K))

# save the figure as a pdf`
f1.savefig('../Results/Plots/LV2_model.pdf')

# plot the second circular figure. this just has the values from above as axis
f2 = p.figure()
p.plot(pops[:,0], pops[:,1], 'r-') # Plot
p.grid()
p.legend(loc='best')
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')
p.text(15, 4,"r = {}, a = {}, z = {}, e = {}, K = {}".format(r, a, z, e, K))

# save as pdf
f2.savefig("../Results/Plots/LV2_FacePlot.pdf")

# show the final population values
finalpopvals = pops[-1]
print("Populations at equlibrium:\n"
      "Prey: {}\nPredator: {}\n".format(finalpopvals[0], finalpopvals[-1]))

