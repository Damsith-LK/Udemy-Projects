import requests
import config


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destinations = []

    def get_destinations(self):
        response = requests.get(config.SHEETY_ENDPOINT)
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
                url=f"{config.SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)