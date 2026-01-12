import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
print(data)

# if response.status_code == 404:
#     raise Exception("The requested resource doesn't exist!")
# if response.status_code == 401:
#     raise Exception("You are not authorised to access this resource!")

response.raise_for_status()