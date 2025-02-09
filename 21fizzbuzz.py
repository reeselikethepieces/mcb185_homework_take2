# writes out #s from 1 to 100
# if # is divisible by 3, write Fizz
# if # is divisible by 5, write Buzz
# if both, write FizzBuzz

i = 0
while True:
	i += 1
	if i % 3 == 0: print(i, 'Fizz')
	if i % 5 == 0: print(i, 'Buzz')
	if i % 3 == 0 and i % 5 == 0: print(i,'FizzBuzz')
	if i == 100: break



for i in range(1, 100):
	if i % 3 == 0: print(i, 'Fizz')
	if i % 5 == 0: print(i, 'Buzz')
	if i % 3 == 0 and i % 5 == 0: print(i,'FizzBuzz')