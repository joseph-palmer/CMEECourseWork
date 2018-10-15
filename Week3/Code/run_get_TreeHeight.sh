#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: run_get_TreeHeight.sh
# Desc: Runs the R script 'get_TreeHeight.sh" with a test file.
# Arguments: None
# Date: Oct-2018

# set the path to test.
example_input="../Data/trees.csv"

echo "Testing R script 'get_TreeHeight.R'"
Rscript get_TreeHeight.R $example_input
echo "Testing Python script 'get_TreeHeight.py'"
python3  get_TreeHeight.py $example_input
