# In this program, we'll be using not only get() but also other methods - post(), put(), delete()
# I'm using this to keep track of my meditation

import requests
import config
import datetime
from datetime import timezone

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# # creating the user
user_params = {
    "token": config.TOKEN,
    "username": config.USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# # created the user

# Creating a graph
graph_params = {
    "id": "graph1",
    "name": "Meditation",
    "unit": "minutes",
    "type": "float",
    "color": "momiji"  # momoji == red
}
headers = {"X-USER-TOKEN": config.TOKEN}
# graph_response = requests.post(url=f"{PIXELA_ENDPOINT}/{config.USERNAME}/graphs", json=graph_params, headers=headers)
# print(graph_response.text)
# created the graph

# Updating the graph
day = input("What do you want to update? (day before yesterday or yesterday or today): ").lower()
minutes = input("How long did you meditate (minutes): ")

if day == 'day before yesterday':
    date = datetime.datetime.now() - datetime.timedelta(days=2)
elif day == "yesterday":
    date = datetime.datetime.now() - datetime.timedelta(days=1)
else:
    date = datetime.datetime.now()

update_params = {
    "date": str(date.strftime("%Y%m%d")),
    "quantity": str(minutes)
}
update_response = requests.post(url=f"{PIXELA_ENDPOINT}/{config.USERNAME}/graphs/graph1", json=update_params, headers=headers)
print(update_response.text)