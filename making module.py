# here we will learn how we can make our own module

x = [25,5,4,6,6,2]

find_digit= int(input('enter a digit \n:'))
for find in x :
	if find_digit == find:
		print('win')
		break
	else :
		print('lose')