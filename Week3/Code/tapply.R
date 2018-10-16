# Using the tapply function.

x <-1:20 # is a vector
y <- factor(rep(letters[1:5], each = 4)) # is a factor


tapply(x, y, sum)

# load the iris dataset
attach(iris)
iris

# get the means of each species for the sepal legnth and width.
by(iris[,1:2], iris$Species, colMeans)

# gets means for each petal width!
by(iris[,1:2], iris$Petal.Width, colMeans)

# replicae is useful to avoid loops for random number generation # This generated 
# 10 sets (columns) of 5 uniformly-distributed random numbers (a 10 × 5 matrix).
replicate(10, runif(5))




Ricker <- function(N0=1, r=1, K=10, generations=50)
{
  # Runs a simulation of the Ricker model
  # Returns a vector of length generations
  
  N <- rep(NA, generations)    # Creates a vector of NA
  
  N[1] <- N0
  for (t in 2:generations)
  {
    N[t] <- N[t-1] * exp(r*(1.0-(N[t-1]/K)))
  }
  return (N)
}

plot(Ricker(generations=10), type="l")