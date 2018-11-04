#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: SpeedComparison.sh
# Desc: Provides summary of the speed of vectorized functions in R and Python.
# Arguments: None
# Date: Oct-2018

# set a divider.
s=$(printf "%-30s" "*")
s2=$(printf "%-60s" "-")
echo "${s2// /-}"
echo "Python Vs R vectorization and loop speed summary"
echo "${s2// /-}"

# Run each script in turn to display the speed.
echo -e "\n${s// /*}"
echo "Vectorise 1 - Execution time"
echo -e "${s// /*}\n"
python vectorize1.py
Rscript vectorize1.R
echo -e "\n${s// /*}"
echo "Vectorise 2 - Execution time"
echo -e "${s// /*}\n"
python vectorize2.py
Rscript vectorize2.R


##############################################################################
# Bash thinking about displaying stats about which ones are fastest.
# Eaisier to do this in python, but good for potential future reference.
# get math
#python_v1="$(python vectorize1.py)"

#PyV1_num=($(echo $python_v1 | grep -o -E '[0-9,.]+' | cut -d: -f1))
#PyV1_num_S=${PyV1_num[0]}
#echo $PyV1_num_S
#declare -A Python_1
#Python_1=( ["Python_Loop"]=$PyV1_num_S ["R_loop"]=  )

#for vect in "${!Python_1[@]}"; do echo "$vect - ${Python_1[$vect]}"; done 

#math="$(expr "${NUMBER[0]}-${NUMBER[1]}" | bc -l)"

#echo $math
