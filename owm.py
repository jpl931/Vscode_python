from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------------------API KEY --------------

owm = OWM('518024a766d32327acf4b49f5e47e52f')
mgr = owm.weather_manager()

#---------------------current weather Lond,GB

w = observation.weather

w.detailed_status
w.wind
w.temperature(celcius)
w.rain
w.heat_index
w.clouds

#Foreczst Lomdon
forecast = mgr.forecast_at_place('London,GB', 'daily')