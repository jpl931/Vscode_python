import random

# Roll the dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

# Calculate the total
total = dice1 + dice2

# Check if the player wins or loses
if total == 7 or total == 11:
    print("You win!")
else:
    print("You lose!")
