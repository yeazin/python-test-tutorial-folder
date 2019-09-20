#user defined function 
'''
def hi(me,u):
	print('hello Brother')
	print('another intruders')
	print(me)
	print(u)
#hi("hello its me","you are none")
hi('string 01','string 2')
'''

'''
def label(name='unknown',age='undefined',oct='none'):
	print("My name is", name ,".My age is", age,".My job is",oct,".")

label(oct='student',age=20)
'''

#infinite arguments 

def Hi_people(*people):
	for list in people:
		print('this is', list)


Hi_people('yeasin','hebok','jury')