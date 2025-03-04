# string(aka text) = container 
	# a container that holds letters, numbers, punctuation, other symbs

# assigning a string to a variable
s = 'hello world'
print(s)

# string delimiters are '' or "", but to do a quote in a string do:
s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

# alternatively, using backslash \ tells python ur not using '' as delimiter:
print('hey "dude" don\'t tell me what to do')

# \n means newline character; \t means horizontal tab


# string operators s/s as maths
# string functions
	# len() length of string or tuple
	# chr(n) get the character whos ASCII value is n
	# ord(C) get the ASCII value of character c

# thus far, we have done fxn syntax for fxns; now, we use method syntax
	# for method syntax, variable/string.nameofoperation()
		# s.count(s1) --> number of occurences of s1 in s
		# s.endswith(s1) --> true if s ends with s1
		# s.startswith(s1) --> true if s starts with s1
		# s.upper() or s.lower() --> uppercase or lowercase version of s
		# s.rstrip() --> strip characters from the right (spaces by default)
		# s.replace(a, b) --> convert substring a to b
	
print(s.upper())
print(s)

# pythong strings are immutable (can't change them)
	# s.upper() doesn't conver s to uppercase string, returns new copy of s

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

# string formatting in python consists of 3 different syntaxes:
	# f=strings - modern/best
		# to create, precede string with 'f'
		# inside anything in {} is interpolated (live)
			# variables are expanded and fxns are called 
			# also inside {} are instructions for how to format the output
				# f for fixed point (default = 6)
				# e for exponent notation
				# < ^ > for left, center, right justify
	# str.format() - oldermethod
		# empty {} are filled with parameters of the str.format() parameters
		# print('{} {:.3f}'.format('str.format', math.pi))
	# print-style - sim to printf() in C
		# similar to above; the '%s' means string and '%.3f' means 3 digitprec
		# print('%s %.3f' % ('printf', math.pi))

import math 

print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
# print(f'{hello world":>20}')   # right justify with space filler
# print(f'{hello world":.>20}')  # right justify with dot filler

# index = is the position of a character
	# every character in a string has one
	# can be negative = count backwards, hebrew

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt)           # prints each nt/line
print()

for nt in seq:
	print(nt, end='')   # prints all 6 nt on the same line
print()

# iterate through letters by indices using:
	# range() this generates the indices and leng() sets the limit
for i in range(len(seq)):
	print(i, seq[i])

# slices = subset of a container 
	# is [:]
	# work like range(initial, end-before), i.e. [0:5]
	# can also have a step size like 3rd parameter in range(), i.e. [::]
	# s, below, is equivalent to
		# s[0:len(s)] and s[::], explicitly or implicitly set the bounds
			# of the splice to the whole string
		# s[::1] is s/s as above; but s[::-1] needs a closer look

s = 'ABCDEFGHIJ'   # below two prints have no step size
print(s[0:5])      # is a slice starting at 0th element, ends before fifth
print(s[0])        # prints the same as above, but indexes single element

print(s[0:8:2])    # with step size

print(s, s[::], s[::1], s[::-1])

# slice a string into codons
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	

# tuples = container that holds multiple values and generally w/ ','
	# like strings, tuples are immutable (can't change content via indices)
		# which is why s[0] = 'C' and tax[0] = 'human' will print errors
	# are linear containers of values and can be indexed and sliced like str

tax = ('Homo', 'sapiens', 9606)    # construction of tuple
print(tax)                         # will have () in output
print(tax[0])                      # index
print(tax[::-1])                   # slice




# enumerate() and zip()
	# whilst stepping through containers, useful to have indices and values
		# can do this via range()
		# or, via enumerate()
	# going in TWO containers in parallel, range() will:
		# simultaneously index separate containers
		# or, via zip()
		
# what we've done thus far:
nts = 'ACGT'
'''for i in range(len(nt)):
	print(i, nts[i])
'''

# instead of above, can do, enumerate():
for i, nt in enumerate(nts):
	print(i, nts)

