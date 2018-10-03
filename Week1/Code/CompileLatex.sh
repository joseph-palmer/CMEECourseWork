#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: CompileLatex.sh
# Desc: Compiles .tex document to pdf and cleans up files
# Arguments: the .tex file to compile
# Date: Oct 2018

# get the filename without the extention for bibtex
filename="${1//.tex/}"

# compile pdf
pdflatex $1
pdflatex $1
bibtex $filename
pdflatex $1 
pdflatex $1 

# open pdf in viewer
evince "$filename.pdf" &

## Cleanup
rm *~
rm *.aux
rm *.dvi
rm *.log
rm *.out
rm *.snm
rm *.toc
rm *.bbl
rm *.blg
