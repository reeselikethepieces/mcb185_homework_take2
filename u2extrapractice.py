# monty Pi-thon
'''
import random 

def dist(x1, y1, x2, y2): return ((x2-x1)**2 + (y2-y1)**2)**0.5

inside = 0
total = 0
while True:
	x = random.random()
	y = random.random()
	if dist(0, 0, x, y) <= 1: inside += 1
	total += 1
	print(4*inside/total)
'''

# parabola and sqrt

import random

above = 1
below = 1
equal = 0
while True:
	x = random.random()
	y = random.random()
	if y > x**0.5: above += 1
	elif y < x**0.5: below += 1
	else: equal += 1
	print(above, below, equal, above/below)
	
	
	

