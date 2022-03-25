#Guess the number game
import random
#Assign random num between 1-100
secret_number = random.randint(1,100)
#get user input
guess = int(input('Guess a number between 1 and 100: '))

#loop until user guess the number
while guess != secret_number:
    if guess > secret_number:
        print('Too high!')
    else:
        print('Too low!')
    guess = int(input('Guess again: '))
#This statement will execute after coming out of the loop
print('You got it!')
