import pyowm
from pyowm import timeutils
from api_key import api_key

degree_sign = u'\N{DEGREE SIGN}'

owm = pyowm.OWM('518024a766d32327acf4b49f5e47e52f')

forecaster = owm.three_hours_forecast('Los Angeles, US')

time = datetime.now() + timedelta(days=0, hours=12)

weather = forecaster.get_weather_at(time)

temperature = weather.get_temparature(unit='fahrenheit')['temp']

print('The temperature at ' + time.strftime('%Y-%m-%d %H:%M:%S') + is + str(temperature) + degree_sign + 'F')


