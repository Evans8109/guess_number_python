import random
start = input('please enter the start number: ')
end = input('please enter the end number: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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
