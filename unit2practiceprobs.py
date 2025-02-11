# write the numbers 1-50, backwards
# if the num is prime, place a '*' after

def is_prime(n):
	for den in range(2, n//2 +1):
		if n % den == 0: return False
	return True
	

limit = 0
for i in range(50, limit, -1):
	if is_prime(i): print(i, '*')
	else: print(i)



# Write a function that calculates the triangular number. 
# This is the sum of numbers from 1 to n.

def triangular(n):
	total = 0
	for i in range(n+1):
		total = total + i
	return total
		
print(triangular(4))



# Write a function that calculates the factorial of a number.

def factorial(n):
	if n == 0: return 1
	total = 1
	for i in range(1, n+1):
		total = total * i
	return total

print(factorial(4))



# Write a function that computes the Poisson probability of k events occurring 
# with an expectation of n: n^k e^-n / k!

import math

def poissonprob(n, k):
	return n**k * math.e**-n / factorial(k)

print(poissonprob(1, 3))



# Write a function that solves "n choose k": n! / k!(n - k)!

def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))

print(nchoosek(1, 2))



# Write a function that estimates Euler's number: e (2.71828...). 
# This can be computed as the infinite sum of 1/n!. Choose a finite number of iterations.

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e

print(euler(3))
print(euler(6))



# Write a function that estimates Pi (3.14159...) using the Nilakantha series. 
# Again, choose a finite limit. Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10)...
# nilakantha

def nilakantha(limit):
	pi = 3
	for i in range(1, limit+1):
		n = 2 * i
		d = n * (n+1) * (n+2)
		if i % 2 == 0: pi = pi - 4 / d
		else:          pi = pi + 4 / d
	return pi