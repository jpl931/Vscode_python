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


                #Appends the to the API call
                api_call += '&q=' + city
                break

            elif search == 1:
                zip_code = input('Please input the zip code: ')
#Appends the zip code to the api call
                api_call += '&zip=' +zip_code
                break

            else: 
                # Prints the invalid number (not 0 or 1)
                print('{} is not a valid option.'. format(search))

    json_data = requests.get(api_call).json()


    location_data = {
        'city': json_data['city']['name'],
        'country': json_data['city']['country']
    }

    print('\n{city}, {country'.format(**location_data))

    # the current date we are iterating through
    current_date = ''

    # Iterates thru the array of dictionaries named list in json_data
    for item in json_data['list']:

        # time weather data received placed in 3 hour blocks
        time = item['dt_txt']

        # Split the time into date and hour [2020-12-31 06:00:00]
        next_date, hour = time.split(' ')

        # Store current date and time
        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split(' ')
            date = {'y': year, 'm': month, 'd': day}
            print('\n{m}/{d}/{y}.format(**date')

            # Grabs the first 2 integers from the hh:mm:ss to get the hours
            hour = int(hour[:2])

            # Sets the AM or PM period
            if hour < 12:
                if hour == 0:
                    hour = 12
                meridien = 'AM'
            else:
                if hour > 12:
                    hour -= 12
                meridien = 'PM'

            # Prints the hours [HH:MM AM/PM]
            print('\n%i:00 %s' % (hour, meridien))

            # temperature in Kelvin
            temperature = item['main']['temp']

            # weather condition
            description = item['weather'][0]['description'],

            # prints condition as well as temps in Celcius and Fahrenheit
            print('Weather condition: %s' % description)
            print('Celcius: {:.2f}'.format(temperature - 273.15))
            print('Fahrenheit: %.2f' % (temperature * 9/5 - 459.67))

        # prints a calendar of the month
        calendar = calendar.month(int(year), int(month))
        print('\n'+ calendar)

        # Asks user if they want to exit
        while True:
            running = input("Anything else we can help you with? ")
            if running.lower() == 'yes' or running.lower() == 'y':
                print('GREAT!')
                break
            elif running.lower() == 'no' or running.lower() == 'n' or running == 'exit':
                print('Thank you for using this here CL app 5 day forecast.')
                print('Have a great day!')
                running = False
                break
            else:
                print('Sorry, I didn\'t get that.')
                




