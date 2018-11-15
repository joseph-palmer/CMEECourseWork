#!/usr/bin/env python3
"""Demonstration of regular expressions in python"""
__appname__ = "RegularExpressions.py"
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__ = "0.0.1"
__license__ = "License for this code/"
__date__ = "Nov-2018"

## imports ##
import sys
import re

# try some basic examples
my_string = "a given string"

# find the space in the string
match = re.search(r'\s', my_string)
print(match)
print(match.group())

# try and find a number in the string
match = re.search(r'\d', my_string)
print(match) # nothing returned as no numbers in the string

# we can use if to see if a pattern was found
MyStr = 'an example'
# find characters before a space
match = re.search(r'\w*\s', MyStr)
if match:
    print('found a match:', match.group())
else:
    print('did not find a match')

# some more examples

# matches the number 2
match = re.search(r'2' , "it takes 2 to tango")
match.group()

# matches any numeric value
match = re.search(r'\d' , "it takes 2 to tango")
match.group()

# match all values including and after a numeric
match = re.search(r'\d.*' , "it takes 2 to tango")
match.group()

# match something starting with a space followed by a word with a lenght between 1 and 3 followed by a space.
match = re.search(r'\s\w{1,3}\s', 'once upon a time')
match.group()

# match a word beginging with a space and ending in a newline
match = re.search(r'\s\w*$', 'once upon a time')
match.group()

# match all words followed by a space, number and any character up to another number
re.search(r'\w*\s\d.*\d', 'take 2 grams of H2O').group()

# find a pattern that at the start of the string is a word of any length folowed by anything of any length folowed by a space.
re.search(r'^\w*.*\s', 'once upon a time').group()

# the * will get everything, to only get the first pattern use ?
re.search(r'^\w*.*?\s', 'once upon a time').group()

# match a HTML tag - greedy
re.search(r'<.+>', 'This is a <EM>first</EM> test').group()

# non - greedy
re.search(r'<.+?>', 'This is a <EM>first</EM> test').group()

# match any number any number of times followed by a single . followed by another number.
re.search(r'\d*\.?\d*','1432.75+60.22i').group()
re.search(r'[AGTC]+', 'the sequence ATTCGT').group()
re.search(r'\s+[A-Z]\w+\s\w+',
         'The bird-shit frog''s name is Theloderma asper').group()

# reading from a webpage
import urllib3
conn = urllib3.PoolManager() # open a connection
r = conn.request('GET',
                 'https://www.imperial.ac.uk/silwood-park/academic-staff/') 
webpage_html = r.data #read in the webpage's contents
type(webpage_html)

# decode it
My_Data  = webpage_html.decode()
print(My_Data)

# extract all names of academics
# pattern begins with Dr followed by a space and work and a space and a word n number of times
pattern = r"Dr\s+\w+\s+[\w']+|Prof\s\w+\s\w+"
regex = re.compile(pattern) # example use of re.compile(); you can also ignore case  with re.IGNORECASE

regex_comand = [x.replace(" ", ", ") for x in set([i.group() for i in regex.finditer(My_Data)])]
regex_comand = "Title, First Name, Surname\n" + "\n".join(regex_comand)
print(regex_comand)


