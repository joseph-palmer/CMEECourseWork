#!/usr/bin/env python3
"""Aligns two sequences in a set file"""

__appname__ = "align_seqs.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys

# open the default file and find the sequences.
fpath = "../Data/DefaultSequences.fasta"
seq_dict = {}
for line in open(fpath):
    if line.startswith(">"):
        key = line.split(">")[-1].rstrip()
    else:
        if key in seq_dict.keys():
            seq_dict[key] += line.rstrip()
        else:
            seq_dict[key] = line.rstrip()

# These are the two sequences to match
seq2 = "ATCGCCGGATTACGGG"
seq1 = "CAATTCGGAT"

# assign the longest sequence s1, and the shortest to s2
# l1 is the length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# function that computes a score
# by returning the number of matches 
# starting from arbitrary startpoint
def calculate_score(s1, s2, l1, l2, startpoint):
    """calculate_score - Calculates scores for matching alignment.

    :param s1:
    :param s2:
    :param l1:
    :param l2:
    :param startpoint:
    """
    # startpoint is the point at which we want to start
    matched = "" # contains string for alignement
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            # if its matching the character
            if s1[i + startpoint] == s2[i]:
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # build some formatted output
    print ("." * startpoint + matched)
    print ("." * startpoint + s2)
    print (s1)
    print (score) 
    print ("")

    return (score)

calculate_score(s1, s2, l1, l2, 0)
calculate_score(s1, s2, l1, l2, 1)
calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score)
my_best_align = None
my_best_score = -1

for i in range(l1):
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2
        my_best_score = z

print (my_best_align)
print (s1)
print ("Best score:", my_best_score)

# save the output to a text file
fsave = "../Results/DefaultSequences_alignment.txt"
with open(fsave, "w") as w:
    w.write("Best Alignment: {}\nBest score: {}".format(my_best_align,
        my_best_score))

print("Results saved at", fsave)
