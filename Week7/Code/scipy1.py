#!/usr/bin/env python3
"""An introduction script to scipy"""
__appname__ = "scipy1.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import scipy as sc

# a one-dimensional array
a = sc.array(range(5))
print(type(a))
print(type(a[0]))

# you can specify the data type of the entire array
a = sc.array(range(5), float)
print(a)
a.dtype # check the type

x = sc.arange(5.) # directly specify float using decimal
print(x)
print(x.shape)

# can also convert to and from python lists
b = sc.array([i for i in range(10) if i%2==1]) # odd numbers between 1 and 0
print(b)
c = b.tolist() # convert back to list
print(c)

# To make a matrix, you need a 2-D numpy array
mat = sc.array([[0, 1], [2, 3]])
print(mat)
print(mat.shape)

# indexing and assessing arrays: [row,column]
print(mat[1]) # accessing whole 2nd row, remember indexing starts at  0
print(mat[:,1]) # accessing whole second column  

# And accessing particular elements
print(mat[0,0]) # 1st row, 1st column element
print(mat[1,0]) # 2nd row, 1st column element
print(mat[:,0]) #accessing whole first column

# indexing also takes negative values like a python list
print(mat[0,1])
print(mat[0,-1])
print(mat[0,-2])

# Manipulating arrays

# replacing, adding or removing elements from an array
mat[0,0] = -1 #replace a single element
print(mat)
mat[:,0] = [12,12] #replace whole column
print(mat)
sc.append(mat, [[12,12]], axis = 0) #append row, note axis specification
print(mat)
sc.append(mat, [[12],[12]], axis = 1) #append column
print(mat)
newRow = [[12,12]] #create new row
print(newRow)
mat = sc.append(mat, newRow, axis = 0) #append that existing row
print(mat)
sc.delete(mat, 2, 0) #Delete 3rd row
print(mat)

# concatenation
mat = sc.array([[0, 1], [2, 3]])
mat0 = sc.array([[0, 10], [-1, 3]])
print(sc.concatenate((mat, mat0), axis = 0))

# Flattening or reshaping arrays - use flattern or melt
print(mat.ravel()) # NOTE: ravel is row-priority - happens row by row
print(mat.reshape((4,1))) # this is different from ravel
print(mat.reshape((1,4))) # NOTE: reshaping is also row-priority
# print(mat.reshape((3, 1))) # But total elements must remain the same!!!

# pre-allocating arrays
print(sc.ones((4,2))) #(4,2) are the (row,col) array dimensions
print(sc.zeros((4,2))) # or zeros
m = sc.identity(4) #create an identity matrix
print(m)
m.fill(16) #fill the matrix with 16
print(m)

# numpy matrices (main advantage is matrix multiplication)
mm = sc.arange(16)
mm = mm.reshape(4,4) #Convert to matrix
print(mm)
print(mm.transpose())
print(mm + mm.transpose())
print(mm - mm.transpose())
print(mm * mm.transpose()) # note The element wise multiplication
# print(mm // mm.transpose()) # gets a zero devision error
print(mm // (mm+1).transpose()) # avoid the error
print(mm * sc.pi)
print(mm.dot(mm)) # MATRIX MULTIPLICATION
mm = sc.matrix(mm) # convert to scipy matrix class
print(mm)
print(type(mm))
print(mm * mm) # now matrix multiplication is syntactically easier

# Scipy stats and scipy intergrate
print("\n---- scipy stats ----\n")
import scipy.stats
import scipy.integrate as intergrate

print(scipy.stats.norm.rvs(size = 10)) # 10 samples from N(0,1)
print(scipy.stats.randint.rvs(0, 10, size =7)) # Random integers between 0 and 10

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

print(type(dCR_dt))

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
print(pops)
print(infodict.keys())

# plot it
import matplotlib.pylab as p
f1 = p.figure()
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')
# show the figure
p.show()
# save the figure as a pdf`
f1.savefig('../Results/Plots/LV_model.pdf')





