# max of 4 #s

def max_of4(a, b, c, d):
	if a > b and a > c and a > d: return a
	elif b > c and b > d: return b
	elif c > d: return c
	return d

'''
print(max_of4(8, 3, 2, 1))
print(max_of4(8, 22, 3, 23))
print(max_of4(9, 2, 39, 20))
print(max_of4(1, 30, -55, 99))
'''



# monty python

x = random.random()      # w/out () will rename the fxn
y = random.random()
# print(x, y)              # checkpt1

dist = (x ** 2 + y ** 2) ** (0.5)
# print(dist)              # checkpt2

in_circle = dist <= 1
# print(in_circle)         # checkpt3

while True:
	x = random.random()
	y = random.random()
	dis = (x ** 2 + y ** 2) ** 0.5
	in_circle = dis <= 1
	# print(x, y, dist, in_circle)
                         # checkpt4
import random 

pi_approx = 0
ins = 0
outs = 0
while True:
	x = random.random()
	y = random.random()
	dis = (x ** 2 + y ** 2) ** 0.5
	in_circle = dis <= 1
	if in_circle:
		ins += 1
	else: out+= 1
	pi_approx = ins/(ins + outs) * 4
	print(x, y, ins, outs, pi_approx)
	