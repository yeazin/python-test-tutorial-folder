#gussing the number
'''
guess = int(input('enter a number between 1-10. \n:'))

while guess !=5:
    if guess < 5:
        print (' number is too low')
        guess=int(input('enter a number between 1-10. \n:'))
    if guess > 5:
        print (' number is too high ')
        guess=int(input('enter a number between 1-10. \n:'))
print('you got the currect number')
        
'''

#advanture game

print ('...................................')
print ('.......Main Menu ..................')
print('....................................')
print('')
print('make a selection ')
print('(A) home ')
print('(B) sword')
print('(C) Dragon')
print('')
while :
    
    s1 = input(':')
    if s1== 'A' or s1  =='a':
        print('')
        print('what type of home you want ?')
        print ('(A) Building')
        print ('(B) cottege ')
        sub1 = input(':')
    if sub1 == "A" or sub1 == "a" :
        print('')
        print (' building is that type of Home that made by many elements that releted to it')
    else:
        print('cottege is made by simple things and easy to made')               
               
