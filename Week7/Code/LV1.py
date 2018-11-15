#!/usr/bin/env python3
"""Numerical integration in python using the Lotka-Volterra model"""
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
    dRdt = r * R - a * R * C
    dCdt = -z * C + e * a * R * C
    return sc.array([dRdt, dCdt])

# assign some parameter values
r = 1.
a = 0.1
z = 1.5
e = 0.75

# define the time vector
t = sc.linspace(0, 15,  1000)

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

# save the figure as a pdf`
f1.savefig('../Results/Plots/LV_model.pdf')

# plot the second circular figure. this just has the values from above as axis
f2 = p.figure()
p.plot(pops[:,0], pops[:,1], 'r-') # Plot
p.grid()
p.legend(loc='best')
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')

# save as pdf
f2.savefig("../Results/Plots/LV_FacePlot.pdf")
