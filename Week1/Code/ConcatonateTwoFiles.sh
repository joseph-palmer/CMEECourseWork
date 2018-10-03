#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: ConcatonateTwoFiles.sh
# Desc: Concatonates two files
# Arguments: $1 the first file to concatonate,
# $2 the second file to concatonate,
# $3 the concatonated file.
# Date: Oct 2018

cat $1 > $3
cat $2 >> $3

echo "Merged File is "
cat $3
