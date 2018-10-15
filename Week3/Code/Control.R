## Some code showing control flow constructs in R 

## If statement
a <- TRUE
if (a == TRUE){
  print("A is TRUE")
} else {
  print("A is False")
}

z <- runif(1) # random number
if (z <= 0.5) {
  print ("Less than a quarter")
}

## For loop using a sequence
for (i in 1:100){
  j <- i * i
  print(paste(i, " squared is", j ))
}

## For loop over vector of strings
for(species in c('Heliodoxa rubinoides', 
                 'Boissonneaua jardini', 
                 'Sula nebouxii'))
{
  print(paste('The species is', species))
}

# for loop using a vector
v1 <- c("a","bc","def")
for (i in v1){
  print(i)
}

# While loop
i <- 0
while (i<100){
  i <- i+1
  print(i^2)
}

# Breaking out of loops - opten you want to break out of a loop when a condition is met.
i <- 0 # Initialize I
while(i<Inf){
  if(i==20){
    break
  } else {
    cat("i equals ", i, "\n")
    i <- i + 1
  }
}

# You can also skip the next iteration of a loop if needed. Both next and {\tt break} can be used within loops
for (i in 1:10){
  if((i %% 2) == 0){
    next
  }
  print(i)
}

 




