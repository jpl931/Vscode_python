import random

secretNumber = random.randint(1, 99)

print('I am thinking of a number between 1 and 99')

#Ask the the player to guess 6 times.

for guessesTaken in range(1, 6):
    print('Take a guess. ')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low. ')

    elif guess > secretNumber:

        print('Your guess is too high.')

    else:

        break    #This condition is the correct guess!

    if guess == secretNumber:
        print('Great job! You guessed my number in ' +str(guessesTaken) +' guesses!')
    else:

        print('Nope! The number I was thinking of was ' + str(secretNumber))