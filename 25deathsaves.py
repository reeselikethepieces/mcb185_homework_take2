# 25deathsaves by Reese

'''
# initialize and figure out what you want the program to give you
trials = 0
dies = 0
stab = 0
revi = 0



print(dies/total, stab/total, revi/total)
'''



import random

trials = 1000
dies = 0
stab = 0
revi = 0

for i in range(trials):
	succ = 0
	fail = 0
	r20 = False
	while succ < 3 and fail < 3 and not r20:
		roll = random.randint(1, 20)
		if roll == 1: fail += 2
		elif roll == 20: r20 = True
		elif roll < 10: fail += 1
		elif roll >= 10: succ += 1
	if fail >= 3: dies += 1
	if succ >= 3: stab += 1
	if r20: revi += 1 

print(dies/trials, stab/trials, revi/trials)
print(dies/trials + stab/trials + revi/trials)