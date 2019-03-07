#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: RunMiniproject.sh
# Desc: Runs all the code to produce the CMEE Miniproject
# Arguments: None
# Date: Feb-2019

# display starting message
echo "Creating Miniproject"

# run DataWrang.py to wrangle the data into a format for model fitting
echo -e "\n----------Preparing data for model fitting ----------"
python3 DataWrang.py
echo -e "----------- Data ready for model fitting --------------\n"

# Run ModelFit.R to fit the models to the R data
echo -e "----------- Fitting models to data --------------------\n"
echo -e "--- ModelFit.R output ---"
Rscript ModelFit.R
echo -e "----------- Model fitting complete --------------------\n"

# Compile latex report
echo -e "---------- Compiling writeup --------------------------\n"
bash CompileLatex.sh ../Writeup/JPalmer_MiniProject.tex
rm *.pdf
echo -e "---------- Writeup compiled ---------------------------\n"
echo -e "\nMiniproject Complete, write up is in directory Writeup"
