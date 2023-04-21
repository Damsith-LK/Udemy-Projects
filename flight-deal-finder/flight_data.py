import requests
import config
import datetime as dt
from pprint import pprint


class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self, max_stop_overs: int = 1, via_city: str = ""):
        self.max_stop_overs = max_stop_overs
        self.via_city = via_city
        self.tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_months_from_now = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")

    def find_cheap_flight(self, city_code: str) -> dict or None:
        """Finds the cheapest possible flight from Colombo to the given city. The city's IATA code is expected as a parameter.
        Returns the departure date, arrival date, price in GBP (British Pounds), number of stop-overs and via cities in a dictionary"""
        params = {
            "fly_from": "CMB",
            "fly_to": city_code,
            "date_from": self.tomorrow,
            "date_to": self.six_months_from_now,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0
        }
        headers = {"apikey": config.KIWI_API_KEY}
        response = requests.get(url=f"{config.KIWI_ENDPOINT}/v2/search", params=params, headers=headers)

        try:  # Avoiding a error (if no flights)
            data = response.json()["data"][0]
        except IndexError:
            if self.max_stop_overs > 0:
                params["max_stopovers"] = self.max_stop_overs
                response = requests.get(url=f"{config.KIWI_ENDPOINT}/v2/search", params=params, headers=headers)

                try:
                    data = response.json()["data"][0]
                except IndexError:
                    return None
                else:
                    arrival = data["local_arrival"]
                    arrival_sepd = {"year": arrival.split("-")[0], "month": arrival.split("-")[1],
                                    "date": arrival.split("-")[2].split("T")[0]}
                    arrival_sepd = {key: int(value) for (key, value) in
                                    arrival_sepd.items()}  # Turning the values in arrival_sepd to ints
                    local_arrival = dt.datetime(year=arrival_sepd["year"], month=arrival_sepd["month"],
                                                day=arrival_sepd["date"])
                    via_cities = []
                    for i in data["route"]:
                        city = i["cityTo"]
                        if city not in via_cities and city != "Colombo":
                            via_cities.append(city)

                    data_dict = {
                        "departure": str(data["local_departure"]).split("T")[0],
                        "return": (local_arrival + dt.timedelta(days=int(data['nightsInDest']))).strftime("%Y-%m-%d"),
                        # Calculating the date of return
                        "price": int(data["price"]),
                        "stop_overs": len(via_cities),
                        "via_cities": via_cities
                    }
                    return data_dict

            else:
                return None

        else:
            arrival = data["local_arrival"]
            arrival_sepd = {"year": arrival.split("-")[0], "month": arrival.split("-")[1], "date": arrival.split("-")[2].split("T")[0]}
            arrival_sepd = {key: int(value) for (key, value) in arrival_sepd.items()}  # Turning the values in arrival_sepd to ints
            local_arrival = dt.datetime(year=arrival_sepd["year"], month=arrival_sepd["month"], day=arrival_sepd["date"])

            data_dict = {
                "departure": str(data["local_departure"]).split("T")[0],
                "return": (local_arrival + dt.timedelta(days=int(data['nightsInDest']))).strftime("%Y-%m-%d"),  # Calculating the date of return
                "price": int(data["price"]),
                "stop_overs": 0,
                "via_cities": None
            }
            return data_dict



# test = FlightData()
# test.find_cheap_flight("NYC")
