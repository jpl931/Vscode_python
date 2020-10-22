import requests
# weather api
api_address = 'http://api.openweathermap.org/data/2.5/weather?APPID=518024a766d32327acf4b49f5e47e52f&q='
city = input("City Name: ")
print()

url = api_address + city
json_data = requests.get(url).json()

formatted_data = json_data['weather'][0]['description']
print(formatted_data.capitalize())
#test