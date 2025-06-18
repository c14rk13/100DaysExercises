import os

import requests
from datetime import datetime

NUTRI_APP_ID = os.environ.get("NUTRI_APP_ID")
NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")


NUTRI_URL = "https://api.syndigo.com"
NUTRI_EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_URL = f"https://api.sheety.co/{SHEETY_API_KEY}/workoutTracking/workouts"


def get_auth_token():
    auth_url = f"{NUTRI_URL}/auth"
    auth_params = {
        "username": NUTRI_APP_ID,
        "secret": NUTRI_API_KEY
    }
    response = requests.post(url=auth_url, params=auth_params)
    auth_token = response.json()["value"]

    return auth_token


def get_exercise_details():
    nutri_exercise_headers = {
        "Content-Type": "application/json",
        "x-app-id": NUTRI_APP_ID,
        "x-app-key": NUTRI_API_KEY
    }

    exercises_done = input("Tell me which exercises you did: ")

    nutri_body_data = {
        "query": exercises_done
    }

    response = requests.post(url=NUTRI_EXERCISE_URL, headers=nutri_exercise_headers,
                             json=nutri_body_data)
    response.raise_for_status()

    return response.json()["exercises"]

    # Test run:
    # input: Walked for 45 minutes around burnham park
    # response: {'exercises':
    #   [{'tag_id': 100, 'user_input': 'walked', 'duration_min': 45, 'met': 3.5, 'nf_calories': 183.75,
    #       'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg',
    #       'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg', 'is_user_uploaded': False},
    #       'compendium_code': 17190, 'name': 'walking', 'description': None, 'benefits': None}]}


exercises = get_exercise_details()
today = datetime.now().date().strftime("%d/%m/%Y")
current_time = datetime.now().time().strftime("%X")

workout_header = {
    "Authorization": f"Bearer {SHEETY_AUTH}"
}

for exercise in exercises:
    workout_data = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_URL, headers=workout_header, json=workout_data)
    print(response.text)
    # RESPONSE: {
    #       "workout": {
    #           "date": "09/06/2025",
    #           "time": "22:59:06",
    #           "exercise": "walking",
    #           "duration": 45,
    #           "calories": 183.75,
    #           "id": 3
    #       }
    #     }


