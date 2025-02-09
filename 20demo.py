# Tuple --> collection of values sep by ','
# AND is own data type: touple and (output) 

t = 1, 2 
print(t)
print(type(t))

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):		# not touple
	x = (x1 + x2) / 2
	y = (y1 + y2) /2
	return x, y						# touple

# print(midpoint((1, 2, 2, 1)))	# is touple going in
# print(midpoint(8, 4, 2, 1))


# call midpoint(fxn) and output --> print(fxn) 
print(midpoint(1, 2, 3, 4))
# assign var 'm' --> value of midpt(fxn) + ()
m = midpoint(1, 2, 3, 4)
# unpack tuple, aka: caller knows that: (fxn) --> 2 values
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)


# or, instead of 'mx, my = midpoint(1,..4)', you want ind value
# each item in a tuple gets a [numeric index], strtpt = 0
print(m[0], m[1])



# Iterations = common soln for complex probs
# i.e. compute std.dev for a set of #s, you
# (1) go thru values, (2) (differences to mean)**2
# Iterations = looping
# loop types: (A) while (B) for i in range(fxn) (C) for item in container

# (A) while = simplest loop(type)
	# while <boolean exp is True>: do_something

##while True:
	# print('hello')

# ending loops
	# above ex, ctrl c got you out of running loop
	# break statement: ex below with 'if' statement, i == 3
    # provide a condition when Boolean exp is no longer True
	
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3:
	i = i + 1
	print('hey', i)

# modify the start, limit, and increment
i = 0
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)


# (B) for i in range(fxn)
	# for loops = most loops in Python

for i in range(1, 10, 3):     # has 3 arguments
	print(i)

for i in range(0, 5):         # has 2 arguments, but still +1
	print (i)

for i in range(5):            # same as above bc range(fxn) starts at 0
	print(i)


# (C) for item in container; this container type is a tuple
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)

for i in range(len(basket)):
	print(basket[i])          # numeric indices


# Nesting
for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else:          print(i, 'is odd')