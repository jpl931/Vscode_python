import requests, json

api_key = " 18024a766d32327acf4b49f5e47e52f"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]

    current_pressure = y["pressure"]

    current_humidity = y["humidity"]

    z = x["weather"]

    weather_description = z[0] ["description"]

    print(" Temperature (in Kelvin unit) = " + str(current_temperature + "\n atmospheric pressure ")
