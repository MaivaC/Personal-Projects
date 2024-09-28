#Here, we want the computer to guess on a random number

import random

def guess(x): #define a function called guess

    random_number= random.randint(1,x) #randint is an inbuilt function that let's the computer guess randomly

    guess=0
    while guess !=random_number:
        guess =int(input(f'Guess a number between 1 and {x}:'))
        if guess<random_number:
            print('Guess again, too low')
            
        elif guess>random_number:
            print('Guess again, too high')

    print (f'!!!! yay you got {random_number} right')

guess(10)  # This helps us call the function