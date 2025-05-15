# the following are 'good' errors to discuss

# line 18, also when break is under the if statement
import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])
shared = 0

for t in range(trials):
	bdays = []
	
	for s in range(students):
		bday = random.randint(0, days-1)
	
		if bday in bdays: shared += 1 break
		bdays.append(bday)

print(shared/trials)
		