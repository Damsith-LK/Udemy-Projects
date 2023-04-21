import requests
import config


class DataManager:
    """This class is responsible for talking to Sheety"""

    def __init__(self):
        self.destinations = []

    def get_destinations(self):
        response = requests.get(config.SHEETY_PRICES_ENDPOINT)
        self.destinations = response.json()["prices"]
        return self.destinations

    def update_destinations(self):
        for city in self.destinations:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{config.SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=config.SHEETY_USERS_ENDPOINT)
        email_list = []

        for user in response.json()["users"]:
            user_email = user["email"]
            email_list.append(user_email)

        return email_list