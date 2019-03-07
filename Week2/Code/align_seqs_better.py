#!/usr/bin/env python3
"""Aligns 2 sequences in fasta format."""
__appname__ = "align_seqs_better2.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Oct-2018"

## imports ##
import sys
import pickle

def GetSeqFromFile():
    """GetSeqFromFile - Extracts the sequences from a fasta file and stores
    in a dictionary.                    
    """
    # set the default sequence paths to use if none provided 
    d1 = "../../Week1/Data/fasta/407228326.fasta"
    d2 = "../../Week1/Data/fasta/407228412.fasta"
    if len(sys.argv) == 1:
        # no sequences given, use defaults
        print ("No sequence provided. "
               "Using {} and {} as default.".format(d1, d2))
        s1 = open(d1)
        s2 = open(d2)
    elif len(sys.argv) == 2:
        # Only 1 sequence given, use and compare with first default.
        print ("Only 1 sequence provided, using {} as comparison.".format(d1))
        s1 = open(d1)
        fasta_seq = sys.argv[1:]
        s2 = open(fasta_seq[-1])
    elif len(sys.argv) > 3:
        # more than 2 sequences given, use the first 2 given.
        print ("More than 2 sequences have been provided. Only using first 2.")
        fasta_seq = sys.argv[1:]
        s1 = open(fasta_seq[0])
        s2 = open(fasta_seq[1])
    else:
        # open the given files and find the sequences.
        print("2 Sequences provided.")
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

    # remove the sequence name and \n to get the sequence for analysis.
    seq1 = seq1.replace(seq_1_name, "").replace("\n", "")
    seq2 = seq2.replace(seq_2_name, "").replace("\n", "")

    # put the output into a dictionary
    seqdict = {seq_1_name : seq1, seq_2_name : seq2}
    return seqdict

def GetScores(s1, s2, l1, l2):
    """GetScores - make a dictionary of scores matched to alignments

    :param s1: str
    :param s2: str
    :param l1: int
    :param l2: int
    """
    scores_dict = {}
    for i in range(l1):
        z = calculate_score(s1, s2, l1, l2, i)
        my_best_align = "." * i + s2
        if not z in scores_dict.keys():
            scores_dict[z] = [my_best_align]
        else:
            scores_dict[z].append(my_best_align)
    return scores_dict

def calculate_score(s1, s2, l1, l2, startpoint):
    """calculate_score - Calculates score for matching alignment.

    :param s1: str
    :param s2: str
    :param l1: int
    :param l2: int
    :param startpoint: int
    """
    # startpoint is the point at which we want to start
    matched = ""
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            # if its matching the character
            if s1[i + startpoint] == s2[i]:
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    return (score)

def main(argv):
    # get sequences from file, extract individual sequences from dictionary.
    sequences = GetSeqFromFile()
    seq1 = list(sequences.values())[0]
    seq2 = list(sequences.values())[-1]

    # asign the longest sequence s1 and the shortest to s2
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    # swap the two lengths
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1

    # calculate scores and alignments into a dictionary.
    scores_dict = GetScores(s1, s2, l1, l2)

    # get the alignment with the highest score. captures if alignments
    # with the same score.
    best_alignments = [(i, scores_dict[i]) for i in scores_dict.keys() 
                       if i == max(scores_dict.keys())]

    # get the last highest score and alignment for writing to file and printing.
    # [-1] gets the last highest score set, [-1] gets the alignment part of that
    # set which is a list, [-1] gets the last string in the list.
    my_best_align = best_alignments[-1][-1][-1]
    my_best_score = best_alignments[-1][0]
    print("\n{}\nAlignment complete".format("-" * 25))
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
    print("\n\nResults saved at {}".format(fsave))
    print("Saved all scores and alignments as dictionary, "
          "saved as pickle object in {}".format(psave))    
    return 0


if __name__ == "__main__":
    status = main(sys.argv)
    print(status)
