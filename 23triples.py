# program that finds all pythag triples for triangles w/ sides 'a' and 'b' < 100
# all sides must be integers

def pythagoras(a, b): return (a**2 + b**2)**0.5

for a in range(1, 100):
	for b in range(1, 100):
		c = pythagoras(a,b)
		if c % 1 == 0: print(a, b, c)