# Modified script to be run in PythonAnywhere site
# All config items referenced as environment variables
# In pyCharm, use command: "dir Env:" to see the environment variables

import os
import smtplib
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY_NAME = "Baguio"
MY_LAT = 16.402332
MY_LNG = 120.596008


def email_me(msg):
    my_email = os.environ.get("EMAIL_FROM")
    password = os.environ.get("EMAIL_PASS") # App password
    to_address = os.environ.get("EMAIL_TO").split(";")
    smtp_server = os.environ.get("EMAIL_SERVER")

    with smtplib.SMTP(smtp_server) as connection: # using "with" closes the connection automatically after
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=msg
        )



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
    api_key = os.environ.get("WEATHER_API_KEY")
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


def send_whatsapp():
    acct_id = os.environ.get("TWILIO_ACCT_ID")
    auth_token = os.environ.get("TWILIO_AUTH")
    whatsapp_from = os.environ.get("WHATSAPP_FROM")
    whatsapp_to = os.environ.get("WHATSAPP_TO")

    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

    client = Client(acct_id, auth_token, http_client=proxy_client)
    message = client.messages.create(
        from_=f"whatsapp:{whatsapp_from}",
        body="Bring an umbrella. You'll probably need it!",
        to=f"whatsapp:{whatsapp_to}"
    )

    print(message.status)


if will_rain_today():
    send_whatsapp()
    email_me("Bring an umbrella. You'll probably need it!")
