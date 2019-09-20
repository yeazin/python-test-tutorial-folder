
'''
print (' ..................................................................')
print (' ................... hello stick whith the name..................... ')
print (' ...................................................................')

name = input('enter your name : ')

age = int(input(' what is your age:'))
print(' your age is ',age)
'''

''' def of the function leap year '''
'''
year= int(input('enter your year please :'))

def leap_year(year):
    make_year = int(year/4)
    if make_year == 0 :
        print ('this is leap year ')
    else:
        print('year you take is not leap year ')
    
'''
print ('................. welcome to my quiz .............')
begin = input(' would u like to begin ? \n: ')
if begin == "yes" or begin=='YES' :
    print ('(A) number  that divides from any number ')
    print ('(B) number that divides from it-self an the number 1 ')
    print ('(C) dont know !!!')
    print ('')
    
    q1 = input('what is the prime number?\n :')
    print ('')
    if q1 == 'b' or q1 == 'B':
        print ('yup you got this ')
    else:
        print (' wrong !! try again ')
    print ('(A) nope')
    print ('(B) yup sometime')
    print ('(C) not really ')
    print ('')
    q2 = input ('do you like math ?\n :')
    print ('')
    if q2=='b' or q2 == 'B':
        print ('good job .keep it up')
    elif q2 == 'a' or q2 =='A':
        print (' thats not good at all ')
    else :
        print ('ok we know the feelings ')
elif begin != "yes" or begin != "YES" or begin !=  'no' or begin != "NO":
    print ('write yes or YES to begin orelse No or no to quit ')
   
else :
    print (' thanks ,Goodbye see ya later ')


          

