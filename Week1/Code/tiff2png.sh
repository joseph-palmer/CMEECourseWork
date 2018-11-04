#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: tiff2png.sh
# Desc: Convert tiff to png.
# Arguments: 
# Date: Oct 2018

for f in *.tiff;
    do
        echo "Converting $f";
        convert "$f"  "$(basename "$f" .tif).jpg";
    done
