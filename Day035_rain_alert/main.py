import util
import requests
from twilio.rest import Client

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
    # weather data: ["list"][n]
    #         ["dt"]
    #         [dt_txt] -- ex. 2025-06-03 12:00:00
    #         ["weather"][0]
    #             ["id"] -- 500 for rain; Any code < 700 umbrella (snow, rain, drizzle, thunderstorm)
    #             ["main"] -- "Rain"

    # Check if it will rain in the next 12 hours (first 4 items in the list)

def will_rain_today():
    umbrella_needed = False
    url_5day_3hrs = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = get_api_key()
    params = {
        "lat": MY_LAT,
        "lon": MY_LNG,
        "cnt": 4, # Need only the 1st 4 items in the forecast to check the next 12 hours
        "appid": api_key
    }

    response = requests.get(url=url_5day_3hrs, params=params)
    response.raise_for_status()
    weather_data = response.json()


    for hour_weather in weather_data["list"]:
        weather_code = hour_weather["weather"][0]["id"]
        if weather_code < 700:
            umbrella_needed = True
            break # exit loop once it's determined that there's chance of rain

    return umbrella_needed



def send_sms(): # Playground only -- unable to send sms using trial US # to PH #
    twilio_acct = util.read_config("Twilio")

    client = Client(twilio_acct["account_sid"], twilio_acct["auth_token"])
    message = client.messages.create(
        body="Bring an umbrella. You'll probably need it!",
        from_= twilio_acct["from"],
        to= twilio_acct["to"]
    )

    print(message.status)


def send_whatsapp():
    twilio_acct = util.read_config("Twilio")

    client = Client(twilio_acct["account_sid"], twilio_acct["auth_token"])
    message = client.messages.create(
        from_=f'whatsapp:{twilio_acct["whatsapp_from"]}',
        body="Bring an umbrella. You'll probably need it!",
        to=f'whatsapp:{twilio_acct["whatsapp_to"]}'
    )

    print(message.status)


if will_rain_today():
    send_whatsapp()
