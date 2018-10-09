"""This script prints out the contents of the tuple of tuples on a seperate line
"""
__author__ = "Joseph Palmer <joseph.palmer18@imperial.ac.uk>"

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )

# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line or output block by species 
# Hints: use the "print" command! You can use list comprehension!

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

#### ONE LINE SOLOUTION ####
# loop through the tuples in the tuple, then loop through the items in the tuple
# then join these into a single string with the items seperated by newline characters.
print("".join(["{}\n".format(str(element)) for tupl in birds for element in tupl]))

#### NICEER SOLUTION ####
# print a guide of latin name, common name and mass to the screen.
print ("{:<30} {:<30} {:<5}\n".format("Latin_name", "Common_name", "Mass"))

# loop throught the tuples in birds, format each value in line with the above guide.
for x in birds:
    print("{:<30} {:<30} {:<5}".format(x[0], x[1], x[2]))
