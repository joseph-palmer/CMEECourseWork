#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: variables.sh
# Desc: Shows the use of variables
# Date: Oct 2018

# There are 3 ways to declare a variable
# 1) Explicit declaration: MYVAR=myvalue
MyVar="Some string"
echo "the currect value of the variable is " $MyVar

# 2) Reading from the user
echo "enter a new value for the variable"
read MyVar
echo "The current value of the variable is " $MyVar

# 3) Command substitution
echo "Enter 2 numbers seperated by spaces (s)"
read a b
echo "You entered " $a " and" $b "." "Their sum is:"
mysum=`expr $a + $b`
echo $mysum
