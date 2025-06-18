import requests
import os
from dotenv import load_dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        load_dotenv()
        self.API_AUTH = os.getenv("SHEET_API_AUTH")
        self.URL_SHEET_FLIGHTS = os.getenv("SHEET_URL_FLIGHTS")
        self.api_headers = {
            "Authorization": self.API_AUTH
        }
        self.prices = []



    def get_sheet_data(self):
        response = requests.get(url=self.URL_SHEET_FLIGHTS, headers=self.api_headers)
        self.prices = response.json()["prices"]
        # {'prices': [{'city': 'Tokyo - Haneda', 'iataCode': 'HND', 'lowestPrice': 110, 'id': 2},
        #             {'city': 'Tokyo - Narita', 'iataCode': 'NRT', 'lowestPrice': 65, 'id': 3},
        #             {'city': 'Ha Noi', 'iataCode': 'HAN', 'lowestPrice': 100, 'id': 4},
        #             {'city': 'Da Nang', 'iataCode': 'DAD', 'lowestPrice': 110, 'id': 5},
        #             {'city': 'Barcelona', 'iataCode': 'BCN', 'lowestPrice': 385, 'id': 6},
        #             {'city': 'Vienna', 'iataCode': 'VIE', 'lowestPrice': 310, 'id': 7}]}

        return self.prices



    def update_iata_code(self, id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.URL_SHEET_FLIGHTS}/{id}", headers=self.api_headers, json=body)


