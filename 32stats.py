# 32stats

# write prog that reports descriptive stats for numbers on CL
# report: number of values, min and max of values, mean and sd, median

import sys
import math

vals = []
for arg in sys.argv[1:]:
	f = float(arg)
	vals.append(f)

total = 0
mean = 1
for val in vals: 
	total += val 
	mean = total/len(vals)

sd = 1
for val in vals:
	sd = (val - mean)**2 / len(vals)
	
'''
medi = 1
for val in vals:
	if len(val) / 2: (len(val)/2 + val/(2+1))/2
	else: val+1/2

# alternatively, vals.sort/2
'''


print(len(vals), min(vals), max(vals), mean, sd)