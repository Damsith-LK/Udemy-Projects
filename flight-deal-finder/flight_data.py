import requests
import config
import datetime as dt


class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self):
        self.tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_months_from_now = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")

    def find_cheap_flight(self, city_code: str) -> dict:
        """Finds the cheapest possible flight from Colombo to the given city (The city's IATA code is expected as a parameter.
        Returns the departure date, arrival date and price in GBP (British Pounds) in a dictionary"""
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

        data = response.json()["data"][0]
        arrival = data["local_arrival"]
        arrival_sepd = {"year": arrival.split("-")[0], "month": arrival.split("-")[1], "date": arrival.split("-")[2].split("T")[0]}
        arrival_sepd = {key: int(value) for (key, value) in arrival_sepd.items()}  # Turning the values in arrival_sepd to ints
        local_arrival = dt.datetime(year=arrival_sepd["year"], month=arrival_sepd["month"], day=arrival_sepd["date"])

        data_dict = {
            "departure": str(data["local_departure"]).split("T")[0],
            "return": (local_arrival + dt.timedelta(days=int(data['nightsInDest']))).strftime("%Y-%m-%d"),  # Calculating the date of return
            "price": int(data["price"])
        }
        return data_dict
