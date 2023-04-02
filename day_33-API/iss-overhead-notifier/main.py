import requests
from datetime import datetime
import smtplib as smtp
import config

MY_LAT = 7.091150
MY_LONG = 79.999634

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise, sunset)

time_now = datetime.now().hour
print(time_now)

# If the ISS is close to my current position - Done
# and it is currently dark - Done
# Then send me an email to tell me to look up. - Done

if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5 and sunset - 2 < time_now < sunset + 6:
    with smtp.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(user=config.my_email, password=config.password)
        conn.sendmail(from_addr=config.my_email, to_addrs=config.send_email,
                      msg="Subject:Look up"
                          "\n\nThe International Space Station is above you. Quick!!!"
                      )
else:
    print("International space Station is not above you")
# BONUS: run the code every 60 seconds.