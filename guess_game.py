import random 

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1 
	num = input('please enter your number: ')
	num = int(num)
	if r == num:
		print('correct')
		break
	elif r > num:
		print('more than', num, ) 

	elif r < num:
		print('less than', num, )
	print ('this is',  count, 'guess')
