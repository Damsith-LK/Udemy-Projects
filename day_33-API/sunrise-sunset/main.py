import requests
import datetime as dt

parameters = {"lat": 6.927079, "lng": 79.861244, "formatted": 0}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]

sunrise_hour = data["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["sunset"].split("T")[1].split(":")[0]

print(f"The sunrise hour for today is {sunrise_hour} and the sunset hour for today is {sunset_hour}. \nThe hour now is {dt.datetime.now().hour} \nNote that hours in here are in 24 hour format")