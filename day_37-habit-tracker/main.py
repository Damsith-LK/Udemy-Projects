# In this program, we'll be using not only get() but also other methods - post(), put(), delete()

import requests
import config

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# # creating the user
# user_params = {
#     "token": config.TOKEN,
#     "username": config.USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# # created the user