import requests

api_key = "518024a766d32327acf4b49f5e47e52f"
api_address = 'http://api.openweathermap.org/data/2.5/weather?APPID=518024a766d32327acf4b49f5e47e52f&q='

base_url = "http://api.openweathermap.org/data/2.5

city = "Herculaneum"
parameters = {"key":api_key, "q":city}       #URL parameters

r = requests.get(f"{base_url}/current.json" , params=parameters)

data = r.json()                            #retreive the json data...maybe

print(data)

