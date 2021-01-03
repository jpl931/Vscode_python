import requests
import json
import pprint
import csv
import sys

api_key = "518024a766d32327acf4b49f5e47e52f"

#where

lat = "38.627003"

lon = "-90.199402"

url ="https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)


response = requests.get(url)

data = json.loads(response.text)

#print(data)
#pp = pprint.PrettyPrinter(indent=7)

#pprint(response.json())

location = data['location']['name']






print(f"Location: {location}")




