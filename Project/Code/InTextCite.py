#!/usr/bin/env python3
"""Gets the citations from text to create only in text bibliography from bib file"""
__appname__  = "InTextCite.py"
__author__   = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"
__version__  = "0.0.1"
__date__     = "08-2019"

## imports ##
import re
import sys

# get files from args.
if len(sys.argv) < 3:
    exit("Both tex file and bib file required (first tex then bib file)")
tex_path = sys.argv[1]
bib_path = sys.argv[-1]
if ".tex" not in tex_path:
    exit("{} is not a .tex file.".format(tex_path))
if ".bib" not in bib_path:
    exit("{} is not a .bib file.".format(bib_path))

# load in file from path.
with open(tex_path, "r") as t1:
    tex_string = t1.read()

# extract referecnes from text.
re_cite = r"\\cite*.\{(.*?)\}"
cites = re.findall(re_cite, tex_string)
all_cites = [i.split(",") for i in cites]
all_cites = list(set([y.strip() for x in all_cites for y in x]))

# load in bibtex file
with open(bib_path, "r") as b1:
    bib_string = b1.read()

# extract bibref from bib string.
bib_dict = {}
for i in all_cites:
    re_bib = r"@.+{}[\s\S]*?\}}\n\}}".format(i)
    bib = re.findall(re_bib, bib_string)
    bib_dict[i] = "".join(bib)
bib_notfound = [k for k in bib_dict if bib_dict[k] == ""]
if len(bib_notfound) > 0:
    print("WARNING: bib entries not found for - {}".format(bib_notfound))

# make new string of just bib files in text
newbib = "\n".join(list(bib_dict.values()))

# write string to new bib file
newbib_path = bib_path.replace(".bib", "_intext.bib")
with open(newbib_path, "w") as nb:
    nb.write(newbib)

# show summary to user
print("----------\n"\
      "File: {}\n"\
      "Citations in Text: {}\n"\
      "Cites found: {}/{}\n"\
      "New bib saved as: {}".format(tex_path,
                                    len(all_cites),
                                    len(all_cites)- len(bib_notfound),
                                    len(all_cites),
                                    newbib_path))