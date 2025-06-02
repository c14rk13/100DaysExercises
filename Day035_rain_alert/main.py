import util
import requests

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY_NAME = "Baguio"
MY_LAT = 16.402332
MY_LNG = 120.596008


def get_api_key():
    return util.read_config("Weather")["api_key"]


def check_current_weather(): #Just a playground
    api_key = get_api_key()
    params = {
        "q": CITY_NAME,
        "units": "metric",
        "appid": api_key
    }

    response = requests.get(url=WEATHER_URL, params=params)
    response.raise_for_status()
    data = response.json()
    weather = data["weather"][0]["main"] #Check for "Rain"

    print(f"Main weather is {weather}")



# 5x-a-day weather forecast:
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}