# what we know thus far
names = ('adenine', 'cytosine', 'guanine', 'thymine')
'''
for i in range(len(names)):
	print(nts[i], names[i])
'''
	
# instead of above, can do zip():
for nt, name in zip(nts, names):
	print(nt, name)

# additionally, you can enumerate the zip 
# unpacking tuples in series using additional ()
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)




# Lists - similar to tuples, but use [] instead of ()
	# elements can be added to the end of lists via list.append()
	# elements can be removed from end of lists via list.pop()
	# like strings, most operations use method syntax
	# lists are sorted with list.sort() 
		# note: elements in the list must have similar types
			# you can mix ints and flots
			# you cannot mix them with strings

nts = ['A', 'T', 'C']
nts[2] = 'G'
nts.append('C')
print(nts)

last = nts.pop()
print(last)
print(nts)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

# if you make a new variable to an existing list, it is not a copy
	# is another name for the same list
	# below, nucleotides is modified AND nts
		# this is bc both variable names = same underlying data

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# to make a copy, use list.copy() = 'shallow' copy 
	# means x-dmsnal lists and other complex data are not fully copied
	# we do not make deep copies in this class

# list() fxn without arguments creates empty lists
items = list()
print(items)
items.append('eggs')
print(items)

# instead of list(), you can also just use empty []
stuff = []
stuff.append(3)
print(stuff)

# the list() fxn coerces other 'iterables' into lists
# below is an ex of turning strings into list of letters
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

# split() and join()
	# str.split() method splits strings into lists of strings
text = 'good day      to you'
words = text.split()
print(words)

# TSV or CSV data, split on \t or comma
line = '1.41,2.72,3.14'
print(line.split(','))

# lists can be turned into strings by joining them with delimiter
	# below the list is an argument to a method owned by delim string
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)




# searching
	# to search for items in containers, you can use:
		# in --> reads well in conditionals (i.e. if 'str' in blah:)
			# if ur unsure if an element is in a list, use 'in'
				# i.e. if thing in list: idx = list.index(thing)
		# find() --> returns index of first element it finds
			# if not found, -1 is returned
		# index() --> returns index of first element it finds
			# if not found, an error is returned

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))




# Command line data
	# when we run 'grep', we don't have to re-write grep with different strings
	# 'grep' reads the command line and operates on various values
		# programs can do this, too

# sys.argv = complete list of words on command line (argv = argu vector)
	# sys.argv[0] = name of program
	# sys.argv[1] = first argument, if there is one

import sys
print(sys.argv)
# the output shows: ['30demo.py', '3.14', '2.71']
	# this makes sense bc sys.argv IS a list, which we know are inside []
	# the numeric values we entered have '' around them bc they are strings

# Converting types
	# one must convert text of numbers to ints and floats BEFORE maths
	# int() and float() fxns do this

i = int('42')
x = float('0.61803')
print(i * x)
sys.exit('hello')
	# we do not learn assert, try, except, or raise in this course





# Pairwise Comparison
	# given a list, a freq operation is to compare all things to each other
		# i.e. list of cities, compare distances to each other
		# i.e. list of proteins, compare which are similar to each other
		# i.e. given list of aas, give an alignment score when paired to each other
	# three ways to do all vs all comparisons:
		# (1) all combinations
		# (2) unique pairing allowing self-comparisons
			# aka, half matrix + diagonal
		# (3) unique pairing disallowing self-comparisons
			# aka half matrix - diagonal
	# given ACGT, there are 2**4 combinations; however, some are s/s
		# i.e AC is s/s to CA, in appropriate context
		# same ex but with different context:
			# first letter = host for dinner party
			# second letter = guest 
			# in this case, AC != CA, in either direction
'''
for i in range(0, len(list)):
	for j in range(X, len(list)):
'''

'''
# all combinations
for i in range(0, len(list)):
	for j in range(0, len(list)):

# half-matrix + diagonal
for i in range(0, len(list)):
	for j in range(i, len(list)):

# half-matrix - diagonal
for i in range(0, len(list)):
	for j in range(x+i len(list)):
'''