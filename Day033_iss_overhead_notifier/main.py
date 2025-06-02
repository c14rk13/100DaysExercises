import time

import requests as req
from datetime import datetime, timezone
import email_me

# Baguio City, PH
MY_LAT = 16.402332
MY_LNG = 120.596008
POSITION_DIFF_MAX = 5


def get_sunset_sunrise_hours():
    # Get sunset time: easier to spot ISS in the sky when it's dark
    sunset_url = "https://api.sunrise-sunset.org/json"
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = req.get(sunset_url, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    # Get the hour of sunrise give the format returned is 2025-05-29T21:23:09+00:00
    # So, split by "T", then split by ":"
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    return {
        "sunrise": sunrise_hour,
        "sunset": sunset_hour
    }


# Get ISS position, return true if with +/- 5 degrees
def is_iss_near_me():
    is_near = False

    response = req.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data= response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    is_near = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5

    return  is_near



now = datetime.now(timezone.utc)
now_hour = now.hour



# If iss is close to current position, and it is currently dark, then, send an email to me to look up
# BONUS: run the code every 60 seconds

# TODO: check the sunset/sunrise hours only once daily
sun_set_rise = get_sunset_sunrise_hours()

# Loop every hour seconds
# Check current hour first, if it's between sunset and sunrise (still dark)
#   only then check iss position (prevents calling the iss api unnecessarily)
while True:
    time.sleep(3600)
    if sun_set_rise["sunset"] <= now_hour <= sun_set_rise["sunrise"]:
        if is_iss_near_me():
            # Email myself
            print(f"ISS is near! - {now}")
            mail_msg = "Subject:ISS is overhead\n\nLook up!"
            email_me.email_me(mail_msg)

