# Habit Tracker
import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = "HabitTrackerSecret"
USERNAME = "sj-dev-2004"
USER_ENDPOINT = "https://pixe.la/@sj-dev-2004"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "sjgraph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Test Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "18"
}

# response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

date_to_update = datetime(year=2026, month=5, day=16).strftime("%Y%m%d")

update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"

new_pixel_config = {
    "quantity": "50"
}

# response = requests.put(url=update_pixel_endpoint, json=new_pixel_config, headers=headers)
# print(response.text)

date_to_delete = datetime(year=2026, month=5, day=17).strftime("%Y%m%d")

delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)