#!/usr/bin/env python3
"""Aligns 2 sequences in fasta format."""

__appname__ = "align_seqs_fasta.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"

## imports ##
import sys
import pickle


# Find which files to read. 
# default sequences to use if none provided by user.
d1 = "../../Week1/Data/fasta/407228326.fasta"
d2 = "../../Week1/Data/fasta/407228412.fasta"
if len(sys.argv) == 1:
    # no sequences given, use defaults
    print ("\nNo sequence provided. Using {} and {} as default.".format(d1,d2))
    s1 = open(d1)
    s2 = open(d2)
elif len(sys.argv) == 2:
    # Only 1 sequence given, use and compare with first default.
    print ("\nOnly 1 sequence provided, using {} as comparison.".format(d1))
    s1 = open(d1)
    fasta_seq = sys.argv[1:]
    s2 = open(fasta_seq[-1])
elif len(sys.argv) > 3:
    # more than 2 sequences given, use the first 2 given.
    print ("\nMore than 2 sequences have been provided. Only using first 2.")
    fasta_seq = sys.argv[1:]
    s1 = open(fasta_seq[0])
    s2 = open(fasta_seq[1])
else:
    # open the given files and find the sequences.
    print("\n2 Sequences provided.")
    fasta_seq = sys.argv[1:]
    s1 = open(fasta_seq[0]) 
    s2 = open(fasta_seq[-1])

# read the files,then close
seq1 = s1.read()
seq2 = s2.read()
s1.close()
s2.close()

# extract the name at the start of the fasta file.
seq_1_name = ">{}".format(seq1.split(">")[1].split("\n")[0])
seq_2_name = ">{}".format(seq2.split(">")[1].split("\n")[0])

# show message of what is being processed
print ("\nAligning {} with {}".format(seq_1_name, seq_2_name))

# remove the sequence name and \n to get the sequence for analysis.
seq1 = seq1.replace(seq_1_name, "").replace("\n", "")
seq2 = seq2.replace(seq_2_name, "").replace("\n", "")

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
    """calculate_score - Calculates score for matching alignment.

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
  #  print ("." * startpoint + matched)
  #  print ("." * startpoint + s2)
  #  print (s1)
  #  print (score) 
  #  print ("")

    return (score)

calculate_score(s1, s2, l1, l2, 0)
calculate_score(s1, s2, l1, l2, 1)
calculate_score(s1, s2, l1, l2, 5)

# Make a dictionary of scores and alignments
scores_dict = {}
for i in range(l1):
    z = calculate_score(s1, s2, l1, l2, i)
    my_best_align = "." * i + s2
    if not z in scores_dict.keys():
        scores_dict[z] = [my_best_align]
    else:
        scores_dict[z].append(my_best_align)


#print (s1)

# get the alignment with the highest score. captures if alignments
# with the same score.
best_alignments = [(i, scores_dict[i]) for i in scores_dict.keys() 
        if i == max(scores_dict.keys())]

# get the last highest score and alignment for writing to file and printing.
# [-1] gets the last highest score set, [-1] gets the alignment part of that
# set which is a list, [-1] gets the last string in the list.
my_best_align = best_alignments[-1][-1][-1]
my_best_score = best_alignments[-1][0]
print("\n{}\nAlignment complete".format("-"*25))
print("\n\nBest Score: {}\nBest Alignment:\n{}".format(my_best_score, 
    my_best_align))


# save the output to a text file
fsave = "../Results/Fasta_alignment.txt"
with open(fsave, "w") as w:
    w.write("Best Alignment: {}\nBest score: {}".format(my_best_align,
        my_best_score))

# saving the pickle object
psave = "../Results/Fasta_alignment_dict.p"
with open(psave, "wb") as w:
    pickle.dump(scores_dict, w)

# print message to screen.
print("\n\nResults saved at", fsave)
print("Saved all scores and alignments as dictionary, "
      "saved as pickle object in", psave)

