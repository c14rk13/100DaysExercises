import requests
from flight_data import FlightData
import os
from dotenv import load_dotenv

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        load_dotenv()
        self.TOKEN = None
        self.FLIGHT_URL = os.getenv("URL_FLIGHT_DEALS")
        self.API_KEY_FLIGHT_DEALS = os.getenv("API_KEY_FLIGHT_DEALS")
        self.API_SECRET_FLIGHT_DEALS = os.getenv("API_SECRET_FLIGHT_DEALS")
        self.MAX_OFFERS = 20

        self.get_token()

        self.req_header = {
            "Authorization": f"Bearer {self.TOKEN}"
        }


    # Token expires every 30mins
    def get_token(self):
        req_body = {
            "client_id": self.API_KEY_FLIGHT_DEALS,
            "client_secret": self.API_SECRET_FLIGHT_DEALS,
            "grant_type": "client_credentials"
        }
        response = requests.post(url=f"{self.FLIGHT_URL}/v1/security/oauth2/token", data=req_body)
        self.TOKEN = response.json()["access_token"]

            # {
            #     "type": "amadeusOAuth2Token",
            #     "username": ,
            #     "application_name": "Flight Deal Finder",
            #     "client_id": ,
            #     "token_type": "Bearer",
            #     "access_token": ,
            #     "expires_in": ,
            #     "state": "approved",
            #     "scope": ""
            # }



    def get_iata_code(self, city):
        url = f"{self.FLIGHT_URL}/v1/reference-data/locations"
        params = {
            "subType": "CITY",
            "keyword": city
        }

        data = None

        try:
            response = requests.get(url=url, params=params, headers=self.req_header)
            response.raise_for_status()
            data = response.json()["data"]
        except requests.exceptions.HTTPError as errh:
            print(errh.response)
            
        return data



    def get_flight_prices(self, details: FlightData):
        url = f"{self.FLIGHT_URL}/v2/shopping/flight-offers"
        params = {
            "originLocationCode": details.ORIGIN_IATA_CODE,
            "destinationLocationCode": details.DESTINATION,
            "departureDate": details.FLIGHT_DATE,
            "returnDate": details.RETURN_DATE,
            "adults": 1,
            "currencyCode": details.CURRENCY,
            "nonStop": details.NONSTOP,
            "maxPrice": details.MAX_PRICE,
            "max": self.MAX_OFFERS
        }

        data = []
        try:
            response = requests.get(url=url, params=params, headers=self.req_header)
            response.raise_for_status()
            data = response.json()["data"]
                # List of flight offers
                # [data][n][price][grandTotal] -- x.data[0].price.grandTotal
        except requests.exceptions.HTTPError as errh:
            print(errh.response)

        return data



