#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: csvtospace.sh
# Desc: Converts commas in a csv file to spaces
# Arguments: $1 the csv input file, $2 the space seperated txt file
# Date: Oct 2018

echo "Creating a space seperated file from a comma seperated file"

# replace .csv with .txt in the file name
filename="${1//.csv/_new.txt}"

for 

cat $1 | tr -s "," "  " >> $filename
echo "Done!"
exit
