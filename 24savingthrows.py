<<<<<<< HEAD
# event 'x' occurs --> saving throw = roll d20 (20 sides) 
#                  --> result: success or not
# event 'x' comes in different difficulty flavors, 'DC'
# event 'x' can have advantage max(two rolls) 
# or disadvantage min(two rolls)

# write a prog simulating saving throws against DC 5, 10, 15
import random

# normal
'''
for dc in range(5, 16, 5):
	trials = 100000
	success = 0
	for i in range(trials):
		roll = random.randint(1, 20)
		if roll >= dc: success += 1
	print(dc, roll, success/trials)
'''
import math 

for dc in range(5, 16, 5):
	trials = 10000
	prob_norm = 0
	for i in range(trials):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		prob_adv = max(r1, r2)
		prob_dis = min(r1, r2)
		if r1 >= dc: prob_norm += 1
		if r1 >= dc and r1 >= dc: prob_dis += 1
		if r1 >= dc or r2 >= dc: prob_adv += 1
	print(prob_norm/trials, prob_dis/trials, prob_adv/trials)


# make table showing prob(success, success+adv, and success+dis)
'''
	| dc | prob_succ | prob_succ+adv | prob_succ+dis |
	| -- | --------- | ------------- | ------------- |
	|  5 |   0.80    |    0.0014     |    0.0012     |
	| 10 |   0.55    |    0.0006     |    0.0004     |
	| 15 |   0.30    |    0.0011     |    0.0006     |
 '''
=======
# 24savingthrows by Reese

# any time we know we're going to be throwing a lot of dice, we know there will be:
	# random.randint()
	# rounds or trials
	# iteration

'''
import random

trials = 5
for rolls in range(trials):
	roll = random.randint(1, 20)
	print(roll)
'''

# we know there are three DCs
'''
import random

dc5 = 5
dc10 = 10
dc15 = 15
while True:
	roll = random.randint(1, 20)
	if roll >= 5: print("dc5, success")
	else: print("dc5, fail")

	if roll >= 10: print "dc10, success"
	else: print "dc10, fail"

	if roll >= 15: print "dc15, success"
	else: print "dc10, fail"
'''

# the above is mundane and the main factor that is changing is 'dc'; so make a loop
'''
import random

dc5 = 0
dc10 = 0
dc15 = 0
for dc in range(5, 16, 5):
	roll = random.randint(1, 20)
	if roll >= 5: dc5 += 1
	if roll >= 10: dc10 += 1
	if roll >= 15: dc15 += 1
'''

#want to combine this with the trials and figure out how many times there is success

import random

trials = 5
total = 0
success = 0

for rolls in range(trials):
	roll = random.randint(1, 20)
	total += roll
	for dc in range(5, 16, 5):
		if roll >= dc: success += 1
		
print(success/total)


	

	
	

>>>>>>> f2ee6cfda96576b0608adaf0b3bc64afe8cca74d
