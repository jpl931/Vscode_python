#Pizza order system written in python

pizza_price = {
    'small': 10,
    'medium': 15,
    'large': 20
}

pizza_size = input("What size pizza would you like? (small, medium, large): ")
pizza_large = pizza_price[pizza_size]
pizza_medium = pizza_price[pizza_size]
pizza_small = pizza_price[pizza_size]

extra_toppings = input("How many extra toppings would you like? ")
one = pizza_large + extra_toppings
two = pizza_medium + extra_toppings
three = pizza_small + extra_toppings



