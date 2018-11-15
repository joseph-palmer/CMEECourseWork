#!/usr/bin/env python3
"""tutorial on using subprocess"""
__appname__ = "subprocess.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import subprocess

# first example
p = subprocess.Popen(["echo", "I'm talking to you, bash!"],
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)

# this creates an object p, from which you can extract the output
stdout, stderr = p.communicate()
print(stderr) # print standard error
print(stdout) # print standard out

# decode the output of standard out
print(stdout.decode())

# another command
p = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
stdout, stderr = p.communicate()
print(stdout.decode())

# you could also even call python from bash within python
p = subprocess.Popen(["python", "boilerplate.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # A bit silly!
stdout, stderr = p.communicate()
print(stdout.decode())

# subprocess makes code OS independent - it will sub on any
MyPath = subprocess.os.path.join('directory', 'subdirectory', 'file')
print(MyPath)
