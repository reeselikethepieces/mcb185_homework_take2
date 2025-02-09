# preddyQ scores Q = -10logP or P = 10**(-Q/10)
# 0-9 symbols with 0 as 0.5 and 9 as .001
import math

def symb_to_prob(symb):
	ascii = (ord(symb))
	power = 64 - ascii
	return 2**power
print(symb_to_prob('C'))