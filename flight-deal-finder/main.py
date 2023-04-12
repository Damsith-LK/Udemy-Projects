# Day 39 and 40 - Flight Deal Finder
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

"""
Program requirements -

1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
   International Air Transport Association (IATA) codes for each city.
   Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
3. If the price is lower than the lowest price listed in the Google Sheet then send an e-mail to your own e-mail
"""

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destinations()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"] = flight_search.give_city_id(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destinations()

for i in sheet_data:
    data = flight_data.find_cheap_flight(i["iataCode"])
    price_data = data["price"]
    lowest_price = i["lowestPrice"]

    if price_data <= lowest_price:
        notification_manager.send_email(lowest_price, i["city"], i["iataCode"], data["departure"], data["return"])
        print("E-mail sent.")

