import requests
from datetime import datetime
import smtplib
import time

My_Email = "cse24083@iiitkalyani.ac.in"
My_Password = ""
My_LAT = 22.9654752
My_LONG = 88.4276363

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitue = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if My_LAT - 5 <= iss_latitue <= My_LAT + 5 and My_LONG - 5 <= iss_longitude <= My_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": My_LAT,
        "lng": My_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(My_Email, My_Password)
        connection.sendmail(
            from_addr=My_Email,
            to_addrs=My_Email,
            msg="Subject:Look Up for ISS \n\nThe ISS is above you in the sky!"
        )