taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ]

# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

# LOOP SOLUTION
# set an empty dictionary to pupulate.
taxa_dic = {}

# loop through the tuples in the list.
# if the order part [-1] in the tuple is in the dictionary keys append the species to the list.
# If the order part is not in the dictionary, make it a key with the species name in a list.
for order in taxa:
    if order[-1] in taxa_dic.keys():
        taxa_dic[order[-1]].append(order[0])
    else:
        taxa_dic[order[-1]] = [order[0]]

# DICTIONARY COMPREHENSION - dos same as above description but on one line
taxa_dic = {}
[taxa_dic.setdefault(order[-1], []).append(order[0]) for order in taxa]

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

# Write your script here:
