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
for val in vals: 
	total += val 
mean = total/len(vals)

vari = 0
for val in vals:
	vari += (val - mean)**2 / len(vals)
sd = (vari)**2

# median
vals.sort()
print(vals)

median = None
n = len(vals)
if n % 2 != 0: median = (vals[n // 2])
else: median = ((vals[n // 2] + vals[n // 2 - 1])/2)


print(len(vals), min(vals), max(vals), mean, sd, median)