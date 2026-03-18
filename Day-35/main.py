import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = ""

weather_params = {
    "lat": 51.759048,
    "lon": 19.458599,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Carry an Umbrella!")