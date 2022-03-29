#Pizza ordering system
import os
available_pizzas = ['Margherita', 'Pepperoni', 'Hawaiian', 'Vegetarian']
available_toppings = ['Cheese', 'Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 'Olives', 'Pineapple']   
pizza_prices = {'Margherita': 10, 'Pepperoni': 12, 'Hawaiian': 14, 'Vegetarian': 8}
pizza_toppings = {'Margherita': ['Cheese'], 'Pepperoni': ['Cheese', 'Pepperoni'], 'Hawaiian': ['Cheese', 'Ham', 'Pineapple'], 'Vegetarian': ['Cheese', 'Mushrooms', 'Onions']}

def ShowMenu():
    os.system('cls')
    print("Available pizzas:\n")
    print(*available_pizzas, sep =' ,  ')
    print("\nAvailable toppings:\n")
    print(*available_toppings, sep =' ,  ')
    print("\n\n")   

def TakeOrderInput():
    order = input("Please enter your order: ")
    ordering = True
    while ordering:
        os.system('cls')
        ShowMenu()
        available_pizzas = input()
        if available_pizzas in available_pizzas:
            ordering = False
        else:
            print("Please enter a valid pizza")
            input("Press enter to continue")    
    return available_pizzas





    
