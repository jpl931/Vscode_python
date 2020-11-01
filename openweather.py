import requests,json

api_key = "518024a766d32327acf4b49f5e47e52f"
base_url = "https://api.openweathermap.org/data/2.5/weather?"


city_name = input("Enter the city bane: ")

complete_url = base_url + "appid" + api_key + "&q=" +city_name

response = requests.get(complete_url)

x = response.json

"404 error message"
if x["cod"] != "404" :
    y = x['main']

    current_temperature = y["temp"]

    current_pressure = y["pressure"]

    current_humidity = y["humidity"]

    z = x["wearher"]

    weather_description = z[0]["description"]

    print(" Temperature(in Kelvin unit)= " + 
                        str(current_temperature ) +
                        "\n atmospheric pressure (in hPa unit) =" +
                        str(current_pressure) +
                        "\n humidity (in percentage) = " +
                        str(current_humidity) +
                        "\n description = " +
                        str(weather_description))

else:
    print("City Not Found")
                        


