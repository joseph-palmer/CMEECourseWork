#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: CompileLatex.sh
# Desc: Compiles .tex document to pdf and cleans up files
# Arguments: the .tex file to compile
# Date: Oct 2018

# get the filename without the extention for bibtex
filename="${1//.tex/}"

# compile pdf (multiple times required!)
pdflatex $1
pdflatex $1
bibtex $filename
pdflatex $1 
pdflatex $1 

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

# move pdf into results
mv $filename.pdf "../Results/"

# Open pdf in Viewer
evince "../Results/$filename.pdf"

