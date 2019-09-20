#while loop in python
'''
def get_answer (prompt):
    answer = input (prompt)

    while answer not in ('yes','no'):
        answer = input(prompt)
    return answer


print (get_answer('yes or no ?'))
'''

def main():
    print (' guess a number')
    randomNumber = 35
    found = False

    while not found :
        UserGuess = int(input(' your guess \n:'))
        if UserGuess == randomNumber:
            print('you have it')
            found= True
        else :
            print('wrong')
if __name__== "__main__":
    main()
