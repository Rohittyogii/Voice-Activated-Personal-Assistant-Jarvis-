import requests
from ss import *

# Assuming key2 is your OpenWeatherMap API key
api_key = key2
latitude = 37.7749  # Replace with your desired latitude
longitude = -122.4194  # Replace with your desired longitude

api_address = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

json_data = requests.get(api_address).json()

def temp():
    try:
        temperature = round(json_data["main"]["temp"] - 273.15, 1)
        return temperature
    except KeyError:
        return "Temperature data not available"

def des():
    try:
        description = json_data["weather"][0]["description"]
        return description
    except KeyError:
        return "Weather description not available"


