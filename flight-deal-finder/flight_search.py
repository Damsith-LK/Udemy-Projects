import requests
import config

class FlightSearch:

    # This class is responsible for talking to the Flight Search API.

    def give_city_id(self, city) -> str:

        params = {"term": city}
        headers = {"apikey": config.KIWI_API_KEY, "limit": "1"}
        response = requests.get(url=f"{config.KIWI_ENDPOINT}/locations/query", params=params, headers=headers)
        return response.json()["locations"][0]["code"]