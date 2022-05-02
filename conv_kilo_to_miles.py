#Python convert kilometers to miles 
#with user input

import pygame
import sys
import math

# Define some colors
# Draw a circlular object
# Make the object the color BLUE
# Set the object's position
# Make the backgound WHITE
# Draw the object
# Draw the background
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Convert Kilometers to Miles")


kilometers = float(input("Enter the number of kilometers: "))

#conversion factor
conv_fac = 0.621371

#calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' % (kilometers, miles)) 

#convert Celcius to Fahrenheit
celsius = float(input("Enter the number of Celsius degrees: "))
fahrenheit = (celsius * 9/5) + 32
print('%0.3f Celsius degrees are equal to %0.3f degrees in Fahrenheit' % (celsius, fahrenheit))

# Program to generate a random number between 1 and 9 (including 1 and 9).

# Importing the random module.
import random

print(random.randint(0, 9))

print("The random number is", random.randint(0, 9))




