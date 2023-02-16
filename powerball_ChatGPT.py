import random

# generate random Powerball numbers
powerball_numbers = []
while len(powerball_numbers) < 5:
    num = random.randint(1, 69)
    if num not in powerball_numbers:
        powerball_numbers.append(num)
powerball_numbers.sort()
powerball_power = random.randint(1, 26)

# get user's numbers
user_numbers = []
print("Enter your 5 Powerball numbers (1-69), one at a time:")
while len(user_numbers) < 5:
    num = int(input())
    if num < 1 or num > 69:
        print("Invalid input, please enter a number between 1 and 69")
    elif num in user_numbers:
        print("You've already entered that number, please enter a different number")
    else:
        user_numbers.append(num)

user_numbers.sort()
print("Enter your Powerball power number (1-26):")
user_power = int(input())

# compare numbers and print results
num_matches = len(set(powerball_numbers) & set(user_numbers))
if powerball_power == user_power:
    power_match = True
else:
    power_match = False

print("The Powerball numbers are:", powerball_numbers)
print("The Powerball power number is:", powerball_power)
print("Your numbers are:", user_numbers)
print("Your Powerball power number is:", user_power)

if num_matches == 0 and not power_match:
    print("Sorry, you didn't win anything.")
elif num_matches == 1 and not power_match:
    print("Sorry, you didn't win anything.")
elif num_matches == 2 and not power_match:
    print("You won $1.")
elif num_matches == 3 and not power_match:
    print("You won $7.")
elif num_matches == 4 and not power_match:
    print("You won $100.")
elif num_matches == 5 and not power_match:
    print("You won $1,000,000.")
elif num_matches == 0 and power_match:
    print("You won $4.")
elif num_matches == 1 and power_match:
    print("You won $4.")
elif num_matches == 2 and power_match:
    print("You won $7.")
elif num_matches == 3 and power_match:
    print("You won $100.")
elif num_matches == 4 and power_match:
    print("You won $50,000.")
elif num_matches == 5 and power_match:
    print("Congratulations! You won the jackpot of $50,000,000!")
