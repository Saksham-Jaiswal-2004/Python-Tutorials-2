import requests
from datetime import datetime

APP_ID = ""
APP_KEY = ""
SHEETY_BEARER_TOKEN = ""

WEIGHT = 82
HEIGHT = 182
AGE = 22
GENDER = "male"

WORKOUT_ENDPOINT = "https://app.100daysofpython.dev"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

calories_endpoint = f"{WORKOUT_ENDPOINT}/v1/nutrition/natural/exercise"

workout_config = {
    "query": "ran 3 miles",
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER
}

response = requests.post(url=calories_endpoint, json=workout_config, headers=headers)
workout_name = response.json()["exercises"][0]["name"].title()
workout_duration = response.json()["exercises"][0]["duration_min"]
workout_calories =response.json()["exercises"][0]["nf_calories"]
print(workout_name)
print(workout_duration)
print(workout_calories)

SHEETY_ENDPOINT = "https://api.sheety.co/241d48952020016014b8dac67cba1b6a/myWorkouts/workouts"

workout_sheet_config = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": workout_name,
        "duration": workout_duration,
        "calories": workout_calories
    }
}

headers = {
    "Authorization": SHEETY_BEARER_TOKEN
}

response = requests.post(url=SHEETY_ENDPOINT, json=workout_sheet_config, headers=headers)
print(response.text)

