#!/usr/bin/env python3
"""Calculates the height of a tree based on distance and angle."""
__appname__ = "get_TreeHeight.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Oct-2018"

## imports ##
import sys
import math
import csv
from pprint import pprint

## Functions ##

def TreeHeight(degrees, distance):
    """TreeHeight - Caluclates the hight of a tree based on
    the distance from the tree and the angle.

    :param degrees: float
    :param distance: float
    """
    radians = degrees * math.pi / 180
    height = distance * math.tan(radians)
    # print("The tree height is {}".format(height))
    return height

def GetFile():
    """GetFile - Open fiel given as command line argument.
    uses default if not given.
    """
    # set input file to work from. Open the file and read in as list.
    # have default in case one not provided.
    default_file = "../Data/trees.csv"
    if len(sys.argv) < 2:
        print("No command line arguments provided.\n"
              "using {} as default".format(default_file))
        filepath = default_file
    elif len(sys.argv) > 2:
        print("More than 1 command line argument provided.\n"
              "Using first argument: {}".format(sys.argv[1]))
        filepath = sys.argv[1]
    else:
        filepath = sys.argv[1]
    return filepath

def ReadCSV(filepath):
    """ReadCSV - Reads a file given and saves the output to a list of lines.

    :param filepath: str
    """
    f = open(filepath, "r")
    reader = csv.reader(f)
    reader = [i for i in reader]
    f.close()
    return reader


def main(argv):
    """main

    :param argv:
    """

    # get the file
    input_path = GetFile()
    
    # Read csv file into a list.
    reader = ReadCSV(input_path)
    
    # Define the headers and content to be calculated.
    headers = reader[:1][0]
    content = reader[1:]

    # Add the headers to the top of the results string.
    headers.append("Tree.Height.m")
    results_str = ",".join(headers) + "\n"

    # Extract the angle and distance values and feed into TreeHeight.
    # Append the tree height result to the original content as a new column
    # Format the content list of that line as a string and add to results_str
    print("Calculating tree height")
    for i in range(len(content)):
        angle = float(content[i][1])
        dis = float(content[i][2])
        content[i].append(str(TreeHeight(angle, dis)))
        results_str += ",".join(content[i]) + "\n"

    # get the location of where to save the output
    outname = input_path.split("/")[-1].replace(".csv", "")
    outpath = "../Results/{}_treeheights.csv".format(outname)
    print("Saving results to {}".format(outpath))

    # write the comma sepperated string to a new file
    with open(outpath, "w") as w:
        w.write(results_str)
    return 0


if __name__ == "__main__":
    # run if executed as script.
    main(sys.argv)
