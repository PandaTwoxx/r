import random

print('r')

data = input('pick random r count(y,n)')
if data == 'y':
	count = random.randint(100,999)
	for i in range(count):
		print(f'printed r {i} times')
else:
	data = input('count to r how many times')
	for i in range(data):
                print(f'printed r {i} times')
