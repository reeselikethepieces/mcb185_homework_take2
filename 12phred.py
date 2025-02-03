# preddyQ scores Q = -10logP or P = 10**(-Q/10)

'''
fxn converting quality value symbols --> error rates
and vis-versa
letter --> ord() returns ASCII
ASCII --> chr() returns letter
'''

import math 

OFFSET = 33
def char_to_prob(char):
	q = ord(char) - OFFSET
	p = 10**(-q/10)
	return p
	if prob <= 0.00000000000001 and prob > 1: return None

print(char_to_prob('A'))
print(char_to_prob('E'))
print(char_to_prob('X'))


def prob_to_char(prob):
	if prob <= 0.00000000000001 and prob > 1: return None
	q = int((-10 * math.log(prob) + OFFSET) // 1)
	return chr(q)

print(prob_to_char(0.001))
print(prob_to_char(0.0001))
print(prob_to_char(0.0003))
print(prob_to_char(0.00000000000001))
print(prob_to_char(1.4))