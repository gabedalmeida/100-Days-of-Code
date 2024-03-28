import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.140049
MY_LNG = 8.647334


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = int(data["iss_position"]["longitude"])
    iss_latitude = int(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG +5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    
    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True 
    
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login("?","?") 
        connection.sendmail(
            from_addr="?",
            to_addrs="?",
            msg="Subject:Look UP\n\nThe ISS is above you in the sky."
                            )
