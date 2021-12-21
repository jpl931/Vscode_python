# python3 pizza order system

#making the lists
available_pizzas = ['pepperoni', 'cheese', 'veggie']
available_toppings = ['pepperoni', 'cheese', 'veggie', 'sauce']
pizza_prices = {'pepperoni': 5.00, 'cheese': 4.00, 'veggie': 3.00}
topping_prices = {'pepperoni': 0.50, 'cheese': 0.50, 'veggie': 0.50, 'sauce': 0.50}
sub_total = [0]
final_order = {}
customer_address = {}



#ordering pizza
print("Hi, Welcome to our text based pizza oerder system")
order_pizza = input("Would you like to order a pizza? (y/n) ")
if order_pizza == 'y':
    input_pizza = input("What type of pizza would you like? ")
    if input_pizza in available_pizzas:
    