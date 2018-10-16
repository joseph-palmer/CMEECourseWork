# Vectorization with apply
# this function multiplies the sum of V by 100 if V is greater than 0, else it returns V.
SomeOperation <- function(v){ # (What does this function do?)
  if (sum(v) > 0){
    return (v * 100)
  }
  return (v)
}

M <- matrix(rnorm(100), 10, 10)
print (apply(M, 1, SomeOperation))