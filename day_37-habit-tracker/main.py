# In this program, we'll be using not only get() but also other methods - post(), put(), delete()
# I'm using this to keep track of my meditation

import requests
import config

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
graph_response = requests.post(url=f"{PIXELA_ENDPOINT}/{config.USERNAME}/graphs", json=graph_params, headers=headers)
print(graph_response.text)
# created the graph