import random
# guess the # game
random_number = random.randint(0, 10)
print(random_number) 
# don't forget to convert to int       
guess = int(input("Enter in your numerical guess. "))
number_of_guess_left = 3
# this is the main loop where the user gets 3 chances to guess the correct number 

while number_of_guess_left > 0:
    number_of_guess_left -= 1
    if guess == random_number:
      print("You Win! ")
      break
    else:
      if number_of_guess_left == 0:
          print("You lose! You have no more chances left.")
          break
      else:
          print(f"The number {guess} was an incorrect guess. and you have {number_of_guess_left} guesses left ")
          guess = int(input("Enter in your numerical guess. "))