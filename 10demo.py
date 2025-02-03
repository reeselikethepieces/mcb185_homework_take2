# 10demo.py by pieces
							# white space
print('hello again') 		# is a statement

"""
this is a
multi-line
comment
"""
print(1.5e-2)
print(2 ** 3)
print(5 % 2)
x = 5
y = 3
print(pow(x, y))
print(0.1 * 1)
print(0.1 * 3)

a = 3
b = 4
c = (a**2 + b**2)**0.5
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n')


import math 


def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c

hyp = pythagoras(3, 4)
print(hyp)



def pythagoras(a, b): return math.sqrt(a**2 + b**2)

print(pythagoras(3, 4))


# Convert temp F to C 
# Covert speed from MPH --> KPH
# Compute [DNA] from OD260
# Arithmetic mean of 3 #s	1/n*(x1 +...xn)
# Geometric mean of 3 #s	(x1 * ... * xn)**(1/n)
# harmonic mean of 3 #s		n/(1/x+...)
# distance b/w 2 pts on a graph 
 
if a == b:
	print('a equals b')			
	print(a, b)					# only reported if equal

if a == b:
	print('a equals b')
print(a, b)						# will print regardless


def is_even(x):
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))


c = a == b			# the a == b is boolean, thus the next line prints
print(c)			# False
print(type(c))

'''
# floating point warning
don't do this:

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b') 

instead, do this:
'''

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a,b): print('close enough')


# string comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

# mistmatched type error
'''
a = 1
s = 'G'
if a < s: print('a < s')
'''

def silly(m, x, b):
	y = m * x + b
	
print(silly(2, 3, 4))


# fxn that determines if n is an integer

def is_integer(x):
	if x % 1 == 0: return True
	return False

print(is_integer(1))
print(is_integer(1.4))
print(is_integer(3.4))
print(is_integer(-23))

# is x a valid probability 
def is_validprob(x):
	if x >= 0 and x <= 1: return True
	return False

print(is_validprob(14))
print(is_validprob(0.33))
print(is_validprob(-.33))

# DNA letter mol wt; if != any nt, return 'None'
def dna_gpm(nt):
	if   nt == 'A': return 507.2
	elif nt == 'C': return 483.2
	elif nt == 'G': return 523.2
	elif nt == 'T': return 482.2
	return 'None'

print(dna_gpm('A'), 'g/mol')
print(dna_gpm('G'), 'g/mol')
print(dna_gpm('X'))

# Shannon's entropy
'''
H(X) = - SUMp(x)*logp(x)
'''
