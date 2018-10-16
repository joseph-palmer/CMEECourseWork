# pre allocation in R - can be faster. 

testme <- function(){
 a <- 1
 for (i in 1:10) {
   a[i] = 10
 }
}

testme2 <- function(){
 a <- rep(NA, 10)
 for (i in 1:10){
   a[i] = 10
 }
}
 
# time the functions
 print(system.time(testme()))
 print(system.time(testme2()))

 