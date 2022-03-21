import random 

r = random.randint(1, 100)

while True: 
	num = input('please enter your number: ')
	num = int(num)
	if r == num:
		print('correct')
		break
	elif r > num:
		print('more than your number' ) 

	elif r < num:
		print('less than your number' )
