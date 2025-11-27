# Read - json.load()
# Write - json.dump()
# Update- json.update()
import json

website = input("Enter Website Name: ")
email = input("Enter Email: ")
password = input("Enter Password: ")
new_data = {
    website: {"email": email, "password": password}
}

with open("data.json", "w") as data:
    json.dump(new_data, data)