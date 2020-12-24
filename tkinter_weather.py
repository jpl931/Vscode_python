from tkinter import *
import pyowm

def open_weather_map():
    owm pyowm.OWM('518024a766d32327acf4b49f5e47e52f')
    city_name = entry.get()
    observation = owm,weather_at_place
    w = observation.get_weather()
    temp = w.get_temperature(unit = 'imperial')
    label1['temp'] = temp

    