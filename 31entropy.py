# 31entropy 

# import necessary libraries
import sys
import math

# harvest words on command line and convert them --> probs
probs =[]                        # sets container for prob
for arg in sys.argv[1:]:         # steps through each arg(word) on CL w/ slice, skip first
	f = float(arg)
	if f <= 0 or f >= 1: sys.exit('error: not a probability')
	probs.append(f)              # adds new floating point to container

# check if sum(probs) on CL == 1 by summing up and seeing if they're ~1.0
total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):
	sys.exit('error: probs must sum to 1.0')

# calculate entropy
h = 0
for p in probs:
	h -= p * math.log2(p)
	
print(f'{h:.4f}')
