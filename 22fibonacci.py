# fibonacci, report first 10 numbers
# each element is the sum of the two elements that precede it
# think milk example

a = -1
b = 1
for _ in range(10):
	c = a + b
	print(c)
	a = b
	b = c