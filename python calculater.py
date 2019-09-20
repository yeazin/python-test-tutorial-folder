import re

print("Our Magical Calculater")
print('Type "quit" to exit \n')

previous = 0
run =True

def mathperform():
	global run
	global previous
	equation=input("Enter equation :")
	if equation=='quit':
		print('Goodbye , Human')
		run = False
	else:
		equation = re.sub('[a-zA-Z,.:()" "]','',equation )
		previous = eval(equation)
		print("Your result is",previous)
 




while run:
	mathperform()


