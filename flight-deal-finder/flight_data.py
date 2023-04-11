import requests
import config
import datetime as dt


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_months_from_now = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")

    def find_cheap_flight(self, city_code: str):
        """Finds the cheapest possible flight from Colombo to the given city (The city's IATA code is expected as a parameter.
        Returns the price in GBP (British Pounds)"""
        params = {
            "fly_from": "CMB",
            "fly_to": city_code,
            "date_from": self.tomorrow,
            "date_to": self.six_months_from_now,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP"
        }
        headers = {"apikey": config.KIWI_API_KEY}
        response = requests.get(url=f"{config.KIWI_ENDPOINT}/v2/search", params=params, headers=headers)
        return response.json()["data"][0]["price"]
