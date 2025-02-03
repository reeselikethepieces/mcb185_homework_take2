def oligo_tm(A, C, G, T):
	length = A + C + G + T
	if length <= 13: return (A+T)*2 + (G+C)*4
	return 64.9 + 41*(G + C - 16.4)/length

print(oligo_tm(1, 3, 4, 6))
print(oligo_tm(1, 2, 2, 1))