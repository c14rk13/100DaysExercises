import os
from dotenv import load_dotenv
from twilio.rest import Client
from flight_data import FlightData

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        load_dotenv()
        self.ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
        self.AUTH_TOKEN = os.getenv("TWILIO__AUTH_TOKEN")
        self.WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
        self.WHATSAPP_TO = os.getenv("TWILIO_WHATSAPP_TO")


    def send_whatsapp(self, flight_info: FlightData):
        msg_body = f"Low price alert! Only {flight_info.CURRENCY_SYMBOL}{flight_info.PRICE} "
        msg_body += f"from {flight_info.ORIGIN_IATA_CODE} to {flight_info.DESTINATION}, "
        msg_body += f"on {flight_info.FLIGHT_DATE} until {flight_info.RETURN_DATE}"
        print(msg_body)

        client = Client(self.ACCOUNT_SID,  self.AUTH_TOKEN)
        message = client.messages.create(
            from_=f'whatsapp:{self.WHATSAPP_FROM}',
            body=msg_body,
            to=f'whatsapp:{self.WHATSAPP_TO}'
        )

        print(message.status)
