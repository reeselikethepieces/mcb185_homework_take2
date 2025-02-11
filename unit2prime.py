# write the numbers 1-50, backwards
# if the num is prime, place a '*' after

'''
def is_prime(x):
	if x % 1 == x: return x
	if x % x == 1: return x

i = 50
while True:
	i -= 1
	if is_prime(i): print(i, '*')
	if i == 1: break
'''
'''
i = 51
while True:
	i -= 1
	if i % 1 == 0 and i % i == 1: print(i, '*')
	else: print(i)
	if i == 1: break
'''

def is_prime(n):
	for den in range(2, n//2 +1):
		if n % den == 0: return False
	return True


i = 51
while True:
	i -= 1
	if is_prime(i): print(i, '*')
	else: print(i)
	if i == 1: break