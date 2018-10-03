#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: CountLines.sh
# Desc: Counts the number of lines in a file
# Date: Oct 2018

NumLines=`wc -l < $1`
echo "The file $1 has $NumLines lines"
echo
