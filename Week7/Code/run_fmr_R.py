#!/usr/bin/env python3
"""Runs the fmr.R script using subprocess - practicle"""
__appname__ = "run_fmr_R.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import subprocess

def RunScript(program, script, args=[], runtime=10):
    """RunScript - Runs a script via the os using subprocess and returns
    the result.

    :param script: str - The script to be ran
    :param program: str - What you run the script in
    :param args: list - a list of command line arguments
    :param runtime: int - the timeout time for the process
    """

    # check for extra command line args, if so add these args
    command_args = [program, script] + args
    p = subprocess.Popen(command_args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    # get the output, use timeout to prevent infinate loop.
    try:
        stdout, stderr = p.communicate(timeout=runtime)
    except subprocess.TimeoutExpired:
        print("Warning: {} timed out after {} seconds.".format(script,
                                                               runtime))
        p.kill()
        stdout, stderr = p.communicate()

    # Return either the error code or the sucessful output.
    if len(stderr) > 0:
        ErrorString = ("\033[0;31mError produced when running {}\033[0m\n"
                       "--- Error message ---\n{}"
                       "--- Output --\n{}"
                       "-------------".format(script,
                                              stderr.decode(),
                                              stdout.decode()))
        return ErrorString
    else:
        DisplayString = ("\033[0;32mFile {} ran with 0 errors\033[0m\n"
                         "--- Output ---\n{}"
                         "--------------".format(script,
                                                           stdout.decode()))
        return DisplayString


# set the path to the r_script and the program to run it.
r_script = "fmr.R"
program = "Rscript"

# run the above and get the output
run = RunScript(program, r_script)

# show the output on the screen
print(run)
