import requests
from datetime import date


def get_weather(city, units):
    today = date.today()
    API_KEY = "518024a766d32327acf4b49f5e47e52f"
    URL =f'https://api.openweathermap.org/data/2.5/weather?q={London}&appid={API_KEY}&units={units}'


    json_data = requests.get(URL).json()

    main = json_data['main']
    temp = main['temp']
    temp_max = main['temp_max']
    temp_min = main['temp_min']
    humididy = main['humidity']
    pressure = main['pressure']

    with open('weather.txt', 'w') as f:
        f.write(str(today) + '\n' + "Current Temperature: ")
                + str(temp) + '\n' + "Max Temperature: " +
                str(temp_max) + '\n' + "Minimum Temperature: " + str(temp_min)
                + '\n' + "Humidity: " +str(humidity) + "%" + '\n')