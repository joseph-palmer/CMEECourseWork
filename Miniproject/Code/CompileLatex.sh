#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: CompileLatex.sh
# Desc: Compiles .tex document to pdf and cleans up files
# Arguments: the .tex file to compile
# Date: Oct 2018

# get the filename without the extention for bibtex
path="$(dirname $1)"
file="$(basename $1)"
filename="${file//.tex/}"

# Files need to be in the correct working directory for Bibtex to work.
mv $path/$filename* .

# compile pdf (multiple times required!)
pdflatex $file >/dev/null
pdflatex $file >/dev/null
bibtex $filename >/dev/null
pdflatex $file >/dev/null
pdflatex $file >/dev/null

## Cleanup
rm *.aux
rm *.log
rm *.toc
rm *.bbl
rm *.blg

# move files back into writeup
mv $filename.* "../Writeup/"

