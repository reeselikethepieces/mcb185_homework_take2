# 33birthday 
# prog that simulates the problem by:
	# filling up classrooms of students + randomly chosen birthdays
	# num of days in calendar and num of ppl in class in CL arguments
	# also run 1000s times

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
shared = 0

for t in range(trials):
	bdays = []

	for i in range(people):
		bday = random.randint(0, days-1)
		
		if bday in bdays:
			shared += 1
			break
		bdays.append(bday)
		
print(bdays, shared/trials)
		
	