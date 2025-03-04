# unit 3 practice problems
# write a fxn that:

# returns min value of a list
def mini(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val 
	return mini
	
## returns both min and max vals of a list
def minimaxi(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

### returns mean of the values in a list
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
#### computes the entropy of a prob dist
import math

def entropy(probs):
	h = 0
	for prob in probs:
		h -= prob * math.log2(prob)
	return h
print(entropy([0.2, 0.3, 0.5]))

##### computes kullback-Leibler dist b/w 2 sets of prob dist
def dkl(P, Q):                        # P,Q prob distributions
	d = 0
	for p, q in zip(P, Q):            # p, q are ind values
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)             # intentional 2 show zip in || w/ () & []
print(dkl(p1, p2))
