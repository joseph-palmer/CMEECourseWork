#!/bin/bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: tabtocsv.sh
# Desc: converts tabs in given file to commas
# Arguments: 1-> tab deliminated file
# Date: Oct 2018

echo "Creating a comma deliminated file"

cat $1 | tr -s "\t" "," >> $1.csv

echo "Done!"

# the output is saved to the same location as the input file as $1
exit
