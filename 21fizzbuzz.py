# writes out #s from 1 to 100
# if # is divisible by 3, write Fizz, instead
# if # is divisible by 5, write Buzz, instead
# if both, write FizzBuzz

i = 0
while True:
	i += 1
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
	elif i % 3 == 0: print('Fizz')
	elif i % 5 == 0: print('Buzz')
	else: print(i)
	if i == 100: break



for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
	elif i % 3 == 0: print('Fizz')
	elif i % 5 == 0: print('Buzz')
	else: print(i)