import requests
import calendar


api_key = '518024a766d32327acf4b49f5e47e52f'
api_call = 'https;//api.openweathermap.org/data/2.5/forecast?appid=' +api_key

running = True

print('Welcome to John\'s 5 day weather forecast app using Open Weather Map\'s API!')

#program loop
while running:

    while True:

        # Input validation
        try:
            print('\nThis app supports search by city(0) or by zip code(1).')
            search = int(input('Please input 0 or 1: '))
        except ValueError:
            print("Sorry, I dont't get it.")
        else:

            #Passded the validation test
            if search == 0:
                city = input('Please input the city name:  ')
                if city.lower() =='sf':
                    city = 'San Francisco, US'