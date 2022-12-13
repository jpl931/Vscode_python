import random

# Function to roll the dice
def roll_dice():
  # Generate a random number between 1 and 6
  dice_roll = random.randint(1, 6)
  return dice_roll

# Main function
def main():
  # Keep rolling the dice until the user wants to stop
  while True:
    # Roll the dice
    roll = roll_dice()

    # Print the result
    print(f"You rolled a {roll}")

    # Ask the user if they want to roll again
    again = input("Do you want to roll again (y/n)? ")

    # If the user does not want to roll again, break out of the loop
    if again.lower() != "y":
      break

# Run the main function
if __name__ == "__main__":
  main()
