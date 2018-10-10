#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: csvtospace.sh
# Desc: Converts commas in a csv file to spaces
# Arguments: $1 the csv input file, $2 the space seperated txt file
# Date: Oct 2018

echo "Creating a space seperated file from a comma seperated file"

# replace .csv with .txt in the file name
filename="${1//.csv/_space.txt}"

# replace the file path with path to the results directory. basename gets the
# name of the file without the path.
new_fname=$(basename $filename)
outname="../Results/$new_fname"

# replace commas with spaces in file and save to new location in results
cat $1 | tr -s "," "  " >> $outname
echo "Done! The file has been saved as $outname"
exit
