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
		# r.rstrip() --> strip characters from the right (spaces by default)
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
			# of the spliace to the whole string
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

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])