import requests
from datetime import date


def get_weather(city, units):
    today = date.today()
    API_KEY = "api_address = 'http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&APPID=518024a766d32327acf4b49f5e47e52f&q="

    URL =f'https://api.openweathermap.org/data/2.5/weather?zip=63048,us&appid={API_KEY}&units={units}'


    json_data = requests.get(URL).json()

    main = json_data['main']
    temp = main['temp']
    temp_max = main['temp_max']
    temp_min = main['temp_min']
    humidity = main['humidity']
    pressure = main['pressure']





            