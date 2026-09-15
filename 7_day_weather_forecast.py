import requests
from datetime import datetime
import creds
#Sample Text: This is a sample text to demonstrate the functionality of the weather forecast app.
# OpenWeatherMap API endpoints
FORECAST_API = 'https://api.openweathermap.org/data/2.5/forecast'
ONECALL_API = 'https://api.openweathermap.org/data/3.0/onecall'

print('Welcome to John\'s 7 day weather forecast app using Open Weather Map\'s API!')

running = True

while running:
    # Get search method (by city or zip code)
    while True:
        try:
            print('\nThis app supports search by city (0) or by zip code (1).')
            search = int(input('Please input 0 or 1: '))
        except ValueError:
            print("Sorry, I didn't get that.")
            continue

        if search == 0:
            city = input('Please input the city name: ')
            if city.lower() == 'sf':
                city = 'San Francisco, US'
            
            # Get coordinates from city name using geocoding
            try:
                geocoding_url = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={creds.api_key}'
                geo_data = requests.get(geocoding_url).json()
                if not geo_data:
                    print('City not found. Please try again.')
                    continue
                lat = geo_data[0]['lat']
                lon = geo_data[0]['lon']
                location_name = f"{geo_data[0]['name']}, {geo_data[0].get('country', 'US')}"
            except Exception as e:
                print(f'Error retrieving location data: {e}')
                continue
            break

        elif search == 1:
            zip_code = input('Please input the zip code (US): ')
            
            # Get coordinates from zip code
            try:
                geocoding_url = f'https://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={creds.api_key}'
                geo_data = requests.get(geocoding_url).json()
                if 'lat' not in geo_data:
                    print('Zip code not found. Please try again.')
                    continue
                lat = geo_data['lat']
                lon = geo_data['lon']
                location_name = f"{geo_data['name']}, US"
            except Exception as e:
                print(f'Error retrieving location data: {e}')
                continue
            break

        else:
            print(f'{search} is not a valid option.')
            continue

    # Fetch 7-day forecast
    try:
        onecall_params = {
            'lat': lat,
            'lon': lon,
            'appid': creds.api_key,
            'units': 'metric'  # Use metric units for Celsius
        }
        response = requests.get(ONECALL_API, params=onecall_params)
        response.raise_for_status()
        weather_data = response.json()

        # Display location information
        print(f'\n--- 7 Day Forecast for {location_name} ---')
        print(f'Coordinates: {lat}, {lon}')
        print('=' * 60)

        # Display daily forecast
        if 'daily' in weather_data:
            for idx, day in enumerate(weather_data['daily'][:7]):
                # Convert timestamp to readable date
                forecast_date = datetime.fromtimestamp(day['dt'])
                day_name = forecast_date.strftime('%A, %B %d, %Y')
                
                print(f'\nDay {idx + 1}: {day_name}')
                print('-' * 60)
                
                # Temperature
                temp_min = day['temp']['min']
                temp_max = day['temp']['max']
                temp_celsius = day['temp']['day']
                
                print(f'Temperature (Current): {temp_celsius:.1f}°C ({temp_celsius * 9/5 + 32:.1f}°F)')
                print(f'Temperature Range: {temp_min:.1f}°C - {temp_max:.1f}°C')
                print(f'                   {temp_min * 9/5 + 32:.1f}°F - {temp_max * 9/5 + 32:.1f}°F')
                
                # Weather conditions
                weather_description = day['weather'][0]['main']
                weather_detail = day['weather'][0]['description']
                print(f'Weather: {weather_description} ({weather_detail.title()})')
                
                # Feels like temperature
                feels_like = day['feels_like']['day']
                print(f'Feels Like: {feels_like:.1f}°C ({feels_like * 9/5 + 32:.1f}°F)')
                
                # Humidity and pressure
                humidity = day['humidity']
                pressure = day['pressure']
                print(f'Humidity: {humidity}%')
                print(f'Pressure: {pressure} hPa')
                
                # Wind speed
                wind_speed = day['wind_speed']
                wind_speed_mph = wind_speed * 2.237  # Convert m/s to mph
                print(f'Wind Speed: {wind_speed:.1f} m/s ({wind_speed_mph:.1f} mph)')
                
                # UV Index
                if 'uvi' in day:
                    uvi = day['uvi']
                    print(f'UV Index: {uvi:.1f}')
                
                # Cloud coverage
                clouds = day['clouds']
                print(f'Cloud Coverage: {clouds}%')
                
                # Precipitation chance (if available)
                if 'pop' in day:
                    precipitation_prob = day['pop'] * 100
                    print(f'Precipitation Probability: {precipitation_prob:.0f}%')

        print('\n' + '=' * 60)

    except requests.exceptions.RequestException as e:
        print(f'Error fetching weather data: {e}')
        continue

    # Ask if user wants to continue
    while True:
        user_input = input("\nWould you like to check another location? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            print('\nGREAT!')
            break
        elif user_input in ['no', 'n', 'exit']:
            print('\nThank you for using the 7-day weather forecast app!')
            print('Have a great day!')
            running = False
            break
        else:
            print('Sorry, I didn\'t get that. Please enter yes or no.')
