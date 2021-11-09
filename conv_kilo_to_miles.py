#Python convert kilometers to miles 
#with user input
kilometers = float(input("Enter the number of kilometers: "))

#conversion factor
conv_fac = 0.621371

#calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' % (kilometers, miles)) 

#convert Celcius to Fahrenheit
celsius = float(input("Enter the number of Celsius degrees: "))
fahrenheit = (celsius * 9/5) + 32
print('%0.3f Celsius is equal to %0.3f Fahrenheit' % (celsius, fahrenheit))

# Program to generate a random number between 1 and 9 (including 1 and 9).

# Importing the random module.
import random

print(random.randint(0, 9))



