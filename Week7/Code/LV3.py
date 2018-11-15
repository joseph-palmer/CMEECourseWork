# 
#!/usr/bin/env python3
"""ExtraExtra credit Descrete time Lotka-Volterra model"""
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

def dCR_dt(R, C, t=0):
    """dCR_dt: A function to return the growth rate of consumer and
    resource population at any given time step.
    :param pops: list
    :param t: int
    """
    Rt = R
    Ct = C
    Rt1 = Rt * (1 + (r * (1-(Rt/K))) - a * Ct)
    Ct1 = Ct * (1 - z + e * a * Rt)
    return sc.array([Rt1, Ct1])


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

# set carrying capacity
K = 50

# define the time vector
t = sc.linspace(0, 15, 100)

# set the inital conditions for the two populations
R0 = 10
C0 = 5

# make a array or arrays to append to
RC0 = sc.array([[R0,C0]])

# now, numerically integrate this system forwards from these conditions
for i in range(100):
    # run the function on the last entries in the RC0 array
    pops = dCR_dt(RC0[-1][0], RC0[-1][-1])

    # append the function output onto the RC0 array
    RC0 = sc.vstack((RC0, pops))
    
    # break out when a population goes extinct
    if pops[0] < 0:
        RC0[-1, 0] = 0
        print("Prey reached extinction after {} iterations".format(i))
        break
    if pops[-1] < 0:
        RC0[-1,-1] = 0
        print("Predator reached extinction after {} iterations".format(i))
        break

# ensure time is not longer than the RC0 data
t_axis = range(len(RC0))

# plot it
f1 = p.figure()
p.plot(t_axis, RC0[:,0], 'g-', label='Resource density') # Plot
p.plot(t_axis, RC0[:,1], 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')

# save the figure as a pdf`
f1.savefig('../Results/Plots/LV3_model.pdf')

# plot the second circular figure. this just has the values from above as axis
f2 = p.figure()
p.plot(RC0[:,0], RC0[:,1], 'r-') # Plot
p.grid()
p.legend(loc='best')
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')

# save as pdf
f2.savefig("../Results/Plots/LV3_FacePlot.pdf")
