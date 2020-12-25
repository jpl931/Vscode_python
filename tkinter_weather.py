from tkinter import *
import pyowm

def open_weather_map(event):
    owm = pyowm.OWM('518024a766d32327acf4b49f5e47e52f')
    city_name = entry1.get()
    observation = owm.weather_at_place('London, UK')
    w = observation.get_weather()
    temp = w.get_temperature(unit = 'celcius')
    label1['temp'] = temp

window = Tk()
window.geometry('300x300')
window.title('Weather')

entry1 = Entry(window, width = 25, font = ('Arial' ,16))
entry1.pack()

button1 = Button(window, text = 'Submit' , font = ('Arial' , 16))
button1.pack()

label1 = Label(window, font = ('Arial' , 20, 'bold'))
label1.pack()

button1.bind("<Button-1>", open_weather_map)
window.mainloop()


