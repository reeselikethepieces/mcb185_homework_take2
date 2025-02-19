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


	

	
	

