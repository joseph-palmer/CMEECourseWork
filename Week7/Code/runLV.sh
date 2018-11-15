#!/usr/bin/env bash
# Author: Joseph Palmer <joseph.palmer18@imperial.ac.uk>
# Script: runLV.sh
# Desc: Runs the two LV scripts (LV1.py and LV2.py)
# Arguments: None
# Date: Nov-2018

echo -e "---Running LV1.py---\n"
python -m cProfile -s cumtime LV1.py  2>&1 | head -20
echo -e "- LV1.py complete\n"
echo -e "---Running LV2.py---\n"
python -m cProfile -s cumtime LV2.py 1. 0.1 1.1 0.8 2>&1 | head -20
echo -e "- LV2.py complete\n"
echo -e "---Running LV3.py---\n"
python -m cProfile -s cumtime LV3.py 1. 0.1 1.1 0.8 2>&1 | head -20
echo -e "- LV3.py complete\n"
echo -e "---Running LV4.py---\n"
python -m cProfile -s cumtime LV4.py 1. 0.1 1.1 0.8 2>&1 | head -20
echo -e "- LV4.py complete\n"
