import random

tickets_per_drawing = 1
num_drawings = 1

total_spent = 0
earnings = 0

times_won = {
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "1+P": 0,
    "P": 0,
    "0": 0.
}

def calc_win_amt(my_numbers, winning_numbers):
    win_amt = 0


for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibles, k=5))
    red_drawing = random.choice(red_possibles)

    winning_numbers = {"whites": white_drawing, "red": red_drawing}

    for ticket in range(tickets_per_drawing):
        total_spent += 2
        my_whites = set(random.sample(white_possibles, k=5))
        my_red = random.choice(red_possibles)


        myNumbers = {"whites": my_whites, "red": my_red}

        #calc_win_amt
