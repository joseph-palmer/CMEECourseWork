#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: boilerplate.sh
# Desc: simple boilerplate for shell scripts
# Arguments: none
# Date: Oct 2018

echo -e "\nThis is a shell script!\n"

echo "Remove  excess  spaces." | tr -s "\b" "  "

echo "remove all the as" | tr -d "a"

echo "set to uppercase" | tr [:lower:] [:upper:]

echo "1.00 onliy numbers 1.33" |  tr -d [:alpha:] | tr -s " " ","
