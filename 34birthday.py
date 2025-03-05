# 34birthday
# instead of a list of birthdays, make a list from the calendar

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared = 0

for t in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	
	for i in range(people):
		bday = random.randint(0, days-1)     # makes sense bc 365 = days
		calendar[bday] += 1
	
	collision = False
	for day in calendar:
		if calendar[day] > 1: collision = True

print(collision)
