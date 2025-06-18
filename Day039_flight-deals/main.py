#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from typing import List

# Program Requirements
#   Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
#   International Air Transport Association (IATA) codes for each city. Most of the cities
#   in the sheet include multiple airports, you want the city code (not the airport code see here).
#
#   Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later
#   for all the cities in the Google Sheet.

#   If the price is lower than the lowest price listed in the Google Sheet then
#   send an SMS (or WhatsApp Message) to your own number using the Twilio API.
#
#   The SMS should include the departure airport IATA code, destination airport IATA code,
#   flight price and flight dates.


from data_manager import *
from flight_search import *
from notification_manager import *
from datetime import datetime, timedelta

dm = DataManager()

sheet_data = dm.get_sheet_data()
print(sheet_data)

# check if sheet_data contains any values for the "iataCode" key.
# If not, then the IATA Codes column is empty in the Google Sheet.
# In this case, pass each city name in sheet_data one-by-one to the FlightSearch class.
# For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code.
# You should use the response from the FlightSearch class to update the sheet_data dictionary
# Test api only contains airport search for United States, Spain, United Kingdom, Germany and India
#

flight_search = FlightSearch()
flights_to_search: List[FlightData] = []

# Calculate date tomorrow and 6 months from now
tomorrow = (datetime.now() + timedelta(days=1)).strftime(format="%Y-%m-%d")
return_date = (datetime.now() + timedelta(days=180)).strftime(format="%Y-%m-%d")

for item in sheet_data:
    # Update missing IATA Code
    if item["iataCode"] == "":
        city_data = flight_search.get_iata_code(item["city"])
        if not city_data is None and not city_data == []:
            dm.update_iata_code(item["id"], city_data[0]["iataCode"])
            item["iataCode"] = city_data[0]["iataCode"]

    if not item["iataCode"] == "":
        # Prepare list of flight data
        flight = FlightData()
        flight.DESTINATION_CITY = item["city"]
        flight.DESTINATION = item["iataCode"]
        flight.MAX_PRICE = item["lowestPrice"]
        flight.FLIGHT_DATE = tomorrow
        flight.RETURN_DATE = return_date
        flights_to_search.append(flight)

#  Loop through each flight to search and check for cheapest flight
notifier = NotificationManager()
for flight_to_search in flights_to_search:
    print(f"Getting flights for {flight_to_search.DESTINATION_CITY}...")
    flight_offer = flight_search.get_flight_prices(flight_to_search)
    cheapest_flight = flight_to_search.find_cheapest_flight(flight_offer)
    if cheapest_flight == 0:
        print(f"{flight_to_search.DESTINATION_CITY}: No flights available")
    else:
        print(f"{flight_to_search.DESTINATION_CITY}: {flight_to_search.CURRENCY_SYMBOL}{cheapest_flight}")
        notifier.send_whatsapp(flight_to_search) # Send notification


